import json
import argparse
import os
import sys
import errno
import datetime
import time
import psutil
from columnar import columnar


class MySnapshot(dict):
    def __init__(self, parent=None, key=None):
        self.parent = parent
        self.key = key

    def __missing__(self, key):
        self[key] = MySnapshot(self, key)
        return self[key]

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)
        try:
            val.parent = self
            val.key = key
        except AttributeError:
            pass


def to_fixed(number, digits=0):
    return f"{number:.{digits}f}"


def check_exist_folder(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def get_human_readable_size(num):
    exp_str = [(0, 'B'), (10, 'KB'), (20, 'MB'), (30, 'GB'), (40, 'TB'), (50, 'PB')]
    n = 0
    while n + 1 < len(exp_str) and num >= (2 ** exp_str[n + 1][0]):
        n += 1
        rounded_val = round(float(num) / 2 ** exp_str[n][0], 2)
    return '%s %s' % (float(rounded_val), exp_str[n][1])


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Interval between snapshots", type=int, default=30)
    parser.add_argument("-t", help="Output file type", default="txt")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    return parser.parse_args()


def create_snapshots(arg):
    headers = ['cpu_average_used', 'cpu_percent_used', 'memory_used', 'memory_percent_used']
    data = []
    now = datetime.datetime.now()
    path = '/tmp/snapshots/'
    filename = 'SNAPSHOT_' + str(now.strftime("%Y-%m-%d_%H:%M:%S"))

    while True:
        cpu_avg = 0.0
        for i in psutil.getloadavg():
            cpu_avg += i

        data.append([str(to_fixed(cpu_avg, 2)), str(psutil.cpu_percent(interval=1)),
                     str(get_human_readable_size(psutil.virtual_memory().used)),
                     str(psutil.virtual_memory().percent)])

        now = datetime.datetime.now()
        current = 'SNAPSHOT_' + str(now.strftime("%Y-%m-%d_%H:%M:%S"))

        if arg.t == "json":
            headers = ['cpu_average_used', 'cpu_percent_used', 'memory_used', 'memory_percent_used']
            snap = MySnapshot()
            check_exist_folder(os.path.join(path, filename + '.json'))
            k = 0
            for i in headers:
                for n in data:
                    snap[current][headers[k]] = str(n[k])
                k += 1
            with open(os.path.join(path, filename + '.json'), 'a', newline='\n') as f:
                json.dump(snap, f, indent=2)
                f.write('\n')
                snap.clear()

        if arg.t == "txt":
            check_exist_folder(os.path.join(path, filename + '.txt'))
            with open(os.path.join(path, filename + '.txt'), 'a') as f:
                f.write(current + ':\n')
                f.write(columnar(data, headers, no_borders=False))
                f.write('\n')
            data.clear()

        time.sleep(arg.i)


create_snapshots(parse_input())
