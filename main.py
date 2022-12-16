import subprocess, json, sys

def startProcess(path):
    proc = subprocess.Popen([f"cd {path} && yarn start"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    

def isRunning(port):
    proc = subprocess.Popen([f"lsof -i:{port}"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if out:
        return True
        
def run():
    if len(sys.argv) <= 2:
        print("First param: port number")
        print("second param: path to api")
        return False
        
    port = sys.argv[1]
    path = sys.argv[2]
    
    if isRunning(port):
        print(f"A process ir running on port {port}")
        return True
    else:
        print(f"There is no process running on port {port}. Starting now")
        startProcess(path)

run()
    
    