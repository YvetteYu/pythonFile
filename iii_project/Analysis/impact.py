with open('match2/TotalMatchTime.txt','r') as fin:
    data = fin.readline().strip().split(' ')
num_com = int(data[1])
print num_com
del data

with open('match2/match_bool.txt','r') as fin:
    mbool = fin.readlines()
i = 1
impact_threshold = 0.5
data = []
for line in mbool:
    points = 0
    bools = line.split(' ')
    bools.remove('\n')
    for ele in bools:
        points = points + float(ele)
    if points/len(bools) >= impact_threshold:
        if i%num_com==0:
            data.append(((i//num_com)-1,(i%num_com)-1)) 
        else:
            data.append(((i//num_com),(i%num_com)-1))      # (sal,com)
    i = i + 1
del mbool
with open('104_company.txt','r') as fcom:
    comlist = fcom.readlines()
with open('salary.txt','r') as fsal:
    sal = fsal.readlines()
with open('match2/match.txt','w')as fmat:    
    for line in data:
        fmat.write(comlist[line[1]].replace('\n','') + ' ' + sal[line[0]])
