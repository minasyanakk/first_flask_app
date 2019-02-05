import requests
def send_telegram(Q): 
	url ="https://api.telegram.org/bot759906627:AAGSAUX41YM0bCJwosVo1CihPxR9OskX_U8/sendMessage?chat_id=344475020&text="+str(Q)
	res = requests.get(url)



 