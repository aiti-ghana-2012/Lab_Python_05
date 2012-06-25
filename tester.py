import sys
import traceback

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	def disable(self):
		self.HEADER = ''
		self.OKBLUE = ''
		self.OKGREEN = ''
		self.WARNING = ''
		self.FAIL = ''
		self.ENDC = ''

try:
	from Lab05 import *
except ImportError:
	print bcolors.FAIL + 'ERROR: No Lab05.py file found' + bcolors.ENDC
	sys.exit(1)


def test_harness(function,*args,**kwargs):

	def inner(*args,**kwargs):
		try:
			return function(*args, **kwargs)
		except Exception as e:
			exc_type, exc_value, exc_traceback = sys.exc_info()
			return "ERROR: \n" + traceback.format_exc()

	return inner

@test_harness
def test_factorial():
	
	try:
		factorial
	except NameError:
		return "ERROR: factorial is not defined. Did you spell it right?"
	
	bla = factorial(1)
	if bla == 1:
		pass
	else:
		return "ERROR: Ran factorial(1). Expected 1, got:"+str( bla)
	bla = factorial(5)
	if bla == 120:
		pass
	else:
		return "ERROR: Ran factorial(5). Expected 120, got:"+str( bla)
	bla = factorial(19)
	if bla == 121645100408832000:
		pass
	else:
		return "ERROR: Ran factorial(19). Expected 121645100408832000, got:" + str( bla )
	return "OK"

@test_harness
def test_fibonacci():
	
	try:
		fibonacci
	except NameError:
		return "ERROR: fibonacci is not defined. Did you spell it right?"
	
	
	bla = fibonacci(1)
	if bla == [1]:
		pass
	else:
		return "ERROR: Ran fibonacci(1). Expected [1], got:"+str( bla)
	bla = fibonacci(2)
	if bla == [1,1]:
		pass
	else:
		return "ERROR: Ran fibonacci(2). Expected [1,1], got:"+str( bla)
	bla = fibonacci(9)
	if bla == [1, 1, 2, 3, 5, 8, 13, 21, 34]:
		pass
	else:
		return "ERROR: Ran fibonacci(9). Expected [1, 1, 2, 3, 5, 8, 13, 21, 34], got:" + str( bla )
	bla = fibonacci(15)
	if bla == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]:
		pass
	else:
		return "ERROR: Ran fibonacci(15). Expected [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], got:" + str( bla )
	return "OK"

@test_harness
def test_prime():
	
	try:
		prime
	except NameError:
		return "ERROR: prime is not defined. Did you spell it right?"
	
	
	bla = prime(1)
	if not bla:
		pass
	else:
		return "ERROR: Ran prime(1). Expected False, got:"+str( bla)
	bla = prime(2)
	if bla:
		pass
	else:
		return "ERROR: Ran prime(2). Expected True, got:"+str( bla)
	bla = prime(121)
	if not bla:
		pass
	else:
		return "ERROR: Ran prime(121). Expected False, got:" + str( bla )
	bla = prime(271)
	if bla:
		pass
	else:
		return "ERROR: Ran prime(271). Expected True, got:" + str( bla )
	return "OK"

@test_harness
def test_isPalindrome():
	
	try:
		isPalindrome
	except NameError:
		return "ERROR: isPalindrome is not defined. Did you spell it right?"


	bla = isPalindrome('able was I ere I saw elba')
	if bla is True:
		pass
	else:
		return "ERROR: Ran isPalindrome('able was I ere I saw elba'). Expected True, got:"+str( bla)
	
	bla = isPalindrome('Able was i ere I saw elba')
	if bla is False:
		pass
	else:
		return "ERROR: Ran isPalindrome('Able was i ere I saw elba'). Expected False, got:"+str( bla)
		
	bla = isPalindrome('amanaplanacanalpanama')
	if bla is True:
		pass
	else:
		return "ERROR: Ran isPalindrome('amanaplanacanalpanama'). Expected True, got:" + str( bla )
		
	bla = isPalindrome('a man a plan a canal panama')
	if bla is False:
		pass
	else:
		return "ERROR: Ran isPalindrome('a man a plan a canal panama'). Expected False, got:" + str( bla )
		
	bla = isPalindrome('yobananaboy')
	if bla is True:
		pass
	else:
		return "ERROR: Ran isPalindrome('yobananaboy'). Expected True, got:"+str( bla)\
		
	bla = isPalindrome('gohangasalamiimalasagnahog')
	if bla is True:
		pass
	else:
		return "ERROR: Ran isPalindrome('gohangasalamiimalasagnahog'). Expected True, got:"+str( bla)
		
	bla = isPalindrome('chicken')
	if bla is False:
		pass
	else:
		return "ERROR: Ran isPalindrom('chicken'). Expected True, got:" + str(bla)
		
	return "OK"

@test_harness
def test_isSubstring():
	
	try:
		isSubstring
	except NameError:
		return "ERROR: isSubstring is not defined. Did you spell it right?"
	
	
	bla = isSubstring('foo', 'foo')
	if bla:
		pass
	else:
		return "ERROR: Ran isSubstring('foo', 'foo'). Expected True, got:"+str( bla)
	bla = isSubstring('foo', 'barfoo')
	if	bla:
		pass
	else:
		return "ERROR: Ran isSubstring('foo', 'barfoo'). Expected True, got:"+str( bla)
	bla = isSubstring('foo', 'barbar')
	if not bla:
		pass
	else:
		return "ERROR: Ran isSubstring('foo', 'barbar'). Expected False, got:" + str( bla )
	bla = isSubstring('foo', 'fo')
	if not bla:
		pass
	else:
		return "ERROR: Ran isSubstring('foo', 'fo'). Expected False, got:" + str( bla )
	bla = isSubstring('ana', 'bananana rum')
	if bla:
		pass
	else:
		return "ERROR: Ran isSubstring('ana', 'bananana rum'). Expected True, got:"+str( bla)
	return "OK"

def tester():
	
	functions = [
				('factorial',test_factorial),
				('fibonacci',test_fibonacci),
				('prime',test_prime),
				('isPalindrome',test_isPalindrome),
				('isSubstring',test_isSubstring)
				]
				
	for name,func in functions:
		print bcolors.HEADER + 'Testing %s.......' % name + bcolors.ENDC
		result	= func()
		if result.startswith('ERROR'):
			print bcolors.FAIL + result + bcolors.ENDC
		else:
			print bcolors.OKGREEN + result + bcolors.ENDC
		print

if __name__ == '__main__':
	tester()
