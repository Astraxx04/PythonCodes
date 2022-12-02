def isPhoneNumber(text):
    print("Input: ",text)
    if len(text) != 12:
        return False
    for i in range(0, 3):
       	if not text[i].isdecimal():
       		return False
    if(text[3] != '-'):
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
           	return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
       	if not text[i].isdecimal():
            return False
    return True
    
text1="123-123-1234"
text2="12-1234-1234"
text3="a23-123-1234"
print(isPhoneNumber(text1))
print(isPhoneNumber(text2))
print(isPhoneNumber(text3))