# -*- coding: utf-8 -*-
'''
Author   : Alexandre
Created  : 2019-12-19 13:40:46
Modified : 2019-12-19 13:42:35

Comments : Python 3.6.7
'''

import json
import os


def get_file_info(measurement_folder_path):
    # load json
    json_path = os.path.join(measurement_folder_path, 'info.json')
    with open(json_path) as json_file:
        jd = json.load(json_file)
    # print
    print('>> %s' % jd['tag'])
    print('  + temperature \t: %.1f °C' % jd['temperature']['value'])
    print('  + cycle duration \t: %i µs' % jd['cycle duration']['value'])
    print('  + photon / cycle \t: %1.3g' % jd['photons per cycle'])
    print('  + tot. duration \t: %.1f hours' % jd['total duration']['value'])
    print('  + photons collected \t: %1.0e' % jd['photons detected'])
    if jd['comments'] != '':
        print('  + comments : %s' % jd['comments'])

    return jd
