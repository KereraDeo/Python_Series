#Dictionary = collection of key-value pairs.
user={'Name':'Kerera Deo','Sex':'Male'}
print(user['Name']) #Acess to user's name

#For a more interesting example, let’s track the position of an alien that 
#can move at different speeds. We’ll store a value representing the alien’s 
#current speed and then use it to determine how far to the right the alien 
#should move:

alien_o={'x_positition':0,'y_position':25,'speed':'medium'}
#move the alien to the right .
#Determine how far to move the alien based on its current speed 
if alien_o['speed']=='slow':
    x_increment=1
elif alien_o['speed']=='medium':
    x_increment=2
else:
    x_increment==3
#new position=old position + x_increment
alien_o['x_positition']=alien_o['x_positition']+x_increment
print(f"the new position:{alien_o['x_positition']}")
#remove key-value pairs using del function ....e.g ..del alien_o['x_position']
for alien in alien_o.values():
    print(alien)

    #LIST OF DICTIONARIES IS POSSIBLE