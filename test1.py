
# Comment 1: print hello world
print("hello world!")

def reply():
	return "world says hello!"


# Comment 2: Implement more functions below.


text = "hello world!"


def upper_case(text):
	try:
		return str(text).upper()
	except:
		print('Invalid input!')