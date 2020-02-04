# comment
print("Hello, World")
a = 1
b = 5
print(a + b)

#list
myList = {1, 2, 3, 4, 3, 2, 1}

print(myList[0:6:2])

# strings are just lists
phrase = 'Catch the Dog'
phrase[2] #t
phrase[4] #h
phrase[-1:0:-3] #strides backwards, -1 right, 0 is l$

#function
def sumfunction(a, b): 
	return a + b

print(sumfunction(2, 20))

#if loop
if(x == 10):
	x = 5
elif(y == -10):
	y = 5
else:
	x = y-x

#loop
Lst = {1, 3, 8, 412, 43, 2, 20}
#length of list
len(Lst)

#for loop by index
for i in range(len(Lst)):
	print(Lst[i])
#for each loop
for val in Lst:
	print(val)
#dictionaries
lookup = {}
lookup['kc'] = 'Chiefs'
lookup['ne'] = 'patriots'
lookup['la'] = 'chargers'
lookup['suck'] = 'raiders'
