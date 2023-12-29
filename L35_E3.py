name,char=input("Enter Comma seperated Name and Character : ").split(",")
print(f"Length of Name is : {len(name)}")
print(f"Character count : {name.lower().count(char.lower())}") #case sensitive
print(f"Character count : {name.strip().count(char.strip().lower())}")