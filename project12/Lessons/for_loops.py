fav_foods = ['Pizza', 'Tacos', 'Salmon']
print( "Typeof is ", type(fav_foods) )


#for food in fav_foods:
#    if food == "Pizza":
#        size = input("What size pizza would you like? ")
#        print( f"You ordered a { size} pizza ")

#print(food)

fav_foods = set( fav_foods)
for f in  fav_foods:
    if f == "Pizza":
        for letter in f:
            print ( letter,  end="\n \n" )
    #print( f ) 

person = {
    "name": "Tdmund",
    "Twitter": "@Tdmund_",
    "Location": "North Carolina"
}

print ( " the type of person: ", type ( person) )

for key, value in person.items():
    print ("The key is {} and the value is {}".format(key, value) ) 