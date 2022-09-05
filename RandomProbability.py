'''create a random integer from 1 to 100'''

from random import randint

value1 = randint (1, 100)
value2 = format(chr(randint(97, 122)))

'''print value1 and value2 as strings'''
print (value1, value2)

value3 = '''random date in unix format''' + str(randint(1, 100)) + ''' and random time in unix format''' + str(randint(1, 100))

'''get current cryptocurrency price for bitcoin''' 
import requests  # import requests library
import json  # import json library
print