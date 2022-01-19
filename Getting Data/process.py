"""
Using subprocess module to run command line functions and stdout and stdin
author@Imran
date 19/01/22
"""
import subprocess



p1 = subprocess.run(['type', 'SomeFile.txt'], shell=True, capture_output=True, text=True, check=True)

p2 = subprocess.run(['findstr', '-n', 'API'], shell=True, capture_output=True, text=True, check=True, input=p1.stdout)

print(p2.stdout)