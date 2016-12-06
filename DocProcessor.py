import os

class ProcessDocuments:
   
    def __init__(self):
        self.fileList = []
    
    '''this method reads files to be processed and return the list of those files'''
    def readFiles(self):
        import os
        p = os.popen("ls *.docx","r")
        
        while 1:
            fileName = p.readline()
            if not fileName: break
            fileName = fileName[:-1]   # removes null character from end of fileName
            self.fileList.append(fileName)
            
        return self.fileList
    
    '''method to convert docx files into pdf''' 
    def convert2PDF(self):
        
        N = len(self.fileList)
         
        for i in range(0,N):
            print "Converting %s to pdf "%self.fileList[i]
            os.system("abiword --to=pdf %s"%self.fileList[i])  # Convert docx to pdf           
         
        os.system("mkdir PDFs")
        os.system("mv *.pdf PDFs")
        
    '''converts generated PDFs to HTML format'''   
    def convert2HTML(self):
        
        os.system("mkdir ~/pdf")  #temporary directory
        htmlFiles=[]
        p = os.popen("ls PDFs/","r")
        while 1:
            filename = p.readline()
            if not filename: break
            filename = filename[0:-1]
            htmlFiles.append(filename)
        
        N = len(htmlFiles)
        os.system("cp PDFs/*.pdf ~/pdf/")
        for i in range(0,N):  
            os.system("docker run -ti --rm -v ~/pdf:/pdf bwits/pdf2htmlex pdf2htmlEX --zoom 1.3 %s"%htmlFiles[i])
           
        os.system("mkdir HTMLs")
        os.system("mv ~/pdf/*.html HTMLs/")
        os.system("rm -r ~/pdf/")
    


            
            
            
