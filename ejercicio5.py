print(" ")
print("nolasco_aguilar_martha_sofia_0948_3W")
print(" ")
f = open("demofile2.txt", "a")#se abre el archivo de texto demonfile2
f.write("Now the file has more content!")#se muestra el archivo de texto 
f.close()#se cierra el archivo de texto 

f = open("demofile2.txt", "r") #se indica que se va a abrir el archivo de texto 
print(f.read())#muestra el archivo de texto 