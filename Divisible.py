print(" Enter a number (Numerator): ")
numn = int(input())
print ("Enter a number (Denominator) : ")
numd = int(input())

if numn%numd==0:
    print("\n" +str (numn) + " is divisble by " + str (numd))
else:
    print(" \ n " + str(numn)+ " is not divisible by " +str (numd))
