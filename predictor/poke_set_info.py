__author__ = 'ruijing'

import json

json_data = open('predictor/bw.json')
set_bw = json.load(json_data)

json_data = open('predictor/dpp.json')
set_dpp = json.load(json_data)

json_data = open('predictor/gse.json')
set_rse = json.load(json_data)

json_data = open('predictor/gsc.json')
set_gsc = json.load(json_data)

json_data = open('predictor/rby.json')
set_rby = json.load(json_data)
