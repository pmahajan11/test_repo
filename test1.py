text = "hello world!"


def upper_case(text):
	try:
		return str(text).upper()
	except:
		print('Invalid input!')