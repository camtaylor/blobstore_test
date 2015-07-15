import requests
import sys
import os
from time import time

def create_file(filename, file_size):
  with open(filename, 'wb') as fout:
    fout.write(os.urandom(file_size))
  upload_blob(filename, file_size)

def upload_blob(filename, file_size):
  url = "http://localhost:8080"
  r = requests.get(url)
  before_request = time()
  print "Uploading blob..."
  requests.post(r.content, files={'file': (filename, open(filename, 'rb'), 'application/pdf')})
  after_request = time()
  latency = after_request - before_request
  print "Blob size: {}".format(file_size)
  print "Latency: {}".format(latency)

if __name__ == "__main__":
  i = 1
  while i <= 256:
    create_file('example.txt',(1048576 * i))
    i*=2
