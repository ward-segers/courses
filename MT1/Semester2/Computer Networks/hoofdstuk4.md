# Computer Networks - Hoofdstuk 4 - Physical Layer

## Purpose of the Physical Layer

### The Physical Connection

- Alvorens om het even welke netwerk communicatie kan plaatsvinden, moet er een fysieke connectie met het lokaal netwerk opgezet zijn.
- Deze connectie kan zowel draadloos als bekabeld zijn (naargelang de opzet van het netwerk)
- Een Network Interface Card (NIC) verbind een toestel met een netwerk.
- Sommige toestellen hebben één of meerdere NIC's. (draadloos en/of bekabeld)
- Niet alle fysieke connectie hebben dezelfde performantie.

### The Physical Layer

- Vervoert bits over de netwerk medium
- Aanvaard een volledig frame van de Data Link Laag en codeert het als een serie van signale die verzonden worden naar de locale media. (laaste stap in het inkapseling proces)
- Het volgende toestel op de route naar de bestemming ontvangt de bits en ontkapselt het frame. Hierna beslist het toestel wat ermee moet gebeuren.

## Physical Layer Characteristics

### Physical Layer Standards

<p align='center'><img src='src/physical_layer_standards.png' alt='Physical Layer Standards' width='50%'></p>

De normen van de Fysieke Laag richten zich op 3 functionele gebieden:

- **Fysiek componenten (physical components)**: Dit zijn hardware toestellen, media en andere connectoren die signalen overbrengen dat de bits vertegenwoordigen.
    - Hardware onderdelen zoals NIC's, interfaces en connectoren, kabel materialen en designs, zijn allemaal beschreven in de normen die horen bij de fysieke laag.
- **Encoding**: Zet de stroom van bits om in een formaat dat herkend wordt door het volgende toestel op de netwerkroute.
    - Voorziet voorspelbare patronen die kunnen herkend worden door het volgende toestel.
- **Signaling**: De manier waarop de bitwaarden voorgesteld worden in het medium.
    - De signalingmethode kan variëren naargelang het type medium dat gebruikt wordt.

### Bandwidth

> **Bandwidth of bandbreedte** is de capaciteit waarmee een medium gegevens kan vervoeren.

Digitale bandbreedte berekend de hoeveelheid data dat van de ene plaats naar de andere kan stromen binnen een gespecifieerd tijdspanne.

Dit kan beïnvloed worden door de eigenschappen van het medium, technologiëen en de fysica.

<table>
    <thead>
        <th>Unit of Bandwidth</th>
        <th>Abbreviation</th>
        <th>Equivalence</th>
    </thead>
    <tbody>
        <tr>
            <td>Bits per second</td>
            <td>bps</td>
            <td>1 bps = fundamental unit of bandwidth</td>
        </tr>
        <tr>
            <td>Kilobits per second</td>
            <td>Kbps</td>
            <td>1 Kbps = 1 000 bps = 10<sup>3</sup> bps</td>
        </tr>
        <tr>
            <td>Megabits per second</td>
            <td>Mbps</td>
            <td>1 Mbps = 1 000 000 bps = 10<sup>6</sup> bps</td>
        </tr>
        <tr>
            <td>Gigabits per second</td>
            <td>Gbps</td>
            <td>1 Gbps = 1 000 000 000 bps = 10<sup>9</sup> bps</td>
        </tr>
        <tr>
            <td>Terabits per second</td>
            <td>Tbps</td>
            <td>1 Tbps = 1 000 000 000 000 bps = 10<sup>12</sup> bps</td>
        </tr>
    </tbody>
</table>

#### Bandwidth Terminology

- **Latency of latentie**: De hoeveelheid tijd, inclusief de vertraging, die gegevens nodig hebben om van het ene punt naar het andere te verplaatsen
- **Throughput of doorvoer**: Het gemeten aantal bits die verplaatsen over een medium gedurende een gegeven tijdspanne. (komt overeen met het resultaat van een speedtest)
- **Goodput**: De meting van bruikbare gegevens die in een bepaalde periode zijn overgedragen. 
    $$Goodput = {Throughput - traffic\text{ } overhead}$$

## Copper Cabling

## Characteristics of Copper Cabling

Koperen bekabeling is vandaag de dag de meest voorkomende vorm van kabels gebruikt in netwerken. 

*Voordelen*:
- goedkoop
- gemakkelijk te installeren
- lage weerstand tegen elektrische stroom

*Beperkingen*:
- Verzwakking - hoe langer elektrische signalen moeten reizen, hoe zwakker ze worden
- Het elektrische signaal is gevoelig voor storing van twee bronnen, die de gegevenssignalen kunnen vervormen en beschadigen (Electromagnetic Interference (EMI) and Radio Frequency Interference (RFI) and Crosstalk).

*Matigingen*:
- Strikte naleving van de kabellengtebeperkingen vermindert de demping
- Sommige soorten koperkabel beperken EMI en RFI door metalen afscherming en aarding te gebruiken.
- Sommige soorten koperkabel verminderen overspraak (Crosstalk) door tegengestelde aders van een circuitpaar in elkaar te draaien.

### Types of Copper Cabling

<p align='center'><img src='src/types_of_copper_cabling.png' alt='Types of copper cabling' width='75%'></p>

#### Unshielded Twisted Pair (UTP)

>*UTP* is het meest voorkomende netwerk medium

- Verbindingen zijn RJ-45 connectoren
- Verbind hosts met tussenliggende netwerkapparaten

*Eigenschappen van UTP*: 

1. Het omhulsel beschermd de koperkabel van fysieke schade
2. Getwiste paren beschermen het signaal tegen storing.
3. De kleurgecodeerde plastic isolatie isoleert de draden van elkaar en identificeert elk paar.

<p align='center'><img src='src/utp.png' alt='UTP' width='50%'></p>

#### Shielded Twisted Pair (STP)

- Betere ruis beveilging dan UTP
- Duurder dan UTP
- Moeilijker te installeren dan UTP
- Verbindingen zijn RJ-45 connectoren
- Verbind hosts met tussenliggende netwerkapparaten

*Eigenschappen van STP*: 

1. Het omhulsel beschermd de koperkabel van fysieke schade
2. Gevlochten of folieschild biedt EMI/RFI-bescherming
3. Folieafscherming voor elk dradenpaar biedt EMI/RFI-bescherming
4. De kleurgecodeerde plastic isolatie isoleert de draden van elkaar en identificeert elk paar.

<p align='center'><img src='src/stp.png' alt='UTP' width='50%'></p>

#### Coaxial cable

*Gebruikt voor:*
- Draadloze installaties (verbind antennes met draadloze toestellen)
- Kabel internet installaties  

*Bestaat uit het volgende:*
1. Omhulsel dat fysieke schade beperkt
2. Een gevlochten koperen vlecht, of metaalfolie, fungeert als de tweede draad in het circuit en als afscherming voor de binnenste geleider.
3. Een laag flexibele isolatie
4. Een koperen geleider wordt gebruikt om de elektronische signalen door te geven.

<p align='center'><img src='src/coax.png' alt='Coaxial cable' width='50%'></p>

Er zijn verschillende soorten connectoren die gebruikt worden met coax kabels:

<p align='center'><img src='src/coax_connectors.png' alt='Coaxial cable connectors' width='50%'></p>