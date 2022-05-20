# Skistar-kassa
Skistar_kassa
Mitt slutprojekt i programmering 1 är en skistar-kassa. 
.
8:50

Daniel Jonsson
NL_README.md
Text
Klasskommentarer

# Tutorial to a Readme (Titel på ditt projekt)

## Description (Beskrivning)
Programmet är skriven i python och är en kassa i en skidort. Användaren kan hyra skidor, boende och liftkort. Det finns ett x antal i "lagret"/lisat/fil och därför tas den mängden utrustningen som användaren hyr bort från lagret/filen. Användaren har även ett alternativ på om användaren vill hyra eller lämna tillbaka.

***Här bör du kort förklara vilket eller vilka språk programmet är skrivet i samt vad syftet med projektet är.***

Denna README är skriven i markdown. Den är till för att ge ett exempel på vad en README kan innehålla och hur den kan se ut.

## Språk och syfte
Programmet är skriven i python. Det finns inte något speciellt syfte mer än att bli underhållen.  

## Språk
- Python

## Krav
- Python 3.9+


***Vad krävs för att köra ditt program? Lista bara kraven.***

- Python 3.9+

## Installation
- För att köra programmet måste du installera följande:
- Python 
    Gå till https://www.python.org/downloads/ och tyrck på download under download latest version


## Kodkonvention
-Frågorna är på svenska men en engelsktalande person kan läsa koden då variablerna och funktionernas namn är på engelska. PEP8 följs.


## Hur det fungerar (Usage)
- T.ex på koden     
    thing, brand, size, amount, price = i.get_all_attributes()
                    old_string = f"{thing}/{brand}/{size}/{amount}/{price}\n"
                    new_string = f"{thing}/{brand}/{size}/{new_amount}/{price}\n"
                    with open("Skistar-kassa\ent_ski.txt", "r+", encoding="utf8") as f:
                        loan_list = f.readlines()
                        for line_str in loan_list:
                            if old_string == line_str:
                                new_list.append(new_string)
                            else:
                                new_list.append(line_str)
                        f.close()
                    with open("Skistar-kassa\ent_ski.txt", "w", encoding="utf8") as f:
                        for _ in new_list:
                            f.write(_)
                        f.close()
- Det här uppdaterar listan till nya värden


## Example (exempelkörning) + 

<img src ="./IMG/img 1.jpg">
<img src ="./IMG/img 2.jpg">



## To do/Roadmap (Att göra/Plan)
- [] Användaren får välja fler saker att hyra istället för en sak åt gången
- [] Mer saker att hyra
- [x] Kan hyra liftkort och skidor under samma betalning

## Changelog
- Inget har ändars 

#### Tillagt eller ändrat
- Inget

## Borttaget

- Tog bort upprepad kod

## Att bidra (Contribution)


Då bedömning ännu ej är gjord på uppgiften så tillåts inga pull requests. Så fort bedömning är gjord kommer detta tillåtas.  



## Licens (License)

[MIT](https://choosealicense.com/licenses/mit/)

## Contact (Kontakt)
Daniel Jonsson - daniel.jonsson4@elev.ga.ntig.se

Projektlänk: https://github.com/Dannesse/Skistar-kassa

## Erkännanden (Acknowledgments)
-Niclas Lund
-Christopher Christensen