import os
import sys

#os.path.isdir();
def grap(tarDir,tarStrs):
	
	resultList = {}
	
	fileNames = os.listdir(tarDir)
	print fileNames
	
	print "the tar string to find is "+tarStrs
	for fn in fileNames:
		if  os.path.isdir(fn):
			pass
		else:
			if os.access(fn, os.R_OK):
				with open(fn) as fp:
					content = fp.read()
					tarIndex = content.find(tarStrs)
					
					
					if( tarIndex != -1):
						#print content[100:200]
						resultList[fn] = content[tarIndex - 20:tarIndex + len(tarStrs)+20]
					#print fp.read()
	
	return resultList
if __name__ == "__main__":	
	if len(sys.argv) == 1 :
		print 'pls input the folder and string you want to find '
	else:
		print sys.argv[:]
		result = grap(sys.argv[1],sys.argv[2])
		print result

	
	
