import config
from config import init_lock
from config import get_lock
from config import set_lock

#config.init_lock()
print (config.get_lock())

while True:
	print ("Press 1 to access the file")
	user_choice = input("Enter your choice :")
	user_choice = (int)(user_choice)
	
	#check for lock variable, if lock = 0 then access the file else prevent the user from accessing the file
	if(config.get_lock() == 0):
		#go on to access the file
		print ("Lock Value is")
		print(config.get_lock())
		
		#acquire the lock
		
		#config.lock=1
		config.set_lock(1)
		
		print("Config Lock =")
		
		print(config.get_lock())
		
		with open('sharedfile.txt', 'r') as f:
			print ("Counter value = "+(str)(f.read()))
			f.close()
			
		while True :
			print ("Press 1 to update the counter value")
			print ("Press 2 to release the lock")
			user_choice_1 = input("Enter your choice :")
			user_choice_1 = (int)(user_choice_1)
			
			if(user_choice_1 == 1):
				#allow user to update the counter in the file
				counter_value = input("Enter the new counter value :");
				with open('sharedfile.txt', 'w') as f:
					#Write counter_value to file and then close the file
					f.write((str)(counter_value))
					f.close()
				
			elif(user_choice_1 == 2):
				#release the lock and break from this while loop
				config.set_lock(0)
				break
			else:
				print ("Some error occured with the program. Please restart the client machine.")
		
	elif(config.get_lock() == 1):
		#prevent the user from accessing the file
		print ("Lock Value = "+(str)(config.lock))
		print ("Some other process is accessing the shared file, please try again after some time.")
		
	else :
		#print error message
		print ("The variable lock is set to an invalid value. Please retry.")
		
