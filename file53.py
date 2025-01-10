import re
str = "No more dull edges in your company.Make your employees into masters Nurture talent with instructor-led courses on trending technologies"
pattern = "in"
result = re.findall(pattern,str)
print(result)


# import re
# str = "xyz@gmail.com,cathy@email.com;amy@gmail.com"
# pattern = ",|;"
# result = re.split(pattern,str)
# print(result)


# import re
# str = "xyz@gmail.com"
# pattern = "@"
# result = re.split(pattern,str)
# print(result)



# import re
# str = "xyz@gmail.com"
# print(re.sub("gmail","ymail",str))