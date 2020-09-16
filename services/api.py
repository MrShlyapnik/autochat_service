import requests

def api():
    headers = {
        'X-Private-Api-Token': '0505dcbab77f0071ce254a246f2b8b89c07ce0ae0cd919ece7bbea373c37c7301a4ecc3a0e2f39e5fb60e2d7471fb1e692369ca9e29978191b67f20b1260c9c2',
    }
    response = requests.post('https://api.pact.im/p1/companies/'+pact_id+'/conversations', headers=headers, data=data).json()
    id=(response)
    id=int(id['data']['conversation']['external_id'])
    response=requests.get("https://api.pact.im/p1/companies/"+pact_id+"/conversations/"+str(id)+"/messages?sort_direction=desc", headers=headers).json()