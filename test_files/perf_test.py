import time
import os

with open("perf_log.dat", "w+") as fout:
    print(0, str(time.time_ns()), file=fout)
    for i in range(10 ** 2):
        rb16 = os.urandom(16) # random bytes 16
        print(i+1, str(time.time_ns()), file=fout)