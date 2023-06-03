#A list = a collection of items in a particular order. You can make a list that 
#          includes the letters of the alphabet, the digits from 0–9, or the names of 
#          all the people in your family enclosed in []
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

#Accessing elements in a list

print(bicycles[1].title())
for bicycle in bicycles:
    print(bicycle.title())

print(f"my first bicycle was a {bicycles[0].title()} !")

#Changing,adding and removing elements from a list
bicycles[0]='ducati' #modifies element at index[0]
print(bicycles)

#adding elements to a list .....use append fxn

bicycles.append('firelli')# adds firelli at the end of the list

print(bicycles)

motorcycles=[]
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('honda')

print(motorcycles)

#Inserting elements in a list....use insert() method

motorcycles.insert(0,'ducati')
print(motorcycles)

#Removing elements from a list....(i)using the del function
del motorcycles[0]
print(motorcycles)

#..................................(ii)using the pop() method
#                                  This removes the item temporarily
#popped_motorcycles=motorcycles.pop()
#print(popped_motorcycles) #prints out only the last element in the list

print(motorcycles) #prints the list minus the last element

#It is possible to [pop any item from the list using its index e.g motorcycles.pop(2)

#Removing an item by value
motorcycles.remove('yamaha') #Removes yamaha from the list

print(motorcycles)

#ORGANISING A LIST

#Sorting a list permanently with the sort()method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
for car in cars:
    print(car.title())
print(cars)

#sorting in reverse order
cars.sort(reverse=True)
for car in cars:
    print(car.title())

#Sorting a list temporarily using the sorted method
cheap_cars=['bmw','audi','toyota','subaru']
print(f"Here is the original list:{cheap_cars}")

print(f"Here is the sorted list: {sorted(cars)}")
#or print(sorted(cars))
#printing a list in reverse order
cheap_cars.reverse()
print(cheap_cars)
#length of a list is obatined by len(cheap_cars) for example....