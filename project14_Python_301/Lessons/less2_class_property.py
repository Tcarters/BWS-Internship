#!/usr/bin/python3

import this


class myclass:
    this_is_a_property = {
        'key_1': 'Value 1'
    }
    this_list = ['Kane', 'Kalob', 'Gully']

    _like_this = "This is a private property"

    #pass
the_animal = myclass()

print (the_animal.this_is_a_property)
print (the_animal.this_is_a_property['key_1'])
print (the_animal.this_list[2] )
print (the_animal.this_list)
print (the_animal._like_this)