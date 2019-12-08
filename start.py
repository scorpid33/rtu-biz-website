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

print("Applying patches...")


def run(args: list):
    run_sp(
        [
            "docker-compose",
            "exec",
            "wordpress",
        ]
        + list(args)
    )


def run_wp(args: list):
    run(
        [
            "wp",
            "--allow-root",
        ]
        + list(args)
    )


run_wp([
    "core",
    "install",
    "--url=localhost:8083",
    "--title='RTU BIZ'",
    "--admin_user=admin",
    "--admin_password=admin",
    "--admin_email=admin@sbnfksd.com",
])

for p in [
    "astra-sites",
    "astra-widgets",
    "elementor",
    "ultimate-addons-for-gutenberg",
    "wpforms-lite",
]:
    run_wp(["plugin", "activate", p])
# run_wp(["theme", "activate", "astra"])


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
