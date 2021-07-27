class csv:
	def __init__(self, csv_name, mode):
		self.f=open(csv_name, mode)
	def write_row(self, *row_values):
		for j,i in enumerate(row_values):
			if j is not len(row_values)-1:
				self.f.write(str(i)+',')
			else:
				self.f.write(str(i)+'\n')
	def close(self):
		self.f.close()
	def read(self):
		csv_values=[]
		for row in self.f:
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
		return csv_values