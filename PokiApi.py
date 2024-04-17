import os
import json
import requests
import random

def Arrangeinfo(response):
    Abilitiesstr=''
    FormStr=''
    for ability in response.json()['abilities']:
        ability=str(ability).split('{')[2].split()[1]
        Abilitiesstr+=ability[1:len(ability)-2]
        Abilitiesstr+=' '
    for form in response.json()['forms']:
        form=str(form).split('{')[1].split()[1]
        FormStr+=form[1:len(form)-2]
        FormStr+=' '
    json_data =   { "Name": response.json()['name'] , \
        "Abilities": Abilitiesstr.split() , \
        "Forms": FormStr.split() , \
        "Weight": response.json()["weight"] } 
    return (json_data)


def printdetails(details):
    print ("\nPokemon's details:")
    print ("Name:", details['Name'])
    print ("Abilities:", ', '.join(details['Abilities']))
    print ("Forms:", ' '.join(details['Forms']))
    print ("Weight:", details['Weight'])



def randompokemon(file,contents):
    #----------randompokemon
    rdpokemon= random.randint(1,1026)
    #----------URL+gettinginfo
    url = "https://pokeapi.co/api/v2/pokemon/" + str(rdpokemon)
    response = requests.get(url,headers={'Accept': 'application.json'})
    pokemonname=response.json()['name']
    #----------Incase pokemon doesnt exist in DB we download it
    if (pokemonname not in str(contents)):
        contents[pokemonname]=Arrangeinfo(response)
        json.dump(contents,file,indent=4)
    #----------Printing pokemon's details
    return contents[pokemonname]
    




def main():
    #----------Opening the file (database)
    FILENAME="/Users/khaleddahly/Documents/PythonProjects/AWSbootcamp/PokiApi/Pokemonfile.json"
    if os.path.exists(FILENAME) and os.path.getsize(FILENAME) > 0:
    # Read the existing JSON file
        with open(FILENAME, 'r') as json_file:
            try:
                FileContents = json.load(json_file)
            except json.decoder.JSONDecodeError:
                FileContents = {}  # If the file is empty or not valid JSON, initialize data as an empty dictionary
    else:
        FileContents = {}
    with open(FILENAME, mode='w') as pokemonfile:
        details=randompokemon(pokemonfile,FileContents)
        
    printdetails(details)
    print ("\nWhat would you like to do next?")



print("Welcome to PokiApi!\nMain Menu:")
while(1):
    print ("1. Randomly draw a pokemon\n2.Exit")
    option=int(input("Please choose an option: "))
    if option==1:
        main()
    elif option==2:
        print ("GoodBye!")
        exit ()
    else:
        print ("You choose invalid option!\n")
