#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Andy Moreno"
__email__ = "andymoreno77@students.columbiabasin.edu"
__date_ = "Spring 2020"
__version__ = "0.0.1"

# LIBRARIES
from datetime import date
import os
import pickle
import json
import subprocess

# SET VARIABLES
my_dir = '/Users/andym/Downloads/test/Logon ID'
my_pickle = '/Users/andym/Downloads/test/Logon ID/051420.pickle'
my_json = '/Users/andym/Downloads/test/Logon ID/051420.json'
port_list = ['192.168.1.4:80', '192.168.1.4:23', '192.168.1.4:22']
nmap_path = '/Users/andym/Downloads/test/Logon ID/Nmap/nmap'
nmap_network = '192.168.1.4/24'

def create_directory():   
    if(os.path.isdir(my_dir)) == False:
        try:  
            os.mkdir(my_dir)
            print ("INFO: The directory was created:", my_dir) 
        except OSError:  
            print ("ERROR: Failed to create directory:", my_dir)
    else:
        print ("INFO: The directory already exists:", my_dir) 
        
def create_date_string():
    date_str = date.today().strftime("%m%d%y")
    print("Date String:", date_str)

def write_files():
    # write the pickle file
    with open(my_pickle, 'wb') as fp:
        pickle.dump(port_list, fp)
    fp.close()
    
    # write the json file
    with open(my_json, 'w') as fp:  
        json.dump(port_list, fp)
    fp.close()

def read_files():
    port_list = []
    
    # read the pickle file
    with open (my_pickle, 'rb') as fp:
        port_list = pickle.load(fp)
    fp.close()
    
    print("pickle:", port_list)
    
    port_list = []
    
    # read the json file
    with open(my_json, 'r') as fp:  
        port_list = json.load(fp)
    fp.close()
    
    print("json:", port_list)

def run_nmap():
    nmap_out = subprocess.run([nmap_path, "-T4", nmap_network], capture_output=True)
    nmap_data = nmap_out.stdout.splitlines()
    print(nmap_data)
    
create_directory()
create_date_string()
write_files()
read_files()
run_nmap()

