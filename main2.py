import json
list_name = []
list_email =[]
list_password=[]
my_dict ={}
for i in range(5):
    names=input("enter your name:")
    password=input("enter your password:")
    if ord(password[0]) < 65 or ord(password[0])>97:
        print("you bayad upercase start in password:")
        password =input("enter password:")
    email=input("enter your email:")
    list_password.append(password)
    list_email.append(email)
    if names not in list_name:
        list_name.append(names)
    elif names in list_name:
        new_name =(f"enter new name:{names.upper()} ")
    else:
        new_name =(f"enter new name:{names.upper()} ")
        list_name.append(new_name)
my_dict["name"] = list_name
my_dict["password"] = list_password
my_dict["name"] = list_email
print(my_dict)
with open("my_dict.json",'w') as file:
    json.dump(my_dict, file)
    file.close()