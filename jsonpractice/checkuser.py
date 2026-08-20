import json

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