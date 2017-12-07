while True:
    x=input("enter a number to count to: " + " when done hit "'q'" to quit")
    if x == 'q' or x == "quit":
        break
    x=int(x)
    y=1
       
    while True:    
        print(y)
        y=y+1
        if y>x:
            break
        elif y==300:
            print("your number is too large")
            break
    
    
     
