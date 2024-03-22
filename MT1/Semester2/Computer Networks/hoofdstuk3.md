# Computer Networks - Hoofdstuk 3 - Protocols and Models

## The rules

Netwerken kunnen verschillen in grootte en compleciteit. Daarom is het niet genoeg om een verbinding te hebben. De apparaten moeten ook afstemmen hoe ze communiceren.

Voor elke succesvolle communicatie bestaan er volgende onderdelen:
- Er is een afzender (_source_)
- Er is een bestemming (_receiver/destination_)
- Er is een kanaal of medium (_channel/media_) dat voor een pad voor de communicatie zorgt

Alle communicatie worden beheerd door protocollen.
Deze protocollen zijn de regels die de verschillende communicaties zullen volgen.
De verschillende regels hangen af van de verschillende protocollen.

### Rule Establishement

- Individueen moeten de vastgestelde regels of afspraken gebruiken om de communicatie te sturen.
- **Protocollen** moeten rekening houden met de volgende vereisten:
    - Een geïdentificeerde verzender en ontvanger
    - Gemeenschappelijke taal en grammatica
    - Snelheid en timing van de levering
    - Bevestiging van de vereisten

### Netwerk Protocol Requirements

Veel gebruikte computer protocollen moeten overeenkomen en de volgende vereisten bevatten:
- Codering van berichten
- Berichtopmaak en -inkapseling
- Berichtgrootte
- Timing van de berichten
- Opties voor het afleveren van de berichten

### Message Encoding

>[!warning]
>**Encoding** is het proces van het converteren van informatie naar een aanvaardbare vorm van transmissie

>[!warning]
>**Decoding** is de inverse van encoding waarbij de informatie geïnterpreteerd wordt.

Encoding tussen hosts moet in een toepasbaar formaat zijn voor het medium.
- Berichten die verzonden worden over een netwerk worden geconverteerd naar bits.
- Deze bits worden gecodeerd naar een patroon van licht, geluid of electrische impulsen.
- De bestemmingshost moet deze signalen decoderen om het bericht te kunnen interpreteren.


<p align='center'><img src='src/encoding_decoding.png'  alt='Encoding vs Decoding' width='100%'></p>

### Message Formatting and Encapsulation

- Wanneer een bericht verzonden is moet dit een speciaal formaat of structuur hanteren.
- Het formaat van het bericht hangt af van het type bericht en het medium dat gebruikt wordt om het bericht te verzenden.

### Message Size

- Wanneer een groot bericht verzonden wordt van de ene host naar de andere over een netwerk, is het noodzakelijk _het bericht op te splitsen in kleiner stukken_
- De regels die de grootte van deze stukken of frames beheren zijn zeer strikt en worden overheen het hele netwerk gecommuniceerd. Ze kunnen tevens verschillen naar gelang het kanaal dat gebruikt wordt. Frames die te groot of te klein zijn worden niet bezorgd bij de ontvanger.
- Bij de ontvangende host worden de frames terug samengesteld in het orginele bericht.

### Message Timing

Message time bestaat uit:

- **Flow control**: beheerd de snelheid van de gegevensoverdracht en bepaalt de hoe hoeveelheid data die verzonden kan worden aan welke snelheid.
- **Response Timeout**: beheerd hoelang een apparaat wacht wanneer het geen antwoord ontvangt van de bestemming.
- **Access method**: beheerd wanneer iemand een bericht kan sturen.
    - Er kunnen zijn verschillende regels die problemen beheren zoals "collisions". <br> <br>
    >[!important]
    >**Collisions** is het fenomeen wanneer meer dan één apparaat op hetzelfde moment berichten stuurt en deze berichten corrupt worden
    - Sommige protocollen zijn proactief en properen dus "collisions" te vermijden, terwijl andere protocollen corrigeren werken en een recovery methode bevatten nadat de collision voorkomt.

### Message Delivery Options

Message Delivery Options kan een van volgende zijn:

- **Unicast**: one to one communication
- **Multicast**: one to many communication (meestal niet alle)
- **Broadcast**: one to all communication

>[!note]
>Broadcast worden gebruikt in IPv4 netwerken, maar zijn geen optie in IPv6. 

<br> 

<p align='center'><img src='src/message_delivery_options.png' alt='Message Delivery Options' width='100%'></p>

**_Deze mogelijkheden worden soms ook als volgens voorgesteld_**

<p align='center'><img src='src/node_message_delivery_options.png' alt='Message Delivery Options node representation' width='100%'></p>

## Protocols

### Netwerk Protocol Overview

Netwerk protocollen definiëren een aantal regels:
- Kunnen geimplementeerd worden op zowel hardware als software, of beide
- Protocollen hebben hun eigen functie, formaat en regels

<table>
<thead>
<tr>
<th>Protocol Type</th>
<th>Beschrijving</th>
</tr>
</thead>
<tbody>
<tr>
<td>Netwerk Communications</td>
<td>Schakel twee of meerder apparaten in om met elkaar over een of meerdere netwerken te communiceren</td>
</tr>
<tr>
<td>Netwerk Security</td>
<td>Gegevens beveiligen om authenticatie, gegevensintegriteit en gegevenscodering te voorzien</td>
</tr>
<tr>
<td>Routing</td>
<td>Schakel routers in om route informatie uit te wisselen, pad informatie te vergelijken, en het beste pad te selecteren</td>
</tr>
<tr>
<td>Service Discovery</td>
<td>Gebruikt voor automatisch detectering van toestellen of diensten</td>
</tr>
</tbody>
</table>

