import base64,os

counter = 0

inputrrr =  input("File name:\n\n")

with open(inputrrr, 'r') as f:
    file = f.read()

def tuamadremorta(file):
    file=str(file)
     
    if file[0] == 'i' or 'b"import base64;exec' in file:
            
        pos = file.find("'")
        pos+=1
        file = file[pos:]
        
        pos = file.find("'")
        file = file[:pos]
        
        return file
        
    return file
    
file = tuamadremorta(file)

decrypted = file

b=1

def afammoo(f):
    f = base64.b16decode(f)
    f = base64.b32decode(f)
    f = base64.b64decode(f)
    return f

while b==1:  
    try:
        decrypted = afammoo(decrypted)
        decrypted = tuamadremorta(decrypted)
        if file[0] == 'i' or 'b"import base64;exec' in file:
            decrypted = decrypted.encode('UTF-8')
        counter+=1
    except:
        print('\n')
        print('Total recursions: ',counter)
        decrypted = decrypted[2:]
        decrypted = decrypted[:-1001]
        b=2


inputrrr = inputrrr[:-3]

decrypted = decrypted.replace('\\n', '\n')



with open(inputrrr+'_decrypted.py', 'w') as f:
    f.write(decrypted)

if os.name=='nt':
    os.system('pause')
    
# afammoc alessio