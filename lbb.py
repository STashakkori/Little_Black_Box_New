# Little Black Box New
# By: Sina Tashakkori, QVLx Labs

#!/usr/bin/env python3

import subprocess
import sys
import os.path
from os import path

# Check args
if len(sys.argv) < 3:
    print("Error: not enough arguments given")
    exit(1)

# Variables
input_string = ""
cryptos_json = " cryptos.json"
firmware_json = " firmware.json"
hardware_json = " hardware.json"
cert = False
key = False
all = False
id_str = ""
key = ""
certificate = ""
output = ""

# Colors
yellow='\033[93m'

# Get key file name or all
filename = sys.argv[1]

# Get key file name or all
outfile = sys.argv[2]

if filename.lower() == "all":
    all = True
elif not path.exists(filename):
    print("Invalid file path.")
    exit(1)
else:
    with open(filename) as f:
        content = f.readlines()
    if "CERTIFICATE" in content[0]:
        cert = True
    elif "KEY" in content[0]:
        key = True
    else:
        print("File needs proper markers to be identified.")
    for line in range(0, len(content)):
        if line != 0 and line != (len(content) - 1):
            input_string += content[line].rstrip('\n')
    if key:
        query = "\'.[] | select(.key==\""
        query += input_string
        query += "\").id\'"
        get_key_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        ID = out_str2
        ID_str = out_str2
        if len(out_str2) > 1:
            print("Key found in database")
            print()
            print(yellow + "ID: " + out_str2)
            print()
        else:
            print("ID: Entry not in database.")
            ID_str += ": Entry not in database"
        query = "\'.[] | select(.key==\""
        query += input_string
        query += "\").type\'"
        get_key_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        TYPE = out_str2
        if len(out_str2) > 1:
            print("Type: " + out_str2)
            print()
        else:
            print("Type: Entry not in database.")
            print()
            TYPE += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").vendor\'"
        get_key_command = "./jq " + query + firmware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        firmware_vendor = out_str2
        if len(out_str2) > 1:
            print("Firmware vendor: " + out_str2)
            print()
        else:
            print("Firmware vendor: Entry not in database.")
            print()
            firmware_vendor += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").description\'"
        get_key_command = "./jq " + query + firmware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        firmware_description = out_str2
        if len(out_str2) > 1:
            print("Firmware description: " + out_str2)
            print()
        else:
            print("Firmware description: Entry not in database.")
            print()
            firmware_description += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").vendor\'"
        get_key_command = "./jq " + query + hardware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        hardware_vendor = out_str2
        if len(out_str2) > 1:
            print("Hardware vendor: " + out_str2)
            print()
        else:
            print("Hardware vendor: Entry not in database.")
            print()
            hardware_vendor += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").model\'"
        get_key_command = "./jq " + query + hardware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        hardware_model = out_str2
        if len(out_str2) > 1:
            print("Hardware model: " + out_str2)
            print()
        else:
            print("Hardware model: Entry not in database.")
            print()
            hardware_model += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").revision\'"
        get_key_command = "./jq " + query + hardware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        hardware_revision = out_str2
        if len(out_str2) > 1:
            print("Hardware revision: " + out_str2)
            print()
        else:
            print("Hardware revision: Entry not in database.")
            print()
            hardware_revision += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").profile\'"
        get_key_command = "./jq " + query + hardware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        hardware_profile = out_str2
        if len(out_str2) > 1:
            print("Hardware profile: " + out_str2)
            print()
        else:
            print("Hardware profile: Entry not in database.")
            print() 
            hardware_profile += "Entry not in database"
        query = "\'.[] | select(.key==\""
        query += input_string
        query += "\").fingerprint\'"
        get_key_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        fingerprint = out_str2
        if len(out_str2) > 1:
            print("Fingerprint: " + out_str2)
            print()
        else:
            print("Fingerprint: Entry not in database.")
            print()
            fingerprint += "Entry not in database"
        query = "\'.[] | select(.key==\""
        query += input_string
        query += "\").certificate\'"
        get_key_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        certificate = out_str2
        if len(out_str2) > 1:
            print("Certificate: " + out_str2)
            print()
        else:
            print("Certificate: Entry is not in our database.")
            print()
            certificate += "Entry not in database"
        print("Key: " + input_string)
        f = open(outfile, "w+")
        f.write("ID: " + ID_str + "\n\n")
        f.write("Type: " + TYPE + "\n\n")
        f.write("Firmware Vendor: " + firmware_vendor + "\n\n")
        f.write("Firmware Description: " + firmware_description + "\n\n")
        f.write("Hardware Vendor: " + hardware_vendor + "\n\n")
        f.write("Hardware Model: " + hardware_model + "\n\n")
        f.write("Hardware Revision: " + hardware_revision + "\n\n")
        f.write("Hardware Profile: " + hardware_profile + "\n\n")
        f.write("Fingerprint: " + fingerprint + "\n\n")
        f.write("Certificate: " + certificate + "\n\n")
        f.write("Key: " + input_string)
        f.close()
    elif cert:
        query = "\'.[] | select(.certificate==\""
        query += input_string
        query += "\").id\'"
        get_key_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        ID = out_str2
        ID_str = out_str2
        if len(out_str2) > 1:
            print("Key found in database")
            print()
            print(yellow + "ID: " + out_str2)
            print()
        else:
            print("ID: Entry not in database.")
            ID_str += ": Entry not in database"
        query = "\'.[] | select(.certificate==\""
        query += input_string
        query += "\").type\'"
        get_key_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        TYPE = out_str2
        if len(out_str2) > 1:
            print("Type: " + out_str2)
            print()
        else:
            print("Type: Entry not in database.")
            print()
            TYPE += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").vendor\'"
        get_key_command = "./jq " + query + firmware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        firmware_vendor = out_str2
        if len(out_str2) > 1:
            print("Firmware vendor: " + out_str2)
            print()
        else:
            print("Firmware vendor: Entry not in database.")
            print()
            firmware_vendor += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").description\'"
        get_key_command = "./jq " + query + firmware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        firmware_description = out_str2
        if len(out_str2) > 1:
            print("Firmware description: " + out_str2)
            print()
        else:
            print("Firmware description: Entry not in database.")
            print()
            firmware_description += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").vendor\'"
        get_key_command = "./jq " + query + hardware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        hardware_vendor = out_str2
        if len(out_str2) > 1:
            print("Hardware vendor: " + out_str2)
            print()
        else:
            print("Hardware vendor: Entry not in database.")
            print()
            hardware_vendor += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").model\'"
        get_key_command = "./jq " + query + hardware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        hardware_model = out_str2
        if len(out_str2) > 1:
            print("Hardware model: " + out_str2)
            print()
        else:
            print("Hardware model: Entry not in database.")
            print()
            hardware_model += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").revision\'"
        get_key_command = "./jq " + query + hardware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        hardware_revision = out_str2
        if len(out_str2) > 1:
            print("Hardware revision: " + out_str2)
            print()
        else:
            print("Hardware revision: Entry not in database.")
            print()
            hardware_revision += "Entry not in database"
        query = "\'.[] | select(.id==\""
        query += ID
        query += "\").profile\'"
        get_key_command = "./jq " + query + hardware_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        hardware_profile = out_str2
        if len(out_str2) > 1:
            print("Hardware profile: " + out_str2)
            print()
        else:
            print("Hardware profile: Entry not in database.")
            print() 
            hardware_profile += "Entry not in database"
        query = "\'.[] | select(.certificate==\""
        query += input_string
        query += "\").fingerprint\'"
        get_key_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        fingerprint = out_str2
        if len(out_str2) > 1:
            print("Fingerprint: " + out_str2)
            print()
        else:
            print("Fingerprint: Entry not in database.")
            print()
            fingerprint += "Entry not in database"
        query = "\'.[] | select(.certificate==\""
        query += input_string
        query += "\").key\'"
        get_key_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_key_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        certificate = out_str2
        if len(out_str2) > 1:
            print("Key: " + out_str2)
            print()
        else:
            print("Key: Entry is not in our database.")
            print()
            certificate += "Entry not in database"
        print("Certificate: " + input_string)
        f = open(outfile, "w+")
        f.write("ID: " + ID_str + "\n\n")
        f.write("Type: " + TYPE + "\n\n")
        f.write("Firmware Vendor: " + firmware_vendor + "\n\n")
        f.write("Firmware Description: " + firmware_description + "\n\n")
        f.write("Hardware Vendor: " + hardware_vendor + "\n\n")
        f.write("Hardware Model: " + hardware_model + "\n\n")
        f.write("Hardware Revision: " + hardware_revision + "\n\n")
        f.write("Hardware Profile: " + hardware_profile + "\n\n")
        f.write("Fingerprint: " + fingerprint + "\n\n")
        f.write("Certificate: " + certificate + "\n\n")
        f.write("Key: " + input_string)
        f.close()

    elif all:
        print("Retrieving all entries")
        query = "\'.[]\'"
        get_all_command = "./jq " + query + cryptos_json
        output = subprocess.check_output(get_all_command, shell=True)
        out_str = output.decode("utf-8")
        out_str2 = out_str.lstrip('\"').rstrip('\n').rstrip('\"')
        if len(out_str2) > 1:
            print(out_str2, end="")
        else:
            print("Entry is not in our database.")
