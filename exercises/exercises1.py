while True:
    try:
        n=int(input("Please input your n number\n"))
        sum= 0
        avgt=0
        count=0

        for i in range(1,n+1) :
            if (i % 2 != 0):
                sum += i
            else:
                avgt += i
                count += 1

        avg = (avgt/count)


        print("Sum of the odd numbers is {}".format(sum))
        print("average of the even numbers is {}".format(avg))


        break

    except ValueError:
        print("Try again with intiger\n")
        continue