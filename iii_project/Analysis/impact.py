with open('match2/TotalMatchTime.txt','r') as fin:
    data = fin.readline().strip().split(' ')
num_com = int(data[1])
num_sal = int(data[4])
print num_com, num_sal
del data
with open('test2/match_bool.txt','r') as fin:
    mbool = fin.readlines()
i = 1
data = []
for line in mbool:
    points = 0
    bools = line.split(' ')
    bools.remove('\n')
    for ele in bools:
        points = points + float(ele)
    if points/len(bools) > 0.5:
        #if i%num_com==0:
        data.append(((i//num_com)-1,(i%num_com)-1))
        #else:
        #    data.append(((i//num_com),(i%num_com)-1))      # (sal,com)
    i = i + 1
del mbool
with open('104_company.txt','r') as fcom:
    comlist = fcom.readlines()
with open('salary.txt','r') as fsal:
    sal = fsal.readlines()
with open('match2/match.txt','w')as fmat:
    for line in data:
        fmat.write(comlist[line[1]].replace('\n','') + ' ' + sal[line[0]])
