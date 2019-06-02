# Eta-Heizung-Domoticz

Python Script um Werte einer ETA-Heizung (http://www.eta.co.at)
als Temperatursensoren in Domoticz anzuzeigen

## Installation des Scripts

das Script in das Homeverzeichnis eines Benutzer platzieren.
e.g
/home/pi

Neben der Ip-Adresse der Heizung müssen
im Skript folgende Werte angepasst werden.
Der Wert "domoticzserver" muss angepasst werden, wenn das Skript nicht auf dem Rechner läuft wo sich die Domoticz Instanz befindet
...
update("user/var/112/10101/0/0/12241", "<Domoticz Virtuelles Device>") #Heizkreis1 Temperatur
...

Um Virtuelle Devices zu erstellen, geht man in Domoticz unter Hardware, wählt als Typ "Dummy aus", fügt die Hardware hinzu und klickt dann beim frisch hinzugefügten Device auf "Virtuellen Sensor erstellen"

Diese virtuellen Sensoren findet man dann unter Einrichtung->Geräte
Die IDX Werte müssen dann im Skript eingetragen werden.


dann mittels sudo crontab -e
``*/1 * * * * /usr/bin/python3 /home/pi/heizung.py >/dev/null 2>&1``
folgende Zeile in Crontab einfügen für eine Ausführung des Skriptes im Minutentakt



## Anpassung des Scripts

Um dieses Script anzupassen ist wie folgt vorzugehen:

Im Browser
http://<heizung.ip>:8080/user/menu
öffnen, den Seitenquelltext anzeigen

Hier sind alle Werte die man braucht in einer XML Datei vorhanden
man sucht sich z.B folgenden Wert
/112/10102/0/0/12241 , das ist z.B die Temperatur für den Vorlauf.
Um diesen zu erhalten, ist folgendes im Browser einzugeben:

http://<heizung.ip>:8080/user/var/112/10102/0/0/12241
Wenn man hier ebenfalls auf Seitenquelltext anzeigen klickt, sieht man 
das es sich wieder um eine XML Datei handelt.
Diese wird im Script geparsed um den gültigen Wert zu erhalten
