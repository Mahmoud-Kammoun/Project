
def histo (x):
    from pyzabbix import ZabbixAPI
    from datetime import datetime

    import time
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    timetill = int(time.mktime(time.localtime()))
    timefrom = timetill - 30
    history = zapi.history.get(itemids=x,
                               time_from=timefrom,
                               time_till=timetill,
                               output='extend',
                               limit='5000',
                               history=4,
                               )

# If nothing was found, try getting it from history (float) data
    if not len(history):
        history = zapi.history.get(itemids=x,
                                   #filter={'application': 'others'},
                                   time_from=timefrom,
                                   time_till=timetill,
                                   output='extend',
                                   limit='5000',
                                   history=4,
                                   )
    for point in history:
        return(point['value'])
def histoo (x):
    from pyzabbix import ZabbixAPI
    from datetime import datetime
    import time
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    timetill = int(time.mktime(time.localtime()))
    timefrom = timetill - 60
    history = zapi.history.get(itemids=x,
                               time_from=timefrom,
                               time_till=timetill,
                               output='extend',
                               limit='5000',
                               history=0,
                               )

# If nothing was found, try getting it from history (float) data
    if not len(history):
        history = zapi.history.get(itemids=x,
                                   #filter={'application': 'others'},
                                   time_from=timefrom,
                                   time_till=timetill,
                                   output='extend',
                                   limit='5000',
                                   history=0,
                                   )
    for point in history:
        return(point['value'])
#print(str(histo(34792)))
#print(type(histo(34792)))
#print(type(str(histo(34792))))
#print("{0}: {1}".format(datetime.fromtimestamp(int(point['clock']))
 #                               .strftime("%x %X"), point['value']))
#a=histoo(34474)
#print(a)
#print("aa \t aa")
#print(a.find('tesr4'))
#print(type(a))
#print(a.rfind(" "))
#print(a.rfind("."))
#print(a[a.rfind("firefox")-20:a.rfind("firefox")-17])
#print(a[a.rfind("firefox")-14:a.rfind("firefox")-11])
#print(a.find("8"))
#print(orgsize(histo(34791)))
def histooo (x):
    from pyzabbix import ZabbixAPI
    from datetime import datetime
    import time
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    timetill = int(time.mktime(time.localtime()))
    timefrom = timetill - 60
    history = zapi.history.get(itemids=x,
                               time_from=timefrom,
                               time_till=timetill,
                               output='extend',
                               limit='5000',
                               history=3,
                               )

# If nothing was found, try getting it from history (float) data
    if not len(history):
        history = zapi.history.get(itemids=x,
                                   #filter={'application': 'others'},
                                   time_from=timefrom,
                                   time_till=timetill,
                                   output='extend',
                                   limit='5000',
                                   history=3,
                                   )
    for point in history:
        return(point['value'])
