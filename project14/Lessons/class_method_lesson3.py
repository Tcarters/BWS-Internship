class myclass:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Kane', 'Kalob', 'Gully']

    def add_name (self, name):
        self.this_list.append(name)
        return self.this_list


    def this_is_a_method(self):
        print (self.this_list)
    
    @property
    # this is used to define below method like a regular property
    def get_gully(self):
        return self.this_list[2]

calling_the_class = myclass()  # calling the class 

# calling_the_class.this_is_a_method()

# g = calling_the_class.get_gully

# print("The cutest gato of all time is", g)
calling_the_class.add_name("Rumba")
print(calling_the_class.this_list)