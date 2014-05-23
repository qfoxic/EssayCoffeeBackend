import os
import errno
import itertools
from datetime import datetime
from django.conf import settings
from django.core.exceptions import SuspiciousFileOperation
from django.core.files import locks, File
from django.core.files.move import file_move_safe
from django.utils.encoding import force_text, filepath_to_uri
from django.utils.functional import LazyObject
from django.utils.module_loading import import_by_path
from django.utils.six.moves.urllib.parse import urljoin
from django.utils.text import get_valid_filename
from django.utils._os import safe_join, abspathu
from django.core.files.utils import FileProxyMixin
from django.utils.encoding import force_bytes, python_2_unicode_compatible
from ftplib import FTP, error_perm, error_reply, error_temp
from django.core.files.storage import Storage
from django.db.models.fields import files
from StringIO import StringIO


class FTPStorage(Storage):
    def __init__(self, location=None, base_url=None):
      self.session = FTP()
      try:
        host, port, user, passwd = settings.FTP_DATA
      except ValueError:
        # Fallback to some unexistent data.
        host, port, user, passwd = '127.0.0.1', 21, 'anonimous', '123' 
      self.session.connect(host, port)
      self.session.login(user, passwd)
      self.session.set_pasv(True)
      
    def _save(self, name, content):
      try:
        username, filename = name.split('/')
      except ValueError:
        return
      try:
        self.session.cwd('/')
        self.session.mkd(username)
      except error_perm:
        pass
      self.session.cwd('/' + username)
      self.session.storbinary('STOR ' + filename, content)
      return name 

    def delete(self, name):
      assert name, 'The name argument is not allowed to be empty.'
      self.session.delete(self.path(name))

    def exists(self, name):
      try:
        self.session.retrlines('LIST /' + self.path(name))
        return True
      except error_temp:
        return False

    def cp(self, name, file_obj, mode='rwb'):
      """Copy ftp file 'name' to file_obj."""
      self.session.cwd('/')
      ftp_answer = self.session.retrbinary('RETR ' + self.path(name), file_obj.write)
      file_obj.flush()
      self.session.cwd('/')

    def listdir(self, path):
        path = self.path(path)
        directories, files = [], []
        for entry in os.listdir(path):
            if os.path.isdir(os.path.join(path, entry)):
                directories.append(entry)
            else:
                files.append(entry)
        return directories, files

    def path(self, name):
        return '/'+ name

    def size(self, name):
        self.session.voidcmd('TYPE I') 
        return self.session.size(self.path(name))

    def accessed_time(self, name):
        return None
        #return datetime.fromtimestamp(os.path.getatime(self.path(name)))

    def created_time(self, name):
        return None
        #return datetime.fromtimestamp(os.path.getctime(self.path(name)))

    def modified_time(self, name):
        return None
        #return datetime.fromtimestamp(os.path.getmtime(self.path(name)))
    
    def close(self):
      self.session.close()

