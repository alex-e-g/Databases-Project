#!/usr/bin/python3 
import psycopg2, cgi 
import login
form = cgi.FieldStorage()

# Get values from the form in previous page 
cni = form.getvalue('cni')
id_sailor = form.getvalue('id_sailor')
iso_code_sailor = form.getvalue('iso_code_sailor')
iso_code_boat = form.getvalue('iso_code_boat')
start_date = form.getvalue('start_date')
end_date = form.getvalue('end_date')

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
	sql_trip = "DELETE FROM trip WHERE cni=%(cni)s AND iso_code_boat=%(iso_code_boat)s AND id_sailor=%(id_sailor)s AND iso_code_sailor=%(iso_code_sailor)s AND start_date=%(start_date)s AND end_date=%(end_date)s";
	sql_reservation = "DELETE FROM reservation WHERE cni=%(cni)s AND iso_code_boat=%(iso_code_boat)s AND id_sailor=%(id_sailor)s AND iso_code_sailor=%(iso_code_sailor)s AND start_date=%(start_date)s AND end_date=%(end_date)s";
	sql_schedule = "DELETE FROM schedule WHERE start_date=%(start_date)s AND end_date=%(end_date)s";
	data = {'cni':cni,'iso_code_boat':iso_code_boat,'id_sailor':id_sailor,'iso_code_sailor':iso_code_sailor,'start_date':start_date,'end_date':end_date}
	data_schedule = {'start_date':start_date,'end_date':end_date}

	cursor.execute(sql_trip, data)
	cursor.execute(sql_reservation, data)
	cursor.execute(sql_schedule, data_schedule)
	print('Reservation removed successfully.')

	# Go back to homepage or add other 
	print('<p><a href="del_reservation.cgi">Remove another reservation</a></p>')
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
