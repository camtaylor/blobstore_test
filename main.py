import cgi
import webapp2
import time
from google.appengine.ext import ndb
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.blobstore import BlobKey
from google.appengine.api import images
from webapp2_extras import sessions, auth, json
import datetime
import json
from time import sleep


class BlobHolder(ndb.Model):
  upload_date = ndb.DateTimeProperty(auto_now_add=True)
  blob_key = ndb.BlobKeyProperty()

class FileUploadFormHandler(webapp2.RequestHandler):
  '''
   blob form
  '''
  def get(self):
    upload_url = blobstore.create_upload_url('/create')
    self.response.out.write(upload_url)

class BlobUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
  '''
  Posts to database the uploaded blob 

  '''
  def post(self):
    uploaded_blob = BlobHolder()
    upload = self.get_uploads()[0]
    uploaded_blob.blob_key = upload.key()
    uploaded_blob.put()
    self.response.out.write("blob written")

app = webapp2.WSGIApplication([
                                ('/', FileUploadFormHandler),
                                ('/create', BlobUploadHandler),
], debug=True)

