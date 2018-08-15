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

# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Welcome to Chronicle! login')
#         user = users.get_current_user()
#         if user:
#             email_address = user.nickname()
#             cssi_user = CssiUser.get_by_id(user.user_id())
#             signout_link_html = '<a href="%s">sign out</a>' % (
#                 users.create_logout_url('/'))
#             if cssi_user:
#                 self.response.write('''
#                      Welcome %s %s (%s)! <br> %s <br>''' % (
#                         cssi_user.first_name,
#                         cssi_user.last_name,
#                         email_address,
#                         signout_link_html))
# #        if user is not None:
# #            self.response.write(' hello notes:')
# #            logout_url=users.create_logout_url(self.request.url)
# #            template_context={
# #                    'user':user.nickname(),
# #                    'logout_url': logout_url,
# #            }
# #            template = jinja_env.get_template('main.html')
# #            self.response.out.write(
# #                        template.render(template_context))
#             else:
#                 self.response.write('''
#                     Welcome to our site, %s! Please sign up! <br>
#                     <form method="post" action="/">
#                     <input type="text" name="first_name">
#                     <input type="text" name="last_name">
#                     <input type="submit">
#                     </form><br> %s <br>
#                     '''%(email_address, signout_link_html))
#         else:
#             self.response.write('''
#                 Please log in to use the site<br>
#                 <a href="%s">sign in</a>'''% (
#                     users.create_login_url('/'))
#                 )
#
#     def post(self):
#         user = users.get_current_user()
#         if not user:
#       # You shouldn't be able to get here without being logged in
#             self.error(500)
#             return
#         cssi_user = CssiUser(
#             first_name=self.request.get('first_name'),
#             last_name=self.request.get('last_name'),
#             id=user.user_id())
#         cssi_user.put()
#         self.response.write('Thanks for signing up, %s!' %
#             cssi_user.first_name)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/main.html')
        current_user = users.get_current_user()
        if not current_user:
            self.response.write(template.render({
                'login_url': users.create_login_url('/'),
            }))
        else:
            self.response.write(template.render({
                'logout_url': users.create_logout_url('/'),
            }))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
