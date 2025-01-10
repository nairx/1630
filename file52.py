import re
str = 'hello'
pattern = "hello|namaste"
flag = re.search(pattern,str)
if flag:
    print("valid")
else:
    print("Invalid")

#[] - set
#\d - sequence


# import re
# str = "%%$^%^"
# pattern = "[a-zA-Z0-9]"
# flag = re.search(pattern,str)
# if flag:
#     print("valid email")
# else:
#     print("Invalid email")
    
# import re
# str = "john@gmail.com"
# pattern = "@"
# flag = re.search(pattern,str)
# if flag:
#     print("valid email")
# else:
#     print("Invalid email")