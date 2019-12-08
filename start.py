#! /usr/bin/env python3

import subprocess
import threading
import webbrowser
import time


def run_sp(args: list, **kwargs):
    subprocess.run(args, **kwargs).check_returncode()


run_sp(["docker-compose", "down"])
run_sp(["docker-compose", "build"])

try:
    run_sp(
        [
            "docker-compose",
            "up",
        ],
        timeout=20,
    )
except subprocess.TimeoutExpired:
    pass

time.sleep(10)


def start_server():
    run_sp(["docker-compose", "up"])


threading.Thread(target=start_server).start()
time.sleep(1)
webbrowser.open("http://localhost:8083/wp-admin")
