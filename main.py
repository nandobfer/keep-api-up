import subprocess, json, sys


def checkPort(port):
    proc = subprocess.Popen([f"lsof -i:{port}"], stdout=subprocess.PIPE, shell=True)
    print()
    (out, err) = proc.communicate()
    print(out)
    
    
    
port = sys.argv[1]