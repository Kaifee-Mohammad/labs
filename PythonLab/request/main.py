import requests

response = requests.get(
    'https://dev.tescolabs.com/product/',
        params={'tpnc': '255245446'},
    headers={'Ocp-Apim-Subscription-Key': 'f772cb0b7a29449da9140e2cb20bffea'} )

if response:
    print('success')
    print(response.text)
else:
    print('failed')

