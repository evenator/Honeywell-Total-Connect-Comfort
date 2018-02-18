from .datatypes import DeviceData

from lxml import html
import pprint
import requests
import time

PORTAL = 'https://mytotalconnectcomfort.com/portal/'


class Client(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.headers.update(
            {'User-Agent': 'MyTotalConnectComfortClient/0.1'})
        self.login()

    def login(self):
        self.session.get(PORTAL)
        r = self.session.post(PORTAL,
                              headers={'Origin': PORTAL},
                              data={
                                  'UserName': self.username,
                                  'Password': self.password,
                                  'RememberMe': 'false'})
        if r:
            title = html.fromstring(r.text).find(".//title").text
            if title == 'THERMOSTAT Control':
                # Success
                return
        raise RuntimeError('Failed to log in')

    def get_json(self, path):
        headers = dict()
        headers['X-Requested-With'] = 'XMLHttpRequest'
        headers['User-Agent'] = 'MyTotalConnectComfortClient/0.1'
        headers['Accept'] = 'application/json, text/javascript'
        headers['Content-Type'] = 'application/json; charset=utf-8'
        r = self.session.post(path, headers=headers)
        return r.json()

    def get_locations(self):
        path = PORTAL + 'Location/GetLocationListData?page=1&filter='
        return self.get_json(path)

    def get_location_data(self, location_id):
        path = '{}Device/GetZoneListData?locationId={}&page=1'.format(
            PORTAL, location_id)
        return self.get_json(path)

    def get_device_data(self, device_id, utc_seconds=None):
        if utc_seconds is None:
            utc_seconds = time.time()
        time_stamp = int(round(utc_seconds*1000))
        path = '{}Device/CheckDataSession/{}?_={}'.format(
            PORTAL, device_id, utc_seconds)
        return DeviceData.from_dict(time_stamp, self.get_json(path))
