# Operating Systems : Hoofdstuk 5 - File Systems

## Persistente opslag

Processen halen hun instructies en data uit het RAM. Naast het RAM hebben processen ook nood aan **persistente** opslag.

- Data in het RAM gaan verloren na het afsluiten van het proces. Wil het proces data bewaren, dan moet dit op een persistent opslagmedium worden bewaard.
- RAM is beperkt in capaciteit. Persistente opslag bied een grotere capaciteit aan.
- Processen werken in hun eigen (virtuele) adresruimte en zijn afgescherm van elkaar. Via een persistent opslagmedium kunne processen data onderling delen.

### Hard disk drive (HDD)

>**Een hard disk drive (HDD)** is een magnetisch opslagmedium dat een grote opslagcapaciteit biedt voor een lage prijs.

Doordat een HDD werkt met draaiende schijven, is er telkens een kleine vertraging (= **seek time**) wanneer de leeskop zich moet positioneren boven de gevraagde data.

### Solid-state drive (SSD)

> **Een solid-state drive (SSD)** ise een performanter maar duurder alternatief voor een HDD. Een SSD heeft geen draaiende delen, de opslage gebeurt door circuits (IC's), waardoor de schijf robuuster is en geen seek time nodig heeft.

>[!important]
>Hogere prijs/GB dan een HDD

### CD/DVD

**CD's en DVD's** zijnoptische opslagmedia. Ze hebben een beperkte capaciteit en performantie en zijn bovendien vaak read-only.

Ze worden vooral gebruikt als distributiemedia of backups.

### USB stick

**USB sticks** maken gebruik van IC's. Het zijn externe opslagmedia die worden aangesloten via USB, waardoor ze een beperkte capaciteit en performantie hebben.

## Files

Een fysiek opslagmedium verdeelt zijn opslagruimte in **blokken**, vaak met een complexe layout.

>**Een file (bestand)** is een abstracte eenheid die data uit één of meerdere blokken groepeert en voorstelt als één geheel.

Het beheer van files en toekennen van blokken behoort tot de taken van een **file system**.

Een bestandssysteem verbergt de complexiteit van de fysieke opslag voor de gebruikers van het besturingssysteem.

### Voorstelling

Naar gebruikers toe wordt een file voorgesteld als een opeenvolging van bytes.

Dit is echter een abstractie: in realiteit kunnen deze bytes verspreid zijn over het opslagmedium.

### Eigenschappen

- Een naam, eventueel met extensie. Sommige besturingssystemen hechten veel belang aan de extensie, bij anderen is dit louter een conventie.
- Een huidige en maximale grootte
- Toegangsrechten
- De datum van aanmaak en laatste wijziging
- Een verwijzing naar de blokken waar de bytes van het bestand opgeslagen zijn.

Welke eigenschappen worden opgeslagen hangt af van besturingssysteem.

### Soorten

Op UNIX systemen worden heel wat zaken voorgesteld als files. Er zijn dus verschillende soorten bestanden:

- Gewone bestanden bevatten data
- **Directories**: bevatten andere bestanden of mappen. (zorgen voor de hiërarchische structuur in het bestandssysteem)
- **Links**: maken een bestand op verschillende plaatsen in het bestandssysteem zichtbaar
- **Block of character special files**: geven toegang aan de hardwer (bv. printers of `/dev/null`)
- **Sockets**: zorgen voor de netwerkcommunicatie
- **Pipes** (FIFO): verbinden de output van een proces met de input van een ander proces.

In de eerste kolom van deze uitvoer kunnen we het type bestand zien.

```bash
ward@ward:~s$ ls -l
total 22172
drwxrwxrwx 1 ward ward     4096 Jun 24  2023 '3D Objects'
drwxrwxrwx 1 ward ward     4096 Aug 10  2023  AppData
lrwxrwxrwx 1 ward ward       40 Aug 10  2023 'Application Data' -> '/mnt/c/Users/Ward Segers/AppData/Roaming'
-rwxrwxrwx 1 ward ward 15990784 May 19 21:24  NTUSER.DAT
-rwxrwxrwx 1 ward ward    65536 Nov  7  2023  NTUSER.DAT{bb781bed-3774-11ee-bef9-f8c5195da7f1}.TM.blf
```

De type bestanden kunnen we ook terugvinden in de MAN page van het commando `ls`

```bash
LS(1)                                             User Commands                                            LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       -b, --escape
              print C-style escapes for nongraphic characters

       --block-size=SIZE
              with -l, scale sizes by SIZE when printing them; e.g., '--block-size=M'; see SIZE format below

       -B, --ignore-backups
              do not list implied entries ending with ~

       -c     with -lt: sort by, and show, ctime (time of last modification of file  status  information);  with
              -l: show ctime and sort by name; otherwise: sort by ctime, newest first

       -C     list entries by columns

       --color[=WHEN]
              colorize  the output; WHEN can be 'always' (default if omitted), 'auto', or 'never'; more info be‐
              low

       -d, --directory
              list directories themselves, not their contents

       -D, --dired
              generate output designed for Emacs' dired mode

       -f     do not sort, enable -aU, disable -ls --color

       -F, --classify
 Manual page ls(1) line 24/225 20% (press h for help or q to quit)
```

De output van `ls -F` toont het type via volgende suffix

<table>
    <thead>
        <th>suffix</th>
        <th>type</th>
    </thead>
    <tbody>
        <tr>
            <td>/</td>
            <td>map</td>
        </tr>
        <tr>
            <td>*</td>
            <td>uitvoerbaar bestand</td>
        </tr>
        <tr>
            <td>@</td>
            <td>link</td>
        </tr>
        <tr>
            <td>=</td>
            <td>socket</td>
        </tr>
        <tr>
            <td>|</td>
            <td>named pipe</td>
        </tr>
    </tbody>
</table>

```bash
ward@ward:~s$ ls -F
'3D Objects'/
 AppData/
'Application Data'@
 NTUSER.DAT*
 NTUSER.DAT{bb781bed-3774-11ee-bef9-f8c5195da7f1}.TM.blf*
```

### Bytes uitlezen

Bestanden kunnen op twee manieren toegang geven tot hun bytes:

- Een bestand met **sequentiële toegang** dient in volgorde uitgelezen te worden. (byte 100 kan niet gelezen worden als byte 1-99 niet gelezen zijn)
- Een bestand met willekeurige toegang (**random access**) kan in eender welke volgorde uitgelezen worden.

## Directories

> **Een directory** (map) groepeert files en kan zelf ook andere directories bevatten. Dit zorgt voor een hiërarchische structuur in het bestandssysteem.

De implementatie van directories is opnieuw de taak van het bestandssysteem. 

### Hiërarchie

Het voorbeeld hieronder toont een hiërarchische structuur waarbij de **root directory** (de hoofdmap) van het bestandssysteem één map per gebruiker bevat. Elke gebruikersmap bevat dan weer andere bestanden en mappen.

<p align='center'><img src='src/dir_hierarchy.png' alt='' width='50%'></p>

### Padnamen

Het **absolute pad** naar een bestand of map start bij de root directory en beschrijft de weg naar dit bestand of naar deze map. Op Linux en Max wordt een slash (/) gebruikt als scheidingsteken in een pad. Op Windows is dit een backslash (\)

```bash
/home/hogent/os
C:\Users\hogent\os
```

Bij Windows start een absoluut pad telkens met een letter die gekoppeld is aan een bestandssysteem. Op Linux en Max worden alle bestadsystemen tot één virtueel bestandsysteem samengebracht en gebruiken we geen letters.

Een relatief pad start vanuit een bestaande directory en kan de speciale verwijzingen **.** (huidige directory) en **..** (parent directory) gebruiken

```bash
../hogent/os
..\hogent\os
```

## Mappenstructuur

### Windows

- I/O-apparaten worden gekoppeld via apparte **schijfletters** (C: , D: ...)
    - Schijfopslag, netwerkopslag, DVD/CD, USB-sticks,...
- **Program files**: uitvoerbare bestanden en applicaties
- **Windows\System32**: systeembestanden
- **User\<gebruikersnaam>**: home directories per gebruiker
- **User\Appdata**: configuratiebestanden (verborgen)
- Algemeen beheer van apparaten gebeurd via Device Manager
    - Apparaten die gelinkt moeten worden binnen folderstructuur worden een schijfletter toegewezen
- Opstartbestanden staan op een aparte bootpartitie (standaard zonder schijfletter)

### Linux

In tegenstelling tot de verschillende stationletters op Windows valt op Linux/Unix elk bestand onder de root-filestructuur. 

- `/home/<gebruiker>`: gebruikersbestanden
- `/dev`: apparaten
- `/mnt` of `/media`: I/O-apparaten 
- `/boot`: opstartbestanden
- `/etc`: configuratiebestanden
- `/(s)bin` en `/usr/(s)bin` of `/opt`: uitvoerbare bestanden
- `/var`: variabele bestanden (bv. logs)

### macOS

Wat op Windows de C-schijf is, heet op macOS de Main Disk

macOS heeft enkele standaardmappen:
- **Applications**: bevat de geïnstalleerde applicaties op de mac
- **Library**: bevat fonts en andere bestanden gebruikt door applicaties. Applicaties plaatsen hierin bestanden die ze nodig hebben om te functioneren. (gedeeld over alle gebruikers)
- **System**: hierin zit het macOS besturingssysteem (kan je niets in wijzigen)
- **Users**: bevat de home directories per gebruiker en een shared map met gedeelde bestanden tussen alle gebruikers.

Wanneer we het `ls -l` uitvoeren op de root van het file systeem merken we een gelijkaardige structuur als op Linux. MacOS verbergt deze mappen voor de eindgebruiker, maar ze zijn wel degelijk aanwezig.

We zien ook een extra map 'Volumes', die we niet zagen op de Main Disk. Deze map bevat alle gekoppelde volumes (bv. Main Disk, externe harde schijf).

<p align='center'><img src='src/macOS_ls_home.png' alt='' width='50%'></p>

## File System

> **Een file system** (bestandssysteem) is een onderdeel van een besturingssysteem. File systems beheren de fysieke opslagruimte en wijzen deze toe aan files en directories. File systems implementeren dus files en directories

De meeste besturingssystemen ondersteunen verschillende file sytems. Er kunnen meerder file systems tegelijkertijd actief zijn.

### Implementatie van files

De implementatie van files kan op verschillende manier gebeuren:

- Contiguous storage
- Linked lists
- File allocation table (FAT)
- Index nodes (inodes)

#### Contiguous storage

Bij **contiguous storage** (samenhangende opslag) wordt elk bestand in één of meer *aansluitende blokken* opgeslagen.

Dit is een eenvoudige methode met een *goede leessnelheid* en met ondersteuning voor *random access*.

Het heeft echter ook de volgende nadelen:
- Als een bestand groeit, dan moet het mogelijk verplaatst worden naar een grotere vrije ruimte.
- Als een bestand verwijderd wordt, en de vrije ruimte wordt ingenomen door een kleiner bestand dan onstaat er **fragmentatie** (*meer en meer kleine ruimtes die niet opgevuld geraken*) 

>Een systeem dat deze techniek gebruikt moet vaak gedefragmenteerd worden om de kleinere vrije ruimtes terug samen te voegen.

Dit is ideal voor read-only of write-once media, zoals een CD of DVD.

<p align='center'><img src='src/contiguous_storage_example.png' alt='' width='50%'></p>

In bovenstaand voorbeeld worden uit (a) bestanden D en F verwijderd, (b) toont de opslag na het verwijderen.

#### Linked lists

Bij **linked lists** (gelinkte lijsten) hoeven de datablokken van een bestand niet aan te sluiten. Elk blok bevat namelijk een **verwijzing** (link) naar het volgende blok, dat zich eender waar mag bevinden.

- lost probleem fragementatie op
- **slechte performantie**, (door de datablokken die verspreid staan, daalt de leesperformantie)
- ondersteund geen random access (blokken moeten in volgorde uitgelezen worden)

<p align='center'><img src='src/linked_lists.png' alt='' width='50%'></p>

#### File allocation table (FAT)

Een **file allocation table (FAT)** (toewijzingstabel) is een verbetering van de linked list techniek. De datablokken van elk bestand vormen nog steeds een linked list, maar alle verwijzingen tussen de blokken worden samengebracht in een tabel.

- kan snel een lijst vinden doordat de tabel in het RAM bewaard is.
- verhoogt leessnelheid
- maakt random access mogelijk
- FAT kan een hoog RAM-verbruik hebben

<p align='center'><img src='src/FAT.png' alt='' width='25%'></p>

#### Index nodes (inodes)

Een **index node (inode)** is een datastructuur die zowel de metadata van een bestand als verwijzingen naar de datablokken bevat. Een bestandssysteem dat inodes gebruikt, hoeft enkel de inodes van de geopende bestanden in het RAM te bewaren.

Deze techniek combineert dus een **goede leessnelheid** met een **beperkt RAM-verbruik**

<p align='center'><img src='src/inodes.png' alt='' width='50%'></p>

### Implementatie van directories

Een directory kan opgeslagen worden in een bestand. Dit bestand bevat dan een **directory entry** voor elke file of subdirectory.

Elk file system kiest zelf welke informatie er wordt opgeslagen in een directory