import sys
import os.path
import uuid
from glob import glob
from datetime import datetime

class HttpServer:
	def __init__(self):
		self.sessions={}
		self.types={}
		self.types['.pdf']='application/pdf'
		self.types['.jpg']='image/jpeg'
		self.types['.txt']='text/plain'
		self.types['.html']='text/html'
	def response(self,messagebody='',headers={}):
		tanggal = datetime.now().strftime('%c')
		resp=[]
		resp.append(messagebody)
		# resp.append("HTTP/1.0 {} {}\r\n" . format(kode,message))
		# resp.append("Date: {}\r\n" . format(tanggal))
		# resp.append("Connection: close\r\n")
		# resp.append("Server: myserver/1.0\r\n")
		# resp.append("Content-Length: {}\r\n" . format(len(messagebody)))
		# for kk in headers:
		# 	resp.append("{}:{}\r\n" . format(kk,headers[kk]))
		# resp.append("{}" . format(messagebody))
		response_str=''
		for i in resp:	
			response_str="{}{}" . format(response_str,i)
		return response_str

	def proses(self,data):
		
		requests = data.split("\r\n")
		baris = requests[0]

		print(baris)
		j = baris.split(" / ")
		try:
			method=j[0].upper().strip()
			if (method=='GET'):
				object_address = j[1].strip()
				return self.http_get(object_address)
			else:
				return self.response(400,'Bad Request','',{})
		except IndexError:
			return self.response(400,'Bad Request','',{})
	def http_get(self,object_address):

		if object_address!='null':
			return self.response('<h1>SERVER HTTP</h1>')

		return self.response('<h1>Bad Request</h1>')

		# files = glob('*.txt')
		# thedir=''
		# if thedir+object_address not in files:
		# 	return self.response(404,'Not Found','',{})
		# fp = open(thedir+object_address,'r')
		# isi = fp.read()
		#
		# fext = os.path.splitext(thedir+object_address)[1]
		# content_type = self.types[fext]
		#
		# headers={}
		# headers['Content-type']=content_type
		

		
			 	
#>>> import os.path
#>>> ext = os.path.splitext('/ak/52.png')

if __name__=="__main__":
	httpserver = HttpServer()
	d = httpserver.proses('GET / HTTP/1.0')
	print(d)
	# d = httpserver.http_get('testing2.txt')
	# print(d)
	# d = httpserver.http_get('testing.txt')
	# print(d)















