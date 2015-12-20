#!/usr/bin/python

import BaseHTTPServer
from socket import gethostname

PORT_NUMBER = 80

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):
    s.send_response(200)
    s.send_header("Content-type", "text/plain")
    s.end_headers()
    s.wfile.write("My hostname: %s\r\n" % gethostname())
    s.wfile.write("Requested using protocol %s\r\n" % s.request_version)
    s.wfile.write("Your originating IP/Port: %s:%s\r\n" % s.client_address)
    s.wfile.write("Request path: %s\r\n" % s.path)
    s.wfile.write("Request Headers:\r\n%s" % s.headers)

if __name__ == '__main__':
  server_class = BaseHTTPServer.HTTPServer
  httpd = server_class(("", PORT_NUMBER), MyHandler)
  print ("Server listening on port %d" % PORT_NUMBER)
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  httpd.server_close()
  print ("Server shutting down...")
