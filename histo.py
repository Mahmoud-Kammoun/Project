from pyzabbix import ZabbixAPI
from datetime import datetime

import time
def list_host ():
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    timetill = int(time.mktime(time.localtime()))
    timefrom = timetill - 30
    history = zapi.host.get(#itemids=x,
                            #itemids="folder size",
                            #templateids=
                            monitored_hosts=[],
                            with_monitored_items=True,
                            time_from=timefrom,
                            time_till=timetill,
                            output='extend',
                            limit='5000',
                            #history=4,
                            )

# If nothing was found, try getting it from history (float) data
    if not len(history):
        history = zapi.host.get(#itemids=x,
                                #filter={'application': 'others'},
                                #itemids="folder size",
                                time_from=timefrom,
                                monitored_hosts=[],
                                with_monitored_items=True,
                                time_till=timetill,
                                output='extend',
                                limit='5000',
                                #history=4,
                                )
    z= {}
    i=1
    for point in history:
        z[str(i)]=point["host"]
        i=i+1
    return (z)
        #print (point["hostid"])
    #print (type(point["host"]))
    #print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
     #                           .strftime("%x %X"), point))
#print(zok())
#print(list_host())
#x=list_host().keys()
#print(x)
#print(type(x))
#p=1
#imp=1
#a={}
#b={}
#for k in list_host():
#    if (int(k)+1) % 2 == 0:
#        a[str(p)]=list_host()[str(k)]
 #       p=p+1
  #  else:
   #     b[str(imp)]=list_host()[str(k)]
#        imp=imp+1
#print(a)
#print(b)

