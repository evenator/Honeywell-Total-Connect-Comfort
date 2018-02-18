import pprint
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeviceData(Base):
    __tablename__ = 'device_data'
    time_stamp = Column(Integer, primary_key=True)
    alerts = Column(String)
    communication_lost = Column(Boolean)
    can_control_humidification = Column(Boolean)
    fan_is_running = Column(Boolean)
    fan_mode = Column(Integer)
    has_fan = Column(Boolean)
    cool_setpoint = Column(Integer)
    cool_next_period = Column(Integer)
    deadband = Column(Integer)
    device_id = Column(String)
    disp_temperature = Column(Integer)
    disp_unit = Column(String)
    heat_setpoint = Column(Integer)
    heat_next_period = Column(Integer)
    hold_until_capable = Column(Boolean)
    is_in_vacation_hold_mode = Column(Boolean)
    schedule_capable = Column(Boolean)
    schedule_cool_setpoint = Column(Integer)
    schedule_heat_setpoint = Column(Integer)
    setpoint_change_allowed = Column(Boolean)
    status_cool = Column(Integer)
    status_heat = Column(Integer)
    system_switch_position = Column(Integer)
    temporary_hold_until_time = Column(Boolean)
    vacation_hold = Column(Boolean)
    vacation_hold_cancelable = Column(Boolean)
    vacation_hold_until_time = Column(Boolean)

    @classmethod
    def from_dict(cls, time_stamp, data_dict):
        latest_data = data_dict['latestData']
        ui_data = latest_data['uiData']
        fan_data = latest_data['fanData']
        return cls(time_stamp=time_stamp,
                   alerts=data_dict['alerts'].strip(),
                   communication_lost=data_dict['communicationLost'],
                   can_control_humidification=latest_data['canControlHumidification'],
                   # TODO drData
                   fan_is_running=fan_data['fanIsRunning'],
                   fan_mode=fan_data['fanMode'],
                   has_fan=latest_data['hasFan'],
                   cool_setpoint=ui_data['CoolSetpoint'],
                   cool_next_period=ui_data['CoolNextPeriod'],
                   deadband=ui_data['Deadband'],
                   device_id=ui_data['DeviceID'],
                   disp_temperature=ui_data['DispTemperature'],
                   disp_unit=ui_data['DisplayUnits'],
                   heat_setpoint=ui_data['HeatSetpoint'],
                   heat_next_period=ui_data['HeatNextPeriod'],
                   hold_until_capable=ui_data['HoldUntilCapable'],
                   # TODO Humidity
                   is_in_vacation_hold_mode=ui_data['IsInVacationHoldMode'],
                   schedule_capable=ui_data['ScheduleCapable'],
                   schedule_cool_setpoint=ui_data['ScheduleCoolSp'],
                   schedule_heat_setpoint=ui_data['ScheduleHeatSp'],
                   setpoint_change_allowed=ui_data['SetpointChangeAllowed'],
                   status_cool=ui_data['StatusCool'],  # TODO: Decode this
                   status_heat=ui_data['StatusHeat'],  # TODO: Decode this
                   # TODO Switch allowed data
                   # TODO: Decode this
                   system_switch_position=ui_data['SystemSwitchPosition'],
                   temporary_hold_until_time=ui_data['TemporaryHoldUntilTime'],
                   vacation_hold=ui_data['VacationHold'],
                   vacation_hold_cancelable=ui_data['VacationHoldCancelable'],
                   vacation_hold_until_time=ui_data['VacationHoldUntilTime'])

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return pprint.pformat(self.__dict__)
