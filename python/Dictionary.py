info = {'name' : 'xmas',
        'email': 'fun',
        'favourite item': 'nil'
       }

print(info.values())
print('name' in info.values())
print("")
#print the keys in the dictionary
for item in info.values():
    print(item)
print("")
#print the item in the dictionary
for item in info:
    print(item)
print("")

for item in info.items():
    key, value = item
    print("the key is: " + key + ", the value is: " + value)
print("")

#adding all info into a list
info2 = {'name' : 'xmas2',
        'email': 'fun2',
        'favourite item': 'nil2'
       }
mycontact = []
mycontact.append(info2)
mycontact.append(info)       #add info into the list
print(mycontact)
print(mycontact[0]['email']) #get the key
