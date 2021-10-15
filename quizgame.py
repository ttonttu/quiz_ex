#This is the amazing quiz game made by Elina and Miia (and Tiina)

oikein = 0
kysymys1 = "Mikä on maailman pienin valtio?"
kysymys2 = "Mikä on maailman pisin joki?"
kysymys3 = "Kuinka monta raitaa Yhdysvaltain lipussa on?"
kysymykset = [kysymys1,kysymys2,kysymys3]
vastaukset = ["Vatikaani", "Niili", "13"]
kysymys = 3
j = 0

start = input("Haluatko käynnistää pelin? Y/N: ")
if start == "Y":
    while True:
        for i in kysymykset:
            kysymykset[j]            
            vastaus = input("Mikä on maailman pienin valtio? ")
            if vastaus == vastaukset[j]:
                oikein +=1
                j+=1
            else:
                pass



        
        
        print(oikein)
        break

elif start == "N":
    pass   
    