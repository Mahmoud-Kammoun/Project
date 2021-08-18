# Project
This project is an aplication web that changes data with Zabbix software through Zabbix's API in order to add other specific commands to the server monitoring which makes access control management easier and more practical to improve efficiency and rapidity.<br/>
To runing perfectly the project you need to follow the steps below
# Step 1
In zabbix_agentd.conf file we locate the **"UserParameters"** attributes and we set them to create our specific command bellow. <br/>
+ UserParameter=run[*],python3 /home/mahmoud/PycharmProjects/final/$1  <br/>
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
# Step 2
In this step we sould create our specific items in all hosts in our zabbix frontend 
A 
![Ltee](/prima.png)
