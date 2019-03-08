import os
import sys
import getopt
import oss2

# config
accessKeyId = 'accessKeyId'
accessKeySecret = 'accessKeySecret'
bucket = 'bucket'
endpoint = 'endpoint'

version = 'v0.0.2'
auth = oss2.Auth(accessKeyId, accessKeySecret)
sdk = oss2.Bucket(auth, endpoint, bucket)
pathArg = ""
saveArg = ""

def dir2oss(path, action='check'):
	dirArr = os.listdir(path)
	root = os.path.split(pathArg)[1]
	for file in dirArr:
		if(os.path.isdir(os.path.join(path, file))):
			dir2oss(os.path.join(path, file), action)
		else: 
			obj = saveArg + root + (path.replace(pathArg, '/').replace('\\', '/') + '/').replace('//', '/') + file
			if action == 'save':
				sdk.put_object_from_file(obj, os.path.join(path, file))
				print('saved ==> ' + obj)
			else:
				print('==> ' + obj)


def file2oss(file):
	filename = os.path.split(file)[1]
	obj = saveArg + filename
	sdk.put_object_from_file(obj, file)
	print('saved ==> ' + obj)

if __name__ == '__main__':
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'hvp:s:f:', ['help', 'version', 'path=', 'save=', 'file='])
	except getopt.GetoptError:
		print('ParamError: upload.py -p <localpath>')
		sys.exit()
	action = 'dir'
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print('usage: upload.py -p <localpath>')
			sys.exit()
		elif opt in ("-v", "--version"):
			print(version)
			sys.exit()
		elif opt in ("-p", "--path"):
			pathArg = arg
		elif opt in ("-s", "--save"):
			saveArg = arg
		elif opt in ("-f", "--file"):
			action = 'file'
			pathArg = arg
	if action == 'file':
		file2oss(pathArg)
	else:
		dir2oss(pathArg)
		print('Sure? y/n')
		sure = raw_input()
		if sure == 'y':
			dir2oss(pathArg, 'save')
		else:
			os._exit(0)