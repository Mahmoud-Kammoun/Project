from pyzabbix import ZabbixAPI
from historyy import histo
from tasti import nameid,nameidd
def subfolder (x,z) :
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')

    zapi.item.update(itemid=nameidd("folder size",z),
                     key_="subsize["+x+"]",)
    return
def folder (x,z) :
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')

    zapi.item.update(itemid=nameidd("folder size",z),
                     key_="size["+x+"]",)
    return
def deel (x,z):
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    zapi.item.update(itemid=nameidd("mkdir_rmdir",z),
                     key_="rm["+x+"]",)
    return
def cre (x,z):
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    zapi.item.update(itemid=nameidd("mkdir_rmdir",z),
                     key_="mk["+x+"]",)
    return
def version (x,z):
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    zapi.item.update(itemid=nameidd("pkgversion",z),
                     key_="version["+x+"]",)
    return
#print(nameidd("pkgversion","mahmoud-Lenovo-G50-70"))
#version("zoom","mahmoud-Lenovo-G50-70")

def top (x,z):
    ZABBIX_SERVER = 'http://127.0.0.1/zabbix/api_jsonrpc.php'
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login('Admin', 'zabbix')
    zapi.item.update(itemid=nameidd("top",z),
                     key_="top["+x+"]",)
    return
