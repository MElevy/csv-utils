def read(filename,titles=[]):
	with open(filename, 'r') as f:
		csv_values={}
		for o,row in enumerate(f):
			csv_row=row.split(',')
			for i,j in enumerate(csv_row):
				if csv_row[i].endswith('\n'):
					csv_row[i]=j[:-1]
				if csv_row[i]=='None':
					csv_row[i]=None
				elif csv_row[i].isnumeric():
					csv_row[i]=int(j)
				elif csv_row[i].replace('.', '', 1).isdigit():
					csv_row[i]=float(j)
			try:
				title=titles[o]
			except Exception as e:
				title=csv_row.pop(0)
			csv_values[title]=csv_row
		return csv_values
def write_row(filename,  *values, a=False):
	if a==False:
		with open(filename, 'w'):
			for j,i in enumerate(row_values):
				if j is not len(row_values)-1:
					f.write(str(i)+',')
				else:
					f.write(str(i)+'\n')
	elif a==True:
		with open(filename, 'a'):
			for j,i in enumerate(row_values):
				if j is not len(row_values)-1:
					f.write(str(i)+',')
				else:
					f.write(str(i)+'\n')
	else:
		raise Exception(str(a)+' is not a valid mode')