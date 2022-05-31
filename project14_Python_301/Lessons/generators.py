lst = [1,2,3]

def my_generator():
    for num in range(50):
        yield num ** num

        # print(num)
#for big_num in my_generator():
#    print(big_num)

#all_numbers = list (my_generator())
#print(all_numbers)
#print ( myfunct() ) 
print( [ x for x in range(10)] )