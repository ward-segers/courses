# Computer Networks : Hoofdstuk 14 - Transport Layer

## Transportation of Data

### Role of the Transport Layer

De transportlaag is:

- Verantwoordelijk voor de logische communicatie tussen applicaties die draaien op verschillende hosts.
- De link tussen de applicatielaag en de lagere lagen die Verantwoordelijk zijn voor de netwerktransmitie.

<p align='center'><img src='src/transport_layer.png' alt='' width='50%'></p>

### Transport Layer Reponsibilities

De transportlaag heeft de volgende verantwoordelijkheden: 

- tracking of individual conversations
- Segmenting data and reassembling segments
- Header informatie toevoegen
- Identify, separate, and manage multiple conversations
- Gebruikt segmentation en multiplexing om verschillende communicatiegesprekken op hetzelfde netwerk te kunnen afwisselen.

### Transport Layer Protocols

- IP specifieert niet hoe de levering of vervoer van de pakketten plaatsvinden.
- De transportlaag protocollen specifiëren hoe we berichten overschrijven tussen hosts. Deze protocollen zijn ook verantwoordelijk voor het beheren van de betrouwbaarheidsvereisten van een gesprek.
- De transportlaag bevat het **TCP (Transmission Control Protocol)** en het **UDP (User Datagram Protocol)**

<p align='center'><img src='src/transport_layer_protocols.png' alt='' width='50%'></p>

### Transmission Control Protocol (TCP)

**TCP** bezorgt betrouwbaarheid en flow control. Basis TCP operaties:

- Nummeren en tracken van data segmenten die uitgezonden zijn naar een specifieke host vanuit een specifieke applicatie.
- Erkennen van ontvangen data.
- Opnieuw uitsturen na een bepaalde tijd, van niet-erkende data.
- Gegevens die mogelijks in een verkeerde volgorde ontvangen zijn, ordennen.
- Data met een efficiënte ratio, aanvaard door de ontvanger, versturen.

### User Datagram Protocol (UDP)

**UDP** biedt standaard functies voor het leveren van datagrams tussen de geschikte applicaties met  weinig overhead en datacontrole.

- UDP is een verbindingsloos protocol
- UDP is gekend als een *best-effort delivery* protocol, omdat er geen erkenning als de data al dan niet ontvangen is op de bestemming.

### The Right Transport Layer Protocol for the Right Application

UDP wordt 