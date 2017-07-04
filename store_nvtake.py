#!/usr/bin/python3
import json
import configparser
import subprocess
data_json = open('data.json', 'r')
pkg_info = json.load(data_json)
config = configparser.ConfigParser(dict_type=dict, allow_no_value=True)
config.read('store.ini')
pkgs_str = ''
for package in pkg_info:
    pkg_name = package["name"]
    if pkg_name in config.sections():
        pkgs_str += pkg_name
        pkgs_str += ' '

nvtake_cmd = "nvtake store.ini %s" % pkgs_str
subprocess.call(nvtake_cmd, shell=True)
