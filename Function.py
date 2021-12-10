def greet_user():
    print('\nHello!!')

greet_user()


def greet_user(username):        #parameter
    print(f'\nHello, { username.title()}!!')

greet_user('Sneha')

# Positional Arguments   (as given in the parameters we need to assign the same position at the the time of function call)
# #
def greet_user(username,lstname,age):
    print(f'\nHello, {username.title()} {lstname.title()}. How are you doing ?')
    print(f'Age of {username.title()} {lstname.title()} is {age}!!')

greet_user('sneha','tripathi',22)
greet_user('neeraj','tripathi',23)    #multiple funcn call
greet_user('rahul','tripathi',15)

#multiple func call

def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print(f"\nI have a {animal_type}.")
 print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')  #(here we need to add animal type but in DEFAULT VALUE we don't need to add pet type at the time of function call)

# Default Values

def describe_pet(pet_name,animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')    #(in default value we don't need to add animal type while we call that function )(its been added by default)
describe_pet(pet_name='Sheru')
