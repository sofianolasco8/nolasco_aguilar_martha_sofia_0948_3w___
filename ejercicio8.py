print(" ")
print("Nolasco_aguilar_martha_sofia_0948_3w")
import os #inica que debe borrar el archivo de texto 
if os.path.exists("demofile.txt"):#indica si el archivo si esxiste 
    os.remove("demofile.txt")
else:
    print("The file does not exist")#indica que si el archivo no existe debe setr borrado 