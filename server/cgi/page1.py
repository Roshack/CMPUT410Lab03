#!/usr/bin/env python
import cgi
print "Content-type: text/html\r\n"
 
form = cgi.FieldStorage()
 
bd = form.getvalue('Birthday')
hobby = form.getvalue('MainHobby')
print ""

if (bd):
 print "Birthday: " + bd + "</br>"
if (hobby):
 print "Main Hobby: " + hobby + "</br>"
print '<form method="post" action="page2.py">'
print 'First Name: <textarea name="FirstName" cols="40" rows="1">'
print '</textarea>'
print '</br>'
print 'Last Name: <textarea name="LastName" cols="40" rows="1">'
print '</textarea>'
print '<input type="submit" value="Submit">'
print '</form>'