def abdo(n) :
    print (n)
    n = str(n)
    length = len(n)



    res = 0
    i = 0
    while i < length :
        res += int(n[i]) * int(n[i])
        i += 1

    if len(str(res)) == 1 :
        print (res)

        if res == 1 :
            print ('true')
        else :
            print ('false')
    else :
        abdo (res)


abdo (222)
