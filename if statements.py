#if= conditional statement
age=int(input("Enter your age:"))

# if age>=100:
#     print("you need to be less than 100 to sign up")
# elif age>=18:
#     print("You are now signed up!")
# elif age<0:
#     print("You haven't been born yet!")
# else:
#     print("You must be 18+ to sign up!")
#
response=input("Would ypou like some food? (Y/N): ")

if response=="Y":
    print("Have some food")
elif response=="":
    print("You did not give us a response")
else:
    print('No food for you!')

for_sale=True

if for_sale:
    print("The item is for sale")
else:
    print("the item aint for sale")