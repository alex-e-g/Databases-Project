#!/usr/bin/python3 
import psycopg2, cgi 
import login
form = cgi.FieldStorage()

# Get values from the form in previous page 
name = form.getvalue('name')
id = form.getvalue('id')
iso_code = form.getvalue('iso_code')

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
	sql_person = "INSERT INTO person(id, name, iso_code) VALUES (%(id)s, %(name)s, %(iso_code)s)";
	sql_sailor = "INSERT INTO sailor(id, iso_code) VALUES(%(id)s, %(iso_code)s)";

	data_person = {'id':id,'name':name,'iso_code':iso_code}
	data_sailor = {'id':id, 'iso_code':iso_code}

	cursor.execute(sql_person, data_person)
	cursor.execute(sql_sailor, data_sailor)
	print('Sailor added successfully.')

	#Go back to homepage or add other
	print('<p><a href="add_sailor.cgi">Register another sailor</a></p>')
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
