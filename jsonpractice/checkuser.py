import json

#this program get a users username and check 
# if the username exist in the json file information 
# prints the password else get the password from user
# and record it in json file

def main():

    username=input("enter userame:")

    with open ("jsonp.json","r") as info:
        users=json.load(info)

    registered,password=checkout(username,users)
    if registered==True:
        print(password)

    else:
        new={"name":username,
            "pass":password}
        
        users.append(new)

        with open ("jsonp.json","w") as info:
            json.dump(users,info,indent=4)
            print("register done!")

def checkout(n,list):
    
        for i in list:
            if n==i["name"]:
                return True,i["pass"]
                
            
        p=input("you didn't register yet.\n please enter a password:")
        return False,p

main()