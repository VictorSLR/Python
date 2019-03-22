import csv

e = open('employees_data.csv', 'r') #employees system data file
csv_e = csv.reader(e)

w = open('web_data.csv', 'r') #file from web, to be updated
csv_w = csv.reader(w)

r = open('report.txt', 'w') #report file

r.write("Woolamaloo Synchronization Report\n") #report file header
r.write("---------------------------------\n\n")
r.write("ID\tName => Status\n")

next(csv_e)
next(csv_w)

for row_e in csv_e:
	w.seek(0)
	for row_w in csv_w:
		if  row_e[0] == row_w[1]: #compares id/employeeNumber, to make sure it's the same person
			if row_e[4] != row_w[4]: #compares department
				r.write("%s\t%s => Changed department. Was %s, now it is %s\n" % (row_e[0], row_e[1], row_w[4], row_e[4]))
				break
			elif row_e[5] != row_w[5]: #compares position
				r.write("%s\t%s => Changed position. Was %s, now it is %s\n" % (row_e[0], row_e[1], row_w[5], row_e[5]))
				break
			elif row_e[3] != "": #checks if the employee is not working in the Woolamaloo anymore
				r.write("%s\t%s => Worked with the Woolamaloo from %s to %s\n" % (row_e[0], row_e[1], row_e[2], row_e[3]))
				break
			else:
				break
	if row_e[0] != row_w[1]: #checks if there's someone new who is not in the web file
		r.write("%s\t%s => Is a new employee. Joined the Woolamaloo in %s\n" % (row_e[0], row_e[1], row_e[2]))

e.close()
w.close()