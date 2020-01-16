def boolsRealm(n):
	
	if n < 1:
		return bool(1 - n)
	else:
		return bool(1 - boolsRealm(n - 1))

