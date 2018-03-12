import vk
import datetime
import time
import math
import matplotlib.pyplot as mp
session = vk.Session(access_token='65d81fc05f369727561d6cc6be632238e2181852b0b1f5b60e799716aef47284638a2b080084d3ec7036a')
vkapi = vk.API(session, v='5.73')

ages={'Undefined age':0}
sex={0:0, 1:0, 2:0}

users=vkapi.groups.getMembers(group_id='warcraft_universes', fields='sex,bdate', offset=0)
count=int(math.floor(users['count']/1000))
users=users['items']

for i in range(1, count+1, 1):
    time.sleep(1)
    vusers=vkapi.groups.getMembers(group_id='warcraft_universes', fields='sex,bdate', offset=i*1000)
    users.extend(vusers['items'])
for i in range(0, len(users), 1):
    sex[users[i]['sex']]=sex[users[i]['sex']]+1
    try:
        date = datetime.datetime.strptime(users[i]['bdate'], '%d.%m.%Y')
    except:
        ages['Undefined age']=ages['Undefined age']+1
        continue
    now=datetime.datetime.today()
    age=now.year - date.year - ((now.month, date.day) < (now.month, date.day))
    try:
        ages[age]=ages[age]+1
    except:
        ages.update({age:1})
fig=mp.figure()
mp.pie(ages.values(), autopct='%1.1f%%',labels=ages.keys())
mp.text(-1.2, -1.2, 'Male: '+str(sex[2])+'\nFemale: '+str(sex[1])+'\nUndefined sex: '+str(sex[0]))
mp.show()