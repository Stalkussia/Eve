myfamily = ("mother", "father", "sister", "brother", "sister") 

print(myfamily) 

print(type(myfamily))
print(myfamily[2],myfamily[4])
#myfamily.append("me")
#myfamily.pop("brother")
#We can't use append() or pop() with tuple type of data, however we can transform the tuple into the list and then append() and pop()
myfamily = ["mother", "father", "sister", "brother", "sister"]
myfamily.append("me")
print(myfamily)
#we added "me" into the list and printed it
myfamily.pop(3)
print(myfamily)
#we removed "brother" from the list and printed it