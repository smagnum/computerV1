import sys
import numpy as np

def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

if len(sys.argv) != 2 :
    print ('Invalid arguments')
    sys.exit()
else :
    # GET first argument
    params = str(sys.argv[1])
   
    # CHANGE - with +-
    params = params.replace('-', '+-')

    # GET the first and second params
    params = params.split('=')

    param1 = params[0]
    param2 = params[1]

    # CHECK negaitve
    if param1[0] == '+' and param1[1] == '-' :
        param1 = param1[1:]

    if param2[0] == '+' and param2[1] == '-' :
        param2 = param2[1:]

    # GET the vars and puiss
    param1 = param1.split('+')
    param2 = param2.split('+')

    len1 = len(param1)
    len2 = len(param2)

    puiss1 = []
    puiss2 = []

    var1 = []
    var2 = []

    i = 0
    while i < len1:
        x = param1[i].replace(' ', '')
        if '*' in x :
            
            x = x.split('*')
            if x[1][-1] == 'X' or x[1][-1] == 'x':
                x[1] = x[1] + '^1'
            var1.append(x[0]) 
            puiss1.append(x[1].upper())
        else :
            var1.append(x)
            puiss1.append('X^0')
        i += 1

    j = 0
    while j < len2:
        x = param2[j].replace(' ', '')
        if '*' in x :
            x = x.split('*')
            if x[1][-1] == 'X' or x[1][-1] == 'x':
                x[1] = x[1] + '^1'

            var2.append(x[0])
            puiss2.append(x[1].upper())
        else :
            var2.append(x)
            puiss2.append('X^0')
        j += 1

    # print (var1)
    # print (puiss1)
    # print (var2)
    # print (puiss2)
    
    # CHECK DUPLICATED
    print ('MAINTENANCE')
    dup = duplicates(puiss1, puiss1[0])
    print ('dup')
    print (dup)
    print ()
    print (var1)

    i = 1
    while i < len(dup):
        var1[dup[0]] = float(var1[dup[0]]) + float(var1[dup[i]])
        i += 1

    i = len(dup) - 1
    while i >= 1:

        
        print ('var1')
        print (var1)
        print ('dup')
        print (dup)
        print (dup[i])
        del var1[dup[i]]
        
        i -=1 


        
    print ('var1')
    print (var1)
    print ()

    print ('MAINTENANCE')

    # while i < len(puiss1):
        
    #     print (dup)
    #     i += 1
    # CHECK DUPLICATED
    # i = 0
    # while i < len(puiss1):
    #     dup = duplicates(puiss1, puiss1[i])

    #     if len(dup) > 1:
    #         j = 1
    #         while j < len(dup) :
    #             print (j)
    #             print (dup)
    #             # print (len(dup))
    #             print (dup[j])
    #             print (var1)

    #             try :
    #                 var1[dup[0]] = float(var1[dup[0]]) + float(var1[dup[j]])
    #                 del(puiss1[dup[j]])
    #                 del(var1[dup[j]]) 
    #             except :
    #                 print ('hania2')
                
    #             try :
    #                 del(dup[j+1])
    #             except:
    #                 print ('hania')
           
    #             #dup[j+1] = int(dup[j+1]) - 1
                
    #             j+=1
    #         # print (dup)
    #     i += 1


# SECONDE

    print ('MAINTENANCE')
    dup = duplicates(puiss2, puiss2[0])
    print ('dup')
    print (dup)
    print ()
    print (var2)

    i = 1
    while i < len(dup):
        var2[dup[0]] = float(var2[dup[0]]) + float(var2[dup[i]])
        i += 1

    i = len(dup) - 1
    while i >= 1:

        
        print ('var2')
        print (var2)
        print ('dup')
        print (dup)
        print (dup[i])
        del var2[dup[i]]
        
        i -=1 


        
    print ('var2')
    print (var2)
    print ()

    print ('MAINTENANCE')

    # i = 0
    # while i < len(puiss2):
    #     dup = duplicates(puiss2, puiss2[i])
    #     if len(dup) > 1:
    #         j = 1
    #         while j < len(dup) :
    #             # print (dup[j])
    #             print (i)
                
    #             var2[dup[0]] = float(var2[dup[0]]) + float(var2[dup[j]])
    #             del(puiss2[dup[j]])
    #             del(var2[dup[j]])
    #             j+=1
    #         # print (dup)
    #     i += 1

    # print (var1)
    # print (puiss1)
    # print (var2)
    # print (puiss2)
    # print (var1)
    # print (var2)
    # print (puiss1)
    # print (puiss2)
  

    
    # print (var1)
    # print (puiss1)
    # print ('=================')
    # print (var2)
    # print (puiss2)
    # print ('=================')

    # len_var = len1 - len2
    # if len_var > 0 :
    #     len_var = len1
    # else :
    #     len_var = len2

    # k = 0
    # while k < len_var : 
    #     if puiss1[k] in puiss2:
    #         print (puiss1[k])
    #         print 
       
    #     k += 1 


    # CHECK the same puiss and do addition
    len1 = len(puiss1)
    len2 = len(puiss2)
    exist = []
    k = 0
    while k < len1:
        u = 0
        while u < len2:
            if puiss1[k] == puiss2[u] :
                # print ('puiss1')
                # print (puiss1[k])
                # print ('puiss2')
                # print (puiss2[u])
                var1[k] = float(var1[k]) - float(var2[u])
                exist.append(puiss2[u])

            u += 1

        k += 1


    # print ('////////@@@VAR1@@@@//////')
    # print (var1)

    # print ('////// @@@@@exist@@@@ ////////')
    # print (exist)


    # print ('////// @@@@@DIFF@@@@ ////////')


    # XOR operator: 
    diff = set(exist) ^ set(puiss2)


    # print (diff)

    for di in diff :
        i = 0 
        while i < len(puiss2):
            if di == puiss2[i] :
                # print (di)
                # print (i)
                puiss1.append(di)
                var1.append(int(var2[i]) * -1)
            i += 1
        # if di in puiss2 :
        #     print (di)
        #     i = 0 
        #     while i < di :
        #         if 


    # print ('////////@@@FINAL_VAR@@@@//////')
    # print (var1)

    # print ('////////@@@FINAL_PUISS@@@@//////')
    # print (puiss1)

    # print (var1)
    # print (puiss1)






    len_res = len(var1)
    # print (len_res)

                # CHECK DUPLICATED
    # i = 0
    # while i < len_res:
    #     dup = duplicates(puiss1, puiss1[i])
    #     print (dup)
    #     if len(dup) > 1 :
    #         j = 0
    #         while j < len(dup) :
    #             var1[dup[0]] = int(var1[dup[0]]) + int(var1[dup[j]])
    #             j += 1
    #         print (dup)
    #         print ('////// VAR1 ///////')
    #         print (var1)
    #     i += 1


    t = 0
    while t < len_res :
        var1[t] = str(var1[t]) + '*' + puiss1[t]
        t += 1

    # print ('#########RESULT#########')
    # print (var1)

    new = sorted(var1, key=lambda x: int(x[-1]))

    # print ('///new///')
    print (new)


