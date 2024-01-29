import time
import schedule
import subprocess

def run_script():
    subprocess.Popen(["python3", "../scrapper/script.py"])
schedule.every(5).seconds.do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)
