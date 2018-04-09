import psycopg2, sys

def print_row(term, course_code, course_name, instructor_name, total_enrollment, maximum_capacity):
	print("%6s %10s %-35s %-25s %s/%s"%(str(term), str(course_code), str(course_name), str(instructor_name), str(total_enrollment), str(maximum_capacity)) )

# Mockup: Print some data for a few made up classes

print_row(201709, 'CSC 106', 'The Practice of Computer Science', 'Bill Bird', 203, 215)
print_row(201709, 'CSC 110', 'Fundamentals of Programming: I', 'Jens Weber', 166, 200)
print_row(201801, 'CSC 370', 'Database Systems', 'Bill Bird', 146, 150)