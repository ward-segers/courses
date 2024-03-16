# Hoofdstuk 2 - Basic switch and End Device configuration

## IOS (Internetwork Operating System) Access 

### Operating Systems

- **Shell**: De user interface dat de gebruiker toelaat specifieke taken aan de computer te vragen. Deze kunnen zowel via de CLI als de GUI gevraagd worden
- **Kernel**: De communicatielaag tussen de hardware en software van een computer. Deze laag beheerd hoe de hardware resources gebruikt worden om de software requirements te behalen.
- **Hardware**: De fysieke onderdelen van een computer, inclusief de electronica

### GUI (Graphical User Interface)

Een GUI laat de gebruiker toe interactie te beleven met een het systeem door een omgeving van grafische iconen, menus en schermen.

Algemeen is een GUI gebruiksvriendelijker en vereist dit minder kennis van de onderlinge commandostructuur.

Voorbeelden: Windows, macOS, Linux KDE, Apple iOS en Android

Een nadeel van GUI is data deze kunnen crashen of niet voldoen aan de verwachtingen. Om deze zaken te vermijden worden netwerk end devices typisch aangesproken doormiddel van een CLI.

### Doel van een OS

Een Operating System van een pc laat de gebruiker toe het volgende te doen:
- Een muis gebruiken om selecties te maken en programma's te runnen
- Tekst en tekst-gebaseerde commando's in te voeren

Een CLI-gebaseerd netwerk operating system laat een netwerk technieker toe volgende zaken uit te voeren:
- Een toetsenbord gebruiken om CLI-gebaseerde netwerk programma's te runnen
- Een toetsenbord gebruiken om tekst en tekst-gebaseerde commando's in te voeren
- Ouput weergeven op een scherm

### Access Methods

- **Console**: Een fysieke beheerpoort die wordt gebruikt om toegang te krijgen tot een apparaat voor onderhoud, zoals het uitvoeren van de eerste configuratie
- **Secure Shell (SSH)**: Opstellen van een beveiligde afstands CLI connectie naar een toestel, doormiddel van een virtuele interface over een netwerk.

> [!TIP]
> Best practise: Gebruik SSH om remotely te verbinden met een device

- **Telnet**: Opstellen van een onveilige afstands CLI verbinding met een toestel over het netwerk.

> [!CAUTION]
> Bij telnet wordt de gebruikers authenticatie, passwoord en commando's over het netwerk in tekstvorm verzonden!

### Terminal Emulation Programs

Terminal Emulation Programs zijn programma's die gebruikt worden om verbinding te maken met een netwerk apparaat door een console poort of door een SSH/Telnet verbinding. (voorbeelden: PuTTY, Tera Term en SecureCRT)

## IOS Navigation

### Primary Command Modes

- **User Exec Mode**:
    - Geeft toegang tot een gelimiteerd aantal basic monitoring commando's
    - Herkenbaar door het `>` symbool in de console

    ```
    Router>

    Switch>
    ```
- **Privileged Exec Mode**:
    - Geeft toegang tot alle mogelijke commando's
    - Herkenbaar door het `#` symbool in de console

    ```
    Router#

    Switch#
    ```

### Configuration Mode and Subconfiguration Modes

- **Gobal Configuration Mode**: Wordt gebruikt om de configuratie opties op het toestel te raadplegen
```
Switch(config)#
```
- **Line Configuration Mode**: Wordt gebruikt om de console, SSH, Telnet of AUX toegangen te configureren
```
Switch(config-line)#
```
- **Interface Configuration Mode**: Gebruikt om de switch port of een router interface te configureren
```
Switch(config-if)#
```

### Navigation Between IOS Modes

- **Privileged Exec Mode**: Om om te schakelen van gebruiker EXEC mode naar privilege EXEC mode gebruiken we het commando `enable`
```
Switch> enable
Switch#
```

- **Global Configuration Mode**: Om te schakelen tussen global configuration mode, maken we gebruik van het `configure terminal` commando. Om terug te keren naar de privilege EXEC mode gebruiken we het `exit` commando.
```
Switch(config)#
Switch(config)# exit
Switch#
```

- **Line Configuration Mode**: Om te schakelen tussen de line configuration mode gebruiken we het `line` commando gevolgd door het "management line type". Om terug te keren naar de global configuration mode gebruiken we het `exit` commando.
```
Switch(config)#line console 0
Switch(config-line)#exit
Switch(config)#
```

- **Subconfiguration Modes**: 

1. Om eender welke subconfiguration mode te verlaten en terug naar de global configuration mode te gaan gebruiken we het commando `exit`. Om terug te keren naar de privilege EXEC mode gebruiken we het `end` commando of doormiddel van de toetsencombinatie `ctrl + z`. 

```
Switch(config)#line console 0
Switch(config-line)#end
Switch(config)#
```
2. Om direct van een subconfiguratie naar een andere te schakelen, voeren we het commando in dat overeenkomt met de subconfiguratie. In het voorbeeld veranderd de command prompt van `(config-line)#` naar `(config-if)#`

```
Switch(config-line)#interface FastEthernet 0/1
Switch(config-if)#
```

## The command structure

### Basis IOS Command Structure

<p align="center">
    <img src="src/ioscmd.png" alt="Basic command structure" width="50%">
</p>

- **Keyword**: Een specifieke parameter gedefinieerd door het operating system (hier ip protocollen)
- **Argument**: Niet ge-predefinieerd, een waarde of variabele gespecifieerd door de gebruiker (hier ip-adres **192.168.10.5**)

### IOS Command Syntax Check

Een commando kan een of meerdere argumenten nodig hebben. Om te achterhalen welke keywoorden of argumenten nodig zijn voor een commando bekijken we de commando syntax.
- Vetgedrukte tekst geeft de commandos of keywoorden weer die ingevoerd worden zoals ze getoond worden
- Schuingedrukte tekst bedoelt een argument waarvoor de gebruiker een waarde moet ingeven

| Regel | Beschrijving |
| ----- | ------------ |
| **boldface** | Vetgedrukte tekst toont commandos en keywoorden leterlijk zoals ze getoond worden |
| _italics_ | Schuingedrukte tekst bedoelt argumenten waarvoor een waarde moet ingegeven worden |
| **[x]** | Vierkante haakjes geven een optioneel element weer (keyword of argument) |
| **{x}** | Accolades indiceert een verplichte waarde (keyword of argument) |
| **[x {y &#124; z}]** | Accolades en verticale lijnen binnenin vierkante haakjes geven een verplichte keuze weer binnenin een optioneel element. Spaties worden gebruikt om delen van het commando op te splitsen |

- De commando syntax heeft een patroon, formaat dat gebruikt wordt wanneer het commando wordt ingegeven.

- Het commando `ping` of `traceroute` heeft een user defined argument, namelijk het ip-adres. <ins>Voorbeeld</ins>: 
    - `ping ip-adres` `ping 192.168.10.5` 
    - `traceroute ip-adres` `traceroute 192.168.10.5` 

- Een commando met verschillende parameters kan er als volgt uitzien:
`Switch(config-if)# switchport port-security aging {static | time time | type {absolute | inactivity}}`

### IOS Help Features

Er zijn twee verschillende soorten help beschikbaar: context-sensitive help en command syntaxt help

<table>
<thead>
<tr>
<td>Context-sensitve</td>
<td>Command syntax</td>
</tr>
</thead>
<tbody>
<tr>
<td><ul><li>Welke commando's zijn beschikbaar in welke mode?</li><li>Welke commando's starten met specifieke characters of groep van characters</li><li>Welke argumenten en keywords zijn beschikbaar in sommige commando's?</li></ul></td>
<td><ul><li>Gaat na indien een correct commando werd ingegeven door de gebruiker</li><li>Als het ingegeven commando niet begrepen werd, zal er feedback geschreven worden omtrent wat er verkeerd is met het commando</li></ul></td>
</tr>
<tr>
<td>

```shell
Router#ping ?
    WORD    Ping destination or hostname
    ip      IP echo
    ipv6    IPv6 echo
```

</td>
<td>

```shell
Switch#interface fastEthernet 0/1
                ^
% Invalid input detecter at '^' marker
```

</td>
</tr>
</tbody>
</table>

### Hot keys and shortcuts

- Het IOS CLI voorziet hot kets en shortcuts dat ervoor zorgt configureren, monitoren en troubleshooten gemakkelijker is.
- Commando's en keywords kunnen ingekort worden tot een minimaal aantal characters zodat deze steeds een uniek woord zijn.

<table>
<tr>
<td>

```shell
Router#con
%   Ambiguous command: "con"
Router#con?
configure   connect
```

</td>
<td>

```shell
Router#conf t
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#
```

</td>
</tr>
</table>

- Onderstaande tabel is een korte lijst of keyboard-shortcuts die het werken in de commandline gemakkelijker maakt.

| Keyboard-shortcut | Beschrijving |
| ----------------- | ----------- |
| Tab | Vervolledigt een deel van de commando invoer |
| Backspace | Verwijdert het character links van de cursor |
| Linker pijl of `Ctrl+B` | Verplaatst de cursor een character naar links |
| Rechter pijl of `Ctrl+F`| Verplaatst de cursor een character naar rechts |
| Pijl naar boven of `Ctrl+P` | Toont het laatst uitgevoerde commando |

Wanneer een commando meer tekst output heeft dan er kan weergegeven worden in het terminal venster. De IOS zal `--More--` op het scherm weergeven. Onderstaande toetsencombinaties kunnen gebruikt worden om daarin te navigeren.

| Keyboard-shortcut | Beschrijving |
| ----------------- | ------------ |
| `Enter` | Toont de volgende lijn |
| `Spatie` | Toont het volgende scherm |
| Elke andere toets | Sluit het uitgebreid scherm af en keert terug naar de "Privileged EXEC mode |

Onderstaande tabel toont alle combinaties die kunnen gebruikt worden om een operatie af te sluiten.

| Keyboard-shortcut | Beschrijving |
| ----------------- | ------------ |
| `Ctrl+C` | Wanneer we in een configuratie mode zijn, sluit dit de configuratie mode af en keren we terug naar de "Privileged EXEC mode" |
| `Ctrl+Z` | Wanneer we in een configuratie mode zijn, sluit dit de configuratie mode af en keren we terug naar de "Privileged EXEC mode" |
| `Ctrl+Shift+6` | Algemeen gebruikt commando om een sequentie af te sluiten DNS lookups, traceroutes, pings, etc. |

## Basic Device Configuration

### Device Names

> [!TIP]
> **Best practise**: het eerste configuratie commando op een toestel zou moeten zijn om het toestel een unieke hostnaam te geven.

- Standaard wordt elk toestel een naam gegeven. Bv. Bij een Cisco IOS switch is dit `Switch`

- Richtlijnen voor de naamgeving van toestellen:
    - Begint met een letter
    - Bevat geen spaties
    - Eindigt met een letter of cijfer
    - Gebruik alleen letters, cijfers of streepjes
    - Moet minder dan 64 characters lang zijn

Verander van een hostname:

```shell
Switch# configure terminal
Switch(config)# hostname Sw-Floor-1
Sw-Floor-1(config)#
```

### Password Guidelines

- Het gebruik van zwakke of makkelijk te raden passwoorden is een veiligheidszorg.
- Alle netwerk toestellen zouden best administratieve toegangen beperken door "Privileged EXEC", "user EXEC" en remote Telnet toegangen te beveiligen met passwoorden.
- Passwoord regelgevingen:
    - Gebruik passwoorden die langer dan 9 characters zijn
    - Gebruik een combinatie van klein- of hoofdletters, cijfers, speciale characters, en/of numerieke sequenties
    - Vermijd het gebruik van hetzelfde passwoord voor alle toestellen
    - Gebruik geen veel gebruikte woorden, deze zijn gemakkelijk te raden.

### Configure passwords

<table>
<tr>
<td>

Beveilingen van de user EXEC mode toegang:
- Ga eerst in line configuration mode door het commando `line console 0` te gebruiken in de global configuration mode
- Daarna specifieer je het passwoord voor de user EXEC mode door het gebruik van het `passwoord` commando, als parameter geef je het gewenste passwoord (_pw_) op.
- Al laatste, schakel de user EXEC toegang in door het gebruik van het `enable` commando

</td>
<td>

```shell
Sw-Floor-1# configure terminal
Sw-Floor-1(config)# line console 0
Sw-Floor-1(config-line)# password pw
Sw-Floor-1(config)# login
Sw-Floor-1(config)# end
Sw-Floor-1#
```

</td>
</tr>
<tr>
<td>

Beveiligen van de privileged user EXEC mode toegang:
- Ga eerst in global configuration mode
- Gebruik hierna het commando `enable secret` met als parameter (_pw_) het passwoord om het passwoord in te stellen.

</td>
<td>

```shell
Sw-Floor-1# configure terminal
Sw-Floor-1(config)# enable secret password pw
Sw-Floor-1(config)# exit
Sw-Floor-1#
```

</td>
</tr>
</tr>
<tr>
<td>

Beveiligen van VTY line toegang:
- Ga eerst in VTY line configuration mode door gebruik te maken van het volgende commando vanuit global configuration mode: `line vty 0 15`
- Daarna specifieer je het VTY passwoord door gebruik te maken van het commando `password` met als parameter het gewenste passwoord (_pw_).
- Als laatst schakel je de VTY toegang in door het commando `login`

> [!NOTE]
> VTY lines staan remote toegang toe via Telnet of SSH naar het toestel. Verschillende Cisco switches ondesteunen tot 16 VTY lines (genummerd 0 tot 15)

</td>
<td>

```shell
Sw-Floor-1# configure terminal
Sw-Floor-1(config)# line vty 0 15
Sw-Floor-1(config-line)# password pw
Sw-Floor-1(config-line)# login
Sw-Floor-1(config-line)# end
Sw-Floor-1#
```

</td>
</tr>
</table>

### Encrypt passwords

<table>
<tr>
<td>

- De startup-config en running-config bestanden moeten de passwoorden weergeven in "plaintext"
- Om alle "plaintext" passwoorden te encrypteren gebruiken we het volgende commando vanuit de global configuration mode: `service password-encryption`

</td>
<td>

```shell
Sw-Floor-1# configure terminal
Sw-Floor-1(config)# service password-encryption
Sw-Floor-1(config)# exit
Sw-Floor-1#
```

</td>
</tr>
<tr>
<td>

Gebruik het `show running-config` commando om na te gaan dat de passwoorden op het toestel ge-encrypteerd zijn

</td>
<td>

```shell
Sw-Floor-1# show running-config
!

!
line con 0
password 7 094F471A1A0A
login
!
Line vty 0 4
Password 7 03095A0F034F38435B49150A1819
Login
!
!
end
```

</td>
</tr>
</table>


### Banner messages

- Een banner message is belangrijk om niet-toegestane gebruikers te waarschuwen bij het proberen toegang te krijgen tot het toestel.
- Om een banner message voor de huidige dag te maken gebruiken we het volgende commando in global configuration mode: `banner motd # bericht van de dag#`

>[!NOTE]
>De `#` in de commando syntaxt noemen we een "delimiting character". Het wordt ingegeven voor en na een bericht.

```shell
Sw-Floor-1# configure terminal
Sw-Floor-1(config)# banner motd #Authorized Access Only!#
```

De banner zal er als volgt uitzien bij niet-toegestane toegangs pogingen:

```shell
Press RETURN to get started.



Authorized Access Only!

User Access Verification

Password:
```

## Save Configurations

### Configuration files

Er zijn twee verschillende bestanden die de toestel configuratie opslaan:
- **startup-config**: Dit is het configuratie bestand dat is opgeslaan in het NVRAM. Het bevat alle commando's dat zullen gebruikt worden bij het opstarten of herstarten van het toestel.
- **running-config**: Dis is het configuratie bestand opgeslagen in het RAM. Het geeft de huidige configuratie weer. Het aanpassen van een "running configuration" is direct toegepast op de meeste toestellen. Het RAM geheugen is een snel maar minder stabiel geheugen. Het verliest al zijn inhoud na het afsluiten of herstarten van een toestel
- Om wijzigingen in de "running configuration" te kopiëren naa de "startup configuration" gebruiken we het commando `copy running-config startup-config` in privileged EXEC mode.

<table>
<tr>
<td>

```shell
Router#show startup-config
Using 624 bytes
!
version 15.4
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
```

</td>
<td>

```shell
Router#show running-config
Building configurations...

Current configurations : 624 bytes
!
version 15.4
no service timestamps log datetime msec
no service timestamps debug datetime msec
no service password-encryption
```

</td>
</tr>
</table>

### Alter the running configurations

Indien er wijzigingen zijn gemaakt aan de "running config" en deze hebben niet het gewenste effect, dan kan de "running config" hersteld worden naar een vorige configuratie, mits de huidige nog niet is opgeslagen. Dit kan als volgend:
- Verwijder de commando's manueel
- Laad het toestel opnieuw door het commando ´reload´ te gebruiken in privileged EXEC mode.
>[!NOTE]
>Het `reload` commando zorgt ervoor dat het toestel tijdelijk offline gaat. Wat leidt tot een onderbreking in het netwerk.

Indien de ongewenste wijzigingen opgeslagen zijn in het startup-config bestand, kan het zijn dat alle configuraties moeten verwijderd worden via het commando `erase startup-config` in privileged EXEC mode.

&#8594; Na het verwijderen van de startup-config, moet het toestel opnieuw geladen worden om de running-config te wissen uit het RAM.

### Capture configuration to a text File

Configuratie bestanden kunnen ook opgeslagen en gearchiveerd worden naar een tekst bestand

- **Stap 1**: Open een terminal emulation software, zoals PuTTY of Tera Term, dat reeds met een switch verbonden is.
- **Stap 2**: Schakel het aanmelden bij de terminalsoftware in en wijs een naam en bestandslocatie toe om het logbestand op te slaan. De afbeelding toont dat "All session output" wordt opgeslagen naar het gespecifieerd bestand.

<p align="center"><img src="src/putty1.png" alt="putty configuratie" width="50%></p>

- **Stap 3**: Voer de commando's `show running-config` en `show startup-config` uit in privileged EXEC mode. De tekst die weergegeven wordt in het terminal scherm zal in het gekozen tekst-bestand worden weergegeven.
- **Stap 4**: Schakel het aanmelden in de terminal software uit. Door de optie "none" te selecteren bij session logging option. (zie afbeelding)

<p align='center'><img src='src/putty2.png' alt='Disabled loggin in through software' width='50%'></p>


>[!NOTE]
>Het aangemaakte bestand kan gebruikt worden als record over hoe het toestel geimplementeerd is.

## Ports and addresses

### IP Addresses

- Het gebruik van ip-addressen is de hoofdzakelijkste manier om een toestel een ander apparaat te laten localiseren en een end-to-end communicatie op te zetten over het internet. vb. `192.168.1.10`
- De structuur van een IPv4 adres noemt met een "dotted decimal notation" and wordt voorgesteld door 4 decimale nummer tussen 0 en 255.
- Een IPv4 subnet mask is een 32-bit waarde dat het netwerk onderdeel van het host onderdeel onderscheidt. Samen met het IPv4 adres, bepaald het subnet mask tot welk subnet een apparaat behoord. vb. `255.255.255.0`
- Het default gateway adres is het ip-adres van de router, waar de host gebruikt van zal maken om toegang tot verschillende externe netwerken (incl. het internet) zal krijgen. vb. `192.168.1.1`
- IPv6 addressen zijn 128 bits in lengte en geschreven als strings van hexadecimale waarden. Elke 4 bits is voorgesteld door één hexadecimaal cijfer. (een totaal van 32 hexadecimale cijfers). Groepen van 4 hexadecimale cijfers worden gescheiden door een `:`. vb. `2a02:1811:d38:cc00:187a:ab5:a2:FastEthernet5e`
- IPv6 addressen zijn niet hoofdlettergevoelig.

>[!NOTE]
> In deze cursus gebruiken we IP voor zowel IPv4 als IPv6 (meest recente versie).

### Interfaces and Ports

- Netwerkcommunicaties hangen af van end user device interfaces, networking device interfaces, en de kabels die ze verbind.
- Netwerk media types: twisted copper cables, fiber-optic cables, coaxial cables, of draadloos.
- De verschillende netwerk media types hebben verschillende functies en voordelen. Enkele verschillen:
    - Afstand waarover de media het signaal succesvol kan dragen
    - Omgeving in welke de media geïnstalleerd kan worden
    - Hoeveelheid gegevens en de snelheid waarmee deze moeten worden verzonden
    - Kost van de media en installatie ervan

## Configure IP Addressing

### Manual IP Address Configuration for End Devices

- End devices op een netwerk hebben een ip-adres nodig om met ander apparaten op het netwerk te kunnen communiceren.
- IPv4 informatie kan manueel in het end device gegeven worden of automatisch via het Dynamic Host Configuration Protocol (DHCP)
    - Om manueel een IPv4 adres op een windows pc te configureren ga naar: **Control Panel > Network Sharing Center > Change adapter settings** en kies hier de adapter. Klik hier na rechts en selecteer **Properties** om de **Local Area Connection Properties** weer te geven.
    - Klik hierna op **Properties** om het **Internet Protocol Version 4 (TCP/IPv4) Properties** scherm te openen. Configureer hierna het IPv4 adres, subnet mask en default gateway.

### Automatic IP Address Configuration for End Devices

- DHCP staat een automatische IPv4 configuratie toe voor alle end devices die DHCP-enabled zijn.
- End devices gebruiken in de meeste gevallen standaard DHCP voor een automatische IPv4 configuratie.
    - Om DHCP in te stellen op een windows pc open **Control Panel > Network Sharing Center > Change adapter settings** en kies een adapter. Klik rechts op de adapter en kies **Properties** om de **Local Area Connection Properties** weer te geven.
    - Klik hierna op **Properties** om het **Internet Protocol Version 4 (TCP/IPv4) Properties** scherm te openen. Selecteer hierna **Obtain an IP address automatically** en **Obtain DNS server address automatically**

### Switch Virtual Interface Configuration

Om extern toegang te hebben tot een switch moet een ip-adres en een subnet mask geconfigureerd zijn op de SVI (Switch Virtual Interface).

Configureren van een SVI op een switch:
- Voer het `interface vlan 1` commando in vanuit global configuration mode
- Geef hierna een IPv4 adres door gebruik te maken van `ip address` met als parameters eerst het _ip-adres_ gevolgd door het _subnet mask_.
- Als laatste schakel je de virtual interface in door een `no shutdown` commando.

```shell
Switch# configure terminal
Switch(config)# interface vlan 1
Switch(config-if)# ip address 192.168.1.20 255.255.255.0
Switch(config-if)# no shutdown
```

hallo