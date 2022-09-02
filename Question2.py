#question 2

"""  Create an empty dictionary called dog
    • Add name, color, breed, legs, age to the dog dictionar """

d={"name":"rosie","color":"brown","breed":"golden ","legs":"4","age":"2 years"}
print("The dog list is ",d)

""" Create a student dictionary and add first_name, last_name, gender, age, marital status, 
skills, country, city and address as keys for the dictionary"""

student={
    "first_name":"pranav",
    "last_name":"garipelli",
    "gender":"male",
    "age":"23",
    "martial status":"single",
    "skills":["java","javascript"],
    "country":"India",
    "city":"hyderabad",
    "address":"3-2-212, hyderabad, telangana, india"

}
print("student info list: ",student)

# Get the dictionary values as a list
print("length of student list :",len(student))

# Get the value of skills and check the data type, it should be a list
print("The values and type of skills key: ",student["skills"],type(student["skills"]))

# Get the dictionary keys as a list
print("printing keys as a list: ",student.keys())

# Get the dictionary values as a list
print("printing values as a list: ",student.values())