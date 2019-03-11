# Copyright 2016 Google Inc.
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

import webapp2
import socket 

#global
server_ip = socket.gethostbyname(socket.gethostname())

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        a = 2**2**2**2**2
        self.response.write(str(a))

    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        result = 2**2**2**2**2
        self.response.write(server_ip + "\n")
        self.response.write(str(self.request.remote_addr) + "\n") #client IP
        self.response.write("2**2**2**2**2 = " + str(result))
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)