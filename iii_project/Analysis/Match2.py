# # Match data by jieba
import codecs
fid = codecs.open('104_company.txt','r',encoding='utf-8')
comlist = fid.readlines()
fid.close()
fid = codecs.open('sal_company.txt','r',encoding='utf-8')
sal_com = fid.readlines()
fid.close()

# step1: compile the source
# step2: cut of the front two or three words from compared company data
# and delivery the value to temp_com2 and tempcom3

import re
## make one fake data in complist[0]
#comlist.insert(0,u'鴻海科技')

import time
tic = time.clock()
import jieba
match_bool=[]
cut_com=[]
#for j in range(0,2):#len(comlist)):
#    for i in range(0,len(sal_com)):
#        temp_com = []
#        temp_bool=[]
#        words = jieba.cut(sal_com[i], cut_all=False)
#        for ele in words:
#            temp_com.append(ele)
#            try:
#                m = re.search(ele,comlist[j])
#                if m:
#                    temp_bool.append(1)
#                else:3
#                    temp_bool.append(0)
#            except:
#                temp_bool.append(0)
#                continue
#        cut_com.append(temp_com)
#        match_bool.append(temp_bool)

for i in range(0,len(sal_com)):
    for j in range(0,len(comlist)):
        words = jieba.cut(sal_com[i], cut_all=False) # 不明原因words在經過一次取值後，內容就會消失
        temp_com = []
        temp_bool=[]
        for ele in words:
            if j==0:
                temp_com.append(ele)
            try:
                m = re.search(ele,comlist[j])
                if m:
                    temp_bool.append(1)
                else:
                    temp_bool.append(0)
            except:                  # 一些無法比對的字元造成error(ex:symbol)，會丟入
                temp_bool.append(0)  # exception, 對比直接給0(可能會有問題)   
                continue
        cut_com.append(temp_com)
        match_bool.append(temp_bool)

toc = time.clock()
totalTime = toc-tic
# output the result in files
fcom =  codecs.open('match2/cut_company.txt','w',encoding='utf-8')
fbool = codecs.open('match2/match_bool.txt','w',encoding='utf-8')
for k in range(0,len(cut_com)):
    temp_com = cut_com[k]
    temp_bool = match_bool[k]
    for ele in temp_com:
        fcom.write(ele + ' ')
    for elebool in temp_bool:
        fbool.write(str(elebool) + ' ')
    fbool.write('\n')
fcom.close()
fbool.close()
ftime = open('match2/TotalMatchTime.txt','w')
ftime.write('match '+str(j+1)+' companies and ' + str(i+1) +' salary data, costs ' + str(totalTime) + 's')
ftime.close()
