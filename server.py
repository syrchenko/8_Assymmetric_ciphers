import socket
 import pickle
 from random import randint

 HOST = '127.0.0.1'
 PORT = 8080
 def random_free_port(p):
 	try:
 		sock = socket.socket()
 		sock.bind(('',p))
 		sock.close
 		return p
 	except:
 		for _ in range(0, 65536):
 			try:
 				p=randint(0,65535)
 				sock = socket.socket()
 				sock.bind(('',p))
 				sock.close
 				return p
 			except:
 				continue    

 def chis(g,l,p):
     return g**l%p

 def crypt(msg, k):
     crypt_msg=''
     for i in range(len(msg)):
         crypt_msg+=chr(ord(msg[i])^k)
     return crypt_msg

 def send_msg(conn, msg, k):
 	conn.send(pickle.dumps(crypt(msg, k)))

 def recv_msg(conn, k):
 	msg=crypt(pickle.loads(conn.recv(1024)), k)
 	return msg

 HOST = '127.0.0.1'
 sock = socket.socket()
 sock.bind((HOST, PORT))
 sock.listen(1)
 port=9090
 port=random_free_port(port)          
 sock.bind((HOST,port))
 print('Введите номер порта:',port)


 sock.listen(0)			
 sock.setblocking(1)
 conn, addr = sock.accept()

 b = randint(1, 256)

 msg = conn.recv(1024)
 print(pickle.loads(msg))
 p, g, Aa = pickle.loads(msg)

 Bb = chis(g,b,p)
 conn.send(pickle.dumps(Bb))

 K = chis(Aa,b,p)
 print('K=',K)
 while True:
 	try:
 		msg = recv_msg(conn, K)
 		print(msg)
 		send_msg(conn, 'Сервер получил и расшифровал', K)
 	except:
 		break

 conn.close()
 conn.close()