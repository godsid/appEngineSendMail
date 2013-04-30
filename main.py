#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import mail

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("""<pre> 
			Example:<br/>
				URL: http://samartwebservice.appspot.com/mail<br/>
				METHOD: POST<br/>
				Parameter:<br/>
						sender*		:	Email of Sender<br/>
						to*		:	Destination email address<br/>
						subject	*	:	Subject of Email<br/>
						cc		:	Destination email address on CC<br/>
						bcc		:	Destination email address on BCC<br/>
						reply_to	:	Email to reply this mail<br/>
						body		:	Email message <br/>
						ishtml		:	Email message is html <br/>
						attachments	:	Email attachments files<br/></pre>
		""")
class SendMail(webapp2.RequestHandler):
	def post(self):
		sender = "samartmultimedia@gmail.com"
		to = self.request.post('to')
		error = False
		errorMsg = ""
		if not mail.is_email_valid(to):
			errorMsg = "to Email is invalid"
			error = True
		elif not self.request.post('subject'):
			errorMsg = "Subject is invalid"
			error = True
		if error:
			self.response.write(errorMsg)
		else:
			message = mail.EmailMessage()
			message.sender = sender
			message.to = to
			message.subject = self.request.post('subject')
			if self.request.post('ishtml') :
				message.html = self.request.post('body')
			else:
				message.body = self.request.post('body')
			if self.request.post('cc'):
				message.cc = self.request.post('cc')
			if self.request.post('bcc'):
				message.bcc = self.request.post('bcc')
			if self.request.post('reply_to'):
				message.reply_to = self.request.post('reply_to')
			message.send()
			self.response.write("Success")
			
		
		#mail.send_mail(sender="Webmaster Horoworld<samartmultimedia@gmail.com>",	 
		#						to=self.request.post('to'),
		#						subject=self.request.post('subject'),
		#						body="testtt",
		#						reply_to="no-reply@horoworld.com"
		#)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/mail', SendMail)
], debug=True)
