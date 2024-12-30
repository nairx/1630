students = []
for i in range(3):
    student={}
    name = input("Enter name: ")
    phone = input("Enter Phone: ")
    city = input("Enter City: ")
    student = {"name":name,"phone":phone,"city":city}
    students.append(student)

for i in students:
    # print(i["name"]+"-"+i["phone"]+"-"+i["city"])
    print(f'{i["name"]}-{i["phone"]}-{i["city"]}')
    


# students = [
#     {"name":"Student1","phone":"3434444","city":"city1"},
#     {"name":"Student2","phone":"7656566","city":"city2"},
#      {"name":"Student3","phone":"7656566","city":"city3"},
# ]
# for i in students:
#     print(i["name"])
    
    

# students = [
#     {"name":"Student1","phone":"3434444","city":"city1"},
#     {"name":"Student2","phone":"7656566","city":"city2"},
#      {"name":"Student3","phone":"7656566","city":"city3"},
# ]
# for i in students:
#     print(i["name"])