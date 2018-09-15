import subprocess
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

print (subprocess.check_output(['ruby', dir_path+'/severyAPI/getDining.rb']))
