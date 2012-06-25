"""
Lab_Python_05
Solutions for problesm 2 -7
"""

## Problem 2 - Factorial
# we can do this recursively and iteratively

# first the iterative method:
def factorial(n):
	answer = 1

	#we want to iterate over all of the numbers from n - 1
	for i in range(n,1,-1):
		answer *= i
	
	return answer

# now recursively:
def factorial(n):
	if n < 2:
		return 1
	else:
		return n * factorial(n-1)



## Problem 3 - Fibonacci
# this one can be done iteratively or recursively too

# first the iterative method:
def fibonacci(n):
	
	if n == 0:
		return []
	elif n == 1:
		return [1]
	else:
		out = [1,1]
		
		for i in range(2,n):
			new_number = out[i - 1] + out[i - 2]
			out.append(new_number)
		
		return out

# now recursively:
def fibonacci(n):
	if n == 0:
		return []
	elif n == 1:
		return [1]
	elif n == 2:
		return [1,1]
	else:
		out = fibonacci(n - 1)
		new_number = out[-1] + out[-2]
		out.append(new_number)
		return out


## Problem 4 - Prime Numbers
def prime(n):
	if n == 1:
		return False

	for i in range(2,n):
		if not n % i:
			return False
	return True



## Problem 5 - Palindrome
def isPalindrome(string):
	
	# strategy will be to look from the right and left simultaneously
	# maintain a left_cursor, which is our position from the left
	# and a right cursor, which is our position on the right
	left_cursor = 0
	right_cursor = len(string) - 1
	
	while right_cursor >= left_cursor:
		if not string[left_cursor] == string[right_cursor]:
			return False
		
		# now moving the cursors inwards
		left_cursor += 1
		right_cursor -= 1
	
	# if we get to this point, then it is a palindrome!
	return True

## Problem 6 - isSubstring
# you can do this in one line using 'substring in string'
# but good practice to do it this way
def isSubstring(substring, string):
	# using the strategy described in the problem
	string_position = 0

	# we want to iterate through every position in the string
	# where it is possible that the substring starts
	while string_position <= len(string) - len(substring):
		
		# if our current position in the string matches the first character of the substring,
		# then we have to check that the next characters in the string also match		
		if string[string_position] == substring[0]:
			match = True
			for i in range(1,len(substring)):
				if not substring[i] == string[string_position + i]:
					match = False
					break;
			
			# if every character in the substring appeared in order in the string,
			# then we win!	
			if match:
				return True
		
		# and now lets look at the next position in the string
		string_position += 1	
	
	# if we get out of the loop, then there was no match. :(
	return False


## Problem 7 - Max test score
# confusing problem for everyone. sorry!
def maxTestScore(answers_wrong, answers_a, answers_b):
	
	score = 0

	for i in range(len(answers_wrong)):
		
		# if the two friends had the same answer
		if answers_a[i] == answers_b[i]:
			
			# then if it was not a wrong answer
			if not answers_a[i] == answers_wrong[i]:
				# we can score 2
				score += 2
		else:
			# then we will always be able to score 1
			score += 1

	return score
