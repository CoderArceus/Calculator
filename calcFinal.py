from math import pi
print('\033[1;36;40m' 'Welcome To The Calculator'.center(70))
print()
print('Available Commands-> ')

print('''1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Exponentiation''' )
print()

while True:
	
	while True:
			ch1 = input('What would you like to do?     ')
			if ch1 not in ('1', '2', '3', '4', '5'):
				print()
				print('⚠ No Such Command ⚠'.center(60))
			else:
				break
	print()
	
	while True:
			inp1 = input('First Number:    ')
			try:
				inp1 = float(inp1)
				break
			except ValueError:
				print()
				print('⚠ Please Type A Valid Number ⚠'.center(60))
			else:
				break
	print()
	
	while True:
			inp2 = input('Second Number:    ')
			try:
				inp2 = float(inp2)
				break
			except ValueError:
				print()
				print('⚠ Please Type A Valid Number ⚠'.center(60))
			else:
				break
	print()
	
	sum = (inp1) + (inp2)
	sub = (inp1) - (inp2)
	multi = (inp1) * (inp2)
	div1 = (inp1) / (inp2)
	div2 = (inp1) % (inp2)
	exp = (inp1) ** (inp2)
	
	if ch1 == '1':
		print('The SUM is -> ' f'{sum:.2f}')
	elif ch1 == '2':
		print('The DIFFERENCE is -> ' f'{sub:.2f}')
	elif ch1 == '3':
		print('The PRODUCT is -> ' f'{multi:.2f}')
	elif ch1 == '4':
		print(f'''The QUOTIENT is -> {div1:.2f}
The REMAINDER is -> {div2:.2f}''')
	elif ch1 == '5':
		print('The EXPONENTIAL form is-> ' f'{exp:.2f}')

	print()
	
	while True:
		ch2 = input('Do you want to Restart? Y/N    ')
	
		if ch2 not in ('y', 'Y', 'n', 'N'):
			print()
			print('⚠ Invalid Input ⚠'.center(60))
			
		elif ch2 in ('y', 'Y'):
			break
		else:
			quit()
		
	print()
		
			
			
			
		
			
	
	
			