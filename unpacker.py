def unpack_str(s, ttype='k'):
    kk = []
    num_bracket = 0
    s_splitted = s.split(".")
    if(len(s_splitted)<2) and (ttype == 'v'):
        return s
    for i in s_splitted:
        if(len(i)>0):
            kk.append(f"<'{i}'")
            num_bracket += 1
    return ":".join(kk) + ':{}' + '>'*num_bracket

def master_unpacker(e, ttype='k'):
    if(type(e) == dict):
        temp = {}
        for k in e:
            kk = master_unpacker(k)
            vv = master_unpacker(e[k], 'v')
            if(type(vv)== str and '<' not in vv):
                hhh = kk.format('"' + vv + '"').replace('<', '{').replace('>', '}')
            else:
                hhh = kk.format(vv).replace('<', '{').replace('>', '}')
                
            temp.update(eval(hhh))
        return temp
            
    if(type(e) == str):
        return unpack_str(e, ttype)
    if(type(e) == list):
        temp = []
        for i in e:
            rr = master_unpacker(i)
            temp.append(rr)
        return temp
    else:
        return e
    
d = {"Key1.Key2.Key3(someparameter)": {"balh.Key1": [{'a1.a2':1, 'b':2}]}}
master_unpacker(d)

# output
#{'Key1': {'Key2': {'Key3(someparameter)': {'balh': {'Key1': [{'a1': {'a2': 1},'b': 2}]}}}}}
