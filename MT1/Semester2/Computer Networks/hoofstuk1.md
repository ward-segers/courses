# Hoofdstuk 1 - Networking Today

Communicatie is bijna even belangrijk als water, lucht voedsel en een dak. In de wereld van vandaag zijn we verbonden door het gebruik van verschillende netwerken.

- Elke computer in een netwerk is **een host** of een **end device**
- Servers zijn computers dat informatie doorgeven aan end devices

| Server type | Description |
| ----------- | ----------- | 
| Email server | Een email server runned email software. Klanten gebruiken client software om hun email te raadplegen |
| Web server | Een webserver runned websoftware. Klanten gebruiken browser software om webpagina's te raadplegen. |
| File server | Een file server kan bedrijfs en private bestanden opslaan. Klanten hun toestellen kunnen gebruikt worden om deze bestanden te raadplegen.|

Met klanten spreken we over toestellen die de requests naar de server sturen.

## Netwerk onderdelen

### Peer-to-peer netwerk

Peer-to-peer netwerk maakt het mogelijk om zowel de client als server in het netwerk te zijn. Dit wordt enkel aangeraden voor kleinere netwerken. 

| Voordelen | Nadelen |
| --------- | ------- |
| Gemakkelijk in opzet | Geen gecentraliseerde administratie |
| Minder complex | Niet zo veilig |
| Lager in kost | Niet schaalbaar |
| Wordt gebruikt voor kleiner taken: versturen van bestanden, delen van printers | Tragere performance |


### End Devices

Een end device is een toestel vanwaar een bericht vertrekt, of waar het bericht toekomt. Data vertrekkende van een end device, loopt doorheen een netwerk en komt aan een end device aan.

### Intermediary Network Devices

= Tussenliggende netwerk apparatuur

Deze apparaten verbinden onderling end devices.
Voorbeelden hiervan zijn; een swtich, draadloze access points, routers, firewalls,...

Een van de taken van deze toestellen is ook het beheer van data dat door een netwerk vloeit:

- Data signalen regenereren en opnieuw verzenden
- Informatie bijhouden over welke paden er binnen een netwerk bestaan
- Andere apparaten berichten over fouten en communicatiefouten

### Netwerk Media

Communicatie over een netwerk gebeurd door een medium die een bericht toelaat te bewegen van de bron naar de bestemming.

| Media types | Beschrijving |
| ----------- | ------------ 
| Metalen draden in kabels | Gebruiken elektrische pulsen |
| Glazen of plastieken vezels in kabels (fiber-optic cable) | Gebruiken licht pulsen |
| Draadloze transmissie | Gebruiken modulaties van specifieke frequenties van elektromagnetische golven |

## Netwerkweergaven en begrippen

### Netwerkweergaven

Netwerk diagrammen, gebruiken vaak symbolen om toestellen binnenin een netwerk voor te stellen.

Enkele belangrijke begrippen:

- Network Interface Card (NIC)
- Physical port (fysieke poort)
- Interface

![netwerk devices](src/image.png)

### Netwerk diagrammen

Netwerk diagrammen geven een visuele weergave over hoe het netwerk verbonden is.

**Fysieke netwerk diagrammen** illustreren de fysieke locatie van tussenliggende netwerkapparatuur en kabel installaties.

![fysiek netwerk diagrammen](src/image2.png)

**Logische netwerk diagrammen ** illustreren toestellen, poorten en het addressenschema van een netwerk

![logische netwerk diagrammen](image3.png)

## Veel voorkomende netwerken

Er bestaan verschillende soorten netwerken deze komen vooral in verschillende groottes:

- Small Home Networks: enkel computers onderling en met het internet verbonden
- Small Office/Home Office: Is instaat een computer in een home of remote office te laten verbinden met een bedrijfs netwerk. (= SOHO)
- Medium to Large Networks: verschillende locaties met honderden of duizenden onderling verbonden computers
- World Wide Networks: Verbind duidende miljoenen computers wereldwijd (zoals het internet)

### LANs en WANs

Netwerken verschillen door:
- Grootte en bedekt gebied
- Aantal verbonden gebruikers
- Aantal en type diensten die beschikbaar zijn
- Verantwoordelijkheidsgebied

De meest voorkomende soorten netwerken zijn:
- Local Area Network (LAN): netwerk infrastructuur in een beperkt geografisch gebied
- Wide Area Network (WAN): netwerk infrastructuur in een groter geografisch gebied

| LAN | WAN |
| --- | --- |
| Verbind end devices in een beperkt gebied | Verbind LAN-netwerken in een wijder gebied |
| Beheerd door één persoon of organisatie | Vaak beheerd door verschillende service providers |
| Voorziet interne apparaten van een hoge snelheid bandbreedte | Vaak lagere snelheden tussen de LAN-netwerken |

![LAN](src/lan.png)
LAN-netwerk

![WAN](src/wan.png)
WAN-netwerk

### Het internet

Het internet is een wereldwijde collectie van onderling verbonden LAN en WAN netwerken.

- LAN-netwerken zijn onderling verbonden doormiddel van WAN-netwerken
- WAN-netwerken kunnen koperen kabels, glasvezels kabels, en draadloze transmissie gebruiken

Het internet is geen eigendom van een persoon of organisatie. Volgende groepen zijn betrokken in het onderhouden van structuur en protocollen op het internet.
- IETF: Internet Engeneering Task Force
- ICANN: Internet Corporation for Assigned Names and Numbers
- IAB: Internet Architecture Board

<p align="center">
    <img src="src/internet.png" alt="internet" width="50%">
</p>

### Intranet en Extranet

