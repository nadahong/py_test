# for
list = [1, 2, 3, 4, 5, 6, 7, 8]

for item in list:
    print(item)


days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ':drink ', drink, '- eat', dessert, '- enjoy', fruit)

for i in range(10, -1, -1):
    print(i)


# lambda

