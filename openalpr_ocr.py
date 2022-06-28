import requests
import base64
import json

def ocr(IMAGE_PATH):
	SECRET_KEY = 'sk_33cfec6d5157c1bf916df028'
	with open(IMAGE_PATH, 'rb') as image_file:
    		img_base64 = base64.b64encode(image_file.read())

	url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=sa&secret_key=%s' % (SECRET_KEY)  #Replace 'sa' with  your country code
	r = requests.post(url, data = img_base64)
	try:
		return(r.json()['results'][0]['plate'])
		
	except:
		print("No number plate found")
