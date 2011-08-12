import dicom
import glob
from pymongo import Connection


""" Open up a mongo connection """
connection = Connection()
db = connection.fdatest
coll = db.full

""" Parsing the files and populating the db """
dirs = glob.glob("*")
tops = [glob.glob(d + "/*") for d in dirs]
topFiles = list()
for t in tops:
  if len(t) > 0:
    for i in t:
      topFiles.append(i)
for i,j in enumerate(topFiles):
  doc = dict()
  data = dicom.read_file(j)
  doc['filename'] = j
  for elt in data.keys():
    try:
      tagName = dicom.datadict.get_entry(elt)[2]
      if len(tagName) > 0:
        print tagName
        print data[elt].repval
        doc[tagName] = data[elt].repval
    except KeyError:
      pass
  coll.insert(doc)
