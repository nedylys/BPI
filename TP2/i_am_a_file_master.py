file=open("toto.txt",'w')
file.write("Bonjour\n")
print('Au revoir', file="toto.txt")
file.close()