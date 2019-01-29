import os
import sys
import getopt
import oss2

# config
accessKeyId = 'accessKeyId'
accessKeySecret = 'accessKeySecret'
bucket = 'bucket'
endpoint = 'endpoint'

auth = oss2.Auth(accessKeyId, accessKeySecret)
sdk = oss2.Bucket(auth, endpoint, bucket)
pathArg = ""
saveArg = ""

def dir2oss(path):
	dirArr = os.listdir(path)
	root = os.path.split(pathArg)[1]
	for file in dirArr:
		if(os.path.isdir(os.path.join(path, file))):
			dir2oss(os.path.join(path, file))
		else: 
			obj = saveArg + root + (path.replace(pathArg, '/').replace('\\', '/') + '/').replace('//', '/') + file
			sdk.put_object_from_file(obj, os.path.join(path, file))
			print('saved ==> ' + obj)

if __name__ == '__main__':
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'hvp:s:', ['help', 'version', 'path=', 'save='])
	except getopt.GetoptError:
		print('ParamError: upload.py -p <localpath>')
		sys.exit()
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print('usage: upload.py -p <localpath>')
			sys.exit()
		elif opt in ("-v", "--version"):
			print('v0.0.1')
			sys.exit()
		elif opt in ("-p", "--path"):
			pathArg = arg
		elif opt in ("-s", "--save"):
			saveArg = arg
	dir2oss(pathArg)