'''
@Author : Suraj Kale
@Date : 2021-10-18
@Last Modified by : Suraj Kale
@Last Modified Date : 2021-10-18
@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”
'''

UserName = str(input("Enter Your UserName "))

if len(UserName) >= 3:
    print("Hello, " + UserName + " How Are You ?")
else:
    print(UserName, "Not Valid")
    print("Enter Minimum 3 Characture UserName")
