# # Match company name by input cutting_company.txt
import codecs
fid = codecs.open('104_company.txt','r',encoding='utf-8')
comlist = fid.readlines()
fid.close()
fid = codecs.open('match2/cutting_company.txt','r',encoding='utf-8')
cut_sal = fid.readlines() # 不會輸出換行符號
fid.close()

import re
import time
tic = time.clock()

## make one fake data in complist[0]
#comlist.insert(0,u'鴻海科技')

match_bool=[]
for i in range(0,len(cut_sal)):
    for j in range(0,len(comlist)):
        words = cut_sal[i].strip().split(' ')
        temp_bool=[]
        for ele in words:
            try:
                m = re.search(ele,comlist[j])
                if m:
                    temp_bool.append(1)
                else:
                    temp_bool.append(0)
            except:
                temp_bool.append(0)
                continue
        match_bool.append(temp_bool)

toc = time.clock()
totalTime = toc-tic

fbool = codecs.open('match2/match_bool.txt','w',encoding='utf-8')
for k in range(0,len(match_bool)):
    temp_bool = match_bool[k]
    for elebool in temp_bool:
        fbool.write(str(elebool) + ' ')
    fbool.write('\n')
fbool.close()
ftime = open('match2/TotalMatchTime.txt','w')
ftime.write('match '+str(j+1)+' companies and ' + str(i+1) +' salary data, costs ' + str(totalTime) + 's')
ftime.close()
