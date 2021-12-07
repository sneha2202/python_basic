def greet_user():
    print('Hello!!')

greet_user()


def greet_user(username):        #parameter
    print(f'Hello,{ username.title()}!!')

greet_user('Sneha')

# Positional Arguments

def greet_user(username,lstname,age):
    print(f'Hello, {username.title()} {lstname.title()}. How are you doing ?')
    print(f'Age of {username.title()} {lstname.title()} is {age}!!')

greet_user('sneha','tripathi',22)
greet_user('neeraj','tripathi',23)    #multiple funcn call
greet_user('rahul','tripathi',15)



