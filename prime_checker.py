to_continue="yes"
while to_continue.lower()=="yes":
    n = int(input("Enter a number: "))
    is_prime="yes"
    for i in range(2, n):
        if n%i!=0:
            is_prime="yes"
            continue
        elif n%i==0:
            is_prime="no"
            break
    if is_prime.lower()=="yes":
        print("Number is prime")
    else:
        print("Number is not prime")
    to_continue=input("Do you wish to continue? ")
        

    









        
        















# while to_continue.lower()=="yes":
#     n = int(input("Enter a number: "))
#     is_prime="yes"
#     for i in range(2, n):
#          if n%i!=0:
#              is_prime="yes"
#             continue
#         elif n%i==0:
#             is_prime="no"
#             break
#     if is_prime.lower()=="yes":
#      print("Number is prime")
#     else:
#         print("Number is not prime")
#     to_continue=input("Do you wish to continue? ")
    
