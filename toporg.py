from historyy import histo
def orgnaize(x):
    a=(histo(x))

    #print(a.rfind(":"))
    b=a.rfind("/")
    #print(len(a))
    mem=(a[:b])
    cpu=(a[b+1:])

    dict={'memory  utilisation %':str(mem),"CPU utilisation %":str(cpu)}
    return dict

#print(orgnaize(34798))
