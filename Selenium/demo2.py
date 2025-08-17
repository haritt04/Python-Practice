import requests

url = 'https://google.com/'
apikey = '4daf1e58fa2a65d060bcb4b46d93b9102e88f34c'
params = {
    'url': url,
    'apikey': apikey,
	'js_render': 'true',
	'premium_proxy': 'true',
}
response = requests.get('https://api.zenrows.com/v1/', params=params)
print(response.text)