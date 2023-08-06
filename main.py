import json
import csv

"""
An email is classified as spam if:

A) email.src has more than 1 value 
B) email[0] != all(email.src)
C) every value in email[1:] is not in email.dst
D) len(email.dst) != (len(email)-1)
"""

#Load json file
with open("INPUT.json",'r',encoding="utf8") as f:
    data = json.load(f)


#Structure of the final csv result file
index=[] #based on json file
time=[] #when the email was sent
smtp_from=[]
smtp_to=[]
msg_from=[]
msg_to=[]
subject=[]
attachment=[]
case_a=[]
case_b=[]
case_c=[]
case_d=[]


#main part, here we look for bad emails
for i,email in enumerate(data):
    cases = [False, False, False, False]
    #case A
    if(len(set(email['email.src']))>1):
        cases[0]=True
    #case B
    if(email['email'][0] not in email['email.src']):
        cases[1] = True
    #case C
    for recipient in email['email'][1:]:
        if recipient not in email['email.dst']:
            cases[2] = True
            break;
    #case D
    a=len(email['email.dst'])
    b=len(email['email'][1:])
    if(a != b):
        cases[3] = True

    #In case we have at least a positive case, we collect the email
    if( True in cases):
        smtp_from.append(email['email'][0])
        smtp_to.append(email['email'][1:])
        msg_from.append(list(set(email['email.src'])))
        msg_to.append(email['email.dst'])
        index.append(i)
        time.append(email['time'])
        case_a.append(cases[0])
        case_b.append(cases[1])
        case_c.append(cases[2])
        case_d.append(cases[3])
        subject.append(email.get('subject',None))
        attachment.append(email.get('attachment',None))

#csv file creation
keys = ['index','time','smtp_from','smtp_to',"msg_from","msg_to","subject","attachment",'case_a','case_b','case_c','case_d']
values = [index,time, smtp_from, smtp_to, msg_from, msg_to,subject,attachment,case_a,case_b,case_c,case_d]

name=(f.name).replace('.json',".csv")
with open(name,'w',newline="") as result:
    write= csv.writer(result,delimiter=';')
    write.writerow(keys)
    for i in range(len(index)):
        row=[]
        for element in values:
            row.append(element[i])
        write.writerow(row)

print("Checked "+str(len(data))+" emails, results saved in "+name)



#In case you prefer Pandas, do not forget to import the library --> import pandas as pd
"""
d = {'index': index,'time':time, 'smtp_from': smtp_from, 'smtp_to': smtp_to, "msg_from": msg_from, "msg_to": msg_to,"subject":subject,"attachment":attachment,
     'case_a': case_a,'case_b': case_b,'case_c': case_c,'case_d': case_d}
df = pd.DataFrame(data=d)

name=f.name
name=name.replace('.json',".csv")
df.to_csv(name, sep=";")
"""

