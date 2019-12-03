#! /usr/bin/env python3

import subprocess
import threading
import webbrowser
import time

subprocess.run(["docker-compose", "down"])
subprocess.run([
    "docker-compose",
    "build",
])

try:
    subprocess.run(
        [
            "docker-compose",
            "up",
        ],
        timeout=20,
    )
except subprocess.TimeoutExpired:
    pass

time.sleep(10)

print("Applying patches...")
subprocess.run([
    "docker-compose",
    "exec",
    "wordpress",
    "wp",
    "--allow-root",
    "core",
    "install",
    "--url=localhost:8083",
    "--title='RTU BIZ'",
    "--admin_user=admin",
    "--admin_password=admin",
    "--admin_email=admin@sbnfksd.com",
])


def start_server():
    subprocess.run(
        [
            "docker-compose",
            "up",
        ],
    )


threading.Thread(target=start_server).start()
time.sleep(1)
webbrowser.open("http://localhost:8083/wp-admin")
