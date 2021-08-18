# Project
This project is an aplication web that changes data with Zabbix software through Zabbix's API in order to add other specific commands to the server monitoring which makes access control management easier and more practical to improve efficiency and rapidity.<br/>
To runing perfectly the project you need to follow the steps below
### Step 1
In zabbix_agentd.conf file we locate the **"UserParameters"** attributes and we set them to create our specific command bellow. <br/>
+ UserParameter=run[*],python3 "...../....../...../$1" ***" You should write the path of this file before "/$1" "***   
+ UserParameter=version[*],dpkg --status $1 | grep -E '^(Version|Package)'
+ UserParameter=list.pkg,dpkg --status  | grep ^Package
+ UserParameter=size[*],du -sh $1
+ UserParameter=subsize[*],du -h $1
+ UserParameter=rm[*],sudo rmdir  $1
+ UserParameter=mk[*],sudo mkdir  $1
+ UserParameter=top[*],top -b -n1| grep $1| awk '{print ($(NF-2)"/"$(NF-3))}'
+ UserParameter=memory,free -t | awk 'NR == 2 {print ($3/$2)*100}'
+ UserParameter=space,df -hT /home | awk 'NR == 2 {print ($4/($4+$5))*100}'
+ UserParameter=cpu,top -b -n1 | awk 'NR == 3 {print ($2)}'
### Step 2
In this step we sould create our 8 specific items in all hosts in our zabbix frontend <br/>
![EXEMPLE](/items.png) <br/>
![Configuration of item](/confg.png) <br/>
The configuration of all items is detailed in the table below <br/>
Name of item | Key | Type of information | Update interval
------------ | ------------- | --------- | ----
folder size | size[/] | Text | 1s
mkdir_rmdir | mk[/home/test] | Text | 1s
per cpu | cpu | Text | 1s
per memory | memory | Text | 1s
pkgversion | version[] | Text | 1s
spaceper | space | Text | 1s
top | top[frontend] | Text | 1s
universal | run[fixed.py] | Text | 1s


**NB! : Host names should only contain  digits (0-9), letters(A-Z, a-z), and a few special characters ( "-" , "." , "_" , "~" ) only.**
### Step 3
Run **" project.py "** and visit **" http://127.0.0.1:5000/ "** in a browser
