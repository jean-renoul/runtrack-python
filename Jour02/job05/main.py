for nombres in range (1,101):

    if nombres % 3 == 0 and nombres %5 == 0:
        print ("FizzBuzz") 
    elif nombres % 3 == 0:
        print ("Fizz")
    elif nombres % 5 ==0:
        print ("Buzz")
    else:
        print (nombres)