def pos_odd(x): 
	cnt = 0
	i = 0

	while i < len (x):
		if x[i] % 2 == 1 :
			cnt = cnt + 1
		i = i + 1

	return cnt


if __name__ == "__main__":
	x = [-10, -9, 0, 99, 100]
	r = pos_odd(x)
	print r

