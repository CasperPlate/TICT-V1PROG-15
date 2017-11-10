import xmltodict

def processXML(winkelmandje):
    with open(winkelmandje) as winkelmandje_xml:
        artikel_string = winkelmandje_xml.read()
        artikelen_dict = xmltodict.parse(artikel_string)
        return artikelen_dict

product_dict = processXML('winkelmandje.xml')
producten = product_dict['artikelen']['artikel']

for artikel in producten:
    print(artikel['naam'])