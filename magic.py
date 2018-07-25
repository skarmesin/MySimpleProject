def is_number(var):
	try:
		int(var)
		return True
	except Exception:
		return False

x = 1
print( is_number(x) )