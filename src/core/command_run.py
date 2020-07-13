import sys
import json
import subprocess
from datetime import datetime


def get_settings(key):
    with open('commands.json') as json_file:
        data = json.load(json_file)
        if key in data:
            return data[key]
        else:
            return []

def run(n):
    cmd = get_settings('scripts')
    for comm in cmd:
        if comm['name'] == n:
            subprocess.call([comm['file']])
            print(comm['name'])
            print(comm['file'])

run(sys.argv[1])


if __name__ == "__main__":
    pass
