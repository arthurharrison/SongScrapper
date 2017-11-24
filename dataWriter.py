import xlsxwriter

def xlsxWriter(data1, data2 , path):
	data = ()
	if(len(data2) != 0 ):
		for i in range(len(data1)):
			data += ([data1[i],str(data2[i])],)
	else:
		raise NameError('Error in the Parameters of the function')	

	workbook = xlsxwriter.Workbook(path + ".xlsx")
	worksheet = workbook.add_worksheet()
	bold = workbook.add_format({'bold': 1})
	worksheet.write('A1', 'Word', bold)
	worksheet.write('B1', 'Value', bold)

	row = 1
	col = 0
	for word, value in data:
		worksheet.write_string(row, col, word)
		worksheet.write_number(row, col + 1, int(value))
		row += 1
	workbook.close()

#Debugger
if __name__ == "__main__":
	list1 = ['a','b','c','d','e']
	list2 = [1,2,3,4,5]
	path = "output.xlsx"
	xlsxWriter(list1, list2, path)