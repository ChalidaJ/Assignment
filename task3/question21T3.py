x="12abcbacbaba344ab"
y=filter(lambda x: x.isalpha(), "12abcbacbaba344ab")

freq_cal ={}

for i in y:
    if i in freq_cal:
        freq_cal[i]+=1 
        
    else:
        freq_cal[i]=1
print(freq_cal)

