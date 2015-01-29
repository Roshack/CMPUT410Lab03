#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8005)
handler.cgi_directories = ["/cgi"]
 
httpd = server(server_address, handler)
httpd.serve_forever()