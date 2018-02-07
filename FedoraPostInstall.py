#! /usr/bin/env python3
"""
Title           :FedoraPostInstall.py
Description     :Post installation script for Fedora
Author          :David P. Rush <davidprush@gmail.com>
Date            :2018
Version         :0.1
License         :MIT
Dependent       :config.json
Status          : In-Work & Not Stable
Description     :This is a port of my fedora-post-install
bash shell script. https://github.com/davidprush/fedora-post-instal
I am mostly doing this for developing my Python programming skills, so
it is not necessarily practical but a learning experience.
"""
from __future__ import print_function

from pathlib import Path

import sys 
import os 
import subprocess 
import glob 
import io 
import getpass 
import httplib2 
import json
import math

global ERRNUM
global ERRDESCR
global ERRPROC

class JsonData(object):
    """
    Creates json class object from file
    Reads/writes data to/from json file
    Prints formatted jason data to stdout
    """
    def __init__(self, name=None):
        self.name=name
        self.json_dict=dict()
        self.json_infile_path=None
        self.json_outfile_path=None
    def open_json_infile(self, pathfile):
        self.json_infile_path=pathfile
        with open(pathfile) as data_file:
            self.json_dict = json.load(data_file)
        data_file.close()
    def open_json_outfile(self, pathfile):
        self.json_outfile_path=pathfile
        with open(pathfile) as outfile:
            json.dump(self.json_dict, outfile)
        outfile.close()
    def print_json_dict_keys(self):
        list_keys=[]
        for key in self.json_dict.keys():
            list_keys.append(key)
        list_keys.sort()
        self.list_format_print(list_keys)
    def print_json_dict_values(self):
        list_values=[]
        for value in self.json_dict.values():
            list_values.append(value)
        list_values.sort()
        print (*list_values)
        print (len(list_values))
    def clear_json_data(self):
        self.json_dict.clear()
        self.json_infile_path=None
        self.json_outfile_path=None
    def print_json_dict(self):
        print (json.dumps(self.json_dict, indent=4, 
                ensure_ascii=True, sort_keys=True))
    def list_format_print(self, obj, cols=4, 
                    columnwise=True, gap=4):
        sobj = [str(item) for item in obj]
        if cols > len(sobj): cols = len(sobj)
        max_len = max([len(item) for item in sobj])
        if columnwise: cols = int(math.ceil(float(len(sobj)) / float(cols)))
        plist = [sobj[i: i+cols] for i in range(0, len(sobj), cols)]
        if columnwise:
            if not len(plist[-1]) == cols:
                plist[-1].extend(['']*(len(sobj) - len(plist[-1])))
            plist = zip(*plist)
        print_format = '\n'.join([
            ''.join([c.ljust(max_len + gap) for c in p])
            for p in plist])
        print (print_format)

class ConfigureSystem(object):
    """
    Configure system configuration files listed in config.json.
    """
    def __init__(self, name=None):
        self.name=name
        self.config_files=dict()
        self.config_dirs=dict()

class MainMenu(object):
    """
    Creates a program menu, gets user input, and tests the input.
    This method is dependent on the config.json file.
    """
    def __init__(self, name=None):
        self.name=name
        self.option=None
        self.command=None
        self.menu=list()
        self.input_list=list()
        self.list_options=list()
        self.list_commands=list()
        self.invalid_list=list()
    def display_menu(self):
        print
    def check_selection(self, option=None, 
                        command=None, *args):
        self.option=option
        self.command=command
        self.input_list=list(*args)
    def do_option(self):
        if (self.test_selection()):
            pass           
    def test_selection(self):
        self.invalid_list()
        for value in self.input_list:
            if ((self.list_commands.count(value)) or 
                (value not in self.list_options)):
                    self.invalid_list.append(value)
        if (len(self.invalid_list) == 0):
            return True
        else:
            return False

def log_event():
    """
    Log events by passing an error number(error_num), error description
    (error_descr), and the erroring method then write it to log.txt.
    """            
    #open("log.txt")
    #ERRNUM=SystemError()
    #ERRDESCR=""
    #ERRPROC=SystemError().message
    #datefmt="%d/%m/%Y %H:%M:%S"

def main():
    """
    Main method where most the work gets done.
    """
    json_config_filepath = "/home/rush/Projects/Temp/postFedora/config.json"
    json_config_file=JsonData()
    json_config_file.open_json_infile(json_config_filepath)
    json_config_file.print_json_dict()
    json_config_file.print_json_dict_keys()
    json_config_file.print_json_dict_values()

#################################################################################
########################MAIN PROGRAM#############################################
#################################################################################

main()
