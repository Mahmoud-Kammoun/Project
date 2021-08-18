from historyy import histo
def nameid (z,x):
    from pyzabbix import ZabbixAPI
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    history = zapi.item.get(output="itemid",
                            hostid=str(x),
                            search={"name":z},
                            )
    x=int(history[0].get("itemid"))
    #print(x)

    return x
def nameid_host (z):
    from pyzabbix import ZabbixAPI
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    history = zapi.host.get(output="hostid",

                            search={"name":z},
                            )
    x=int(history[0].get("hostid"))
    #print(x)
    return x
#print(nameid("folder size",nameid_host("mahmoud-Lenovo-G50-70")))

#print(nameid("Memory utilization",nameid_host("Zabbix server")))
def nameidd (z,x):
    from pyzabbix import ZabbixAPI
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    history = zapi.item.get(output="itemid",
                            host=str(x),
                            search={"name":z},
                            )
    x=int(history[0].get("itemid"))
    #print(x)

    return x
