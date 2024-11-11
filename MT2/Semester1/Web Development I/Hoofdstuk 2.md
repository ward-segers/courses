# Web Development 1 : HTML Basis - Deel 2

## Lijsten

HTML heeft 3 verschillende soorten lijsten:

- *Ordered list*:
    - Kan als attributen: start, type, reversed hebben

<table>
<tr>
<th>Syntax</th>
<th>Output</th>
</tr>
<tr>
<td>

```html
    <ol type="i">
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ol>
```

</td>
<td>

<ol type="i">
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ol>

</td>
</tr>
</table>

- *Unordered list*:
    - Worden vaak gebruikt bij het maken van een navigatie-menu

<table>
<tr>
<th>Syntax</th>
<th>Output</th>
</tr>
<tr>
<td>

```html
    <ul>
        <li>First item</li>
        <li>Second item</li>
        <li>Third item</li>
    </ul>
```

</td>
<td>

<ul>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>

</td>
</tr>
</table>

- *Lijst met beschrijving of definities*
    - Wordt gebruikt voor de FAQ

<table>
<tr>
<th>Syntax</th>
<th>Output</th>
</tr>
<tr>
<td>

```html
    <dl>
        <dt>200 OK</dt>
        <dd>The request succeeded</dd>
        <dt>404 Not Found</dt>
        <dd>The server can find the requeste resource. This code is most likely the most famous one on the internet, due to its frequent occurences</dd>
        <dt>500 Internal Server Error</dt>
        <dd>The server has encountered a situation it does not know how to handle.</dd>
    </dl>
```

</td>
<td>

 <dl>
        <dt>200 OK</dt>
        <dd>The request succeeded</dd>
        <dt>404 Not Found</dt>
        <dd>The server can find the requeste resource. This code is most likely the most famous one on the internet, due to its frequent occurences</dd>
        <dt>500 Internal Server Error</dt>
        <dd>The server has encountered a situation it does not know how to handle.</dd>
    </dl>

</td>
</tr>
</table>

Het is ook mogelijk om lijsten te subnesten. Hierbij wordt de gesubneste lijst in een subitem van een andere lijst geplaatst.

## Backline en inline elementen

Sinds HTML5 worden inline-level en block-level indeling voor elementen niet meer gebruikt. We bespreken de principes hier aangezien de termen vaak wel nog gebruikt worden.

Ook omdat de nieuwe indeling binnnen HTML5 nogal complex is.

- **Block elements**: Een block element start steeds op een nieuwe lijn en neemt de volledige breedte van de webpagina in.

- **Inline elements**: Een inline element begint niet op een nieuwe lijn en neemt enkel de breedte in die nodig is voor het element.

Daarbuiten zijn er ook 2 elementen die geen semantische betekenis hebben. nl. `<div>` en `<span>`

- `<div>` is een block element en een algemene container. Het wordt vaak gebruikt om elementen te groeperen. Bijvoorbeeld om ze later te kunnne stijlen met behulp van CSS of om gemeenschappelijke attributen zoals "lang" toe te voegen.

### Text-block level elementen

- `<blockquote>`: gebruikt voor langere citaten
- `<ul> <ol> <dl>`: functionaliteit reeds besproken
- `<figure>`: groepeert een illustratie met zijn bijschrift. Het hoeft niet een beeld te zijn. Het kan een grafiek, tabel, citaat of meer zijn.
    - `<figcaption>`: beschrijft het bijschrift van de figuur
- `<address>`: markeren van address informatie
- `<pre>`: behouden van tabs, witruimtes, etc in code. (pre-formatted)
- `<hr>`: een thematische scheiding tussen paragrafen.

### Text-inline elementen

- `<strong>`: een stuk tekst met een belangrijke betekenis. Wordt standaard door de browser in het vet aangeduidt.
- `<em>`: (emphasize) - de klemtoon leggen. De browser zal dit standaard cursief aanduiden.
- `<b>`: Gebruikt om de aandacht van de lezer op de tekst te leggen. Die verder niet bepaald belangrijk is.
- `<i>`: Gebruikt om tekst aan te duiden met als doel de leesbaarheid van de tekst te vergroten.
- `<small>`: aanvullende informatie, bv. copyright tekst
- `<cite>`: voor het markeren van de naam van een auteur of van een creatief werk (geen attribuut voor bron vermelding)
- `<q>`: voor korte citaten in de lopende zin. (quote) Gebruik het attribuut cite om de bron te vermelden
- `<abbr>`: gebruikt voor een afkorting
- `<dfn>`: markeert de eerste keer dat een definitie voorkomt
- `<code>`: markeren van programma code
- `<time>`: gebruikt om een tijdstip of datum aan te duiden
- `<samp>`: computer uitvoer
- `<kbd>`: gebruikersinvoer
- `<s>`: informatie die niet meer klopt (suppress)
- `<sub>`: gebruikt voor subscript
- `<sup>`: gebruikt voor superscript
- `<mark>`: markeer tekst (om tekst met speciale relevantie te markeren)
- `<ins>`: geeft aan dat informatie is toegevoegd
- `<del>`: geeft aan dat informatie is verwijderd

### Hyperlinks