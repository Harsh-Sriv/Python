# ============================================
# INTERMEDIATE PYTHON - JSON
# ============================================

import json


# ============================================
# 1. Python dictionary
# ============================================

user = {
    "name": "Alice",
    "age": 25,
    "is_active": True,
    "skills": ["Python", "Docker", "MongoDB"],
    "address": {
        "city": "Bhubaneswar",
        "country": "India"
    }
}

print("--- Python Dictionary ---")
print(user)
print(type(user))


# ============================================
# 2. Convert Python object → JSON string
# ============================================

json_string = json.dumps(user)

print("\n--- JSON String ---")
print(json_string)
print(type(json_string))


# ============================================
# 3. Pretty JSON
# ============================================

pretty_json = json.dumps(
    user,
    indent=4
)

print("\n--- Pretty JSON ---")
print(pretty_json)


# ============================================
# 4. sort_keys
# ============================================

sorted_json = json.dumps(
    user,
    indent=4,
    sort_keys=True
)

print("\n--- Sorted Keys ---")
print(sorted_json)


# ============================================
# 5. Convert JSON string → Python object
# ============================================

json_data = """
{
    "name": "Bob",
    "age": 30,
    "skills": ["Python", "FastAPI"]
}
"""

person = json.loads(json_data)

print("\n--- JSON → Python ---")
print(person)
print(type(person))


# ============================================
# 6. Access JSON data
# ============================================

print("\nName:", person["name"])
print("Age:", person["age"])
print("Skills:", person["skills"])


# ============================================
# 7. Modify parsed JSON
# ============================================

person["age"] = 31
person["skills"].append("Docker")

print("\nModified:")
print(person)


# ============================================
# 8. JSON data types
# ============================================

data = {
    "string": "Hello",
    "integer": 100,
    "float": 3.14,
    "boolean": True,
    "null_value": None,
    "list": [1, 2, 3],
    "object": {
        "key": "value"
    }
}

json_data = json.dumps(
    data,
    indent=4
)

print("\n--- JSON Data Types ---")
print(json_data)


# ============================================
# 9. Python ↔ JSON mapping
# ============================================

print("""
Python             JSON

dict       →       object
list       →       array
tuple      →       array
str        →       string
int        →       number
float      →       number
True       →       true
False      →       false
None       →       null
""")


# ============================================
# 10. Writing JSON to a file
# ============================================

user = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Docker"]
}

with open("user.json", "w") as file:

    json.dump(
        user,
        file,
        indent=4
    )


print("\nJSON written to user.json")


# ============================================
# 11. Reading JSON from a file
# ============================================

with open("user.json", "r") as file:

    loaded_user = json.load(file)

print("\nLoaded from file:")
print(loaded_user)


# ============================================
# 12. dumps vs dump
# ============================================

# dumps → Python object to JSON STRING

json_string = json.dumps(user)

print("\ndumps:")
print(json_string)


# dump → Python object to JSON FILE

with open("user2.json", "w") as file:

    json.dump(user, file, indent=4)


# ============================================
# 13. loads vs load
# ============================================

# loads → JSON STRING to Python object

data = json.loads('{"name": "Alice"}')

print("\nloads:")
print(data)


# load → JSON FILE to Python object

with open("user.json", "r") as file:

    data = json.load(file)

print("load:")
print(data)


# ============================================
# 14. Handling invalid JSON
# ============================================

invalid_json = '{"name": "Alice",}'

try:

    data = json.loads(invalid_json)

except json.JSONDecodeError as error:

    print("\nInvalid JSON:")
    print(error)


# ============================================
# 15. Nested JSON
# ============================================

response = """
{
    "status": "success",
    "user": {
        "id": 101,
        "name": "Alice",
        "profile": {
            "city": "Bhubaneswar",
            "skills": ["Python", "AI", "Docker"]
        }
    }
}
"""

data = json.loads(response)

print("\n--- Nested JSON ---")

print(data["status"])
print(data["user"]["name"])
print(data["user"]["profile"]["city"])
print(data["user"]["profile"]["skills"][0])


# ============================================
# 16. JSON array
# ============================================

json_array = """
[
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 28}
]
"""

users = json.loads(json_array)

print("\n--- JSON Array ---")

for user in users:
    print(user["name"], user["age"])


# ============================================
# 17. Convert JSON and process it
# ============================================

json_data = """
[
    {"name": "Alice", "marks": 90},
    {"name": "Bob", "marks": 75},
    {"name": "Charlie", "marks": 88}
]
"""

students = json.loads(json_data)

top_students = [
    student
    for student in students
    if student["marks"] >= 80
]

print("\nStudents with marks >= 80:")
print(top_students)


# ============================================
# 18. Ensure ASCII
# ============================================

data = {
    "name": "Harsh",
    "language": "Python"
}

json_string = json.dumps(
    data,
    ensure_ascii=False
)

print("\nUnicode-safe JSON:")
print(json_string)


# ============================================
# 19. Custom serialization
# ============================================

from datetime import datetime

data = {
    "event": "login",
    "time": datetime.now()
}

# datetime isn't directly JSON serializable

json_string = json.dumps(
    data,
    default=str
)

print("\nCustom serialization:")
print(json_string)


# ============================================
# 20. Practical API-style example
# ============================================

api_response = """
{
    "success": true,
    "data": {
        "id": 123,
        "name": "Alice",
        "email": "alice@example.com"
    },
    "error": null
}
"""

response = json.loads(api_response)

if response["success"]:

    user = response["data"]

    print("\nAPI successful:")
    print("ID:", user["id"])
    print("Name:", user["name"])
    print("Email:", user["email"])

else:

    print("API failed:", response["error"])