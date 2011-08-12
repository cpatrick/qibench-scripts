import dicom
import sys

if __name__ == '__main__':
  data = dicom.read_file(sys.argv[1])
  print data
