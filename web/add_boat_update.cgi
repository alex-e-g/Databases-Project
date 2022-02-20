#!/usr/bin/python3
import psycopg2, cgi
import login

form = cgi.FieldStorage()

#getvalue uses the names from the form in previous page
name = form.getvalue('name')
year = form.getvalue('year')
cni = form.getvalue('cni')
iso_code = form.getvalue('iso_code')
id_owner = form.getvalue('id_owner')
iso_code_owner = form.getvalue('iso_code_owner')
mmsi = form.getvalue('mmsi')

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
	sql = 'INSERT INTO boat(name,year,cni,iso_code,id_owner,iso_code_owner) VALUES (%(name)s,%(year)s,%(cni)s,%(iso_code)s,%(id_owner)s,%(iso_code_owner)s);'
	data = {'name':name,'year':year,'cni':cni,'iso_code':iso_code,'id_owner':id_owner,'iso_code_owner':iso_code_owner}
	cursor.execute(sql, data)

	if mmsi is not None:
		sql_vhf = 'INSERT INTO boat_vhf(mmsi,cni,iso_code) VALUES (%(mmsi)s,%(cni)s,%(iso_code)s);'
		data_vhf = {'mmsi':mmsi,'cni':cni,'iso_code':iso_code}
		cursor.execute(sql_vhf, data_vhf)

	print('Boat added successfully.')
	
	# Go back to homepage or add other
	print('<p><a href="add_boat.cgi">Register another Boat</a></p>')
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
