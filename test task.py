listOfID = []
listOfPw = []
print("1) Creater a new User ID \n 2) Change a password \n 3) Display all user IDs \n 4) Quit")
selection = int(input("Enter Selection: "))

def pwCheck(pw):
    score = 0
    listOfNumbers = ["1","2","3","4","5","6","7","8","9"]
    listOfSpecial = ["!", "£", "%", "&", "<", ">", "*", "@"]
    scoreP1 = False
    scoreP2 = False
    if len(pw) > 7:
        score += 1   
    for letter in pw:
        if letter in listOfNumbers:
            scoreP1 = True
        if letter in listOfSpecial:
            scoreP2 = True      
    if scoreP1 == True:
        score += 1
    if scoreP2 == True:
        score += 1
        
    if score <= 2:
        answer = "weak"
    else:
        answer = "strong"
    return(answer)
        
while selection != 4:
    if selection == 1:
        idEnter = input("Enter user ID: ")
        while idEnter in listOfID:
            idEnter = input("ID already in use, choose another: ")
        listOfID.append(idEnter)
        password = input("Enter a password: ")
        while pwCheck(password) == "weak":
            password = input("Password too weak, must contain numbers, special characters and should have at least 8 characters \n Enter password: ")
        print("This password is strong")
        
        print(" \n1) Creater a new User ID \n 2) Change a password \n 3) Display all user IDs \n 4) Quit")
        selection = int(input("Enter Selection: "))
    elif selection == 2:
        IDchecker = input("Insert ID")
        while IDchecker not in listOfID:
            IDchecker = input("Invalid ID, please enter existing ID: ")
        if IDchecker in listOfID:
            newPw = input("Enter new password: ")
            while pwCheck(newPw) == "weak":
                newPw = input("Password too weak, must contain numbers, special characters and should have at least 8 characters \n Enter password: ")
                pwCheck(newPw)
            for pwInList in listOfPw:
                if listOfPw[pwInList] == IDchecker:
                    listOfPw[pwInList] = newPw
            print("Your password has been changed")
            
            print(" \n1) Creater a new User ID \n 2) Change a password \n 3) Display all user IDs \n 4) Quit")
            selection = int(input("Enter Selection: "))
    elif selection == 3:
        print(listOfID)
        print(" \n1) Creater a new User ID \n 2) Change a password \n 3) Display all user IDs \n 4) Quit")
        selection = int(input("Enter Selection: "))
        
        
        
        
        