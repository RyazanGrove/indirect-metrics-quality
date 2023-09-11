import os
import subprocess
import sys
import json

# Gets the path from args if available. If not starts from the current directory 
target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

print('Started analyzing dir: ' + target_dir)

total_cc_count = 0
total_cc_files = 0
total_mi_count = 0
total_mi_files = 0
total_hal_count = 0
total_hal_files = 0
total_raw_loc_count = 0
total_raw_comments_percentage_count = 0
total_raw_files = 0

def parse_cc_response(file_name, response):
    response = json.loads(response)
    if file_name in response:
        return (response[file_name][0]['complexity'], 1)
    return (0,0)

def parse_mi_response(file_name, response):
    response = json.loads(response)
    if file_name in response:
        return (response[file_name]['mi'], 1)
    return (0,0)

def parse_hal_response(file_name, response):
    response = json.loads(response)
    if file_name in response:
        return (response[file_name]['total']['volume'], 1)
    return (0,0)

def parse_raw_response(file_name, response):
    response = json.loads(response)
    if file_name in response:
        loc = response[file_name]['loc']
        comments = response[file_name]['comments'] + response[file_name]['multi']
        comments_percentage = comments / loc if loc != 0 else 0
        return (loc, comments_percentage, 1)
    return (0,0, 0)

for root, subdirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.py'):
            os.chdir(root)
            execution_str = "radon cc -j " + file
            output_str = subprocess.getoutput(execution_str)
            res = parse_cc_response(file, output_str)
            total_cc_count += res[0]
            total_cc_files += res[1]

            execution_str = "radon mi -j " + file
            output_str = subprocess.getoutput(execution_str)
            res = parse_mi_response(file, output_str)
            total_mi_count += res[0]
            total_mi_files += res[1]

            execution_str = "radon hal -j " + file
            output_str = subprocess.getoutput(execution_str)
            res = parse_hal_response(file, output_str)
            total_hal_count += res[0]
            total_hal_files += res[1]

            execution_str = "radon raw -j " + file
            output_str = subprocess.getoutput(execution_str)
            res = parse_raw_response(file, output_str)
            total_raw_loc_count += res[0]
            total_raw_comments_percentage_count += res[1]
            total_raw_files += res[2]

print("Total cyclomatic complexity is: ",total_cc_count)
print("Analyzed files for cyclomatic complexity: ",total_cc_files)

print("Total maintainability index is: ",total_mi_count)
print("Analyzed files for maintainability index: ",total_mi_files)

print("Total Halstead volume is: ",total_hal_count)
print("Analyzed files for Halstead volume: ",total_hal_files)

print("Total raw loc is: ",total_raw_loc_count)
print("Total raw comments percentage is: ",total_raw_comments_percentage_count)
print("Analyzed files for raw metrics: ",total_raw_files)

    