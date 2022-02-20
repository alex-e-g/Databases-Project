#!/usr/bin/python3 
import cgi
form = cgi.FieldStorage()
print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Boat Management System</title>') 
print('</head>')
print('<body>')
print('<h3>Register owner</h3>')

# The form will send the info needed for the SQL query 
print('<form action="add_owner_update.cgi" method="post">') 

# Information on the new owner will be inserted here
print('<p>Name: <input type="text" name="name"/></p>')
print('<p>ID: <input type="text" name="id"/></p>') 
print('<p>Country ISO code: <input type="text" name="iso_code"/></p>')
print('<p>Birthdate: <input type="date" name="birthdate"/></p>')

# Submit
print('<p><input type="submit" value="Submit"/></p>') 
print('</form>')
print('</body>')
print('</html>')
