f=open("sample.txt","r")
f1=open("sam.txt","a")
for line in f.readlines():
    f1.write(line)
f1.close()
