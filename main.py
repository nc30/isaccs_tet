from __future__ import print_function
import datetime
import sys
import os


sys.stdout.write("hello\r\n")
sys.stdout.write("this is {:%Y-%m-%d %H:%M:%S}\r\n".format(datetime.datetime.now()))
sys.stdout.write("environs.\r\n")
for i in os.environ.items():
    sys.stdout.write("{0}: '{1}'\r\n".format(*i))

sys.stdout.write("this is stdout message.\r\n")
sys.stderr.write("this is stderr message.\r\n")
sys.stdout.write("i go exit. goodbye.\r\n")
sys.exit(0)
