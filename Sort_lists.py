# Sorted function

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list) # [400, 220, 100, 100, 83, 40, 10, 3, 1]
print(sale_prices) # [100, 83, 220, 40, 100, 400, 10, 1, 3]


# Sort list

tags = ['python', 'development', 'tutorials', 'code']

print(tags) # ['python', 'development', 'tutorials', 'code']

tags.sort() #Alphabetical order

print(tags) # ['code', 'development', 'python', 'tutorials']

# Reassignation operator
post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')
print (post)

post += ('tags',)

first, second, third, fourth, fifth = post

print(first)
print(second)
print(third)
print(fourth)
print(fifth)