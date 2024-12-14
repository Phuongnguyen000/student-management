path='QLSV.txt'
def save(line):
    f=open(path,'a',encoding='utf8')
    f.writelines(line)
    f.writelines('\n')
    f.close()

def read():
    sv=[]
    f=open(path,'r',encoding='utf8')
    for i in f:
        data=i.strip()
        arr=data.split('-')
        sv.append(sv)
    f.close()
    return sv