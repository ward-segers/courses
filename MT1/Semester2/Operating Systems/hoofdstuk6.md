# Operating Systems : Hoofdstuk 6 - Threads

## Wat zijn threads?

### Processen: 2 concepten

Tot nu toe hebben we processen steeds behandeld als een onscheidbaar deeltje in het besturingssysteem. Een proces kan verschillende toestanden hebben via de scheduler, heeft toegang tot bestanden en rekenkracht, kan prioriteiten krijgen, ...

Als we dieper gaan kijken naar wat een proces nu precies is, zien we dat het idee van een proces eigenlijk hebben gebruikt voor twee aparte concepten: eigendom van bronnen en het uivoeren van de instructies.
- Eigendom van bronnen: Het besturingssysteem kent bronnen zoals bestanden, geheugenruimten, apparaten, ... toe aan een proces. Het besturingssysteem zorgt er ook voor dat processen elkaars bronnen niet zomaar kunnen beïnvloeden.
- Het uitvoeren van de instructies: de fetch-execute cyclus haalt continu instructies op en voert deze uit. Hiervoor wordt er gebruik gemaakt van een Program Counter om de volgende uit te voeren instructies bij te houden, registers en stack om informatie bij te houden. 

Deze twee concepten staan eigenlijk los van elkaar. Bv. of een proces nu actief is op de CPU of geblokkeerd is: bronnen zoals bestanden blijven toegewezen aan het proces.

### Proces: eigendom bronnen

- Elk proces krijgt controle of eigenaarschap over bronnen (locking)
- Afgeschermd van andere processen door het besturingssysteem
- Voorbeelden van bronnen:
    - Address space (geheugen voor procesbeeld: instructies, data,...)
    - Geheugen (in RAM, HDD, SSD,...)
    - Bestanden
    - Apparaten (CPU,...)

### Proces: uitvoering programma

- Uitvoeren van instructies
    - Via fetch-execute cyclus
- Bijhouden van registers en stack
    - bv. program counter (PC)
- Scheduling
    - Bijhouden toestand/staat
    - Is proces actief/geblokkeerd/...?

### Processen vs. threads

Een proces zal verschillende taken uitvoeren via de fetch-execute cyclus. <br>
Het uitvoeren van instructies binnen een proces gebeurt in een thread. Daarom wordt in de context van uitvoering ook vaak over threads gesproken, terwijl we voor eigendom van bronnen meestal spreken over processen of taken.

Een proces kan meerdere threads bevatten. Een thread is de kleinste eenheid van geprogrammeerde instructies die onafhankelijk van elkaar kunnen worden beheerd door een scheduler, dus met andere woorden: binnen één proces kunnen gelijkertijd meerdere threads actief zijn.

Wanneer een proces bestaat uit één enkele thread voor de uitvoering, spreken we van een **single-threaded proces**.

Wanneer een proces echter zijn werk verdeeld over meerdere threads, spreken we van een **multi-threaded proces**. Deze threads kunnen parallel uitgevoerd worden door het systeem, wat vooral interessant is voor systemen met meerdere processoren en/of multi-core CPU's.

Threads kunnen zich net zoals processen in verschillende toestanden bevinden. (geblokkeerd, actief,...) Het wisselen tussen threads op de CPU loopt bovendien analoog aan het wisselen tussen processen: er wordt een context switch voor threads uitgevoerd. (dit is wel "goedkoper" voor threads)

<p align='center'><img src='src/threads_vs_processen.png' alt='' width='50%'></p>


### Opbouw threads

Net zoals een computer de CPU, geheugen, hardware,... deelt met één of meerdere processen, deelt een proces de instructies, data, toegewezen bronnen,... met één of meerdere threads. Elke thread heeft dus toegang tot alle bronnen toegewezen aan dat proces. (bv. bestand toegewezen aan proces kan ook door thread gelezen worden)

Daarnaast heeft ook elke thread zijn eigen registers (bv. Program Counter), stack, toestand, thread id,... zodat het onafhankelijk van andere threads binnen het proces instructies kan uitvoeren.

Er is geen afscherming tussen threads binnen een proces. Threads binnen eenzelfde proces kunnen elkaars gegevens lezen, schrijven, verwijderen,... zonder beperking. Dit is een groot verschil met processen waar het besturingssysteem de processen van elkaar afschermt.

Threads hebben net als processen een toestand:
- actief
- gereed
- inactief
- ...

Een thread kan dus bv. gedeactiveerd worden en een andere thread van dat proces geactiveerd. Dit gebeurd net als bij processen met een context switch. De context voor een thread is de inhoud van diens register (inclusief de Program Counter) en de stack. Threads kunnen net als processen gesynchroniseerd worden. Aangezien zijn minder data bevatten (instructies, data, toegang tot bronnen zijn gedeeld) is deze context switch dus goedkoper.

>[!caution]
>De instructies zelf (opgeslagen in de adress space in het geheugen) behoren tot het proces

>[!caution]
>Het uitvoeren van de instructies is de verantwoordelijk van de threads. Met behulp van een eigen Program Counter kunnen ze de juiste instructie van het proces lezen om deze uit te voeren. (en nadien de volgende waarde voor de PC in te laden)