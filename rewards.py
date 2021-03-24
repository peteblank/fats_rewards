import requests
import json


response2 = json.loads(requests.get("https://api.secretapi.io/staking/validators/secretvaloper1msnh9grlsyxgucld8qg6z2d4wrtueqy35k7g3f").text)
value2=response2['result']['tokens']
value3=int(value2)
print (value3/1000000)

response = json.loads(requests.get("https://api.secretapi.io/staking/validators/secretvaloper1msnh9grlsyxgucld8qg6z2d4wrtueqy35k7g3f/delegations").text)
value=response['result']
x=0
y=0
z=0
for i in range(len(value)-1):
	x+=1
	amount=response['result'][x]['balance']['amount']
	wallet=response['result'][x]['delegator_address']
	amount2=int(amount)/1000000
	amount3=(amount2/(value3/1000000))*1000
	#you have to multiply the value times a thousand for it to work in secretcli
	if amount3<4:
		amount3=4
	if amount2>=80:
		print("secretcli tx snip20 send secret1xzlgeyuuyqje79ma6vllregprkmgwgavk8y798  			"+wallet+" ", end='')
		print(amount3, end='')
		print(" --from 'pete' --memo string staking")
		print(" ")
		z+=amount3
	else:
		print("null")
		print(" ")
		y+=1
print(y)#amount of nulls
print(int(z)/1000)#amount of fats 

