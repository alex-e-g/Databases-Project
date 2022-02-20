#!/usr/bin/python3
import cgi

form_name = cgi.FieldStorage()

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Boat Management System</title>')
print('</head>')
print('<body>')
print('<h3>Register boat</h3>')

# The form will send the info needed for the SQL query 
print('<form action="add_boat_update.cgi" method="post">')

# Information on the new boat will be inserted here
print('<p>Name: <input type="text" name="name"/></p>')
print('<p>Year: <input type="text" name="year"/></p>')
print('<p>CNI: <input type="text" name="cni"/></p>')
print('<p>Iso Code: <input type="text" name="iso_code"/></p>')
print('<p>Owner Id: <input type="text" name="id_owner"/></p>')
print('<p>Owner Iso Code: <input type="text" name="iso_code_owner"/></p>')
print('<p>MMSI (optional) : <input type="text" name="mmsi"/></p>')

# Submit
print('<p><input type="submit" value="Submit"/></p>')
print('</form>')
print('</body>')
print('</html>')
