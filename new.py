name=input("Name: ")
age=int(input("Age: "))
fav_num=int(input("Favorite number: "))
print(age+10)
print(fav_num**2)
if fav_num%2==0:
    print("Even")
    k="Even"
else :
    print("Odd")
    k="Odd"
print(f"Hi {name}! In 10 years you'll be {age+10} . Your favorite number squared is {fav_num**2}, and it is {k}.")
