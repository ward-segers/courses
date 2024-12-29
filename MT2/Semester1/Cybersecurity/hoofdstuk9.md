# CYBERSECURITY : Hoofdstuk 9 - Blue team

## Een diepe verdediging

- **Layering** (gelaagdheid) : zorgt voor de meest omvangrijke beveiliging
    - wanneer cybercriminelen de eerste laag kunnen binnendringen is er nog steeds de tweede
    - beveiligen in lagen betekent dat je meerdere barrières gaat maken
- **Limiting** (beperking) : het beperken van toegang tot informatie vermindert de kans op een aanval
    - een organisatie beperkt best de toegang om er voor te zorgen dat werknemers alleen toegang hebben tot de info die ze nodig hebben om hun job uit te voeren
- **Diversity** (diversiteit) : verieer in manieren van beveiliging
    - toegang tot eerste laag, mag niet de andere lagen in gevaar brengen
    - gebruik in andere lagen bv. een ander encryptie algoritme
- **Obscurity** (verduistering) : verduisteren van informatie
    - Een organisatie hoeft niet vrij te geven welke OS versie of firewall ze gebruikt
    - Security through Obscurity kan handig zijn, maak hier echter nooit de hoeksteen van je beveiliging van
- **Simplicity** (eenvoud) : lijdt meestal tot een hogere beschikbaarheid
    - Complexe beveiliging vergroot de kans op fouten

> Steun nooit op slechts een concept
> Streef naar een gevarieerde combinatie

## Systemen en apparaten beschermen

Er zijn verschillende aspecten aan het beheren van ICT-omgevingen die we moeten beschermen:
- Fysieke toegang
- Gebruikersbeheer
- Hosts (individuele gebruikerstoestellen)
    - Laptops, smartphones,...
- Servers
- Netwerk(apparaten)

### Fysieke bescherming

- Mag je niet vergeten!
- Kan enorm schadelijk zijn
    - Diefstal
    - Rogue device planten
    - Vandalisme

#### Hoe voorkomen?

- Sluit toegang af
    - Omheining, barricades, bewaking,...
    - Beperkte toegangstijden
- Dwing identificatie af
    - Biometrie
    - Badge
- Beveilig toestellen
    - Kabelsloten
    - Veiligheidskooien
    - Logout timers (automatisch vergrendelen na periode van inactiviteit)

#### Wat bij diefstal?

- Hou logboeken bij
    - wie had het laatst toegang?
- GPS tracking

#### Hou je toestellen blij

- Redundante en voldoende stroomvoorziening
- HVAC
    - Verwarming, ventilatien, airco
    - Regelt de omgeving (temperatuur, vochtigheidn, luchtstroom en luchtfiltering)
- Monitor de hardware
    - Alerts als er iets foutgaat

### Gebruikersbeheer

#### De zwakste schakel

- Gebruikers (klanten, werknemers, IT-personeel) zijn onvoorspelbaar
    - Hebben soms slechte bedoelingen
    - Maken fouten
- Limiteer de rechten van een gebruiker zoveel mogelijk

> Principle of least privilege!

#### AAAA framework

- **A**uthentication
    - Wie mag iets doen?
- **A**uthorisation
    - Wat mag iemand wel/niet doen?
- **A**ccounting
    - Wie heeft wat gedaan?

Voorbeeld 1: Bankautomaat

- **A**uthentication
    - Enkel iemand met de juiste bankkaart en pincode heeft toegang tot de bankrekening
- **A**uthorisation
    - Iemand kan niet meer geld afhalen dan hij heeft
    - Er is een maximum bedrag dat afgehaald kan worden per dag
- **A**ccounting
    - Op de rekeninguitreksels staat er welk bedrag er wanneer is gestort op of afgehaald van de rekening

> [!tip]
> Meer voorbeelden in de slides 
> [voorbeeld Forum](https://hogenttin.github.io/cybersecurity-slides/h9.html?showNotes=true#/24)

#### Hulpmiddel voor authenticatie

- **Multi-Factor Authentication (MFA/2FA)**
    - What you know
        - wachtwoorden, wachtwoordzinnenn, pincodes
    - What you have
        - Smartcards, beveiligingssleutelhangers, toegang tot GSM (authenticator app of SMS), toegang tot e-mailaccount (verificatie e-mail)
    - Who you are
        - Biometrie: een uniek fysiek kenmerk zoals vingerafdruk, netvlies, stem
    - **Minstens 2 van de 3 nodig**

#### Hulpmiddel voor autorisatie

- Rechten
    - Op basis van niveau's
        - bv. *unclassified* > *confidential* > *secret* > *top secret* niveau's in het leger
    - Op basis van rechten toegekend door eigenaar
        - bv. `rwxrwxrwx` bij Linux bestanden
    - Op basis van functie
        - bv. enkel dokters mogen patiëntendossiers zien

#### Hulpmiddel voor accounting

- Logfiles
    - Inlogtijd
    - Succesvol aangemeld?
    - Welke bronnen gebruikt?

### Host Hardening

- Beveiliging van het besturingssysteem
    - Standaardconfiguratie aanpassen
    - Verwijderen onnodige software
    - Beveiligingspatches en updates
- Installeren **anti-malware**
    - bescherming tegen virussen, worms, keyloggers, spyware,...
    - Mobiele apparaten zijn ook kwetsbaar
    - **Let op met gratis software!**
        - frauduleuze anti-malware, kan zelf malware bevatten
- Beheer van **patches**

    - > **Patches** zijn code-updates die fabrikanten bieden om te voorkomen dat een nieuw ontdekt virus of worm een succesvolle aanval plaatst 

    - kunnen centraal beheerd worden
        - automatisch
        - eventueel verplicht
    - > Combinatie van patches en upgrades noemen we **een servicepack**
- Host-gebaseerde firewall
    - regelt inkomend en uitgaand netwerkverkeer op het eigen toestel
- **Host Intrusion Detection System** (HIDS)
    - Controleert verdachte activiteiten op het eigen toestel

#### Draadloze en mobiele apparaten

- **Wired Equivalent Privacy** (WEP)
    - Basisbescherming Wi-Fi
    - 10 tot 26 hexadecimale karakters (40-104 bits)
    - ⚠️ **Niet meer veilig!**
- **Wi-Fi Protected Access** (WPA/WPA2)
    - Grote verbetering ten opzichte van WEP
    - Gebaseerd op AES
    - ✅ Tegenwoordig is WPA2 de standaard
- Toevoegen van **wederzijdse authenticatie**:
    - voorkomt MitM aanval (rogue access point)
    - Authenticatie tussen beide entiteiten

#### Bescherming van (host) data

- **Bestandstoegangscontrole**
    - Machtigingen op bestanden en mappen
    - Ingesteld per gebruiker of groep gebruikers
- **File encryption**
    - Encrypteren van gevoelige data
    - Kan op individuele bestanden of op hele harde schijven
        - bv. BitLocker op Windows of LUKS op Linux
- Systeem- en gegevens **back-ups**
    - reserve kopie van gevoelige data
    - Typisch op verwijderbare media
    - > Een van de meest effectieve manieren om gegevensverlies te voorkomen

#### Content control

- Content screening en blokkering
    - Beperkt de inhoud waartoe een gebruiker toegang heeft met een webbrowser via internet
    - Kan bepaalde sites blokkeren

#### Disk cloning, deep freeze

- Software om besturingssysteem en configuratiebestanden te beschermen
- **Disk clone**
    - Image (bv. ISO) van volledige harde schijf
- **Deep freeze**
    - "Bevriest" de partitie van de harde schijf
    - Alle wijzigingen door gebruiker verloren bij herstarten
    - Vooral nuttig voor publieke toestellen
        - bv. internet café

#### Kiosk mode

- Afgesloten omgeving waar je niet zomaar uit kan
- Heeft niets te maken met harde schijven of partities, het is meer een software matige gevangenis
- Meer preventief t.o.v. disk clone en deep freeze
- Vooral nuttig voor publieke toestellen (bibliotheek, zelf-scan, bestelkassa)

#### Virtualisatie / Sandboxing

- Programma's worden uitgevoerd in een virtuele omgeving (ook soms sandbox)
- Programma's hebben niet door dat ze in een virtuele omgeving draaien
- Als hackers via de software zich een weg naar binnen hacken, zitten ze nog steeds vast in de virtuele omgeving en niet direct op het besturingssysteem van het toestel
- Soms lukt het daders echter om deze sandbox te omzeilen en zo toch code uit te voeren op het besturingssysteem van het slachtoffer

Een gelijkaardig voorbeeld in *Webhosting*.

- het is economisch niet voordelig om elke website op een server te draaien
- vaak wordt dus op 1 server verschillende virtuele servers geeïnstalleerd
- Dankzij deze virtualisatie kunnen gebruikers van de ene virtuele machine niet aan de andere

> Voorbeeld **Docker**

### Server hardening