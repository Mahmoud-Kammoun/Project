import flask
from toporg import orgnaize
from flask import request, jsonify,redirect,render_template
from historyy import histo,histoo,histooo
from tasti import nameid,nameid_host,nameidd
import time
from updatexml import add_command,delete_command,update_command,delete_commandid
from Organisation import orgpack,orgsize
from update_item import subfolder,folder,deel,cre,version,top
from universal import universalCL
from add import getname,getCL
from histo import list_host
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():
    x=list_host()

    okk={}

    for key in x:
        tes={}
        tes["Memory"]=float((histo(nameidd("per memory",str(x[key])))))
        tes["Space"]=float(histo(nameidd("space per",str(x[key]))))
        tes["CPU"]=float(histo(nameidd("per cpu",str(x[key]))))
        okk[x[key]]=tes

    return render_template("index.html", result = okk,memory=str(round(float(histoo(34474)),2)),space=str(round(float(histoo(34557)),2)),cpu=str(round(float(histoo(34473)),2)))

@app.route('/aa', methods=['GET','POST'])
def form():

        return render_template('login.html')
@app.route('/aa/3', methods=['GET'])
def forme():
    l=list_host()
    p=1
    imp=1
    a={}
    b={}
    okk={}
    okkk={}

    for k in l:
        if (int(k)+1) % 2 == 0:
            a[str(p)]=l[str(k)]
            p=p+1
            tes={}
            tes["Memory"]=float((histo(nameidd("per memory",str(l[k])))))
            tes["Space"]=float(histo(nameidd("space per",str(l[k]))))
            tes["CPU"]=float(histo(nameidd("per cpu",str(l[k]))))
            okk[l[k]]=tes


        else:
            b[str(imp)]=l[str(k)]
            imp=imp+1
            tes={}
            tes["Memory"]=float((histo(nameidd("per memory",str(l[k])))))

            tes["Space"]=float(histo(nameidd("space per",str(l[k]))))
            tes["CPU"]=float(histo(nameidd("per cpu",str(l[k]))))
            okkk[l[k]]=tes




    return render_template('action.html',y=getname("command.xml"),result=l,p=okk,imp=okkk)

@app.route('/api/action', methods=['GET','POST'])
def api_id():
    l={}
    host_id=request.args.getlist("host")
    id = int(request.args['id'])
    for i in range (len(host_id)):
            l[str(i+1)]=str(host_id[i])

    if id==3:
        path = str(request.args['path'])
        k={}
        for i in range (len(l)):

            subfolder(path,l[str(i+1)])

            w=orgsize(histo(str(nameidd("folder size",(str(l[str(i+1)]))))))
            k[l[str(i+1)]]=w


        return render_template("action_folder.html", result = w ,aa=l,res=k, title= "Subfolder Size",type="SubFolder",the=host_id)
    elif id==4:
        path = str(request.args['path'])
        k={}
        for i in range (len(l)):

            folder(path,l[str(i+1)])
            w=orgsize(histo(str(nameidd("folder size",(str(l[str(i+1)]))))))
            k[l[str(i+1)]]=w


        return render_template("action_folder.html", result = w ,aa=l,res=k,title= "Subfolder Size",type="SubFolder",the=host_id)

    elif id==1:
        path = str(request.args['path'])
        for i in range (len(l)):
            cre(path,l[str(i+1)])


        return render_template("action_create.html", result = path, title= "Creation of a folder",dict=l,memory=str(round(float(histoo(34474)),2)),space=str(round(float(histoo(34557)),2)),cpu=str(round(float(histoo(34473)),2)),the=host_id)
    elif id==2:
        path = str(request.args['path'])
        for i in range (len(l)):
            deel(path,l[str(i+1)])

        return render_template("action_delete.html", result = path, title= "Deletion of a folder",dict=l,memory=str(round(float(histoo(34474)),2)),space=str(round(float(histoo(34557)),2)),cpu=str(round(float(histoo(34473)),2)),the=host_id)
    elif id==5:
        path = str(request.args['path'])
        k={}
        for i in range (len(l)):
            version(path,l[str(i+1)])
            w=orgpack(histo(str(nameidd("pkgversion",(str(l[str(i+1)]))))))
            k[l[str(i+1)]]=w
        return render_template("action_version.html", result = k,title= "Version of a Package",memory=str(round(float(histoo(34474)),2)),space=str(round(float(histoo(34557)),2)),cpu=str(round(float(histoo(34473)),2)),the=host_id)
    elif id == 6:
        path = str(request.args['path'])
        k={}
        for i in range (len(l)):
            top(path,l[str(i+1)])
            w=orgnaize((str(nameidd("top",(str(l[str(i+1)]))))))
            k[l[str(i+1)]]=w

        return render_template("action_top.html", v=k,name=path)
    else:
        k={}
        universalCL(getCL("command.xml")[str(id)])
        for i in range (len(l)):
            w=histo(str(nameidd("universal",(str(l[str(i+1)])))))
            k[l[str(i+1)]]=w


        return render_template("action_terminal.html",result=k,path=host_id)


@app.route('/aa/1', methods=['GET','POST'])
def data():

   return render_template("add.html")
@app.route('/aa/2', methods=['GET','POST'])
def handle_data():

    name=request.form['name']
    script = request.form['script']
    dict=getCL("command.xml")
    fix=6

    for i in dict.keys():
        if int(i)>int(fix):
            fix=i
    iddd=int(fix)+1
    add_command(str(name),str(script),str(iddd))

    l=list_host()
    p=1
    imp=1
    a={}
    b={}
    okk={}
    okkk={}

    for k in l:
        if (int(k)+1) % 2 == 0:
            a[str(p)]=l[str(k)]
            p=p+1
            tes={}
            tes["Memory"]=float((histo(nameidd("per memory",str(l[k])))))
            tes["Space"]=float(histo(nameidd("space per",str(l[k]))))
            tes["CPU"]=float(histo(nameidd("per cpu",str(l[k]))))
            okk[l[k]]=tes

        else:
            b[str(imp)]=l[str(k)]
            imp=imp+1
            tes={}
            tes["Memory"]=float((histo(nameidd("per memory",str(l[k])))))
            tes["Space"]=float(histo(nameidd("space per",str(l[k]))))
            tes["CPU"]=float(histo(nameidd("per cpu",str(l[k]))))
            okkk[l[k]]=tes
    return render_template('action.html',y=getname("command.xml"),result=l,p=okk,imp=okkk)


@app.route('/aa/delete', methods=['GET'])
def delete():

   return render_template("delete.html",result=getname("command.xml"))
@app.route('/aa/delete', methods=['POST'])
def handle_dataa():
    n = request.form['root']
    name=str(n)
    delete_command(name)
    z=name+" was deleted"


    return render_template("delete.html",result=getname("command.xml"))
@app.route('/aa/update', methods=['GET'])
def update():

   return render_template("update.html",result=getname("command.xml"))
@app.route('/aa/update/1', methods=['POST'])
def handle_dataaa():
    n = request.form['root']
    tuple=update_command("command.xml",n)

    return render_template("update_1.html",id=tuple[0],name=tuple[1],script=tuple[2])
@app.route('/aa/update/2', methods=['GET','POST'])
def handle_dat():
    id = request.form['id']
    name=request.form['name']
    script = request.form['script']
    delete_commandid(str(id))
    add_command(str(name),str(script),str(id))
    o=list_host()
    l=list_host()
    p=1
    imp=1
    a={}
    b={}
    okk={}
    okkk={}

    for k in l:
        if (int(k)+1) % 2 == 0:
            a[str(p)]=l[str(k)]
            p=p+1
            tes={}
            tes["Memory"]=float((histo(nameidd("per memory",str(l[k])))))
            tes["Space"]=float(histo(nameidd("space per",str(l[k]))))
            tes["CPU"]=float(histo(nameidd("per cpu",str(l[k]))))
            okk[l[k]]=tes


        else:
            b[str(imp)]=l[str(k)]
            imp=imp+1
            tes={}
            tes["Memory"]=float((histo(nameidd("per memory",str(l[k])))))

            tes["Space"]=float(histo(nameidd("space per",str(l[k]))))
            tes["CPU"]=float(histo(nameidd("per cpu",str(l[k]))))
            okkk[l[k]]=tes
    return render_template('action.html',y=getname("command.xml"),result=l,p=okk,imp=okkk)

app.templates_auto_reload=True
app.run()
