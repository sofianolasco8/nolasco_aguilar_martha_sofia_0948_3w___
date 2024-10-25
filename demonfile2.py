print(" ")
print("Nolasco_Aguilae_Martha_sofia_0948_3W")
print(" ")
f = open("demofile2.txt", "a") #abro mi archivo de texto
f.write("Now the file has more content!")#indico el texto que va a crrer 
f.close()#se cierra el archvo

f = open("demofile2.txt", "r")
print(f.read())