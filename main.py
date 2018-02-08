from __future__ import print_function
import datetime
import sys

sys.stdout.write("hello\r\n")
sys.stdout.write("this is {:%Y-%m-%d %H:%M:%S}\r\n".format(datetime.datetime.now()))
sys.stdout.write("this is stdout message.\r\n")
sys.stderr.write("this is stderr message.\r\n")
sys.stdout.write("i go exit. goodbye.")
sys.exit(0)
