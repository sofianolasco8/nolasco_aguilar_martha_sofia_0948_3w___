print(" ")
print("Nolasco_Aguilar_martha_sofia_0948_3w")
f = open("demofile3.txt", "w")#se abre el archivo de texto con write
f.write("Woops! I have deleted the content!")#indica el mensaje que se va a mostrar 
f.close()#se cierra el archivo de texto 

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")#se abre el archivo de texto demonfile3.txt
print(f.read())#se imprime el archivo de texto demonfile3.txt
