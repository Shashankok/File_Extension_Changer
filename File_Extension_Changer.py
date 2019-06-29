old=input("Enter the file path you want to change the extension of")
ex=input("enter the extension of new file you want")
ne=old.rsplit('.',1)[0]

fin=ne+"."+ex


try:
    f=open(old, "r")
    c=(f.read())
    f.close()
except:
    print("no file of this name exists")
f1=open(fin, "w")
f1.write(c)
f1.close()
print("File with new extension is created at", fin)