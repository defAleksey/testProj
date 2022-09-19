list_some = [1, 2, '4', 'er', 5, 3, 3, 3, 4, 5]
some = []
for _ in list_some:
	if type(_) == int or str(_).isdigit():
		if int(_) < 5:
			some.append(_)
print(some)
