#!/usr/bin/python2.7
#main.py


import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class CssiUser(ndb.Model):
     first_name = ndb.StringProperty()
     last_name = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('main.html')
        current_user = users.get_current_user()
        if not current_user:
            self.response.write(template.render({
                'login_url': users.create_login_url('/'),
            }))
        else:
            self.response.write(template.render({
                'logout_url': users.create_logout_url('/'),
            }))
        if not current_user:
            self.redirect(users.create_login_url('/Chronicle'))

class CalendarPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('index.html')
        self.response.write(template.render({
            'logout_url': users.create_logout_url('/'),
            }))
            
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/Chronicle', CalendarPage)
], debug=True)
