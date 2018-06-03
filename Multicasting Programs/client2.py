#This python file is client 2 which can send messages to client 1 and 3 based on user choice

import socket               # Import socket module
import sys					# Import system module
import _thread				# Import thread module
import time 				# Import time module

timestamp_client_2 = 0

def send_message(dummyparam1, dummyparam2):
	while True:
		print("Press 1 if you want to send a message to Client 1")
		print("Press 2 if you want to send a message to Client 3")
		user_choice = input("Enter your choice :")
	
		message = input("Enter your message :")
	
		user_choice_int = (int)(user_choice);

		if(user_choice_int == 1):
			#Code to send a message to client 1
		
			try:
				machine = 1
				print ("Before s.connect")
				s=socket.socket()
				s.connect(("127.0.0.1",1234)) #DESKTOP-JH3J8A5
				print ("After s.connect")
				s.sendall(message.encode())
				time.sleep(5)
				s.sendall((str(machine)).encode())
				time.sleep(5)
				s.sendall((str(timestamp_client_2)).encode())
				time.sleep(5)
				s.close
			except OSError as err:
				print("OS error: {0}".format(err))
		
		
		else:
			#Code to send a message to client 3
		
			try:
				machine = 3
				print ("Before s.connect")
				s=socket.socket()
				s.connect(("127.0.0.1",3000))
				print ("After s.connect")
				s.sendall(message.encode())
				time.sleep(5)
				s.sendall((str(machine)).encode())
				time.sleep(5)
				s.sendall((str(timestamp_client_2)).encode())
				time.sleep(5)
				s.close
			except OSError as err:
				print("OS error: {0}".format(err))
		
def receive_message_indicator(dummyparam1, dummyparam2):

	try:
		#s.connect(("127.0.0.1",2000))
		s.listen(3)
		while True:
			print ("Before s.accept")
			c, addr = s.accept()
			print ("Got connection from ",addr)
			print ("Before receiving message") # Debug statement
			message = str(c.recv(1024))
			print (message) #Debug Statement
			print("Before receiving machine")
			machine = int(c.recv(1024))
			print((str)(machine)) #Debug Statement
			print("Before receiving timestamp")
			timestamp = int(c.recv(1024))					
			receive_message(message,machine,timestamp)
			
			#It was getting stuck here so I thought of breaking this while loop and calling send_message
			break
		
		send_message(1,2)
		receive_message_indicator(3,4)
		
	except TypeError as err:
		print ("Type error: {0}".format(err))
	
	

def receive_message(message, machine, timestamp) :
	global timestamp_client_2
	#This function should get executed only when the socket receives some incoming data, hint : some while loop or something
	print ("Message :" + (str)(message) + "from machine number : "+str(machine) + "with timestamp "+(str)(timestamp))
	timestamp_client_2 = (int)(timestamp_client_2)
	timestamp_client_2 = (int)(timestamp) + 1
	print("Timestamp of Machine 2 is : "+(str)(timestamp_client_2))
	return;
	
# Create two threads as follows
try:


	s = socket.socket()         # Create a socket object
	#host = socket.gethostname() # Get local machine name
	host = 'localhost'
	port = 2000               # Reserve a port for your service.

	s.bind(("127.0.0.1", port))        # Bind to the port
	#s.listen(5)

	timestamp_client_2 = 0
	print ("Initial Timestamp is " + str(timestamp_client_2))
	print (socket.gethostname())
   
	_thread.start_new_thread(send_message,(1,2,)) #thread.start_new_thread( print_time, ("Thread-1", 2, ) )
	_thread.start_new_thread(receive_message_indicator,(3,4,)) #thread.start_new_thread( print_time, ("Thread-2", 4, ) )
   
	while True : pass

except:
   print ("Unexpected error:", sys.exc_info()[0]) #print ("Error: unable to start thread")
	
