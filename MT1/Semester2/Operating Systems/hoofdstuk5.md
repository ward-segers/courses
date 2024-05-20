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

