def pgcd_1(val1,val2):
    while val1!=val2:
      if val1<val2:
        val2=val2-val1
      else:
        val1=val1-val2
    return val1
def pgcd():
   val1=int(input("Entrer un entier strictement positif:"))
   val2=int(input("Entrer un entier strictement positif:"))
   if val1<=0 or val2<=0:
      raise ValueError("L'entier doit etre strictement positif")
   return pgcd_1(val1,val2)
print(pgcd())