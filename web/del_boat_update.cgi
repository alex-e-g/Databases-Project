#!/usr/bin/python3
import psycopg2, cgi
import login
form = cgi.FieldStorage()

#getvalue uses the names from the form in previous page
cni = form.getvalue('cni')
iso_code = form.getvalue('iso_code')
mmsi = form.getvalue('mmsi')

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Register</title>')
print('</head>')
print('<body>')
print('<h3>Confirmation of Update</h3>')

connection = None
try:
        # Creating connection
	connection = psycopg2.connect(login.credentials)
	cursor = connection.cursor()
        # Making query
	sql = 'DELETE FROM boat WHERE cni = %(cni)s and iso_code = %(iso_code)s;'
	data = {'cni':cni,'iso_code':iso_code}

	if mmsi is not None:
		sql_vhf = 'DELETE FROM boat_vhf WHERE cni = %(cni)s and iso_code = %(iso_code)s;'
		data_vhf = {'cni':cni,'iso_code':iso_code}
		cursor.execute(sql_vhf, data_vhf)


	cursor.execute(sql, data)
	print('Boat deleted successfully.')

	# Go back to homepage or add other 
	print('<p><a href="del_boat.cgi">Remove another Boat</a></p>')
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
