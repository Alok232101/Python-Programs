name=input("Enter your name :")
fc=input("which character would you want to know are present in your name or not :")
if fc in name:
    print(f"{fc} is present in {name}")
else:
    print(f"{fc} is not present in {name}")