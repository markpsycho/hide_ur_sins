import base64
import sys
import random
# print ("enter: filename d|en corruptionword[greater than 3] outputfile ")
# www=sys.stdin.readline()
# args=www.split()

try:
    arg=sys.argv[2]#args[1]        #input("encode/decode:")
    filename =sys.argv[1]#args[0]  #input("input file:")
    filename2 =sys.argv[4]#args[3] #input("output file")
    dummyname =sys.argv[3]#args[2] #input("enter dummy name")
    if (( arg !='d') & (arg != 'en')) :
        print ("ERROR:\nenter: filename d|en corruptionword[greater than 3] outputfil ")
        sys.exit()
except Exception as e:
        print ('ERROR: requires 4 arguements: ')
        print ("enter: filename d|en corruptionword[greater than 3] outputfile ")
        sys.exit()

try:
        fileobject=open(filename,"rb")
        fileobject1=open(filename2,"wb")
except Exception as e:
        print ('Did I jump directly to here?' + str(e))
        sys.exit()

data=fileobject.read()
try:
    if(arg=='en'):
       encoded_data1=base64.b64encode(data)
       x=random.randint(20,100)
       if (x<len(encoded_data)/2):
           encoded_data = encoded_data1[:x]+bytes(dummyname, 'utf-8')+encoded_data1[x:]
       else:
           encoded_data = encoded_data1[:10]+bytes(dummyname, 'utf-8')+encoded_data1[10:]
       x=random.randint(len(encoded_data)/2,len(encoded_data))
       random_encoded=encoded_data[:x]+bytes(dummyname, 'utf-8')+encoded_data[x:]
    elif(arg=='d'):
       data1=data.replace(bytes(dummyname, 'utf-8'),bytes('', 'utf-8'))
       encoded_data = base64.b64decode(data1)
       random_encoded=encoded_data
except Exception as e:
        print ('ERROR: wrong password :p')
        sys.exit()

fileobject1.write(random_encoded)
fileobject1.close()
fileobject.close()
