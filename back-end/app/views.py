from app import app
import os
from multiprocessing import Process
from flask import Response, request
import json
import pandas as pd
import numpy as np
import math

import sys

# from test import run

p = None
status = False
base_path = '/home/czh/VAGMM/src'
sys.path.append(base_path)
records_num = 0
epoch_num = 100

from run_nae import run

class Data():
	def __init__(self, index, prec, rec, fscore):
		global epoch_num
		self.trial = index % epoch_num + 1
		self.precision = prec
		self.recall = rec
		self.fscore = fscore

@app.route('/')
@app.route('/index')
def index():
	global status
	data = {'status': status}
	return json.dumps(data, default=lambda o: o.__dict__), 200

def parse_config(config):
	try:
		for _key in config.keys():
			if _key == 'K' or _key == 'epoch_num':
				config[_key] = int(config[_key])
			elif _key != 'layer':
				config[_key] = float(config[_key])
			else:
				config[_key] =list(map(lambda x: int(x), config[_key].split(' ')))
		return config
	except:
		return {}

@app.route('/start', methods=['POST'])
def start():
	global p; global status; global epoch_num
	config = request.get_json()
	config = parse_config(config)
	epoch_num = int(config['epoch_num'])
	if len(config) == 0:
		return Response(status=301)
	if p is not None and status == True:
		return "Process Alrealy Running!", 201
	p = Process(target=run, kwargs=config)
	p.start()
	status = True
	return "Start!", 200

@app.route('/stop', methods=['GET'])
def stop():
	global p; global status
	if p is not None and status == True:
		p.terminate()
		p = None
		status = False
		return "Stopped!"
	else:
		return "No Process Running"

@app.route('/data', methods=['GET'])
def data():
	global base_path; global records_num; global epoch_num
	try:
		data = pd.read_csv('result.csv', header=None)
	except:
		data = pd.DataFrame()
	records_num = data.shape[0]
	data_list = []
	for index, row in data.iterrows():
		data_list.append(Data(index, row[0], row[1], row[2]))
	_data = {'data_list': data_list, 'page_size': epoch_num}
	return json.dumps(_data, default=lambda o: o.__dict__),200

@app.route('/table/<num>', methods=['GET'])
def table(num):
	global base_path; global records_num; global epoch_num
	num = int(num)
	try:
		all_data = np.array(pd.read_csv('result.csv', header=None))[:, 2]
	except:
		all_data = np.array([])
	records_num = all_data.shape[0]
	data_list = []
	num_records = math.ceil(records_num * 1. / epoch_num)
	for i in range(min(epoch_num, records_num)):
		_dict = {}
		_dict['Epoch'] = i
		j = num-1
		if j * epoch_num + i < records_num:
			_dict[str(j+1)] = all_data[j * epoch_num + i]
		data_list.append(_dict)
	columns = ['Epoch', str(num)]
	dict_data = {
		'rows': data_list,
		'columns': columns,
		'num_records': num_records,
	}
	return json.dumps(dict_data, default=lambda o: o.__dict__), 200