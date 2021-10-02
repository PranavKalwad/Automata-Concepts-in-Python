# Given regex of the form PES[0-9]UG[0-9]{2}{CS|EC|EE|ME|CV|BT}[0-9]{3} 
string=input("Enter a string:")
def check_regex(string):
    if string[0:3]==("PES"):
        if int(string[3]) in range(0,10):
            if string[4:6]=="UG":
                if int(string[6:8]) in range(0,100): 
                    if string[8:10]=="CS" or string[8:10]=="EC" or string[8:10]=="EE" or string[8:10]=="ME" or string[8:10]=="CV" or string[8:10]=="BT":
                        if int(string[10:13]) in range(0,1001):
                            return 1
    else:
        return 0
x=check_regex(string)
if(x==1):
    print("String is according to the given regex")
else:
    print("String is not according to given regex")