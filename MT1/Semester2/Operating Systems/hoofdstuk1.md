# Operating Systems : Hoofdstuk 1 - Besturingssystemen

>[!WARNING]
>**Een besturingssysteem** _(Operating System = OS)_ is een programma dat het mogelijk maakt de hardware van een computer te gebruiken. 

Een gebruiker geeft geen instructies aan de hardware, maar aan het besturingssysteem. Een besturingssysteem geeft de hardware de opdracht de gewenste taken uit te voeren. 

### Taken van een besturingssysteem

- Programma's de mogelijkheid geven informatie op te slaan en terug te herhalen
- Programma's afschermen van specifieke hardware zaken
- De gegevensstroom door de componenten van de computer regelen
- Programma's in staat stellen te werken zonder door andere programma's te worden onderbroken
- Onafhankelijke programma's de gelegenheid geven, tijdelijk samen te werken en informatie gemeenschappelijk te gebruiken.
- Reageren op fouten of aanvragen van de gebruiker
- Een tijdsplanning maken voor programma's die resources willen gebruiken

### Enkele voorbeelden

<table>
<thead>
<td></td>
<td>

Windows

</td>
<td>

Apple

</td>
<td>

Andere

</td>
<tbody>
<tr>
<td>

x86 / x64 <br>
laptop/desktop</td>

<td>

Windows 10 <br>
Windows 11 <br>
Windows Server 2022

</td>
<td>

MacOS 14 <br>
Sonoma

</td>
<td>

Fedora 39 <br>
Ubuntu 22/04 LTS <br>
AlmaLinux 9 [^1] <br>
...

</td>
</tr>
<tr>
<td>Mobile devices</td>
<td>

Windows 10 Mobile <br>
(end of support)

</td>
<td>

IOS 17 <br>
iPadOS 17

</td>
<td>

Android 14 <br>
Plasma Mobile <br>
Ubuntu Touch <br>
...

</td>
</tr>
<tr>
<td>ARM devices</td>
<td>

Windows 11 on 1ARM

</td>
<td>

MacOS 14 <br>
Sonoma
(for Apple silicon)

</td>
<td>

 Rapsberry Pi OS <br>
 Fedora 39 ARM <br>
 Ubuntu 22 Server ARM <br>
 AlmaLinux 9 ARM <br>
 ...

</td>
</tr>
</tbody>
</thead>
</table>

[^1]: AlmaLinux: een van de opvolgers van CentOS

## Soorten besturingssystemen

We kunnen een onderscheid maken tussen:

- _Single-tasking systemen_: 1 taak kan tegelijkertijd actief zijn
- _Multitasking, single-user systemen_: meerdere taken kunnen tegelijkertijd actief zijn
- _Mulit-user systemen_: meerdere gebruikers kunnen gelijktijdig het systeem gebruiken

### Single-tasking besturingssystemen

>[!Warning]
>Bij _Single-tasking_ besturingssystemen is er maar één gebruiker die maar één applicatie tegelijk draait. 

Een bekend voorbeeld hiervan is MS-DOS, de (niet-grafische) voorloper van Windows

### Multitasking single user besturingssystemen

>[!warning]
>De meeste besturingssystemen zijn multitasking, meerder programma's kunne tegelijkertijd geopend en uitgevoerd worden.

Deze systemen staan nog steeds maar één gebruiker tegelijkertijd toe. Maar deze kan wel verschillende taken simultaan uitvoeren. 

Aangezien bij deze systemen een gebruiker verschillende taken tegelijkertijd uitvoerd, worden bepaalde functies van het besturingssysteem (zoals geheugenbeheer) ingewikkelder.

### Multi-User besturingssystemen

>[!warning]
>Multi-user systemen, ook wel multiprogrammering systemen, moeten niet alleen alle gebruikers bijhouden, er moet ook voorkomen worden dat deze elkaar hinderen of in het werk van anderen rondneuzen.

Hierdoor worden bepaalde functies van een besturingssysteem nog complexer, want er kunnen meerdere gebruikers tegelijkertijd actief zijn op het systeem, en elke gebruiker kan ook meerdere taken tegelijkertijd uitvoeren.

## Concepten van besturingssystemen

### verschillende lagen

Veel besturingssystemen implementeren de interface tussen gebruiker en computer als een reeks stappen of lagen. 

1. De bovenste laag of _**shell**_ (of command interpreter) is de laag waarin de functies vastgelegd zijn. De gebruiker communiceert met deze laag. Deze laag bestaat uit routines van het besturingssysteem die ontworpen zijn om op opdrachten van de gebruiker te reageren.

2. Vaak vraagt een opdracht van een gebruiker veel van het besturingssysteem en zijn deze te ingewikkelijd. Deze worden vaak niet door de shell uitgevoerd. De _**utilities**_ laag bevat vele routines die deze zaken behandeld.

3. De onderste laag is de _**kern of kernel**_. Dit is het hart van het besturingssysteem. Deze laag bevat de routines die het vaaks gebruikt worden en waar het meest op aankomt.

Wanneer een gebruiker een opdracht geeft, verzorgen de utitilies het grootste deel van de controle en voorbereiding voor de uitvoering die nodig is.

### Programma's / taken

Er bestaan verschillende soorten multi-user-computers, afhankelijk van de soorten programma's die ze aankunne:

- **Interactieve programma's**: 