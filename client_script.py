import requests
import sys

def upload_blob(filename):
  url = "http://localhost:8080"
  r = requests.get(url)
  requests.post(r.content, files={'file': (filename, open(filename, 'rb'), 'application/pdf')})
  requests.post(url+"/create")

if __name__ == "__main__":
  upload_blob(sys.argv[1])                                                                              
