# DATABASES : Hoofdstuk 5 - Van het conceptueel naar het logisch model

## Inleiding

Databankproces:

<p align='center'><img src='src/databankproces.png' alt='Databankproces' width='75%'></p>

Nadat het ERD van de databank ontworpen is, zetten we het om naar een relationele databank. (met tabbellen en kolommen)

> Dit hoeft niet naar een relationele databank (bv. NoSQL databank kan ook) deze cursus beperken we ons to relationele databanken.

Er bestaan verschillende databasemodelleertools die automatisch het (E)ER-model omzetten naar een relationeel datamodel. Wanneer de de juiste vertaalregels toegepast worden, is het resultaat automatisch genormaliseerd.

> Het manueel omzetten geeft ons inzichten in een goed databankontwerp en de gevolgen van bepaalde ontwerpbeslissingen, door de relationele concepten te koppelen aan hun (E)ER tegenhangers.

*Hoe gaan we een ERD naar tabellen met rijen en kolommen? Hoe mappen we een conceptueel ERD naar een relationeel model?*

## Bouwstenen voor het relationeel model

<table align="center">
    <thead>
        <tr>
            <th>Conceptueel model</th>
            <th>Logisch model</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>entiteittypes</td>
            <td>tabellen</td>
        </tr>
        <tr>
            <td>attribuuttypes</td>
            <td>kolommen</td>
        </tr>
        <tr>
            <td>entiteiten</td>
            <td>rijen (tupels)</td>
        </tr>
    </tbody>
</table>

### Tupel

> **Een tupel** is een geordende lijst met waarden van kenmerken die een object beschrijven.

> [!important]
> **Een tupel** is steeds uniek

**voorbeeld:** tupel van een product - *100, 'Pringles', 'Classic Paprika', '175g', 2.5*

### Attribuut

> **Een attribuut** is een benoemd kenmerk van een tupel. Het kan maar één waarde hebben, **de attribuutwaarde**.

**voorbeeld:** het attribuut *merk* uit de tupel *100, 'Pringles', 'Classic Paprika', '175g', 2.5* 

### Domein

> **Een domein** is een verzameling van waarden die voor de attributen in de tupels van een relatie mogen gebruikt worden.

**voorbeeld:** domein van prijs zijn alle toegestane prijzen die een product kan hebben

### Relatie

> **Een relatie** is een verzameling van tupels die gelijksoortige objecten beschrijven.

**voorbeeld:** verzameling tupels die producten beschrijven: *{(100, 'Pringles', 'Classic Paprika', '175g', 2.5), (101, 'Lays', 'Max Naturel', '185g', 2.3), (102, 'Croky', 'Barbecue Rings', '100g', 1.8)}*

Een relatie kunnen we ook zien als een gestructureerde verzameling gegevens. Het zijn gegevens die allemaal betrekking hebben op gelijkaardige objecten en ze komen in groepjes voor (tupels), en binnen elk groepje in dezelfde volgorde.

### Sleutels

In een relatie moet elk tupel uniek zijn. 

Attribuuttypen die toelaten de tupels van elkaar te onderscheiden worden **sleutelattribuuttypen** (of sleutels) genoemd. 

We spreken van een sleutel wanneer een minimale verzameling van attributen als combinatie de tupel binnen de relatie uniek kan identificeren.

Er zijn verschillende soorten sleutels:

- **Kandidaatsleutel**: verschillende mogelijke combinaties, deze mogelijke sleutels zijn kandidaatsleutels
- **Primaire sleutel**: een gekozen kandidaatsleutel die primair wordt aangeduid. Deze waarde kan niet *NULL* zijn. In het relationeel model wordt deze onderstreept.
- **Alternatieve sleutel**: Elke kandidaatsleutel die geen primaire sleutel is.
    - waarde kan *NULL* zijn, verliest echter dan welk de functie van sleutel
- **Vreemde sleutel**: sleutel gebruikt om verbanden te leggen met andere relaties in het relationeel model. Deze sleutel heeft niets te maken met de idenificatie vna de tupel.
    - De verbindende schakel tussen twee relaties.
    - Met deze waarde kunnen we in een andere tabel de juiste tupel opzoeken

<p align='center'><img src='src/foreign_key.png' alt='Foreign Key' width='50%'></p>

## Vergelijking met het ER-model

### Entiteittypes en attribuuttypes

Elke tabel vertegenwoordigt een entiteittype, en de kolommen van de tabel vertegenwoordigen de attributen van het entiteittype. 

<table align="center">
    <thead>
        <tr>
            <th>ER-model</th>
            <th>Relationeel model</th>
            <th>Databank</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Entiteittype</td>
            <td>Relatie</td>
            <td>Tabel</td>
        </tr>
        <tr>
            <td>Entiteit</td>
            <td>Tupel</td>
            <td>Rij</td>
        </tr>
        <tr>
            <td>Attribuuttype</td>
            <td>Attribuut</td>
            <td>Kolom</td>
        </tr>
        <tr>
            <td>Attribuutwaarde</td>
            <td>Attribuutwaarde</td>
            <td>Kolomwaarde</td>
        </tr>
    </tbody>
</table>

**Relatietypes**

Relaties tussen entiteiten worden in het ER-model weergegeven als lijnen of verbindingen tussen deze entiteiten. (vaak geassocieerd met cardinaliteiten)

## Regels van een relationeel model

Het relationeel model is een logisch model dat aan volgende regels voldoet:
- Elke tupel in een relatie is uniek
- Elk attribuut is enkelvoudig (samengestelde attribuutwaarden zijn niet toegestaan)
- Elk attribuut is enkelwaardig (meerwaardige attribuutwaarden zijn niet toegestaan)
- Verbanden tussen relaties worden gelegd aan de hand van **vreemde sleutels**

## Mapping

Het omzetten (mapping) van het conceptueel model naar het logisch model gebeurt in enkele stappen en volgens strikte regels. Door het volgen van volgende stappen is het relatief eenvoudig:

- STAP 1: Elk entiteittype wordt een relatie. Bij het mappen van een EERD waar specialisatie in voorkomt, kan het gebeuren dat entiteittypes verdwijnen.

- STAP 2: Enkelvoudige attribuuttypes overnemen

- STAP 3: Samengestelde attribuuttypes opsplitsen in enkelvoudige attribuuttypes

- STAP 4: Als er nog meerwaardige attributen in het conceptueel model aanwezig zijn, dienen deze in een nieuwe relatie geplaastst te worden.

- STAP 5: Primaire sleutel bepalen. Opgelet bij zwakke entiteiten

- STAP 6: Voor elke relatie: vreemde sleutel(s) bepalen op volgende wijze:
    - 1-op-1 relatie: vreemde sleutel in de één of andere relatie (afhankelijk van de minimumcardinaliteit)
    - 1-op-N relatie: vreemde sleutel in de relatie aan N-zijde
    - M-op-N relatie: aparte relatie met beide vreemde sleutels als samengestelde primaire sleutel
    - unaire 1-op-1 of 1-op-N relatie: vreemde sleutel in zelfde relatie

- STAP 7: Bij elke vreemde sleutel de integriteitregels bepalen:
    - naar welke primaire sleutel deze vreemde sleutel verwijst
    - of de vreemde sleutel verplicht of optioneel is
    - eventueel of de vreemde sleutel uniek is

### Mapping van entiteittypes

De eerste stap is om elk entiteittype in een relatie te mappen. Eenvoudige attribuuttypes kunnen direct omgezet worden naar een kolom. Een samengesteld attribuuttype moet worden opgesplits in enkelvoudige attribuuttype. Een van de kandidaatsleutels van het entiteittype kan worden ingesteld als de primaire sleutel van de relatie.

<p align='center'><img src='src/entiteittype.png' alt='Entiteittype' width='25%'></p>

Hieronder tonen we een aantal voorbeeld tuples die intuïtief laten aanvoelen dat het bovenstaande entiteittype gemapt moet worden naar een relatie die er als volgt uitziet:

<table>
    <tr>
        <th>wncode</th>
        <td>voornaam</td>
        <td>familienaam</td>
        <td>straat</td>
        <td>huisnummer</td>
        <td>postcode</td>
        <td>woonplaats</td>
        <td>geboortedatum</td>
        <td>emailadres</td>
    </tr>
    <tr>
        <td>JJA60</td>
        <td>Jan</td>
        <td>Janssens</td>
        <td>Fonteinstraat</td>
        <td>7</td>
        <td>9000</td>
        <td>Gent</td>
        <td>1/02/1960</td>
        <td>jan.janssens@bedrijf.be</td>
    </tr>
    <tr>
        <td>MER70</td>
        <td>Mohamed</td>
        <td>Erdogan</td>
        <td>Marktweg</td>
        <td>5</td>
        <td>9700</td>
        <td>Oudenaarde</td>
        <td>5/12/1970</td>
        <td>mohamed.erdogan@bedrijf.be</td>
    </tr>
    <tr>
        <td>EME75</td>
        <td>Eva</td>
        <td>Mertens</td>
        <td>Steenstraat</td>
        <td>11</td>
        <td>8000</td>
        <td>Brugge</td>
        <td>2/09/1975</td>
        <td>eva.mertens@bedrijf.be</td>
    </tr>
    <tr>
        <td>FAR85</td>
        <td>Fatma</td>
        <td>Arici</td>
        <td>Kerkstraat</td>
        <td>10</td>
        <td>9090</td>
        <td>Melle</td>
        <td>22/11/1985</td>
        <td>fatma.arici@bedrijf.be</td>
    </tr>
    <tr>
        <td>MPA90</td>
        <td>Maarten</td>
        <td>Pauwels</td>
        <td>Brouwerijstraat</td>
        <td>5</td>
        <td>9850</td>
        <td>Aalter</td>
        <td>12/03/1990</td>
        <td>maarten.pauwels@bedrijf.be</td>
    </tr>
</table>

Het entiteittype WERKNEMER wordt daarom formeel gemapt naar volgende relatie:

WERKNEMER(<u>wncode</u>, voornaam, familienaam, straat, huisnummer, postcode, woonplaats, geboortedatum)

> Het samengestelde attribuut adres werd opgesplits in straat, huisnummer, postcode en woonplaats

### Mapping van Relatietypes

Het mappen van de attribuuttypes hangt af van de maximumcardinaliteit.

#### 1:1 - relatie met aan één kant minimumcardinaliteit=1

<p align='center'><img src='src/mapping_relatietypes_minimumcardinaliteit.png' alt='Mapping relatietypes met minimumcardinaliteit = 1' width='50%'></p>

**Voorbeeldtuples voor Werknemer en Bedrijfswagen**

*WERKNEMER*

<table>
    <tr>
        <th>wncode</th>
        <td>voornaam</td>
        <td>familienaam</td>
        <td>emailadres</td>
        <td>geboortedatum</td>
    </tr>
    <tr>
        <td>JJA60</td>
        <td>Jan</td>
        <td>Janssens</td>
        <td>jan.janssens@bedrijf.be</td>
        <td>1/02/1960</td>
    </tr>
    <tr>
        <td>MER70</td>
        <td>Mohamed</td>
        <td>Erdogan</td>
        <td>mohamed.erdogan@bedrijf.be</td>
        <td>5/12/1970</td>
    </tr>
    <tr>
        <td>EME75</td>
        <td>Eva</td>
        <td>Mertens</td>
        <td>eva.mertens@bedrijf.be</td>
        <td>2/09/1975</td>
    </tr>
    <tr>
        <td>FAR85</td>
        <td>Fatma</td>
        <td>Arici</td>
        <td>fatma.arici@bedrijf.be</td>
        <td>22/11/1985</td>
    </tr>
    <tr>
        <td>MPA90</td>
        <td>Maarten</td>
        <td>Pauwels</td>
        <td>maarten.pauwels@bedrijf.be</td>
        <td>12/03/1990</td>
    </tr>
</table>

*BEDRIJFSWAGEN*

<table>
    <tr>
        <th>nummerplaat</th>
        <td>merk</td>
        <td>type</td>
    </tr>
    <tr>
        <td>1-POL-189</td>
        <td>Toyota</td>
        <td>Corolla</td>
    </tr>
    <tr>
        <td>1-OUL-784</td>
        <td>Mercedes</td>
        <td>A-Klasse</td>
    </tr>
    <tr>
        <td>1-MPO-965</td>
        <td>Ford</td>
        <td>Puma</td>
    </tr>
</table>

*Hoe kunnen we de entiteittypes WERKNEMER en BEDRIJFSWAGEN mappen naar het relationeel model?*

Er zijn twee mogelijkheden:

- **Mogelijkheid 1**: we voegen een kolom nummerplaat toe aan de WERKNEMER tabel. Elke nummerplaat kan slechts eenmaal voorkomen in de kolom nummerplaat in de WERKNEMER tabel. Omdat niet elke WERKNEMER een bedrijfswagen heeft (minimumcardinaliteit = 0) zijn er mogelijks wel *NULL* waarden

<table>
    <tr>
        <th>wncode</th>
        <td>voornaam</td>
        <td>familienaam</td>
        <td>emailadres</td>
        <td>geboortedatum</td>
        <td>nummerplaat</td>
    </tr>
    <tr>
        <td>JJA60</td>
        <td>Jan</td>
        <td>Janssens</td>
        <td>jan.janssens@bedrijf.be</td>
        <td>1/02/1960</td>
        <td>1-POL-189</td>
    </tr>
    <tr>
        <td>MER70</td>
        <td>Mohamed</td>
        <td>Erdogan</td>
        <td>mohamed.erdogan@bedrijf.be</td>
        <td>5/12/1970</td>
        <td></td>
    </tr>
    <tr>
        <td>EME75</td>
        <td>Eva</td>
        <td>Mertens</td>
        <td>eva.mertens@bedrijf.be</td>
        <td>2/09/1975</td>
        <td>1-OUL-784</td>
    </tr>
    <tr>
        <td>FAR85</td>
        <td>Fatma</td>
        <td>Arici</td>
        <td>fatma.arici@bedrijf.be</td>
        <td>22/11/1985</td>
        <td>1-MPO-965</td>
    </tr>
    <tr>
        <td>MPA90</td>
        <td>Maarten</td>
        <td>Pauwels</td>
        <td>maarten.pauwels@bedrijf.be</td>
        <td>12/03/1990</td>
        <td></td>
    </tr>
</table>

*BEDRIJFSWAGEN*

<table>
    <tr>
        <th>nummerplaat</th>
        <td>merk</td>
        <td>type</td>
    </tr>
    <tr>
        <td>1-POL-189</td>
        <td>Toyota</td>
        <td>Corolla</td>
    </tr>
    <tr>
        <td>1-OUL-784</td>
        <td>Mercedes</td>
        <td>A-Klasse</td>
    </tr>
    <tr>
        <td>1-MPO-965</td>
        <td>Ford</td>
        <td>Puma</td>
    </tr>
</table>

- **Mogelijkheid 2**: we voegen een kolom wncode toe aan de tabel BEDRIJFSWAGEN. Elke wncode kan slechts eenmaal voorkomen in de kolom wncode in de tabel BEDRIJFSWAGEN. Omdat elke BEDRIJFSWAGEN aan ten minste 1 WERKNEMER toebehoort (minimumcardinaliteit = 1) zijn er geen *NULL* waarden

<table>
    <tr>
        <th>wncode</th>
        <td>voornaam</td>
        <td>familienaam</td>
        <td>emailadres</td>
        <td>geboortedatum</td>
    </tr>
    <tr>
        <td>JJA60</td>
        <td>Jan</td>
        <td>Janssens</td>
        <td>jan.janssens@bedrijf.be</td>
        <td>1/02/1960</td>
    </tr>
    <tr>
        <td>MER70</td>
        <td>Mohamed</td>
        <td>Erdogan</td>
        <td>mohamed.erdogan@bedrijf.be</td>
        <td>5/12/1970</td>
    </tr>
    <tr>
        <td>EME75</td>
        <td>Eva</td>
        <td>Mertens</td>
        <td>eva.mertens@bedrijf.be</td>
        <td>2/09/1975</td>
    </tr>
    <tr>
        <td>FAR85</td>
        <td>Fatma</td>
        <td>Arici</td>
        <td>fatma.arici@bedrijf.be</td>
        <td>22/11/1985</td>
    </tr>
    <tr>
        <td>MPA90</td>
        <td>Maarten</td>
        <td>Pauwels</td>
        <td>maarten.pauwels@bedrijf.be</td>
        <td>12/03/1990</td>
    </tr>
</table>

*BEDRIJFSWAGEN*

<table>
    <tr>
        <th>nummerplaat</th>
        <td>merk</td>
        <td>type</td>
        <td>wncode</td>
    </tr>
    <tr>
        <td>1-POL-189</td>
        <td>Toyota</td>
        <td>Corolla</td>
        <td>JJA60</td>
    </tr>
    <tr>
        <td>1-OUL-784</td>
        <td>Mercedes</td>
        <td>A-Klasse</td>
        <td>EME75</td>
    </tr>
    <tr>
        <td>1-MPO-965</td>
        <td>Ford</td>
        <td>Puma</td>
        <td>FAR85</td>
    </tr>
</table>

> Mogelijkheid 2 geniet de voorkeur omdat er geen *NULL* waarden voorkomen. (ookal zijn beide mogelijkheden correct).

*Formele notatie*:

Werknemer(<u>wncode</u>, voornaam, familienaam, emailadres, geboortedatum) <br>
Bedrijfswagen(nummerplaat, merk, type,wncode) <br>
IR: Vreemde sleutel wncode verwijst naar wncode uit Werknemer, verplicht, uniek

#### 1:1 - relatie met aan beide kanten minimumcardinaliteit = 0

<p align='center'><img src='src/mapping_relatietypes_minimumcardinaliteit_0.png' alt='relatie met aan beide kanten minimumcardinaliteit 0' width='50%'></p>

**Voorbeeldtuples voor Werknemer en Bedrijfswagen**

*WERKNEMER*

<table>
    <tr>
        <th>wncode</th>
        <td>voornaam</td>
        <td>familienaam</td>
        <td>emailadres</td>
        <td>geboortedatum</td>
    </tr>
    <tr>
        <td>JJA60</td>
        <td>Jan</td>
        <td>Janssens</td>
        <td>jan.janssens@bedrijf.be</td>
        <td>1/02/1960</td>
    </tr>
    <tr>
        <td>MER70</td>
        <td>Mohamed</td>
        <td>Erdogan</td>
        <td>mohamed.erdogan@bedrijf.be</td>
        <td>5/12/1970</td>
    </tr>
    <tr>
        <td>EME75</td>
        <td>Eva</td>
        <td>Mertens</td>
        <td>eva.mertens@bedrijf.be</td>
        <td>2/09/1975</td>
    </tr>
    <tr>
        <td>FAR85</td>
        <td>Fatma</td>
        <td>Arici</td>
        <td>fatma.arici@bedrijf.be</td>
        <td>22/11/1985</td>
    </tr>
    <tr>
        <td>MPA90</td>
        <td>Maarten</td>
        <td>Pauwels</td>
        <td>maarten.pauwels@bedrijf.be</td>
        <td>12/03/1990</td>
    </tr>
</table>

*BEDRIJFSWAGEN*

<table>
    <tr>
        <th>nummerplaat</th>
        <td>merk</td>
        <td>type</td>
    </tr>
    <tr>
        <td>1-POL-189</td>
        <td>Toyota</td>
        <td>Corolla</td>
    </tr>
    <tr>
        <td>1-OUL-784</td>
        <td>Mercedes</td>
        <td>A-Klasse</td>
    </tr>
    <tr>
        <td>1-MPO-965</td>
        <td>Ford</td>
        <td>Puma</td>
    </tr>
</table>

*Hoe kunnen we de entiteittypes WERKNEMER en BEDRIJFSWAGEN mappen naar het relationeel model?*

Er zijn twee mogelijkheden:

- **Mogelijkheid 1**:  we voegen een kolom nummerplaat toe aan de WERKNEMER tabel. Elke nummerplaat kan slechts eenmaal voorkomen in de kolom nummerplaat in de WERKNEMER tabel. Omdat niet elke WERKNEMER een bedrijfswagen heeft (minimumcardinaliteit = 0) zijn er mogelijks wel *NULL* waarden

<table>
    <tr>
        <th>wncode</th>
        <td>voornaam</td>
        <td>familienaam</td>
        <td>emailadres</td>
        <td>geboortedatum</td>
        <td>nummerplaat</td>
    </tr>
    <tr>
        <td>JJA60</td>
        <td>Jan</td>
        <td>Janssens</td>
        <td>jan.janssens@bedrijf.be</td>
        <td>1/02/1960</td>
        <td>1-POL-189</td>
    </tr>
    <tr>
        <td>MER70</td>
        <td>Mohamed</td>
        <td>Erdogan</td>
        <td>mohamed.erdogan@bedrijf.be</td>
        <td>5/12/1970</td>
        <td></td>
    </tr>
    <tr>
        <td>EME75</td>
        <td>Eva</td>
        <td>Mertens</td>
        <td>eva.mertens@bedrijf.be</td>
        <td>2/09/1975</td>
        <td></td>
    </tr>
    <tr>
        <td>FAR85</td>
        <td>Fatma</td>
        <td>Arici</td>
        <td>fatma.arici@bedrijf.be</td>
        <td>22/11/1985</td>
        <td>1-MPO-965</td>
    </tr>
    <tr>
        <td>MPA90</td>
        <td>Maarten</td>
        <td>Pauwels</td>
        <td>maarten.pauwels@bedrijf.be</td>
        <td>12/03/1990</td>
        <td></td>
    </tr>
</table>

*BEDRIJFSWAGEN*

<table>
    <tr>
        <th>nummerplaat</th>
        <td>merk</td>
        <td>type</td>
    </tr>
    <tr>
        <td>1-POL-189</td>
        <td>Toyota</td>
        <td>Corolla</td>
    </tr>
    <tr>
        <td>1-OUL-784</td>
        <td>Mercedes</td>
        <td>A-Klasse</td>
    </tr>
    <tr>
        <td>1-MPO-965</td>
        <td>Ford</td>
        <td>Puma</td>
    </tr>
</table>

- **Mogelijkheid 2**: we voegen een kolom wncode toe aan de tabel BEDRIJFSWAGEN. Elke wncode kan slechts eenmaal voorkomen in de kolom wncode in de tabel BEDRIJFSWAGEN. Omdat elke BEDRIJFSWAGEN niet noodzakelijk toebehoort aan een WERKNEMER (minimumcardinaliteit = 0) zijn er mogelijks *NULL* waarden

<table>
    <tr>
        <th>wncode</th>
        <td>voornaam</td>
        <td>familienaam</td>
        <td>emailadres</td>
        <td>geboortedatum</td>
    </tr>
    <tr>
        <td>JJA60</td>
        <td>Jan</td>
        <td>Janssens</td>
        <td>jan.janssens@bedrijf.be</td>
        <td>1/02/1960</td>
    </tr>
    <tr>
        <td>MER70</td>
        <td>Mohamed</td>
        <td>Erdogan</td>
        <td>mohamed.erdogan@bedrijf.be</td>
        <td>5/12/1970</td>
    </tr>
    <tr>
        <td>EME75</td>
        <td>Eva</td>
        <td>Mertens</td>
        <td>eva.mertens@bedrijf.be</td>
        <td>2/09/1975</td>
    </tr>
    <tr>
        <td>FAR85</td>
        <td>Fatma</td>
        <td>Arici</td>
        <td>fatma.arici@bedrijf.be</td>
        <td>22/11/1985</td>
    </tr>
    <tr>
        <td>MPA90</td>
        <td>Maarten</td>
        <td>Pauwels</td>
        <td>maarten.pauwels@bedrijf.be</td>
        <td>12/03/1990</td>
    </tr>
</table>

*BEDRIJFSWAGEN*

<table>
    <tr>
        <th>nummerplaat</th>
        <td>merk</td>
        <td>type</td>
        <td>wncode</td>
    </tr>
    <tr>
        <td>1-POL-189</td>
        <td>Toyota</td>
        <td>Corolla</td>
        <td>JJA60</td>
    </tr>
    <tr>
        <td>1-OUL-784</td>
        <td>Mercedes</td>
        <td>A-Klasse</td>
        <td></td>
    </tr>
    <tr>
        <td>1-MPO-965</td>
        <td>Ford</td>
        <td>Puma</td>
        <td>FAR85</td>
    </tr>
</table>

> Beide oplossingen zijn juist, maar mogelijkheid 2 geniet de voorkeur doordat hier minder *NULL* waarden zijn.

*Formele notatie*:

Werknemer(<u>wncode</u>, voornaam, familienaam, emailadres, geboortedatum) <br>
Bedrijfswagen(nummerplaat, merk, type,wncode) <br>
IR: Vreemde sleutel wncode verwijst naar wncode uit Werknemer, verplicht, optioneel