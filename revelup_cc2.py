# coding challange 2
# bojan karas 15.10.2018.


import requests
import json

## 1.Using the below API key/secret, please authenticate with this client

## 2.Retrieve the web order menu for Establishment -2 using

headers = {  'API-AUTHENTICATION': '6c39370b27d0414ea095b47005b09309:4a1fb827c4954c8bb2b56d74cb085f8dfe4ea12a6cf24297824c68f3d0d843bc',    'Content-Type': 'application/json' }
url = 'https://api-playground.revelup.com/weborders/menu/?establishment=2'
r = requests.get(url, headers=headers)
data=json.loads(r.text)
print('')
print('task 2:')
print data['data']

## 3. Sort and Find the Product Category name: Dinner with id : 72.

d1=[]
for z in data['data']['categories']:
	if z['parent_name']=='Dinner':
		d1.extend([[z['parent_name'], z['sort']]])
print('')
print('task 3:')
print  sorted(d1, key=lambda dt: dt[1])


## 4. Sort and Find the Product name: Red Sparkling with id : 274.
print('')
print('task 4:')

for z in data['data']['categories']:
	for x in z['products']:
		if x['name']=='Red Sparkling':
			print x['name'], x['id']

## 5.


url = 'https://api-playground.revelup.com/specialresources/cart/calculate/'
headers = {  'API-AUTHENTICATION': '6c39370b27d0414ea095b47005b09309:4a1fb827c4954c8bb2b56d74cb085f8dfe4ea12a6cf24297824c68f3d0d843bc',    'Content-Type': 'application/json' }
data = '{"establishmentId":2,"items":[{"modifieritems":[],"special_request": "","price": 16,"product": 274,"product_name_override":"Red Sparkling","quantity": 1}],"orderInfo": {"dining_option": 0}}'

r=requests.post(url, data=data, headers=headers)
print r, r.text

d1=json.loads(r.text)

print()
print('task 5:')
print d1['data']['final_total']






