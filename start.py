#! /usr/bin/env python3

import subprocess
import threading
import webbrowser
import time


def run_sp(args: list, **kwargs):
    subprocess.run(args, **kwargs).check_returncode()


print("removing previous images...")
run_sp(["docker-compose", "down"])

print("downloading images...")
run_sp(["docker", "pull", "scorpid33/rtu-biz-website-db"])
run_sp(["docker", "build", "."])


def start_server():
    print("starting server...")
    run_sp(["docker-compose", "up"])


threading.Thread(target=start_server).start()
time.sleep(10)
webbrowser.open("http://localhost:8083/wp-admin")
