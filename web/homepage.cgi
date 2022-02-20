#!/usr/bin/python3 
import psycopg2
import login
print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Boat Management System</title>') 
print('</head>')
print('<body>')
print('<h3>Boat Management System</h3>')
print('<p>Welcome to the Boating Management System!</p>')
print('<p> Here, you can add or remove boats, owners, sailors and reservations from the system, as well as list all boat sailors registered.</p>')
print('<iframe src="https://gifer.com/embed/6b2" width=480 height=276.480 frameBorder="0" allowFullScreen align="right"></iframe>')
connection = None
try:
        # Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()

        # List options to user
	print('<p><a href="owner.cgi">Register or remove owners</a></p>')
	print('<p><a href="boat.cgi">Register or remove boats</a></p>')
	print('<p><a href="sailor.cgi">Insert, list and remove boat sailors</a></p>')
	print('<p><a href="reservations.cgi">Create and remove reservations</a></p>')

        # Closing connection
	cursor.close() 

except Exception as e:
        # Print errors on the webpage if they occur 
	print('<h1>An error occurred.</h1>') 
finally:
	if connection is not None:
		connection.close()

print('</body>')
print('</html>')
