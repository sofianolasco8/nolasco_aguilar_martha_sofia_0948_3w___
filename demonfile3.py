print(" ")
print("Nolasco_aguilar_martha_sofia_0948_3W")
print(" ")
f = open("demofile3.txt", "w")#se abre el archivo de texto 
f.write("Woops! I have deleted the content!")#se indica el texto 
f.close()#se cierra el archvo

f = open("demofile3.txt", "r")
print(f.read())#se imprime lo que esta dentro de a variable f 

