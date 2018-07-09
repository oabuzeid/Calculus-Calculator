#The following definition allows users to run the program in terminal/command prompt.
# int() function checks if the users input is an integer, and input() function 
#allows for typing in instructions that will show on the command prompt.
def calculus_calculator():
	case = str(input("Hello! Welcome to the official Calculus Calculator. Please enter what you would like me to do! Possible commands are first-degree, second-degree, third-degree, fourth-degree, poly-derivative, definite-integral, and riemann-sum: "))
	if case == "first-degree":
		a = int(input("Please enter a value for 'a', your first coefficient"))
		b = int(input("Please enter a value for 'b', your second coefficient (constant)"))
		x = int(input("Please enter a value for 'x', the point where you want to take your derivative"))
		number_of_derivatives = int(input("How many times would you like your function to be differentiated?"))
		return one_degree_derivative_value(a, b, x, number_of_derivatives)
	if case == "second-degree":
		a = int(input("Please enter a value for 'a', your first coefficient"))
		b = int(input("Please enter a value for 'b', your second coefficient"))
		c = int(input("Please enter a value for 'c', your third coefficient (constant)"))
		x = int(input("Please enter a value for 'x', the point where you want to take your derivative"))
		number_of_derivatives = int(input("How many times would you like your function to be differentiated?"))
		return two_degree_derivative_value(a, b, c, x, number_of_derivatives)
	if case == "third-degree":
		a = int(input("Please enter a value for 'a', your first coefficient"))
		b = int(input("Please enter a value for 'b', your second coefficient"))
		c = int(input("Please enter a value for 'c', your third coefficient"))
		d = int(input("Please enter a value for 'd', your fourth coefficient (constant)"))
		x = int(input("Please enter a value for 'x', the point where you want to take your derivative"))
		number_of_derivatives = int(input("How many times would you like your function to be differentiated?"))
		return three_degree_derivative_value(a, b, c, d, x, number_of_derivatives)
	if case == "fourth-degree":
		a = int(input("Please enter a value for 'a', your first coefficient"))
		b = int(input("Please enter a value for 'b', your second coefficient"))
		c = int(input("Please enter a value for 'c', your third coefficient"))
		d = int(input("Please enter a value for 'd', your fourth coefficient"))
		e = int(input("Please enter a value for 'e', your fifth coeffcient (constant)"))
		x = int(input("Please enter a value for 'x', the point where you want to take your derivative"))
		number_of_derivatives = int(input("How many times would you like your function to be differentiated?"))
		return four_degree_derivative_value(a, b, c, d, e, x, number_of_derivatives)
	if case == "poly-derivative":
		isdone = False
		list_of_coeff = []
		integer = None
		while isdone != True:
			integer = input("Please enter a list of coefficients for your derivative. Remember that the order of your list values corresponds to the order they will be plugged into the function! For example, if your list is [1, 2, 3], the corresponding function will be 1x^2 + 2x + 3. Type 'done' to complete the list.")
			if integer == "done":
				isdone = True
			else:
				list_of_coeff.append(int(integer))
		x = int(input("Please enter a value for 'x', the point where you want to take your derivative"))
		number_of_derivatives = int(input("How many times would you like your function to be differentiated?"))
		return poly_derivative(list_of_coeff, x, number_of_derivatives)
	if case == "definite-integral":
		isdone = False
		list_of_coeff = []
		integer = None
		while isdone != True:
			integer = input("Please enter a list of coeffcients for your integral. Remember that the order of your list values corresponds to the order they will be plugged into the function! For example, if your list is [1, 2, 3], the corresponding function will be 1x^2 + 2x + 3. Type 'done' to complete the list.")
			if integer == "done":
				isdone = True
			else:
				list_of_coeff.append(int(integer))
		lowerx = int(input("Please enter a value for the lower bound of the integral"))
		upperx = int(input("Please enter a value for the upper bound of the integral"))
		number_of_integrals = int(input("How many times would you like your function to be integrated?"))
		return definite_integral(list_of_coeff, number_of_integrals, lowerx, upperx)
	if case == "riemann-sum":
		lowerbx = int(input("Please enter a lower bound value for you Riemann sum integral"))
		upperbx = int(input("Please enter an upper bound value for your Riemann sum integral"))
		num_of_rect = int(input("Please enter a value for the number of rectangles you would like to use for your Riemann sum. Remember that the more rectangles inputted, the more accurate the result!"))
#Calculates definite derivatives of the form ax + b. If the number of
#derivatives inputted is 0, then the same function is returned. If the
#derivative is 1, then by the definition of a derivative, the program
#will return a. Any value other than 0 or 1 for the number of derivatives
# will return a value of 0.
def one_degree_derivative_value(a, b, x, number_of_derivatives):
	if number_of_derivatives == 0:
		return a * x + b
	elif number_of_derivatives == 1:
		return a
	else:
		return 0

#Calculates definite derivatives of the form ax^2 + bx + c. Users input
#the values wanted for a, b, c, x, and the number of derivatives wanted.
#If the derivative is equal or greater than 1, the function uses the
#previous function (One_degree_derivative_value) to return the derivative
#in the second degree.
def two_degree_derivative_value(a, b, c, x, number_of_derivatives):
	if number_of_derivatives == 0:
		return a * x ** 2 + b * x + c
	elif number_of_derivatives >= 1:
		return one_degree_derivative_value(2 * a, b, x, number_of_derivatives - 1)

#Calculates definite derivatives of the form ax^3 + bx^2 + cx + d.
#Same idea as the previous code, except that it uses (Two_degree_
#derivative value in the else-if statement)
def three_degree_derivative_value(a, b, c, d, x, number_of_derivatives):
	if number_of_derivatives == 0:
		return a * x**3 + b * x^2 + c * x + d
	elif number_of_derivatives >= 1:
		return two_degree_derivative_value(3 * a, 2 * b, c, x, number_of_derivatives - 1)

#Calculates definite derivatives of the form ax^4 + bx^3 + cx^2 + dx + e.
#Same idea as the previous code, except that it uses (Three_degree_
#derivative value in the else-if statement)
def four_degree_derivative_value(a, b, c, d, e, x, number_of_derivatives):
	if number_of_derivatives == 0:
		return a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e
	elif number_of_derivatives >= 1:
		return three_degree_derivative_value(4 * a, 3 * b, 2 * c, d, x, number_of_derivatives - 1)

#Calculates complex polynomial derivatives using recursion.
#First takes length of the list of coefficients and sets that value
#= to number_of_coeffs. Value = 0 (will be used later). If the number
#of derivatives = 0, index is set to 0, and a for loop is used.
#The range is reversed (for example, if number_of_coeffs = 4, range
#will go from 3 to 0 (takes into account 0-indexing)). This then takes
#index value 0 initially and takes that value from the list of
#coefficients (In case list_of_coeff[0], it will take the first item
#of that list, then multiply it by x^i). Index will then add 1 to itself
#in order to go to the next item in the list of coefficients.
#elif case takes derivatives of 1 onwards, creates a new empty list,
#then uses the for loop in the same way as in the base case. Program
#then appends the item of the list of coefficients multiplied by i. 
#this is done recursively, until the base case is reached, giving a
#derivative of the users choosing.
def poly_derivative(list_of_coeff, x, number_of_derivatives):
	number_of_coeffs = len(list_of_coeff)
	value = 0
	if number_of_derivatives == 0:
		index = 0
		for i in reversed(range(number_of_coeffs)):
			value += list_of_coeff[index] * x**i
			index += 1
		return value
	elif number_of_derivatives >= 1:
		counter = 0
		new_list = []
		for i in reversed(range(number_of_coeffs)):
			new_list.append(list_of_coeff[counter] * i)
			counter += 1
		new_list.pop()
		return poly_derivative(new_list, x, number_of_derivatives - 1)

#Allows users to calculate definite integrals recursively. number_of_coeffs is
#set to the length of the list of coefficients. Base case accounts for the upper bound
#and lower bound. It takes the lower bound value and subtracts that from the upper
#bound value. This case works for the regular formula without integration. Recursive
#case works similarly to the recursive case in poly_derivative, except that it 
#does the opposite function on i to take an integral instead of a derivative.
def definite_integral(list_of_coeff, number_of_integrals, lowerx, upperx):
	number_of_coeffs = len(list_of_coeff)
	lower_bound_value = 0
	upper_bound_value = 0
	if number_of_integrals == 0:
		index = 0
		for i in reversed(range(number_of_coeffs)):
			lower_bound_value += list_of_coeff[index] * lowerx**i
			upper_bound_value += list_of_coeff[index] * upperx**i
			index += 1
		return upper_bound_value - lower_bound_value
	elif number_of_integrals >= 1:
		counter = 0
		new_list = []
		for i in reversed(range(number_of_coeffs)):
			new_list.append(list_of_coeff[counter] / (i + 1))
			counter += 1
		new_list.append(0)
		return definite_integral(new_list, number_of_integrals - 1, lowerx, upperx)

#This allows users to integrate using Riemann sum rectangle approximations. 
#As apposed to the definite_integral code, this gives the user the chance
#to integrate using Riemann approximations.
def riemann_sums_integral(lowerbx, upperbx, num_of_rect):
	riemannsum = 0
	width = (upperbx - lowerbx) / num_of_rect
	for i in range(num_of_rect):
		height = (lowerbx + i*width)
		area = height * width
		riemannsum += area
	return riemannsum