import  random
print("                      -:CRC ERROR DETECTION SIMULATOR:-\n")
def xor(x, y):
	xored = []
	for i in range(1, len(y)):
		if x[i] == y[i]:
			xored.append('0')
		else:
			xored.append('1')

	return ''.join(xored)
def div(d1, d2):
	l = len(d2)
	arr = d1[0 :l]
	while l < len(d1):
		if arr[0] == '1':
			arr = xor(d2, arr) + d1[l]
		else:
			arr = xor('0'*l, arr) + d1[l]
		l += 1
	if arr[0] == '1':
		arr = xor(d2, arr)
	else:
		arr = xor('0'*l, arr)
	code_word = arr
	return code_word

bs=""
for i in range(32):
    temp= str(random.randint(0,1))
    bs+= temp
print("Data stream: ",bs)
while len(bs)%16!=0:
    bs="0"+bs
print("Tokenized Data stream           :",bs)
#CRC-8 = x8 + x2 + x + 1
crc="100000111"
print("CRC-8             :",crc)
bs1=""
appended=""
for i in range(int(len(bs)/16)):
    bs1=bs[i*16:(i+1)*16]
    appended=appended+bs1+"00000000"
final=""
new=""
for i in range(int(len(appended)/24)):
    appended_data=appended[i*24:(i+1)*24]
    remainder=div(appended_data,crc)
    new= bs[i*16:(i+1)*16]
    final=final+new+remainder
codeword=list()
for i in range(len(final)):
    codeword.append(int(final[i]))
print("\nFinal Codeword Generated at Sender Side : ",codeword)
hop=int(input("Enter number of hops : "))
if hop==1:
    p=float(input("Enter user probability : "))
if hop==2:
    p = float(input("Enter 1st user probability : "))
    q = float(input("Enter 2nd user probability : "))
    p1=p*(1-q)+q*(1-p)
final2=[]
final_2=""
for i in range(int(len(final)/24)):
    final1=final[24*i:(i+1)*24]
    if hop==1:
        values=range(11)
        for i in range(len(final1)):
           final2.append(int(final1[i]))
        print("\nOriginal data stream :", final2)
        for i in range(len(final2)):
            p_rand = random.choice(values) / 10
            if p_rand<p:
                if final2[i]==1:
                    final2[i]=0
                else:
                    final2[i]=1
        print("\nData stream with error  :",final2)
    if hop==2:
        values = range(11)
        for i in range(len(final1)):
            final2.append(int(final1[i]))
        print("\nOriginal Word ", i + 1, " : ", final2)
        for i in range(len(final2)):
            p_rand = random.choice(values) / 10
            if p_rand<p1:
                if final2[i] == 1:
                    final2[i] = 0
                else:
                    final2[i] = 1
        print("\nData stream with error  :", final2)
    for i in range(len(final2)):
        if final2[i]==1:
            final_2=final_2+'1'
        else:
            final_2=final_2+'0'
    final2=[]
print("\nData after passing through Binary Symmetric Channel :",final_2)
print("\n                   -:error detection:-  ")
print("___________________________________________________________")
for i in range(int(len(final_2)/24)):
    e_final=final_2[i*24:(i+1)*24]
    remainder=div(e_final,crc)
    if remainder=="00000000":
        print("\nword ",i+1," accepted")
    else:
        print("\nword ", i + 1, " discarded")
