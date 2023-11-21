for nombres in range (1,1001):
    if nombres>1:
        for i in range(2,nombres):
            if(nombres%i)==0:
                break
        else:
            print(nombres)