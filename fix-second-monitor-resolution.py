# This script has the purpose to do in a simple script the fix specified on:
# https://askubuntu.com/questions/73007/cant-set-a-higher-screen-resolution-in-a-external-display-in-a-dell-mini-10v-la


import os
import inquirer

# Function user for cleaning monitor output for options
def clean_monitor_output(data):
  return data.split("  ").pop()

# Define commands to use
get_resolution_cmd = 'cvt 1650 900'
get_monitors_cmd = 'xrandr --listmonitors'
add_modeline_cmd = 'xrandr --newmode {0}'
add_resolution_to_output_cmd = 'xrandr --addmode {0} 1656x900_60.00'

# Get all the data I need
resolution_output = os.popen(get_resolution_cmd).read()
monitors_output = os.popen(get_monitors_cmd).read()

arr = resolution_output.split('Modeline')

# Prepare question options
monitors = monitors_output.split('\n')
monitors.pop()
monitors.pop(0)

# Request user which monitor needs to add a new resolution

questions = [
    inquirer.List('monitor',
                  message="Which monitor will you add the new resolution?",
                  choices=map(clean_monitor_output, monitors)
                 )
]

monitor = inquirer.prompt(questions)['monitor']

resolution_to_use = resolution_output.split('\n')[1].split('Modeline')[1]

# Add a new mode

os.popen(add_modeline_cmd.format(resolution_to_use))
os.popen(add_resolution_to_output_cmd.format(monitor))
