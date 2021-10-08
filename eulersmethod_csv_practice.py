#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:22:50 2021

@author: emily
"""

import csv

file = "/home/emily/Downloads/acceleration_function_csv - Sheet1 (1).csv"

dict_data_acc = []
with open(file, newline ="") as acceleration_csv:
    acceleration_reader = csv.DictReader(acceleration_csv)
    for row in acceleration_reader:
        row['x'] = int(row['x'])
        row['y'] = int(row['y'])
        dict_data_acc.append(row)

def euler_method(acc_points, initial_dict_point):
    vel_points = [{'x': initial_dict_point[0], 'y': initial_dict_point[1]}]
    total = initial_dict_point[1]
    for i in range(len(acc_points)-1):
        total += acc_points[i]['y']*(acc_points[i+1]['x']-acc_points[i]['x'])
        coordinate = {'x': acc_points[i+1]['x'], 'y': total}
        vel_points.append(coordinate)
    return vel_points

velocity_coordinates = euler_method(dict_data_acc, (0,0))
      
    
fields = ['x', 'y']


with open('vel_points.csv', 'w') as vel_points_csv:
  
  vel_points_csv = csv.DictWriter(vel_points_csv, fieldnames=fields)

  vel_points_csv.writeheader()
  for item in velocity_coordinates:
    vel_points_csv.writerow(item)


