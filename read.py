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

    puiss1 = []
    puiss2 = []

    var1 = []
    var2 = []

    i = 0
    while i < len1:
        x = param1[i].replace(' ', '')
        if '*' in x :
            x = x.split('*')
            var1.append(x[0])
            puiss1.append(x[1])
        i += 1

    j = 0
    while j < len2:
        x = param2[j].replace(' ', '')
        if '*' in x :
            x = x.split('*')
            var2.append(x[0])
            puiss2.append(x[1])
        j += 1
    
    print (var1)
    print (puiss1)
    print ('=================')
    print (var2)
    print (puiss2)
    print ('=================')

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



    exist = []
    k = 0
    while k < len1:
        u = 0
        while u < len2:
            if puiss1[k] == puiss2[u] :
                var1[k] = float(var1[k]) - float(var2[u])
                exist.append(puiss2[u])

            u += 1

        k += 1


# print ('////////@@@VAR1@@@@//////')
# print (var1)

print ('////// @@@@@exist@@@@ ////////')
print (exist)


print ('////// @@@@@DIFF@@@@ ////////')
# XOR operator: 
diff = set(exist) ^ set(puiss2)

print (diff)

for di in diff :
    i = 0 
    while i < len(puiss2):
        if di == puiss2[i] :
            print (di)
            # print (i)
            puiss1.append(di)
            var1.append(int(var2[i]) * -1)
        i += 1
    # if di in puiss2 :
    #     print (di)
    #     i = 0 
    #     while i < di :
    #         if 


print ('////////@@@FINAL_VAR@@@@//////')
print (var1)

print ('////////@@@FINAL_PUISS@@@@//////')
print (puiss1)

