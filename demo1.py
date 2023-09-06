import sys
from Utilities.config import obj_read_config


print("Name of file:", sys.argv[1])
test_case_json = sys.argv[1]
test_file = obj_read_config.read_data(test_case_json,"file_to_be_run")
name = obj_read_config.read_data(test_case_json,"name")
password = obj_read_config.read_data(test_case_json,"password")
passkey = obj_read_config.read_data(test_case_json,"passkey")
print(test_file,name,password,passkey)