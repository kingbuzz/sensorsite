from temperatur.pyduino import *
from temperatur.models import Measurement
import datetime

a = Arduino()
print(a.status)


def persist_measurement_values():
    measured_values = read_sensors()
    v1 = measured_values[0]
    v2 = measured_values[1]
    v3 = measured_values[2]
    v4 = measured_values[3]
    __write_measurements(    v1['hum'],    v1['temp'],v2['hum'],    v2['temp'],v3['hum'],    v3['temp'],v4['hum'],    v4['temp'])
    return "done"


def read_sensors():
    sens1 = a.sensor_read(2)
    sens2 = a.sensor_read(3)
    sens3 = a.sensor_read(4)
    sens4 = a.sensor_read(5)
    return [sens1, sens2, sens3, sens4]


def read_sensor(pin_number):
    return a.sensor_read(pin_number)


def __write_measurements(temp1, hum1, temp2, hum2, temp3, hum3, temp4, hum4):
    m = Measurement()
    m.hum1 = hum1
    m.temp1 = temp1
    m.hum2 = hum2
    m.temp2 = temp2
    m.hum3 = hum3
    m.temp3 = temp3
    m.hum4 = hum4
    m.temp4 = temp4
    m.timestamp = datetime.datetime.now()
    m.save()
    return m.__str__()


def read_measurements():
    m = Measurement.objects.all()
    return m
