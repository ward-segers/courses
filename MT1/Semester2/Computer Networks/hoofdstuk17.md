# Computer Networks : Hoofdstuk 17 - Build a Small Network

## Devices in a Small Network

### Small Network Topologies

- De meeste bedrijven zijn klein, hierdoor zijn de meeste netwerken ook klein.
- Het netwerkdesign van een klein netwerk is redelijk eenvoudig.
- Kleine netwerken hebben meestal één enkele WAN connectie, voorzien door een DSL kabel of een Ethernet connectie.
- Grotere netwerken hebben een IT departement nodig voor het beheren, beveiligen (o.a. van bedrijfsgegevens) en het troubleshooten van netwerktoestellen. Kleine netwerken worden meestal beheerd door een lokale IT technieker of door een betaalde professional.

### Device Selection for a Small Network

Net zoals grotere netwerken, hebben kleinere netwerken ook planning en design nodig om de aan de gebruiker zijn vereisten te voldoen. Planning zorgt er dat men nadenkt over alle vereisten, kost factoren, en ontwikkelingensmogelijkheden. Een van de grootse factoren om na te gaan is te kijken welke tussenapparaten er gebruikt zullen worden om het netwerk te ondersteunen.

Factoren waarmee rekening moet gehouden worden wanneer we netwerktoestellen selecteren:

- kost
- snelheid en type poorten/interfaces
- schaalbaarheid
- features en services van het operating system

### IP Addressing for a Small Network

Wanneer we een netwerk opstellen, is het best een IP addresseringsschema op te stellen en ook te gebruiken. Alle hosts en toestellen binnen een internetwerk moeten een uniek adres hebben. Toestellen die we betrekken in het IP addresseringsschema zijn:

- End user devices: Het aantal en type verbindingen (bekabeld, draadloos, extern toegankelijk)
- Servers en peripheral devices (printers, security camera's)
- Tussenapparaten zoals switches, access points.

Het is aangeraden om te plannen, documenteren en beheren van een IP addresseringsschema gebasseerd op het toesteltype. Het gebruik van een geplanned addresseringsschema maakt het gemakkelijker om een type toestel te identificeren en problemen te troubleshooten.

### Redundancy in a Small Network

Om een hoge betrouwbaarheid te garanderen is *redundantie* nodig in het netwerkdesign. Het helpt om single points of failure te elimineren.

Redundantie kan bereikt worden door dubbele apparaten te installeren. Ook kan het bereikt worden door dubbele netwerk links te voorzien op critische plaatsen.

<p align='center'><img src='src/redundancy.png' alt='' width='50%'></p>

### Traffic Management

- Het doel voor een goed netwerk design is de productiviteit van de werknemers te verhogen en het minimaliseren van *downtime*.
- De routers en switches in een klein netwerk zouden best geconfigureerd worden om real-time verkeer, zoals voice en video, te ondersteunen. 
- Priority queuing heeft voor wachtrijen. De wachtrij met hoge prioriteit wordt altijd als eerste geleegd.

<p align='center'><img src='src/traffic_management_priority_queueing.png' alt='' width='50%'></p>

## Small Network Applications and Protocols

### Common Applications

Nadat het netwerk is opgezet zijn enkele applicaties en protocollen nodig om te kunnen functioneren.

Er zijn twee soorten programma's of processen die toegang to het netwerk geven:

- **Network Applications**: Applicaties die de applicatielaagprotocollen implementeren en direct kunnen communiceren met de lagere lagen of de protocol stack.
- **Application Layer Services**: Applicaties die niet op de hoogte van het netwerk zijn. De applicaties die een interface hebben met het netwerk en de gegevens klaarmaken voor een transfer.