str1="dhoni"
str2=input()
c=0 
status=0
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if(str2[j] in str1):
            if(str1[i]==str2[j]):
                str1[i].replace(str1[i],'*')
                c+=1
        else:
            status=1
        
if(len(str1)==c and status==0):
    print('yes')
else:
    print('no')
