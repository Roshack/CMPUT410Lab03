#!/usr/bin/env python
 
print "Content-type: text/html\r\n"
 
print '<form method="post" action="test_form.py">'
print '<textarea name="comments" cols="40" rows="5">'
print 'Enter comments here...'
print '</textarea>'
print '<input type="submit" value="Submit">'
print '</form>'