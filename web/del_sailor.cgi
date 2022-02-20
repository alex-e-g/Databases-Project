#!/usr/bin/python3 
import cgi
form = cgi.FieldStorage()
print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Boat Management System</title>') 
print('</head>')
print('<body>')
# The string has the {}, the variables inside format() will replace the {} 
print('<h3>Remove sailor</h3>') 

# The form will send the info needed for the SQL query 
print('<form action="del_sailor_update.cgi" method="post">') 

# Information on the new sailor will be inserted here
print('<p>ID: <input type="text" name="id"/></p>') 
print('<p>Country ISO code: <input type="text" name="iso_code"/></p>')

# Submit
print('<p><input type="submit" value="Submit"/></p>') 
print('</form>')
print('</body>')
print('</html>')
