# Local entrepreneur profile - Olivier Matabaro

business = {
    "Role": "Local Entrepreneur",
    "Strong in": [
        "Fruit juice production",
        "Peanut butter making",
        "Porridge flour processing"
    ]
}

print("Entrepreneur Profile\n")

print(f"Role: {business['Role']}")
print("Key strengths:")

for activity in business["Strong in"]:
    print(f"- {activity}")
