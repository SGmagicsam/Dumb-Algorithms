def boolsRealm(n):
	
	if n < 0:
		return bool(1 - boolsRealm(n + 1))
	if n < 1:
		return bool(1 - n)
	else:
		return bool(1 - boolsRealm(n - 1))
