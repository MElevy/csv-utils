def write_row(csv,*row_values,a=False):
	if a==False and csv is not None:
		f=open(csv, 'w')
	elif a==True and csv is not None:
		f=open(csv,'a')
	for j,i in enumerate(row_values):
		if j is not len(row_values)-1:
			f.write(str(i)+',')
		else:
			f.write(str(i)+'\n')
	f.close()
def read(csv):
	f=open(csv, 'r')
	csv_values=[]
	for row in f:
		csv_row=row.split(',')
		for i,j in enumerate(csv_row):
			if csv_row[i].endswith('\n'):
				csv_row[i]=j[:-1]
			if csv_row[i]=='None':
				csv_row[i]=None
			elif j.isnumeric():
				csv_row[i]=int(j)
			elif csv_row[i].replace('.', '', 1).isdigit():
				csv_row[i]=float(j)
		csv_values.append(csv_row)
	f.close()
	return csv_values