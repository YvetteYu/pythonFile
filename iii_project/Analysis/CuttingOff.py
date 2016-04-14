# ## Cutting of the compared companies
import codecs
fid = codecs.open('sal_company.txt','r',encoding='utf-8')
sal_com=fid.readlines()
fid.close()

import jieba
cut_com=[]
for i in range(0,len(sal_com)):
    k=0                           # initialized k
    temp_com = []
    words = jieba.cut(sal_com[i], cut_all=False)
    for ele in words:
        if k==0:                 # 讓每個斷詞中間有空格隔開, 但第一個斷詞前面不會有空格
            temp_com.append(ele)
        else:
            temp_com.append(' '+ele)
        k=k+1
    cut_com.append(temp_com)

fid = codecs.open('match2/cutting_company.txt','w',encoding='utf-8')
for lines in cut_com:
    for ele in lines:
        fid.write(ele)
fid.close()    

