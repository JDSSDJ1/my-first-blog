# I'm obsessed with Pokemon apparently
Greeting ='Hello'
Me = {'Name' : 'Turtwig', 'Type' : 'Grass'}
Friend = {'Name' : 'Torterra', 'Type' : 'Grass'}
Enemy = {'Name' : 'Chimchar', 'Type' : 'Fire'}
MissingNo = {'Name' : 'NA', 'Type' : 'NA'}

Pokedex = [Me,Friend,Enemy,MissingNo]

def theEnd():
    print("End")

def theCheck(Me, Pokemon):
    return Me['Type'] == Pokemon['Type']

for Pokemon in Pokedex:
    if theCheck(Me, Pokemon):
        print(Greeting + ' ' + Pokemon['Name'])
    else:
        theCheck(Me,Friend)
        print("DANGER!!!! Not " + Me['Type'])

for i in range(1,6):
    print(i)


theEnd()