from google.appengine.api import users

import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):

        user = user.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())

        else:
            self.redirect(user.create_login_url(self.request.uri))


    application = webapp2.WSGIApplication([
        ('http://plato.cs.virginia.edu/~cso4tb/ms5/', MainPage),
        ], debug=True)
