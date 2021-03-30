import sys


if len(sys.argv) != 2 :
    print ('Invalid arguments')
else :
    params = str(sys.argv[1])
    params = params.replace('-', '+-')
    params = params.split('=')
    
    param1 = params[0]
    param2 = params[1]

    param1 = param1.split('+')
    param2 = param2.split('+')


    len1 = len(param1)
    len2 = len(param2)

    if len1 > 3 or len2 > 3:
        print ('Sorry')








    else :
        i = 0
        while i < len1:
            if i == 0:
                c = param1[i].replace(' ', '')
                c = c.split('*')
                c = c[0]
                c = float(c)
                print (c)

            elif i == 1:
                b = param1[i].replace(' ', '')
                b = b.split('*')
                b = b[0]
                b = float(b)
                print (b)
            
            elif i == 2:
                a = param1[i].replace(' ', '')
                a = a.split('*')
                a = a[0]
                a = float(a)
                print (a)
            i += 1
        
        j = 0
        while j < len2:
            if j == 0:
                c2 = param2[j].replace(' ', '')
                c2 = c2.split('*')
                c2 = c2[0]
                c2 = float(c2)
                print (c2)
      
            elif j == 1:
                b2 = param2[j].replace(' ', '')
                b2 = b2.split('*')
                b2 = b2[0]
                b2 = float(b2)
                print (b2)

            elif j == 2:
                a2 = param2[j].replace(' ', '')
                a2 = a2.split('*')
                a2 = a2[0]
                a2 = float(a2)
                print (a2)
            j += 1

        
    if len1 == 1:
        b = 0
        a = 0
        print (b)
        print (a)
    if len1 == 2:
        a = 0
        print (a)


    if len2 == 1:
        b2 = 0
        a2 = 0
        print (b2)
        print (a2)
    if len2 == 2:
        a2 = 0
        print (a2)


c = c - c2
b = b - b2
a = a - a2

print ("++++++++++++++++++++")
print (c)
print (b)
print (a)