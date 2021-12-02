import random

first_names = ['John', 'Jane', 'Sneha', 'Neeraj', 'Rahul', 'Dhananjay', 'Pushpa', 'Sam', 'Mishty', 'Purva', 'Pappu', 'Manju', 'Harsh', 'Sarika', 'Khushi', 'Somya', 'Sunita', 'Jeetendra', 'Sanjay', 'Manu', 'Rubi', 'Neeru', 'Sonu', 'Akshay', 'Sharukh']

last_names = ['Tripathi', 'Tiwari', 'Mishra', 'Dixit', 'Pawar', 'Tayade', 'Patil', 'Waghere', 'Gole', 'Shaikh', 'Khan', 'Kumar', 'Jadhav', 'Kolhi', 'Dhoni', 'Singh', 'Sharma', 'Varma', 'Kansh', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Vaswani', 'Abc', 'Washington', 'Lake', 'Hill']

fake_cities = ['Pune', 'Mumbai', 'Kolkata', 'Kokan', 'Goa', 'South Park', 'Atlantis', 'Banglore', 'Hyderabad', 'Dawnstar', 'Bombay', 'Gorakhpur', 'Hadapsar', 'Qvi', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@gmail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')