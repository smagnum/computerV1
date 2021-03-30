
import math


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
        print ("The polynomial degree is stricly greater than 2, I can't solve.")
        sys.exit()


    else :
        i = 0
        while i < len1:
            x = param1[i].replace(' ', '')
            if '*' in x :
                x = x.split('*')
                if x[1][-1] == '0' :
                    c = x[0]
   
                elif x[1][-1] == '1' or x[1][-1] == 'X':
                    b = x[0]
  
                elif x[1][-1] == '2' :
                    a = x[0]
        
               
            elif 'X' in x:
                if x[-1] == '0' :
                    c = 1
               
                elif x[-1] == '1' or x[-1] == 'X':
                    b = 1

                elif x[-1] == '2' :
                    a = 1
                
            else :
                c = param1[i]
               
            i += 1
            # if i == 0:
            #     c = param1[i].replace(' ', '')
            #     c = c.split('*')
            #     c = c[0]
            #     c = float(c)
            #     print (c)

            # elif i == 1:
            #     b = param1[i].replace(' ', '')
            #     b = b.split('*')
            #     b = b[0]
            #     b = float(b)
            #     print (b)
            
            # elif i == 2:
            #     a = param1[i].replace(' ', '')
            #     a = a.split('*')
            #     a = a[0]
            #     a = float(a)
            #     print (a)
            # i += 1


if 'a' not in globals():
    a = 0

if 'b' not in globals():
    b = 0

if 'c' not in globals():
    c = 0

print ('A = ' + str(a))
print ('B = ' + str(b))
print ('C = ' + str(c))
