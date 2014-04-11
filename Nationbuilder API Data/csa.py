from rauth import OAuth2Service
token = '6ec59d1ea41a8d50352a33137a6f7becc7ddc474ce5e0eb0133076df427c5673'
nation_slug = 'commonssenseaction'
access_token_url = "http://commonssenseaction.nationbuilder.com/oauth/token"
authorize_url = nation_slug + ".nationbuilder.com/oauth/authorize"
service = OAuth2Service(
            client_id = "f5eda5ee072a6eb8618756ec72845216b736a8a2f2c028241f142de6f216a12f",
            client_secret = "8fb35f5b20be0fba3f926ecce13900832ff163e3ed26131a51737e9c2af4573e",
            name = "Leaderboard",
            authorize_url = authorize_url,
            access_token_url = access_token_url,
            base_url = nation_slug + ".nationbuilder.com")
session = service.get_session(token)         

def getallTags():
    firstcall = session.get('https://commonssenseaction.nationbuilder.com/api/v1/tags', 
                      params={'per_page': '100'})
    dictofPages = dict()
    numberofpages = firstcall.json()['total_pages']
    numberofpages = numberofpages + 1
    for i in range(1,numberofpages):
        dictofPages[i] = session.get('https://commonssenseaction.nationbuilder.com/api/v1/tags', 
                      params={'per_page': '100', 'page' : i})
        dictofPages[i] = dictofPages[i].json()['results']
    tags = [1]
    for x in range(1, numberofpages):
        for y in range(0,len(dictofPages[x])):
            tags.append(dictofPages[x][y].values()) 
    del(tags[0])
    for i in range(0,len(tags)):
        tags[i] = tags[i][0]
    return(tags)
test = getallTags()
positions = [i for i, word in enumerate(test) if word.endswith('_endorsers')]
tags = [test[i] for i in positions]

def getEndorserCounts():
    counts = dict()
    for i in tags:
        counts[i] = session.get('https://commonssenseaction.nationbuilder.com/api/v1/tags/' + i + '/people')
        counts[i] = counts[i].json()['total']    
    return counts
counts = getEndorserCounts()
counts = dict([(k[3:-10], v) for k, v in counts.items()])
counts['national'] = counts['ional']
del(counts['ional'])
counts['national']
#need bu and umich b/c don't transfer right
token_Umich = '8e74e0b290ab45c641f71e1079b277b9d08065c86374e2fb4043e6d1c0a30a0a'
nation_slug_Umich = 'csaumich'
access_token_url_Umich = "http://csaumich.nationbuilder.com/oauth/token"
authorize_url_Umich = nation_slug_Umich + ".nationbuilder.com/oauth/authorize"
service_Umich = OAuth2Service(
            client_id = "763f7fe6d103a5aec4ec698b024ec6737db6450bd61db979655b30534b18c41e",
            client_secret = "546aa36128e0019594f6da8bfe5cd2ffc5161c45da68e13cb99fc7e675a0a294",
            name = "Leaderboard",
            authorize_url = authorize_url_Umich,
            access_token_url = access_token_url_Umich,
            base_url = nation_slug_Umich + ".nationbuilder.com")
session_Umich = service.get_session(token)        
umichcount = session_Umich.get('https://csaumich.nationbuilder.com/api/v1/tags/endorsed_age/people')
umichcount = umichcount.json()['total']

counts['umich'] = umichcount


token_bu = 'ca5f72d81f43cc63eb4327c34e0fc3887b6addef3adab752082a2e81f45bf2b0'
nation_slug_bu = 'csabu'
access_token_url_bu = "http://csabu.nationbuilder.com/oauth/token"
authorize_url_bu = nation_slug_bu + ".nationbuilder.com/oauth/authorize"
service_bu = OAuth2Service(
            client_id = "068eb9f9cd45212b679ca5ec481facd3ba250863babcfe5fd01b6c6362ebf3b3",
            client_secret = "b5335bcaf9eea8f8bac3837cbe7a31f92be110e037d90dd33af6dcd2aa30c267",
            name = "Leaderboard",
            authorize_url = authorize_url_bu,
            access_token_url = access_token_url_bu,
            base_url = nation_slug_bu + ".nationbuilder.com")
session_bu= service_bu.get_session(token_bu)        
bucount = session_bu.get('https://csabu.nationbuilder.com/api/v1/tags/endorsed_age/people')
bucount= bucount.json()['total']


counts['bu'] = bucount

sorted(counts)

