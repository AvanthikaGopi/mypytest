to_continue="yes"
while to_continue=="yes":
    numbers=[]
    for i in range(5):
        n=int(input("Enter a number: "))
        numbers.append(n)
    print(numbers)
    to_continue=input("Do you want to continue? (yes/no): ")
print("Thank you")