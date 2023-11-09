name = "Baii"
phone = "01327012122"
email = ""
size_name = len(name)
size_phone = len(phone)
size_email =len(email)



if(size_name ==0 or size_phone ==0 or size_email==0 ):
    print("the field can not be empty")
else:
    if(size_name<3):

        print("the size name must be minimum 3")
    elif(size_phone!=11):
        print("the phone size must be minimum 11")
    else:
        print("success")


