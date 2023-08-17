import random
l=['0','1','2','3','4','5','6','7','8','9']
otp=""
for i in range(4):
    otp=otp+random.choice(l)
print(otp)    
