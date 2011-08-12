x = open('good_runs.out')
for i in x.readlines():
  if i.startswith('Arguments'):
    j = i.split()
    k = j[5].split('/')
    l = k[8]
    m = l.split('_')
    res = '%s,%s,%s,%s,%s,%s' % (m[0],m[1],m[2],'1','Volumetric',m[0])
  if i.startswith('Volume'):
    n = i.split()[-1]
    print '%s,%s' % (res,n)
  
y = open('segs_failed.out')
for i in y.readlines():
  if i.startswith('Arguments'):
    j = i.split()
    k = j[5].split('/')
    l = k[8]
    m = l.split('_')
    res = '%s,%s,%s,%s,%s,%s,%s' % (m[0],m[1],m[2],'1','Volumetric',m[0],'-1')
    print res

z = open('no_overlap.out')
for i in z.readlines():
  if i.startswith('Arguments'):
    j = i.split()
    k = j[5].split('/')
    l = k[8]
    m = l.split('_')
    res = '%s,%s,%s,%s,%s,%s,%s' % (m[0],m[1],m[2],'1','Volumetric',m[0],'-1')
    print res
