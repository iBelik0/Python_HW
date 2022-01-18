my_string = "Hello"
print (type(my_string), my_string)

my_float = 3.14
print (type(my_float), my_float)

my_int = 1
print (type(my_int), my_int)

my_bytes = b'Alexey'
print (type(my_bytes), my_bytes)

my_list = ([1,2,3,4,'a',5])
print (type(my_list), my_list)

my_tumple = ('Alex','Belyaev')
print (type(my_tumple), my_tumple)

my_set = {"Alexey", 1 , 3.14}
print (type(my_set), my_set)

my_frozenset = frozenset({1,2,3})
print (type(my_frozenset), my_frozenset)

my_dict = {'a' : 10, 'b' : 20}
print (type(my_dict), my_dict)

my_string2 = "World"
d = (my_string)+(my_string2)
print ('(my_string)+(my_string2)',type(d))

print ('my_string+my_int',type(my_string),type(my_int))

print (my_string+str(my_int))




