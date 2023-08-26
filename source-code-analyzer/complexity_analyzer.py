import os
import subprocess
import sys
import json

# Gets the path from args if available. If not starts from the current directory 
target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

print('Started analyzing dir: ' + target_dir)

total_cc_count = 0
total_cc_files = 0

def parse_cc_response(file_name, response):
    response = json.loads(response)
    if file_name in response:
        return (response[file_name][0]['complexity'], 1)
    return (0,0)

for root, subdirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith('.py'):
            os.chdir(root)
            execution_str = "radon cc -j " + file
            output_str = subprocess.getoutput(execution_str)
            res = parse_cc_response(file, output_str)
            total_cc_count += res[0]
            total_cc_files += res[1]


print("Total cyclomatic complexity is: ",total_cc_count)
print("Analyzed files for cyclomatic complexity",total_cc_files)



    