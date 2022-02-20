#!/usr/bin/python3 
import psycopg2
import login
print('Content-type:text/html\n\n') 
print('<html>')
print('<head>')
print('<title>Boat Management System</title>') 
print('</head>')
print('<body>')
print('<h3>Reservations</h3>')
connection = None 
try:
        # Creating connection
	connection = psycopg2.connect(login.credentials) 
	cursor = connection.cursor()

        # List options to user: add or remove owners
	print('<p><a href="add_reservation.cgi">Add Reservation</a></p>')
	print('<p><a href="del_reservation.cgi">Remove Reservation</a></p>')

        # Closing connection
	cursor.close() 

except Exception as e:
        # Print errors on the webpage if they occur 
	print('<h1>An error occurred.</h1>') 
	print('<p>Please try again.</p>')
finally:
	if connection is not None:
		connection.close()

print('</body>')
print('</html>')
