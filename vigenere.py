def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
    return dic 

def encrypt_vigenere(value, key):
    dic = comparator(value, key)
    print 'Compare encrypt_vigenere', dic
    lis = []
    d = form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis

def decrypt_vigenere(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict() 

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code
