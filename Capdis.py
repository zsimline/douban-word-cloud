import requests,base64
 
def capdis(url_image):
	url_api="http://route.showapi.com/184-5"
	send_data=[
				('showapi_appid','50251'),
				('showapi_sign','6e74e1c4cdc5488ca49bc292d68b0135'),
				('typeId', "20"),
			   ]		
	print('发现验证码，正在尝试调用API识别验证码....................')
	image=requests.get(url_image).content
	image_base64=base64.b64encode(image)
	send_data.append(('img_base64',image_base64))
	response = requests.post(url_api,data=send_data)
	result=eval(response.text)
	cap=result['showapi_res_body']['Result']
	print ('验证码识别成功，验证码是:   ',cap)
	print ('...继续.....................')
	return cap

