#!/usr/bin/python3 
import psycopg2, cgi 
import login
form = cgi.FieldStorage()

# Get values from the form in previous page 
name = form.getvalue('name')
id = form.getvalue('id')
iso_code = form.getvalue('iso_code')
birthdate = form.getvalue('birthdate')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Boat Management System</title>')
print('</head>')
print('<body>')
print('<h3>Confirmation of Update</h3>')

connection = None 
try:
        # Creating connection
	connection = psycopg2.connect(login.credentials) 
	cursor = connection.cursor()

        # Making query
	sql_owner = "DELETE FROM owner WHERE id=%(id)s and iso_code=%(iso_code)s";
	sql_person = "DELETE FROM person WHERE id=%(id)s and iso_code=%(iso_code)s";

	data = {'id':id,'iso_code':iso_code}

	cursor.execute(sql_owner, data)
	cursor.execute(sql_person, data)
	print('Owner removed successfully.')

	# Go back to homepage or add other 
	print('<p><a href="del_owner.cgi">Remove another owner</a></p>')
	print('<p><a href="homepage.cgi">Return to Homepage</a></p>')

        # Commit the update (without this step the database will not change)
	connection.commit()

        # Closing connection
	cursor.close()

except Exception as e:
        # Print errors on the webpage if they occur 
	print('<h1>An error occurred.</h1>') 
	print('<p> Please try again. Check if the values you wrote are valid.</p>')
	connection.rollback()
finally:
	if connection is not None:
		connection.close()
print('</body>')
print('</html>')
