# DATABASES : Hoofdstuk 6 - Normalistatie

## Inleiding

> **Normalistatie** is in essentie een proces voor het evalueren en corrigeren van de structuur van tabellen om redundantie te elimineren.

Door redundantie te elimeren en de stuctuur van de databank te optimaliseren, worden anomalieën voorkomen, wordt het risico op fouten verminderden is de databank beter schaalbaar en gemakkelijker te onderhouden.

Normalistatie werkt via een reeks stappen (= **normaalvormen**)
- nulde normaalvorm (0NF)
- eerste normaalvorm (1NF)
- tweede normaalvorm (2NF)
- derde normaalvorm (3NF)

Structureel gezien is 3NF beter dan 2NF en 2NF beter dan 1NF,...

>[!important]
> Voor de meeste doeleinden is normalistatie tot 3NF voldoende.

Normalistatie tot de hoogste vorm (5NF) is niet altijd wenselijk.

Over het algemeen geldt hoe hoger de normaalvorm, hoe meer JOIN operaties nodig zijn om de gewenste uitvoer te registreren.

>[!important]
> Het databankmanagementsysteem heeft ook meer middelen nodig om te reageren op de vraag van eindgebruikers wanneer er meer JOIN operaties zijn. Een goed databankontwerp dient ook rekening te houden met de vraag van de gebruikers naar snelle prestaties.

## Het nut van normalistatie

- verminderen van redundantie en anomalieën door structureren gegevens op een consistente, efficiënte en georganiseerde manier
- verbeteren prestaties van de databank
- eenvoudiger te beheren en onderhouden

**Voorbeeld**

<table>
    <thead>
        <tr>
            <th>wncode</th>
            <th>werknemernaam</th>
            <th>functie</th>
            <th>loon</th>
            <th>departementcode</th>
            <th>departementadres</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>JJA60</td>
            <td>Jan Janssens</td>
            <td>manager</td>
            <td>6000</td>
            <td>HR</td>
            <td>Vredestraat 7, Brugge</td>
        </tr>
        <tr>
            <td>SDM70</td>
            <td>Stijn De Smet</td>
            <td>assistent</td>
            <td>3500</td>
            <td>IT</td>
            <td>Vogelmarkt 9, Gent</td>
        </tr>
        <tr>
            <td>EME75</td>
            <td>Eva Martens</td>
            <td>verantwoordelijke</td>
            <td>5000</td>
            <td>Marketing</td>
            <td>Stationsstraat 5, Aalst</td>
        </tr>
        <tr>
            <td>EWI85</td>
            <td>Emma Winters</td>
            <td>manager</td>
            <td>6500</td>
            <td>Marketing</td>
            <td>Stationsstraat 5, Aalst</td>
        </tr>
        <tr>
            <td>MB090</td>
            <td>Mohammed Bouazza</td>
            <td>assistent</td>
            <td>4000</td>
            <td>HR</td>
            <td>Vredestraat 7, Brugge</td>
        </tr>
    </tbody>
</table>

### Vermindering van gegevensredundantie

> **Gegevensredundantie** wil zeggen dat dezelfde informatie meerdere keren op verschillende plaatsen wordt opgeslagen.

Dit kan leiden to inconsistente gegevens.

Uit ons voorbeeld blijkt dat we de gegevens voor een departementadres op verschillende plaatsten moeten wijzigen wanneer dit veranderd.

### Vermijden van invoeg-, verwijder- en modificatie-anomalieën

#### Invoeganomalie

In een niet-genormaliseerde tabel kan je soms geen gegevens toevoegen zonder onvolledige, nutteloze informatie in te voeren. 

Het toevoegen van een nieuw departement in het voorbeeld is niet mogelijk zonder het toevoegen van een werknemer.

#### Verwijderanomalie

Het verwijderen van bepaalde gegevens kan er toe leiden dat ook andere, nog steeds relevante gegevens onbedoeld verwijderd worden.

Wanneer we in het voorbeeld de werknemer "Stijn De Smet" verwijderen, verwijderen we ook alle informatie van het departement "IT".

#### Modificatie-anomalie

Dit kan optreden wanneer dezelfde gegevens op verschillende plaatsen opgeslagen zijn. Het wijzigen van gegevens moet zo op al die verschillende plaatsen gebeuren, dit is foutgevoelig en kan leiden tot inconsistenties.

Wanneer we in ons voorbeeld het adres van het departement "Marketing" willen wijzigen moeten welke elke vermelding handmatig wijzigen.

#### Oplossingen anomalieën

We kunnen bovenstaande tabel normaliseren door de gegevens van de werknemers en de departementen gescheiden te houden.

<table>
    <thead>
        <tr>
            <th>wncode</th>
            <th>werknemernaam</th>
            <th>functie</th>
            <th>loon</th>
            <th>departementcode</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>JJA60</td>
            <td>Jan Janssens</td>
            <td>manager</td>
            <td>6000</td>
            <td>HR</td>
        </tr>
        <tr>
            <td>SDM70</td>
            <td>Stijn De Smet</td>
            <td>assistent</td>
            <td>3500</td>
            <td>IT</td>
        </tr>
        <tr>
            <td>EME75</td>
            <td>Eva Mertens</td>
            <td>verantwoordelijke</td>
            <td>5000</td>
            <td>Marketing</td>
        </tr>
        <tr>
            <td>EWI85</td>
            <td>Emma Winters</td>
            <td>manager</td>
            <td>6500</td>
            <td>Marketing</td>
        </tr>
        <tr>
            <td>MBO90</td>
            <td>Mohammed Bouazza</td>
            <td>assistent</td>
            <td>4000</td>
            <td>HR</td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th>departementcode</th>
            <th>departementadres</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>HR</td>
            <td>Vredestraat 7, Brugge</td>
        </tr>
        <tr>
            <td>IT</td>
            <td>Vogelmarkt 9, Gent</td>
        </tr>
        <tr>
            <td>Marketing</td>
            <td>Stationsstraat 5, Aalst</td>
        </tr>
    </tbody>
</table>

- we kunnen nu nieuwe departementen toevoegen zonder ook werknemergegevens in te voeren. 
- We kunnen de werknemer "Stijn De Smet" verwijderen zonder de informatie van het departement "IT" te verliezen.
- We kunnen het adres van het departement "Marketing" wijzigen zonder dat er inconsistente gegevens ontstaan.

### Verhoging van gegevensinconsistentie

Door redundantie te verminderen is er minder kan dat verschillende kopieën van dezelfde gegevens verschillende waarden bevatten.

### Betere gegevensintegriteit

Gegevensintegriteit houdt in dat de gegevens in de databank juist, volledig en geldig zijn. Normalistatie helpt bij het implementeren van integreitsregels door afhankelijkheden tussen de gegevens te structureren.

### Verbeterde onderhoudbaarheid en schaalbaarheid

Na verloop van tijd veranderen gegevens in een databank. Het bijwerken van een goed genormaliseerde databank is eenvoudiger en minder foutgevoelig, omdat de gegevens gestructureerd en logisch opgeslagen zijn.

## Functionele afhankelijkheid

Functionele afhankelijkheid en normalisatie zijn nauw aan elkaar verbonden. Het proces van normalisatieis gebaseerd op het identificeren en elimineren van functionele afhankelijkheden tussen attributen.

> **Functionele afhankelijkheid** beschrijft de relatie tussen attributen (kolommen) in een databank. Een attribuut B is functioneel afhankelijk van een attribuut A als de waarde van A de waarde van B bepaald.

Voor elke unieke waarde van A is er dus maar één corresponderende waarde van B.

Wanneer we de waarde van het attribuuttype A in een tupel kennen, kunnen we de waarde van de functioneel afhankelijke attribuuttypes eenduidig bepalen of terugvinden.

*Notatie:* A ➡️ B

We zeggen A bepaalt B of B is functioneel afhankelijk van A.

In het voorbeeld is werknemernaam FA van wncode en is functie FA van wncode.
Dit betekent dat de naam en de functie van de werknemer afhankelijk is van de wncode, aangezien elke wncode slechts aan één werknemer gekoppeld is.

wncode ➡️ werknemernaam, functie

### Partiële functionele afhankelijkheid

> **Partiële afhankelijkheid** komt alleen voor in tabellen met een *samengestelde primaire sleutel*.

B is partieel functioneel afhankelijk van A als B slechts functioneel afhankelijk is van een deel van A.

B is partieel afhankelijk als geldt: A ➡️ B en er is een $A' \subset A$, waarvoor geldt A' ➡️ B

<table>
    <thead>
        <tr>
            <th>wncode</th>
            <th>werknemernaam</th>
            <th>functie</th>
            <th>loon</th>
            <th>projectcode</th>
            <th>projectnaam</th>
            <th>gewerkteuren</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>JJA60</td>
            <td>Jan Janssens</td>
            <td>manager</td>
            <td>6000</td>
            <td>ANA</td>
            <td>Analytics</td>
            <td>20</td>
        </tr>
        <tr>
            <td>SDM70</td>
            <td>Stijn De Smet</td>
            <td>assistent</td>
            <td>3500</td>
            <td>HDP</td>
            <td>Hadoop</td>
            <td>50</td>
        </tr>
        <tr>
            <td>EME75</td>
            <td>Eva Mertens</td>
            <td>verantwoordelijke</td>
            <td>5000</td>
            <td>ANA</td>
            <td>Analytics</td>
            <td>10</td>
        </tr>
        <tr>
            <td>EME75</td>
            <td>Eva Mertens</tsd>
            <td>verantwoordelijke</td>
            <td>5000</td>
            <td>HDP</td>
            <td>Hadoop</td>
            <td>10</td>
        </tr>
    </tbody>
</table>

De primaire sleutel van deze tabel bestaat uit zowel wncode als projectcode, omdat gewerkte uren afhankelijk is van wncode als projectcode.

wncode, projectcode ➡️ werknemernaam, gewerkteuren

werknemernaam is partieelafhankelijk van wncode en projectcode want wncode ➡️ werknemernaam

gewerkteuren is wel functioneel afhankelijk van wncode en projectcode