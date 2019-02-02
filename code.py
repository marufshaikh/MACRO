#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:11:42 2019

@author: marufshaikh
"""

f=open("macin.txt")
st=f.read()
f.close()
l=st.split('\n')
print(l)
lt=len(l)
mn=[]
mac={}
r=open("mdt.txt","w")
x=open("mnt.txt","w")
#print(lt)
for i in range(0,lt):
    if l[i]=="MACRO":
        #r.write(l[i]+"\n")
        dict={l[i+1]:[]}
        x.write(l[i+1]+"\n")
        r.write(l[i+1]+"\n")
        mac.update(dict)
        mn.append(l[i+1])
        for j in range(i+2,lt):
           if l[j]=="MEND":
               r.write(l[j]+"\n")
               break
           else:
               r.write(l[j]+"\n")
               mac[l[i+1]].append(l[j])
print(mn,mac)
r.close()
x.close()
f=open("macout.txt","w+")
sta=[]
for i in range(0,len(l)):
    if l[i]=="MACRO":
        sta.append(l[i])
    if l[i]=="MEND":
        sta.pop()
    if l[i] in mn and len(sta)==0:
        for j in mac[l[i]]:
            f.write(j+"\n")
    if (l[i] not in mn or len(sta)>=1) or l[i]=="MEND":
        f.write(l[i]+"\n")        
f.close()
