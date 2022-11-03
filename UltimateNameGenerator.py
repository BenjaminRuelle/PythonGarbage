from ast import While
import random
from time import sleep

#Base de donnée de génération
Nom1 = ("Average","Super","Ultimate","Underrated","Anxious","Excited","Virgin","Determined","Professional","Sneaky","Young","Epic","Underaged","Furious","Overated","Naughty","Angry","Hungry","Dark","Newbie","Lil","Thiccc","Disgusting","Friendly","Tights") 
Nom2 = ("apple pie","balls","nut","socks","python","church","titties","butt","virgin","ass","boobies","pussy","zboob","feet","dick","zgeg","anal","doll","cock ring","BBW","Dva","hentai","step mom","18cm")
Nom3 = ("slayer","eater","ripper","fucker","smasher","blaster","destroyer","lover","enjoyer","killer","shredder","exterminator","smeller","kiffeur","sucker","tester","evaluator")
Nom = ""
reponse = ("Tu préfère pas plutôt ","j'aurais plutôt dit ","T'es sûr de toi ", "T'es sur que c'est pas ","Mouais c'est moins bien que ","On va garder ","Maintenant ce sera ","C'est comme ca que tu écrit ")

def generation_Nom(): #génération d'un nom en assemblant 3 morceaux des tables Nom1, Nom2 et Nom3 
 id_Nom1 = random.randint(0,len(Nom1)-1)
 id_Nom2 = random.randint(0,len(Nom2)-1)
 id_Nom3 = random.randint(0,len(Nom3)-1)
 NomGenere = Nom1[id_Nom1] +" "+ Nom2[id_Nom2] +" "+ Nom3[id_Nom3]
 return NomGenere

def verification_Nom(registreVerif):
 NomVerif = generation_Nom()                      #Ici on crée le nom avec la fonction generation
 for i in range(len(registreVerif)):
  if registreVerif[i].split(",")[0] == NomVerif:  #On vérifie si le nom n'est pas dans le registre 
     NomVerif = generation_Nom()
     verification_Nom(registreVerif)            #Si c'est le cas on refait une génération + vérif  
 return NomVerif

while True:
 registre = []
 with open("Registre.txt") as file: #Lecture du registre de pseudo pour eviter d'attribué deux fois le même pseudo
   lines = file.readlines()
 for i in range(len(lines)):
  registre.append(lines[i].rstrip('\n'))
  
 print("--------ULTIMATE NAME GENERATOR V3--------")
 sleep(1)
 User = input("Entre ton nom stp ")
 print("Ah ouais... " + User + " ?")
 sleep(2)

 for i in range(len(registre)):
  if registre[i].split(",")[1] == User:
   print("Ahh mais on se connait " + registre[i].split(",")[0] + " !")
   break
  if i+1 == len(registre):
   Nom = verification_Nom(registre) #Cette fonction permet de verifier si un nom n'est pas déjà dans le registre    
   saved = Nom + "," + User
   file = open("Registre.txt","a")
   file.write(saved+"\n")
   print(reponse[random.randint(0,len(reponse)-1)] + Nom)


