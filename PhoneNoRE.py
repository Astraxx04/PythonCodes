import re
def isPhoneNumber(text):
    x=re.findall("[1-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]",text)
    if x==[]:
        return False
    return True

text1="123-123-1234"
text2="12-1234-1234"
text3="a23-123-1234"
print(isPhoneNumber(text1))
print(isPhoneNumber(text2))
print(isPhoneNumber(text3))