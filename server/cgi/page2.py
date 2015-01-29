#!/usr/bin/env python
import cgi
print "Content-type: text/html\r\n"
 
form = cgi.FieldStorage()
 
fn = form.getvalue('FirstName')
ln = form.getvalue('LastName')
print ""

if (fn):
 print "First Name: " + fn + "</br>"
if (ln):
 print "Last Name: " + ln + "</br>"

print '<form method="post" action="page1.py">'
print 'Birth Date: <textarea name="Birthday" cols="40" rows="1">'
print '</textarea>'
print '</br>'
print 'Main Hobby <textarea name="MainHobby" cols="40" rows="1">'
print '</textarea>'
print '<input type="submit" value="Submit">'
print '</form>'