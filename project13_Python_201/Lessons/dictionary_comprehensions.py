names = [("name", " Kalob"), ("occupation", "Coder")]
d = {}

print ("Type :", type(names) )


for key, value in names:
    d[key] = value
    print (d)

d2 = {key: value for key, value in names}
print(d2)

d3 = dict(names)
print (d3)