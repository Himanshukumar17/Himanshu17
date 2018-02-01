while True:
	print("Enter 'x' for exit.")
	num = input("Enter a number: ")
	if num == 'x':
		break
	else:
		number = int(num)
		for i in range(1, 11):
			print(number, "*", i, "=", number*i)
