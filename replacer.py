#from __future__ import print_function
import time
from datetime import date
from datetime import timedelta
import os
import re
from dateutil.relativedelta import relativedelta


def rep1(matchobj):
    delta = matchobj.group(0)[2:-2]
    newdate = date.today() + eval(delta)
    return newdate.strftime("%Y%m%d")


for filename in os.listdir("."):
    if filename.endswith(".template"):
        outfilename = re.sub(r".template", "", filename)
        of = open(outfilename, 'w')
        with open(filename) as f:
            for line in f:
                # print(line)
                line = re.sub(r"#(.*?)#", rep1, line)
                print(line)
        continue
    else:
        continue
