# add_drop.py
# CSC 370
#
# Student Alex L. DEWEERT
# V00855767

import sys, csv, psycopg2

if len( sys.argv ) < 2:
	print( "Usage: %s <input file>", file=sys.stderr )
	sys.exit(0)

input_filename = sys.argv[1]

#Open DB Connection
try:
	conn = psycopg2.connect( dbname="alexand", user="alexand", host="studdb1.csc.uvic.ca", password="V00855767")
	#print("Connected!")
except:
	print("Error: Unable to connect to the database!")

cur = conn.cursor()

input_row = []
row_list = []
student_set = []

#Read in input to row lists
with open(input_filename) as f:
	for row in csv.reader(f):
		if len(row) == 0:
			continue #ignore blank row
		if len(row) < 4:
			print("Error: Invalid input line \"%s\""%(','.join(row)), file=sys.stderr)
			#Abort here if necessary
			break
		input_row = row[0:]
		row_list.append(input_row)

#Add students
for s in row_list:
	if s[1:3] not in student_set:
		student_set.append(s[1:3])
#student_set = set(student_set)
for s in student_set:
	#print(s)
	try: 
		cur.execute("""INSERT INTO students VALUES('{}','{}');""".format(s[0],s[1]))
		#conn.commit()
	except psycopg2.Error as e:
		conn.rollback()
		print(e.pgerror)

#Add to the enrollments table
for a in row_list:
	#print(a)
	try:
		if a[0] == 'ADD':
			cur.execute("""INSERT INTO enrollments VALUES('{}',{},'{}',null);""".format(a[3],a[4],a[1],a[3]))
		else:
			cur.execute("""DELETE FROM enrollments WHERE course_id = '{}' AND term_code = {} AND student_id = '{}';""".format(a[3],a[4],a[1]))
	except psycopg2.Error as e:
		conn.rollback()
		print(e.pgerror)

conn.commit()
cur.close()
conn.close()
