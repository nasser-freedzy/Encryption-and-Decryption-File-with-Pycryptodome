import hashlib   # Import du module hashlib pour générer le hachage du mot de passe 
import timeit   # Import du module time pour mesurer le temps d'exécution 
import sys   # Import du module sys pour accéder aux arguments de ligne de commande 
from Crypto.Cipher import AES   # Import du chiffrement AES depuis la bibliothèque pycryptodome 
from Crypto.Util import Padding   # Import du module hashlib pour générer le hachage du mot de passe 


# Fonction pour chiffrer un fichier 
def encryptFile(password, IV, filename):     
    key = hashlib.sha256(password.encode()).digest() # Générer la clé de chiffrement à partir du mot de passe          
    with open(filename, 'rb') as f :  # Ouvrir le fichier en mode lecture binaire         
        file_data =f.read()  # Lire le contenu du fichier     
    starttime = timeit.default_timer()  # Enregistrer le temps de début de l'opération de chiffrement 
 
    cipher = AES.new(key, AES.MODE_CBC, IV)  # Initialiser le chiffrement AES avec la clé et l'IV     
    padded_file_data = Padding.pad(file_data,16)  # Rembourrer les données pour qu'elles soient multiples de 16 octets     
    encrypte_file_data = cipher.encrypt(padded_file_data)  # Chiffrer les données     
    time =  timeit.default_timer() -starttime  # Enregistrer le temps de fin de l'opération de chiffrement 
 
    with open(filename,'wb') as ef :  # Ouvrir le fichier de sortie en mode écriture binaire         
        ef.write(encrypte_file_data)  # Écrire les données chiffrées dans le fichier de sortie     
        print("File encrypted successfully.")  # Afficher un message indiquant que le fichier a été chiffré avec succès    
    return 'Done in ' + str(time)  + 'second(s)' 

def decrytFile(password, IV , filename):     
    key = hashlib.sha256(password.encode()).digest() # Générer la clé de chiffrement à partir du mot de passe 
 
    with open(filename, 'rb') as f :         
        file_data =f.read() 
 
    starttime = timeit.default_timer()     
    cipher = AES.new(key, AES.MODE_CBC, IV)     
    padded_file_data = Padding.pad(file_data,16)     
    decrypte_file_data = cipher.decrypt(file_data)     
    unpadded_file_date = Padding.unpad(decrypte_file_data, 16)  # Supprimer le rembourrage des données déchiffrées

    time =  timeit.default_timer() -starttime 
 
    with open(filename,'wb') as ef :         
        ef.write(unpadded_file_date)     
        print("File decrypted successfully.")  # Afficher un message indiquant que le fichier a été déchiffré avec succès     
    return 'Done in ' + str(time)  + ' second(s)'  

    # Vérifier les arguments de ligne de commande 
if len(sys.argv) != 4:  # Vérifier si le nombre d'arguments est correct 
    print("Usage: python script.py <mode> <password> <filename> ")     
    sys.exit(1)  # Quitter le programme avec un code d'erreur 
if sys.argv[1] == "-e" :     
    print(encryptFile(sys.argv[2], '1234567890ASDFGH'.encode(), sys.argv[3])) 
elif sys.argv[1] == '-d' :     
    print(decrytFile(sys.argv[2], '1234567890ASDFGH'.encode(), sys.argv[3])) 
else :     
    
    print("l'algorithme n'est pas correct esseyer a nouveau")