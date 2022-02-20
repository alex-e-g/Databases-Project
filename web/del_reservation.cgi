#!/usr/bin/python3 
import cgi
form = cgi.FieldStorage()
print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Boat Management System</title>') 
print('</head>')
print('<body>')
print('<h3>Delete reservation</h3>')

# The form will send the info needed for the SQL query 
print('<form action="del_reservation_update.cgi" method="post">') 

# Information on the new reservation will be inserted here
print('<p>CNI(boat): <input type="text" name="cni"/></p>')
print('<p>Country ISO code of boat: <input type="text" name="iso_code_boat"/></p>')
print('<p>ID of Sailor: <input type="text" name="id_sailor"/></p>') 
print('<p>Country ISO code of Sailor: <input type="text" name="iso_code_sailor"/></p>')
print('<p>Start date: <input type="date" name="start_date"/></p>')
print('<p>End date: <input type="date" name="end_date"/></p>')

# Submit
print('<p><input type="submit" value="Submit"/></p>') 
print('</form>')
print('</body>')
print('</html>')
