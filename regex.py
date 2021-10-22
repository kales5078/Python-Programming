import re

inp = "Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016"

inp = re.sub('<<name>>','suraj',inp)
inp = re.sub('<<full name>>','suraj kale',inp)
inp =  re.sub('xxxxxxxxxx','9274631451',inp)
inp = re.sub('01/01/2016','21/10/2021',inp)
print(inp)