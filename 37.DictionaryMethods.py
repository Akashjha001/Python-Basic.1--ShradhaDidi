student = {
    "name": "akash jha",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "maths": 99
    }
}
print(student.keys())
print(list(student.keys()))

print(student.values())
print(list(student.values()))

print(student.items())
print(list(student.items()))

print(student.get("name"))

student.update({"state": "Delhi"})
print(student)