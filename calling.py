import subprocess
import time
import os
# def connect_to_remote_receiver(server_name, username, password):
#     command = f"remmina -c vnc://{username}:{password}@{server_name}"
#     subprocess.Popen(command, shell=True)
#     time.sleep(10)

def connect_to_remote_calling(server_name, username, password):
    command = f"remmina -c vnc://{username}:{password}@{server_name}"
    subprocess.Popen(command, shell=True)
    time.sleep(10)

def execute_commands():
    command_call = "source /opt/ros/humble/setup.bash && source ~/ros2_ws/install/setup.bash && ros2 run keyboard_publisher command_publisher1 &"
    # command_receive = "source /opt/ros/humble/setup.bash && source ~/ros2_ws/install/setup.bash && ros2 run keyboard_publisher command_publisher2 "
    subprocess.run(command_call,shell=True, executable="/bin/bash")
    # subprocess.run(command_receive,shell=True, executable="/bin/bash")
    time.sleep(100)


# server_name = '10.91.237.84'
# username = 'poc-agent-002'
# password = 'Test123'
# connect_to_remote_receiver(server_name,username,password)

server_name = '10.91.237.117'
username = 'poc'
password = 'Test123'
connect_to_remote_calling(server_name,username,password)
execute_commands()