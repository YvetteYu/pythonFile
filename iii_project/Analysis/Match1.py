import codecs
fid = codecs.open('104_company.txt','r',encoding='utf-8')
complist = fid.readlines()
fid.close()
fid = codecs.open('sal_company.txt','r',encoding='utf-8')
sal_com = fid.readlines()
fid.close()

# step1: compile the source
# step2: cut of the front two or three words from compared company data
# and delivery the value to temp_com2 and tempcom3

import re
## make one fake data in complist[0]
#complist.insert(0,u'鴻海科技')
import time
tic = time.clock()

fid = codecs.open('match_2words.txt','w',encoding='utf-8')
fp = codecs.open('match_3words.txt','w',encoding='utf-8')
for j in range(0,len(complist)):
    for i in range(0,len(sal_com)):
        if len(sal_com[i])>=2:
            temp_com2 = sal_com[i][0:2]
        if len(sal_com[i])>=3:
            temp_com3 = sal_com[i][0:3]
        m2 = re.search(temp_com2,complist[j])
        m3 = re.search(temp_com3,complist[j])
        if m2:
            fid.write(str(j)+','+str(i)+','+m2.group()+'\n')  # m2.group return a string obj
        if m3:
            fp.write(str(j)+','+str(i)+','+m3.group()+'\n')
fid.close()
fp.close()
toc = time.clock()
totalTime = toc-tic
ftime = open('matchTime.txt','w')
ftime.write('match '+str(j)+' companies and ' + str(i) +\
'salary data, costs ' + str(totalTime) + 's')
ftime.close()
