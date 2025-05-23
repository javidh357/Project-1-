names = []
user=input("Enter names : ")
names.append(user)

user=input("Enter names : ")
names.append(user)

user=input("Enter names : ")
names.append(user)

user=input("Enter names : ")
names.append(user)

print(names)

remove_names=input("Enter names to remove : ")

if remove_names in names:
    names.remove(remove_names)
    print(names)
else:
    print("Sorry, the name is not in the list.")
