
from historyy import histo
def orgpack (a) :
    #a=histo(z)
    b=a[len("Package: "):a.find("Version")-1]
    c=a[a.find('Version')+len('Version: ') : len(a)]
    L= {'Package':b,'Version':c}

    return L
def orgsize (z):
    dict={}
    i=1
    a=str(z)+"\n"
    while len(a)>2:
        x=a.find("\n")
        y=a.find("\t")
        dict[str(i)+": "+a[y+1:x]]=a[:y]
        i=i+1
        a=a[x+1:]
    return dict
#x=orgsize(histo(34797))
#print(x[1])


#app.run()
