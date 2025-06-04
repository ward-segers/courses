# It2business : Hoofdstuk 1 - Project Management - Deel 4

## Wat zijn de noden van onze klant?

> #requirements analyseren

> We spreken pas over een project zodra de business case effectief is goedgekeurd en er vanuit het management een beslissing is gekomen om het project op te starten.

### Proces van requirementsanalyse

> Requirements (of vereisten) zijn een specificatie van wat dient te worden geïmplementeerd. Dat omschrijft hoe een digitale oplossing zich moet gedragen en welke de kenmerken zijn van de oplossing. Daarnaast kunnen vereisten ook een beperking opleggen aan de implementatie en ontwikkeling van de digitale oplossing.

<p align='center'><img src='src/requirementsanalyse.png' alt='requirementsanalyse' width='50%'></p>

**We onderscheiden in het proces van requirementsanalyse de volgende 4 fasen:**

1. *Bevragen*
   - Definieer productvisie en projectscope
     - Wat is de reden voor het initiëren van he project (moet duidelijk zijn voor alle stakeholders)
     - Belangrijk dat het einddoel ook duidelijk is
       - Strategie: Wat willen we bereiken met dit initiatief?
       - Scope: Wat is er allemaal inbegrepen en wat niet?
     - Strategie en visie blijven ongewijzigd. Scope kan later in het project nog gewijzigd worden
   - Identificeer gebruikersgroepen en hun eigenschappen (eventueel met sleutelgebruikers)
     - Beschrijf de gebruikersgroepen op basis van taken, gedragingen, locatie of een ander criterium. Maak eventueel personas om ze te concretiseren.
     - > **Een persona** is een beschrijving van een hypothetische, generische persoon die gebruikt wordt als een stand-in voor een groep gebruikers die dezelfde noden en karakteristieken hebben.
     - Sommige gebruikersgroepen kunnne erg groot zijn, daarom is het zinvol een sleutelgebruiker voor deze gebruikersgroep te selecteren.
     - Hou focusgroepen met de huidige gebruikers
       - Huidige manier van werken kan vaak een goedinzicht geven in de verwachtingen.
   - Definieer user requirements en welke meerwaarde dit oplevert
     - Beschrijven welke taken een gebruiker zal moeten uivoeren in de oplossing en welke meerwaarde dit voor de onderneming kan hebben.
   - Definieer digitale triggers
     - Welke triggers lokken een reactie naar een digitale oplossing uit?
       - Externe triggers: bv. sensor die beweging detecteert
       - Geplande triggers: bv. elk uur moet er eens status rapport worden verstuurd
       - Trigger van de gebruiker uit: bv. een gebruiker drukt op een knop in de oplossing

   - Technieken bevragen van vereisten:
     - Interviews
     - Workshops
     - Job monitoring: observatie van sleutelgebruikers om te bepalen welke taken er worden uitgevoerd en op welke manier
     - Enquêtes
     - Documentanalyses
     - Problem reports
     - Bestaande requirements

2. *Analyseer*

Na het ontvangen van de informatie in het bevragingsproces, moeten we die gaan analyseren zodat er een eerste ruwe versie van de oplossing kan worden geschetst. Ook hier zijn een aantal stappen die we doorlopen:

   - Moddeleer de omgeving &rarr; visuele ondersteuning
     - Visuele ondersteuning door middel van diagrammen toont:
       - hoe oplossing in huidige omgeving past
       - met welke andere oplossingen ze communiceert
       - welke outputs er verwacht kunnen worden
     - Volledig nieuwe oplossing?
       - zinvol om een prototype of user interface te bouwen
   - Haalbaarheid van requirements
     - Haalbaar?
     - Dragen ze voldoende bij tot de doelen?
     - Indien doel kostenbesparend, geen hogere implementatiekost?
   - Prioritiseren van requirements
     - Volgens de MOSCOW-methode
   - Beschrijf technische vereiste
   - Splits op in deeloplossingen indien nodig
3. *Specifieer* 
    > = eenduidige communicatie van wat er concreet vereist wordt
4. *Validatie*
    > = formeel akkoord van de vereisten opdat project succesvol is (scope!)
    1. formele review
    2. testscenario's om de vereisten te testen
    3. vastleggen van acceptatiecriteria

#### Type vereisten

| Term                             | Definitie                                                                                                                                                     | Voorbeeld                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| *Business requirement*           | Strategische doel van het bedrijf dat de software implementeert en de meerwaarde die deze oplossing kan bieden                                                | 'We hebben een webshop nodig om onze verkoop te kunnen stimuleren'                   |
| *Business rule*                  | Een policy, richtlijn of standaard die een bepaalde voorwaarde stelt aan de software. Is geen requirement op zich, maar leidt tot een of meerdere equirements | 'Elke bestelbon moet ondertekend worden door een manager'                            |
| *Constraint*                     | Een beperking die wordt opgelegd waardoor de keuzes die we kunnen maken beperkter worden. (vaak omstandigheden waar we weinig invloed op hebben)              | 'In ons bedrijf is enkel JAVA-kennis aanwezig'                                       |
| *External interface requirement* | Beschrijving van een link tussen verschillende systemen en/of hardware                                                                                        | 'Betalingen online gebeuren via PayPal'                                              |
| *Feature*                        | Een set van functionaliteiten die een logisch geheel en een meerwaarde voor de klant vormen                                                                   | 'Er moet een productcatalogus ter beschikking zijn'                                  |
| *Functional requiremen*          | Een beschrijving van hoe het systeem zich zal gedragen onder bepaalde omstandigheden                                                                          | 'Als een product niet op voorraad is, moet de verwachte levertermijn getoond worden' |
| *Non-functional requirement*     | Een beschrijving van een eigenschap van het systeem                                                                                                           | 'De webshop moet ook kunnen worden getoond op mobiel toestellen'                     |
| *System requirement*             | De systeemvereisten die nodig zijn om een softwareproduct te kunnen maken                                                                                     | 'Het inloggen in de webshop vereist een tweestapsverificatie'                        |
| *User requirement*               | Taken die een user moet kunnen uitvoeren                                                                                                                      | 'Een verkoper moet alle bestelbonnen kunnen bekijken'                                |

### Rollen en verantwoordelijkheden

> Het uitvoeren van de requirementsanalyse gebeurd hoofdzakelijk door de eindgebruikers en de businessanalist

1. **De businessanalist**: grootste rol bij het verzamelen, analysere en documenteren van de vereisten
2. **De eindgebruikers**: meest betrokken bij de bevraging en de analyse als de input van informatie
3. **De sleutelgebruikers**: zullen vooral aanwezig zijn in interviews en focusgroepen, maar bieden ondersteuning bij de analyse- en documentatiefase. Bij de validatie zullen ze ook hun goedkeuring moeten geven
4. **De sponsor**: worden vooral bevraagd voor het identificeren van de business requirements, business rules en constraints
5. **De architect**: wordt ingeschakeld wanneer in de initiatiefase het al noodzakelijk is een aantal technische vereisten te bepalen

### Deliverables

> Zijn de documenten van de vereisten

1. Scope statement
2. User stories
3. Software requirements specification (SRS)

### Beheersen van een project

<p align='center'><img src='src/beheersaspecten_tgkio.png' alt='Beheersaspecten TGKIO' width='50%'></p>

#### Beheersing in de praktijk

- Planning vooraf (T)
  - Activiteiten en werkuren
  - Dependecies
  - Nodige resources
  - Milestones - wanneer moet/kan iets af zijn
- Voortgangsbewaking (T, I)
  - Rapporteren
  - Tijdsverantwoording - Trello (Estimate/Time Spent/Time Remaining)
  - Weekverslag
- Overleggen (I, O)
  - Wekelijkse meetings
  - Demo's, stand-up
  - Skype/hipchat/slack/discord
- Planning aanpassen (T)
- Bewaking budget (G)
  - Startbudget = koopt eindproduct
  - Kosten blijven opvolgen en afzetten tegen over projectvoortgang en het totale budget
  - Kosten baten blijven evalueren &rarr; scope aanpassen of stopzetten van project kan als gevolg optreden
- Bewaking kwaliteit (K)
  - Op basis van specificaties een verwachting
    - Roeiboot verwachting waterdicht, maar zeewaardig tijdens hevige storm is onredelijk
  - Tussentijdse kwaliteitscontroles zijn nodig
  - Kwaliteit heeft zijn prijs
  - SMART doelstellingen
- Verspreiding en archivering info
  - Wiki - confluence
  - Ontwerpen en documentatie
- Bewaking projectdoel (O)
  - Scope-creep
  - Afwegen van de wijzigigen
    - Geen wijzigingen toesten &rarr; minder bruikbaar eindresultaat
    - Te veel wijzigigen toestaan &rarr; tijd/kost in gevaar
  - Financiële consequenties schriftelijk duiden aan opdrachtgever
  - Officieel wijzigingsverzoek
- Bedreigingen project (O)
  - Motivatie zakt weg
  - Taakverdeling onduidelijk
  - Meningsverschillen
  - Eigen doelen
  - Besluitvorming te traag
  - Onduidelijk doel
  

### Project risico's

- Gevaar voor schade of verlies door onzekere gebeurtenis
- Grootte risico = kans x gevolg
- Kans kan klein zijn maar met grote gevolgen
- Scope - planning - materiaal - mensen - organisatie ...

#### Risico analyse

- Inventariseer risico's
- Analyseer risico's
- Formuleer maatregelen
  - Preventief/repressief
  - Overdragen
  - Acceptatie

#### Project stoppen?

<p align='center'><img src='src/risico_analyse_project_stoppen.png' alt='Risico Analyse, project stoppen' width='75%'></p>

### Project management methoden

- System Development Methodology
  - Automatisering
  - Strakke fasering - waterval
- Scrum
- Prince2
  - Checklist, richtlijnen, Project Initiation Document
- PMBoK
  - Best practises
- P6

<p align='center'><img src='src/project_management_methoden.png' alt='Project Management Methoden' width='50%'></p>
