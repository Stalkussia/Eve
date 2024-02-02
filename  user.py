#First of all, we gather the info about user

username = input("What is the user's name? ")
users_age = input("What is the user's age? ")
users_country = input("What is the user's country of birth? ")
users_fame = input("What is the user known for? ")
#After gathering information all together, we make a dictionary and put the data(keys and values) in the dictionary
user = {'name': username,'age' : users_age,'country' : users_country,'fame' : users_fame}
#Then we print out the output
print(user)