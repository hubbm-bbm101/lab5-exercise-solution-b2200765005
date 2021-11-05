x = str(input("input your e-mail\n"))
while True:
    try:
        k=0
        m=0
        for i in x:
            if ( i == '@'):
                k=1


            elif(i == '.'):
                m=1

        if(k==1 and m==1):
            print("its valid")
        else:
            print("its not  valid")

        break
    except:
        print("try again")
        continue
