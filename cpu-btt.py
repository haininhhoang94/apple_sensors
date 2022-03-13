# -*- coding: UTF-8 -*-
import json
import os

def find_cpu_temp(str_name, str_value):
    global i
    list_name = str_name.split(',')
    list_value = str_value.split(',')
    # print(list_name)
    # print(list_value)
    res_l = {}
    for i in range(len(list_name)):
        res_l[list_name[i]] = list_value[i]
    # print(res_l)
    # print(' PMGR SOC Die Temp Sensor0')
    # print(res_l[' PMGR SOC Die Temp Sensor0'])
    try:
        return "SOC:"+ res_l['PMGR SOC Die Temp Sensor0']+" C",float(res_l['PMGR SOC Die Temp Sensor0'])
    except Exception as e:
        return "SOC:"+ res_l[' PMGR SOC Die Temp Sensor0']+" C", float(res_l[' PMGR SOC Die Temp Sensor0'])




global process, output
process = os.popen("/Users/haininhhoang94/temp_sensor") # return file
output = process.read()
list_output = output.split('\n')
str_name = list_output[0]
str_value = list_output[1]
cpu_temp,float_cpu_temp = find_cpu_temp(str_name, str_value)

process.close()
# print(cpu_temp)



# make json
"""
"{\"text\":\"newTitle\",                                                 
\"icon_data\": \"base64_icon_data\",                                                 
\"icon_path":\"path_to_new_icon\",                                                 
\"sf_symbol_name":\"symbol_name\",                                                 
\"sf_symbol_size":\"size_of_the_symbol\",                                                 
\"background_color\": \"255,85,100,255\",                                                 
\"font_color\": \"100,200,100,255\",                                                 
\"font_size\": 10}"
"""


if float_cpu_temp>70:
    tmp = {
        "text":cpu_temp,
        # "icon_data":"base64_icon_data",
        # "icon_path":"path_to_new_icon",
        # "sf_symbol_name":"symbol_name",
        # "sf_symbol_size":"size_of_the_symbol",
        #"background_color": "226,107,67,255",
        # "font_color": "100,200,100,255",
        # "font_size": 10
    }
    json_str = json.dumps(tmp)
    print(json_str)

elif float_cpu_temp>0:
    tmp = {
        "text": cpu_temp,
        # "icon_data":"base64_icon_data",
        # "icon_path":"path_to_new_icon",
        # "sf_symbol_name":"symbol_name",
        # "sf_symbol_size":"size_of_the_symbol",
        #"background_color": "249,217,96,255",
        # "font_color": "225,225,225,255",
        # "font_size": 10
    }
    json_str = json.dumps(tmp)
    print(json_str)

# elif float_cpu_temp>=0:
#     tmp = {
#         "text": cpu_temp,
#         # "icon_data":"base64_icon_data",
#         # "icon_path":"path_to_new_icon",
#         # "sf_symbol_name":"symbol_name",
#         # "sf_symbol_size":"size_of_the_symbol",
#         "background_color": "101,167,186,255",
#         "font_color": "225,225,225,255",
#         # "font_size": 10
#     }
#     json_str = json.dumps(tmp)
#     print(json_str)