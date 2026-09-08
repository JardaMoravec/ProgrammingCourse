"""Čtení XML — ElementTree."""

import xml.etree.ElementTree as ET

koren = ET.parse("zaci.xml").getroot()
for zak in koren.findall("zak"):
    print(zak.find("jmeno").text, zak.find("vek").text)
