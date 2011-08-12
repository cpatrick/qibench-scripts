import glob
import subprocess as sp
dirs = glob.glob("*")
tops = [glob.glob(d + "/*") for d in dirs]
topFiles = list()
for t in tops:
  if len(t) > 0:
    for i in t:
      res = '/usr/bin/python /home/cpatrick/getImageFormation.py /data/1A/PIVOTAL/' + i
      sp.call(res,shell=True)
      break
