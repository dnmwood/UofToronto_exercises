largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        num = "uhoh"

    if num == "uhoh":
        print("Invalid input")
    elif largest is None and smallest is None:
        largest = num
        smallest = num
    elif num < smallest:
        smallest = num
    elif num > largest:
        largest = num

print("Maximum", largest)
print("Minimum", smallest)
