import requests
import xmltodict

auth_details = ('casper.plate@student.hu.nl', '2UCgadvq5-c_C_6K3bLaJTFuEqEjfLPvfmzwrmYNIymJ8QQbXsygKQ')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=ede-wageningen'

response = requests.get(api_url, auth=auth_details)
vertrekXML = xmltodict.parse(response.text)
print('Dit zijn de vertrekkende treinen:')

for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']
    vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]  # 18:36
    print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)