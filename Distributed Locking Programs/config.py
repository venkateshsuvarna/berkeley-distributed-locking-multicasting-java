global lock
with open('lock.txt', 'r') as f:
	lock = (int)(f.read())
	#print ("Counter value = "+(str)(f.read()))
	f.close()

def init_lock():
	print ("Init Lock called")
	global lock
	#lock = 0
	with open('lock.txt', 'w') as f:
		#Write counter_value to file and then close the file
		f.write((str)(0))
		f.close()
	print("Lock initialized to 0")

def set_lock(lock_value):
	global lock
	with open('lock.txt', 'w') as f:
		#Write counter_value to file and then close the file
		f.write((str)(lock_value))
		f.close()
	print("The value of lock in config file is")
	print(lock)
	
def get_lock():
	global lock
	with open('lock.txt', 'r') as f:
		lock = (int)(f.read())
		#print ("Counter value = "+(str)(f.read()))
		f.close()
	return lock
