admins =["samar","sahar","seham","asmaa","arwa","talia"]#admin list
#login
name = input("Please Enter Your name").strip().lower()
# if name in admins
if name in admins:
    print(f"hello {name} welcome back")
    option = input("Delete or Update your name?").strip().capitalize()
    if option == "Update":
        theNewName = input("Your new name please:").strip().lower()
        admins[admins.index(name)]= theNewName

        print("Name updated")
        print(admins)
    elif option =="Delete":
        admins.remove(name)
        print("name deleted")
        print(admins)
    else :
        print("wrong option")
else:
    # print("You are not admin")
    status = input("not admin ,add you Y,N?").strip().capitalize()
    if status =="Yes" or status =="Y":
       print("you have been added")
       admins.append(name)
       print(admins)
    else:
       print("you are not added")


