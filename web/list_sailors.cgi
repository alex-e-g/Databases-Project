#!/usr/bin/python3 
import psycopg2 
import login

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Boat Management System</title>')
print('</head>')
print('<body>')
print('<h3>List of Registered Sailors</h3>')

connection = None 
try:
        # Creating connection
	connection = psycopg2.connect(login.credentials) 
	cursor = connection.cursor()

        # Making query
	sql = "SELECT * FROM sailor";
	cursor.execute(sql)
	result = cursor.fetchall()
	num = len(result)

        # Displaying results
	print('<p><a href="homepage.cgi">Return to Homepage</a></p>')
	print('<p>Number of sailors registered: {}</p>'.format(num))
	print('<table border="1" cellspacing="0" style="width:15%;">') 
	print('<tr><th style="text-align:center">ID</th><th style="text-align:center">ISO Code</th></tr>')
	for row in result:
		print('<tr>')
		for value in row:
			print('<td style="text-align:center">{}</td>'.format(value))
		print('</tr>')
	print('</table>')       

        # Closing connection
	cursor.close()

except Exception as e:
        # Print errors on the webpage if they occur 
	print('<h1>An error occurred.</h1>') 
	print('<p> Please try again. Check if the values you wrote are valid.</p>')
finally:
	if connection is not None:
		connection.close()
print('</body>')
print('</html>')
