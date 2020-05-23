ice_cream_rating = 10
sleeping_rating = 5

first_name = input("Please enter your first name? ")
last_name = input("Please enter your last name ? ")
my_name = first_name + " " + last_name

print("Benim adım", my_name)

happiness_rating = (ice_cream_rating + sleeping_rating) / 2

print(my_name,"your average happiness rating is",happiness_rating)
print(type(ice_cream_rating))
print(type(sleeping_rating))
print(type(first_name))
print("my name is", first_name, "and I give eating icecream a score of", ice_cream_rating, "out of 10! \n"
"I am ", my_name, " and my sleeping enjoymentrating is", sleeping_rating," out of 10! \n"
"Based on the factors above", "my happiness rating is ",happiness_rating,"out of 10! or 85.0 % \n")
