# CYBERSECURITY : Hoofdstuk 3 - Bedreigingen, aanvallen en kwetsbaarheden

## Inleiding

### Interne vs. Externe aanvallen

- Aanvallen kunnen afkomstig zijn van binnen organisatie of van buiten de organisatie.
- **Interne** aanvallen:
    - Afkomstig van een **interne gebruiker**, zoals medewerker of contractpartner
    - kan per ongeluk of opgezet zijn
    - Interne aanvallen kunnen grotere schade aanrichten dan externe dreigingen, omdat interne gebruikers rechtstreeks toegang hebben tot het gebouw en de bijbehorende infrastructuur/apparatuur
    - Interne aanvallers hebben doorgaans kennis van het bedrijfsnetwerk, de bronnen en de vertrouwelijke gegevens. Ze hebben mogelijk ook kennis van beveiligingsmaatregelen, beleidsregels en hogere niveaus van beheerdersrechten.

- **Externe** aanvallen:
    - van amateurs of ervaren aanvallers kunnen misbruik maken van kwetsbaarheden in netwerkapparaten, of kunnen social engineering gebruiken, zoals bedrog, om toegang te krijgen
    - maken misbruik van zwakheden of kwetsbaarheden om toegang te krijgen tot internen bronnen

### Opkomst van mobiele apparaten

- In het verleden gebruikten werknemers doorgaans door het bedrijf uitgegeven computers die waren verbonden met een bedrijfsnetwerk.
- Tegenwoordig wordt er steeds meer gebruik gemaakt van **mobiele apparaten** op de werkvloer.

> Dit noemt men **Bring Your Own Device (BYOD)** en is een groeiende trend

- Het moeilijk centraal beheren en updaten van mobiele apparaten, vormt een bedreiging voor organisaties die mobiele apparaten van werknemers op hun netwerken toestaan.

### Opkomst van Internet-of-Things (IoT)

> **Het Internet-of-Things** (IoT) is de verzameling technologieën die de verbinding van verschillende apparaten met het internet mogelijk maakt.

- IoT-technologieën stellen mensen in staat miljarden apparaten met het internet te verbinden.
- Deze apparaten omvatten lichten, sloten, motoren en entertainmentapparaten, om er maar een paar te noemen.
- Dit heeft invloed op de hoeveelheid gegevens die moet worden beschermd. Gebruikers hebben op afstand toegang tot deze apparaten, waardoor het aantal netwerken en toestellen dan moet worden beschermd toeneemt.
- Voorbeelden IoT:
    - Connected cars
    - Smart appliances
    - Connected security systems
    - Smart agriculture equipment
    - Connected retail
    - Connected healthcare monitors
    - Connected manufacturing equipment
    - Connected cities
- Fabrikanten geven weinig prioriteit aan de beveiliging van IoT-apparaten, daarom is het net een geliefd doelwit van criminelen.

### Impact van Big Data

> **Big Data** is het resultaat van *datasets* die groot en complex zijn, waardoor traditionele dataverwerkingstoepassingen ontoereikend zijn.

Big data biedt zowel uitdagingen als kans op basis van drie dimensies:
- Het volume of de hoeveelheid gegevens
- De verscheidenheid of het bereik van gegevenstypen en bronnen
- De snelheid van gegevens

> Worden ook wel de 3 V's genoemd, **V**olume, **V**ariety, **V**elocity.

### Bredere reikwijdte en cascade-effect

**Federatief identiteitsbeheer** verwijst naar meerdere ondernemingen die hun gebruikers dezelfde identificatiegegevens laten gebruiken om toegang te krijgen tot de netwerken van alle ondernemingen in de groep. Het doel van federatief identiteitsbeheer is om identificatieinformatie automatisch over domeingrenzen heen te delen.

De meest gebruikelijke manier om de federatieve identiteit te beschermen, is door inlogmogelijkheid te koppelen aan een geautoriseerd apparaat.

Voorbeelden van federatief identiteitsbeheer:
- Je kan op verschillende sites inloggen met facebook-/google-/steam-/... account, ook al heeft die website daarmee niets te maken.
- Je kan je op verschillende sites inloggen met je e-id

### Verhoogde waakzaamheid

De verdediging tegen cyberaanvallen aan het begin van het cybertijdperk was laag. Een slimme middelbare scholier of scriptkiddie kon toegang krijgen tot systemen.

- Nu zijn landen over de hele wereld zich meer bewust geworden van de dreiging van cyberaanvallen. De dreiging van cyberaanvallen staat nu in de meeste landen bovenaan de lijst van grootste bedreigingen voor de nationale en economische veiligheid.

- Hoe doen we het in België?
    - Je kan terecht als slachtoffer bij:
        - [safeonweb](https://www.safeonweb.be/nl/nuttige-links) voor nuttige links over cybercriminaliteit
        - de lokale politie om aangifte te doen

## Malware en kwaardaardige code

### Verschillende soorten malware

Cybercriminelen vallen de toestellen van de gebruikers aan door het installeren van kwaadaardige code.

#### Virussen

> **Een computervirus** is een kwaadaardig stukje code die vasthangt aan een uitvoerbaar bestand.

De meeste virussen hebben een zekere vorm van actie van de eindgebruiker nodig. De virussen kunnen dan onmiddelijk of op een bepaald moment worden geactiveerd.

#### Worm

> Een stukje kwaadaardig code die zich kenmerkt doordat het zichzelf repliceert door gebruik te maken van een kwetsbaardheid in het netwerk.

Worms zullen hierdoor vaak ook het netwerk vertragen.

**Verschil met een virus**: een virus heef een host programma nodig om te draaien, een worm kan op zichzelf draaien.

> Behalve de initiële infectie heeft de worm geen interactie van de gebruiker nodig.

#### Trojan Horse

> Malware die verborgen zit in gewenste bestanden zoals foto's of een game.

- Een gebruiker is hier niet van bewust
- Een Trojan Horse verschil van een virus omdate het een niet-uitvoerbaar bestand infecteert
- Een virus heeft een executable bestand nodig.
- Een Trojan Horse is dus geen programma dat zelfstandig beschadigingen aan de geïnfecteerde computer veroorzaakt.
- Het moet bovendien door de gebruiker zelf worden gekopieerd en kopieert zichzelf niet naar andere computers zoals een worm wel doet.

#### Logic bomb

> Een kwaadaardig programma die wordt geactiveerd op een bepaald moment (=trigger). 

- Wacht op de trigger om te activeren en schade toe te brengen
- Trigger kan een bepaalde datum zijn, een ander programma dat wordt opgestart, of een bepaalde actie die werd gedaan.

#### Ransomeware

> Een computersysteem of data wordt geblokkeerd of geëncrypteerd tot het moment dat het slachtoffer een geldsom betaalt.

- De key om data opnieuw te decrypteren blijft geheim tot er betaald wordt.
- Soms heb je geluik en kan je toch data decrypteren en herstellen
    - [No More Ransom - Decryptiontools](https://www.nomoreransom.org/en/decryption-tools.html#header) - samenwerken van politiediensten
    - Voorkomen is beter dan genezen! Maak vaak back-ups

#### Backdoor en Rootkits

> Een rootkit zal het operating system aanpassen en zo een backdoor creëren?

Deze backdoor wordt dan gebruikt om het gecompromitteerde systeem binnen te dringen, zonder enige vorm van authenticatie.

#### Keyboard logging

> Een computerprogramma die de toetsenbordaanslagen (keystrokes) gaat opnemen of loggen.

Dit stukje sofware wordt dan op het toestel van het slachtoffer geïnstalleerd. De dader programmeert de software om dan na afloop de log file of opname via mail door te sturen naar de dader. In de log file kan dan gevoelige informatie staan, zoals emailadressen, wachtwoorden, pincodes,...

## Misleiding en oplichting

### De kunst van het oplichten

- Social Engineering:
    - Gebruikt geen technologische hoogstandjes, maar is daarom niet minder doeltreffend. Het bestaat erin om het vertrouwen van jouw slachtoffer te winnen om dan nadien van het slachtoffer iets te verlangen.
    - voorbeeld: voordoen als iemand van de beveiligingsfirma en vragen om de poort te openen
- Tegenwoordig een van de meest populaire hack-methodes
    - 80%
    - Zeer doeltreffend
    - Mensen zijn vaak de zwakste schakel