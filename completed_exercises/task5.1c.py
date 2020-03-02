#!/usr/bin/env python3.6
from sys import argv




london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
test = input ('Введите имя устройства ')
#st = list(london_co['r1'].keys())
test2 = input ('Введите имя параметра {} '.format(list(london_co[test].keys())))
test2=test2.lower()
print(london_co[test].get(test2, 'Нет такого параметра'))

