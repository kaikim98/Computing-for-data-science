def P2(lst):
    n = len(lst)
    L1 = []
    while change = 0:
        change = 0 
        for i in range(n-1):
            if len(lst[i]) > len(lst[i+1]):
                a = lst[i]
                b = lst[i+1]
                lst[i] = b
                lst[i+1] = a
                break
            elif len(lst[i]) == len(lst[i+1]):
                if lst[i] > lst[i+1]:
                    a = lst[i]
                    b = lst[i]
                    lst[i] = b
                    lst[i+1] = a
                    break
                
    
    return 


def P2(lst):
   #L1 = []
    #for i in lst:
        #L1.append(len(lst[i]))
    a = sorted(lst)
    return a

P2(['solve','this','problem','or','you','will','get','f'])