import urllib.request
import base64
from xml.etree import ElementTree

domoticzserver   = "127.0.0.1"
domoticzusername = ""
domoticzpassword = ""
heizungip = "http://192.168.1.209:8080/"		

base64string = base64.encodestring(('%s:%s' % (domoticzusername, domoticzpassword)).encode()).decode().replace('\n', '')

def domoticzrequest (url):
        print(url)
        request = urllib.request.Request(url)
        request.add_header("Authorization", "Basic %s" % base64string)
        response = urllib.request.urlopen(request)
        return response.read()

def update(address, idxtemp):
		request = urllib.request.Request(""+heizungip+address)
		response = urllib.request.urlopen(request)
		root = ElementTree.fromstring(response.read())
		print(root[0].attrib["strValue"])
		temp=root[0].attrib["strValue"]
		domoticzrequest("http://" + domoticzserver + "/json.htm?type=command&param=udevice&idx=" + idxtemp + "&nvalue=0&svalue=" + temp)

update("user/var/112/10101/0/0/12241", "14488") #Heizkreis1 Temperatur
update("user/var/112/10102/0/0/12241", "14489") #Heizkreis2 Temperatur
update("user/var/112/10021/0/0/12241", "14490") #Kessel Temperatur
update("user/var/112/10111/0/0/12271", "14491") #Warmwasser Temperatur
update("user/var/112/10251/0/0/12242", "14550") #Puffer oben Temperatur
update("user/var/112/10251/0/0/12244", "14551") #Puffer unten Temperatur
update("user/var/112/10241/0/0/12197", "14552") #Aussentemperatur



