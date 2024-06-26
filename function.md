Lecture: List in Python



Creating a list of people.

people = ['John','Rob','Mike']


Printing out this list

print(people)


Printing an individual element inside of a list.

print(people[0])


Print the second members name

print(people[1])


Creating a list of numbers

numbers =[10,20,30,40,50]


A list with different types of data.

Movies = [Spiderman,Batman,1,2,4.5,Hello]


Checking order of lists

Example two lists

a = [1,2]
b=[2,1]
print(a==b)


Lecture: List Slicing

List slicing:

a[m:n] Returns list items from index m to n but does not include n
# -ve index  -6        -5      -4       -3           -2           -1
fruits = ['apple', 'mango', 'peach', 'orange', 'watermelon', 'grape']
# index     0         1       2         3          4            5

# list slicing
print(fruits[0:3])
print(fruits[1:3])

Lecture: List slicing using negative index

a[-m:-n] Returns list items from index -m to -n but does not include n
Example:

# -ve index  -6        -5      -4       -3           -2           -1
fruits = ['apple', 'mango', 'peach', 'orange', 'watermelon', 'grape']
# index     0         1       2         3          4            5

Negative indexing:

print(fruits[-6])
# slicing using -ve indexing
print(fruits[-5:-1])
Lecture: In and not operators



fruits = ['apple','mango','peach','orange','watermelon','grape']

print('apple' in fruits)
print('banana' in fruits)
print('apricot' not in fruits)
print('orange' not in fruits)
Lecture: List functions



Calculating number of items in string

print(len(fruits))


Inserting elements into a list:

fruits.insert(index,"Element to be inserted")
fruits.insert(1,"Pineapple")


Append

fruits.append('Hello')



Adding contents of one list into another

fruits.append(['guvava','apricot'])



Add items of one list to another, we use extend

fruits.extend(['guvava','apricot'])


Remove objects from a list

fruits.remove('apple')


Remove the last item in the list using pop

fruits.pop()
print(fruits)


Finding index of an item

print(fruits.index('apple'))


Min and max:

scores = [1, 2, 3, 4, 5, 6, 90, 30]
print(max(scores))
Lecture: Concat & Replicate operations on a list



Concat

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)


Replicate

print(a*3)


Lecture: Nesting lists

a = [1, 2, [3, 4, 5], 6, 7, 8, [9, 10]]

print(a[2])
print(a[2][0])


Lecture: Mutability of lists



a = [1, 2, 3]
a[1] = 100
print(a)
Modifying multiple items in a list:

a = [1, 2, 3]
a[0:4] = [10, 20, 30]
print(a)


Lecture: Tuples



#creating a tuple
fruits = ('apple','orange','mango','pineapple')
# printing a tuple
print(fruits)
#immutability of a tuple
fruits[1]='peach'
print(fruits)
# indexing
print(fruits[1])
#slicing
print(fruits[1:3])
#negative indexing
print(fruits[-1])


Lecture: Dictionaries



people={"John":32,"Rob":40,"Tim":20}
print(people["Rob"])
Mutability



people["Rob"]=90
print(people["Rob"])




ids = {1:"John",2:"Rob",3:"Matt"}
print(ids[2])


Another way to create a dictionary ,using the dict() function:

The argument to the dict function should be a key value pair

people =dict(
    john=32,
    rob=45,
    tim=20
)
print(people["john"])


Adding a new value

people={"John":32,"Rob":40,"Tim":20}
people["Mike"]=34
print(people)


Deleting an entry using a key

del people["John"]
print(people)


Lecture: Dictionary functions

people={"John":32,"Rob":40,"Tim":20}


print(people.get('John'))



prices ={'iphone':500,'ipad':400}
new_prices = {'iphone':600,'ipad':400,'imac':1500}
prices.update(new_prices)
print(prices)


new_prices = {'iphone':600,'ipad':400,'imac':1500}
new_prices.pop('ipad')
print(new_prices)

print(new_prices.keys())


print(new_prices.items())


print(new_prices.values())


Lecture: Sets



Set function

#creating a set
numbers = set([1,2,3,4,5,6])
print(numbers)


Creating a set is by simply using curly braces

numbers = {1,2,3,4,5}
print(numbers)


Checking the uniqueness property of set:

numbers = {1,2,3,4,1,4}
print(numbers)


Passing duplicate strings to a set:

names = {'John','Rob','Mike','John'}
print(names)


Set with different data types

s = {"John",2,4.5,True}
print(s)




Lecture: Set operations

Check if an item is present in the set

s = {"John",2,4.5,True}
print("John" in s)


Union

seta = {1,2,3,4,5}
setb = {4,5,6,7,8}


print(seta | setb )
print(seta.union(setb))


Intersection

seta = {1,2,3,4,5}
setb = {4,5,6,7,8}

print(seta & setb )
print(seta.intersection(setb))


Difference operation



print(seta - setb )
print(seta.difference(setb))


Symmetric difference.



print(seta ^ setb)
print(seta.symmetric_difference(setb))


Lecture: Adding & removing elements of a set

Adding element to set

seta.add(10)
print(seta)


Removing element from a set:

seta.remove(1)
print(seta)


Discard element from a set



seta.discard(10)
print(seta)


Pop



a = seta.pop()
print(a)


Clear

Removes all the elements from a set

seta.clear()


Lecture: Searching items in a list

products = ['phone','tablet','computer','laptop','journal'] item = input("Enter product to search: ") print(item in products)



Lecture: Adding & Removing Items

#inital list of products
products = ['phone','tablet','computer','laptop','journal']

# displaying initial list of products
print(f"Current list of items is:{products}")

# removing products
remove_item = input("Enter product to remove: ")
products.remove(remove_item)

# displaying list after product removal
print(f"Current list of items is:{products}")

#adding products
add_item = input("Enter product to add: ")
products.append(add_item)

# displaying list after adding products
print(f"Current list of items is:{products}")

Lecture: Adding list item at a position
#inital list of products
products = ['phone','tablet','computer','laptop','journal']

# displaying initial list of products
print(f"Current list of items is:{products}")


#adding products
add_item = input("Enter product to add: ")

#Accept product after where you want to place the current product
add_after = input(f"After which product do you want to place {add_item} ?")
index = products.index(add_after)
print(index)
products.insert(index+1,add_item)

# displaying list after adding products
print(f"Current list of items is:{products}")


Lecture: Adding, Deleting, Editing Dictionary Values

products ={
'phone':100,'tablet':200,'computer':300,'laptop':400,'journal':40
}

# print all the items inside a dictionary
print(products)

# search for price of product
product = input("Enter product to get price: ")
print(f"Price of {product} is ${products[product]}")


# add a product along with the price
new_product = input("Enter the product you want to add: ")
new_product_price = input(f"Enter the price for {new_product}")
products[new_product]=new_product_price
#showing the entire dictionary
print(f"Product successfully added, here is the list of products {products}")

# delete a product
deleted_product = input("Enter the product you want to delete")
del products[deleted_product]
print(f"Product successfully deleted, here is the list of products {products}")


# change price of the product
price_change_product = input("Enter the product to change price")
prince_change = input(f"Enter the new price for {price_change_product}")
products[price_change_product]=prince_change
print(f"Price successfully changed, here is the list of products {products}")
