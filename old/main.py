
import math


import sys


if len(sys.argv) != 2 :
    print ('Invalid arguments')
    sys.exit()
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
        
        j = 0
        # while j < len2:
        #     if j == 0:
        #         c2 = param2[j].replace(' ', '')
        #         c2 = c2.split('*')
        #         c2 = c2[0]
        #         c2 = float(c2)
        #         print (c2)
      
        #     elif j == 1:
        #         b2 = param2[j].replace(' ', '')
        #         b2 = b2.split('*')
        #         b2 = b2[0]
        #         b2 = float(b2)
        #         print (b2)

        #     elif j == 2:
        #         a2 = param2[j].replace(' ', '')
        #         a2 = a2.split('*')
        #         a2 = a2[0]
        #         a2 = float(a2)
        #         print (a2)
        #     j += 1



        while j < len2:
            x = param2[j].replace(' ', '')
            if '*' in x :
                x = x.split('*')
                if x[1][-1] == '0' :
                    c2 = x[0]
                    
                elif x[1][-1] == '1' or x[1][-1] == 'X':
                    b2 = x[0]
                  
                elif x[1][-1] == '2' :
                    a2 = x[0]
                   
               
            elif 'X' in x:
                if x[-1] == '0' :
                    c2 = 1
                   
                elif x[-1] == '1' or x[-1] == 'X':
                    b2 = 1
                    
                elif x[-1] == '2' :
                    a2 = 1
                   
            else :
                c2 = param2[j]
               
            j += 1

    # if len1 == 1:
    #     b = 0
    #     a = 0
    #     print (b)
    #     print (a)
    # if len1 == 2:
    #     a = 0
    #     print (a)


    # if len2 == 1:
    #     b2 = 0
    #     a2 = 0
    #     print (b2)
    #     print (a2)
    # if len2 == 2:
    #     a2 = 0
    #     print (a2)



if 'a' not in globals():
    a = 0

if 'b' not in globals():
    b = 0

if 'c' not in globals():
    c = 0


if 'a2' not in globals():
    a2 = 0

if 'b2' not in globals():
    b2 = 0

if 'c2' not in globals():
    c2 = 0


c = float(c) - float(c2)
b = float(b) - float(b2)
a = float(a) - float(a2)

print ("++++++++++++++++++++")
print (c)
print (b)
print (a)

cp = c
bp = b
ap = a

reduce = "Reduced form: " 
if cp != 0:
    if cp < 0:
        reduce += '- '
        cp = cp*-1
    reduce += str(cp) + ' * X^0 ' 

if bp != 0:
    if bp < 0:
        reduce += '- '
        bp = bp*-1
    else :
        reduce += '+ '
    reduce += str(bp) + ' * X^1 ' 

if ap != 0:
    if ap < 0:
        reduce += '- '
        ap = ap*-1
    else :
        reduce += '+ '
    reduce += str(ap) + ' * X^2'

reduce += '= 0'

print (reduce)
#Reduced form: 1 * X^0 + 4 * X^1 = 0
# print("Give me the a : ")
# a = input()
# a = float(a)

# print("Give me the b : ")
# b = input()
# b = float(b)

# print("Give me the c : ")
# c = input()
# c = float(c)


if a == 0 and b == 0 and c == 0:
    print ("All numbers is a solution")

elif a == 0 and b == 0 and c != 0:
    print ("There is no solution")

elif a == 0:
    print ("The only solution is :")
    print(-c/b)

else:

    delt = (b*b) - (4*a*c)

    print (delt)

    if delt > 0:
        print ("D > 0")
        print("The solutions is : ") 
        print((-b+math.sqrt(delt))/(2*a)); 
        print((-b-math.sqrt(delt))/(2*a)); 

    elif delt == 0:
        print ("D == 0")
        print ("The only solution is : ")
        print(((-b)/(2*a))); 

    elif delt < 0:
        print ("D < 0")
        print ("The solutions is : ")
        print (str(-b / (2*a)) + " + i * " + str(math.sqrt(-delt)/(2*a)))
        print (str(-b / (2*a)) + " - i * " + str(math.sqrt(-delt)/(2*a)))

