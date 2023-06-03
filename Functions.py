#Function=named block of code designed do a specific task or job
def greet_user(username):
    """Display a greeting message when called"""
    print(f"hello {username}!")

greet_user('Deo')

#Value returning functions
#This function takes a first and last name, and returns a neatly 
#formatted full name

def my_full_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
firstname=input("Enter your firstname:")
secondname=input("Enter your secondname:")
musician=my_full_formatted_name(firstname,secondname)
print(musician)
