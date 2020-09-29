print ('''Create four variables. Assign numeric values to two of them.
Assign string data to one of them. Assign a boolean value to one of them. ''')
var1 = 1
var2 = 2
var3 = 'a string'
var4 = True

print ('''\nAdd the two numbers together and store the result in a new variable. ''')
var5 = var1 + var2
print (var5)

print ('''\nUse string concatenation to add some text to the string variable and store the 
result back into the original variable. Hint += works for strings too!''')
var3 += ', but longer'
print (var3)

print ('''\nUse the "not" operator not on your boolean variable and see what it does. ''')
print (not var4)

print ('''\nCombine the boolean and a number.''')
combination1 = var4 + 3
print (combination1)

print ('''\nCombine a string and a number.''')
#TODO: This is a breaking exercise
try:
   combination2 = var3 + 3
except:
   print ('can\'t combine a string and a number')
   exiterr = 1
   pass

print ('''\nCombine a string and a boolean.''')
#TODO: This is a breaking exercise
try: 
   combination3 = var3 + True
except:
   print ('can\'t combine a string and a bool')
   exiterr = 1
   pass

#Pass error to the shell
if exiterr == 0:
   exit (0)
else:
   print ('\nmuch sadness')
   exit (1)

# What happens when you run the code?
# Is it the same for each combination?
