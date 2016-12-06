from DocProcessor import ProcessDocuments




if __name__ == '__main__':
	
	x = ProcessDocuments()
	x.readFiles()
	x.convert2PDF()
	x.convert2HTML()
