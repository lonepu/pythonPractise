user = {"name": "Nova", "age": 15, "city": "Yangon"}
print(user["name"])  # Output: Nova
print(user.get("age"))  # Output: 15
user["email"] = "no@thankyou.com"
print(user.get("email"))  # Output: