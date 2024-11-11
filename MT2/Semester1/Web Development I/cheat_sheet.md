# Web Development 1 - Cheat Sheet

Doel van dit document is het oplijsten van alle html-elementen, tags, css-snippets en hun beschrijving ervan.

Het document wordt opgesplits per onderwerp.

<table>
<tr>
<th>Element / code snippet</th>
<th>Beschrijving</th>
</tr>
<tr>
<td>

```html
<p> </p>
```

</td>
<td>een tag die een paragraaf beschrijft</td>
</tr>
<tr>
<td>

```html
<br>
<br />
```

</td>
<td>Een line break tag. Deze tag zorgt er voor de het volgende element op een nieuwe lijn wordt weergegeven.
De tweede notatie wordt gebruikt om compatibel te zijn met XML</td>
</tr>
<tr>
<td>

```html
<strong></strong>
```

</td>
<td>Een element gebruikt om iets te benadrukken. Standaard zal de tekst in het vet weergegeven worden.</td>
</tr>
<tr>
<td>

```html
<h1></h1>
...
<h6></h6>
```

</td>
<td>Elementen gebruikt om headings (titels) weer te geven. Er zijn 6 verschillende headings</td>
</tr>
<tr>
<td>

```html
<a></a>
<a href="src"></a>
```

</td>
<td>Element gebruikt om een link weer te geven. Dit kan naar een andere pagina op de server zijn, of een externe webpagina <br>
Met het href-attribuut geven we de doellocatie van de de link mee.</td>
</tr>
<tr>
<td>

```html
<img />
<img src="src" alt="een afbeelding" />
```
</td>
<td>Een void element gebruikt om een afbeelding op een webpagina weer te geven. Een attiribuut src geven we mee aan het img element om weer te geven op welke locatie de afbeelding staat die we willen weergeven. "alt" is een verplicht attribuut. Dit attribuut geef een textuele weergave van de applicatie wanneer de afbeelding niet kan ingelezen worden. Ook is dit het attribuut dat wordt in gelezen door de zoekmachine crawlers bij het overlezen van de webpagina.</td>
</tr>
<tr>
<td>

```html
<a id="class_id" lang="language" class="class_name"></a>
```

</td>
<td>

Er bestaan sommige gobale attributen. "class" "lang" en "id" zijn hier een voorbeeld van. Ze willen respectievelijk het volgende zeggen:
 - "class": geeft een klasse-naam aan een element. Dit kan aan meerdere elementen gegeven worden.
 - "lang": specifieert de taal van het element
    - Best practise: stel steeds een language in voor je html-element (algemene pagina taal)
 - "id": geeft een unique identifier aan een element
</td>
</tr>
<tr>
<td>

```html
<!DOCTYPE html>
```

</td>
<td>Dit is geen html-element. Het geeft eerder een introductie aan de browser en geeft weer via welke html standaard de pagina moet geïnterpreteerd worden</td>
</tr>
<tr>
<td>

```html
<html>
    <head></head>
    <body></body>
</html>
```

</td>
<td>

Standaard structuur van een pagina.
- "head"-element bevat de metadata. (titel van de webpagina, verwijzingen naar externe documenten,...)
- "body"-element bevat alle zichtbare content van de webpagina.
</td>
</tr>
<tr>
<td>

```html
<div><div>
```
</td>
<td>Een algemeen block element dat gebruikt wordt om algemene containers te beschrijven. Enkel te gebruiken indien er geen elementen met semantische betekenis bestaan. </td>
</tr>
<tr>
<td>

```html
<span></span>
```
</td>
<td>Hetzelfde element als een "div" maar dan als een inline element</td>
</tr>
<tr>
<td>

```html
<blockquote></blockquote>
```
</td>
<td>Gebruikt voor langere citaten</td>
</tr>
<tr>
<td>

```html
<figure>
    <figcaption></figcaption>
</figure>
```
</td>
<td>Groepeert een illustratie met zijn bijschrift. Het hoeft niet een beeld te zijn. Het kan een grafiek, tabel, citaat of meer zijn. Figcaption is het element dat het bijschrift van de figuur beschrijft</td>
</tr>
<tr>
<td>

```html
<address></address>
```
</td>
<td>Describes a piece of contact information.</td>
</tr>
<tr>
<td>

```html
<pre></pre>
```
</td>
<td>Beschrijft een stuk voorgedefinieerde tekst. De tekst zal exact getoond worden zoals beschreven in de html-code</td>
</tr>
<tr>
<td>

```html
<hr>
```
</td>
<td>Een thematische scheiding tussen verschillende paragrafen.</td>
</tr>
<tr>
<td>

```html
<em></em>
```
</td>
<td>Een element gebruikt om de klemtoon ergens op te leggen. Standaard zal de browser dit cursief weergeven.</td>
</tr>
<tr>
<td>

```html
<b></b>
```
</td>
<td>Gebruikt om de aandacht van de lezer op de tekst te leggen. Die verder niet bepaald belangrijk is.</td>
</tr>
<tr>
<td>

```html
<i></i>
```
</td>
<td>Gebruikt om tekst aan te duiden met als doel de leesbaarheid van de tekst te vergroten.</td>
</tr>
<tr>
<td>

```html
<small></small>
```
</td>
<td>aanvullende informatie, bv. copyright tekst</td>
</tr>
<tr>
<td>

```html
<cite></cite>
```
</td>
<td>voor het markeren van de naam van een auteur of van een creatief werk (geen attribuut voor bron vermelding)</td>
</tr>
<tr>
<td>

```html
<q cite="bron"></q>
```
</td>
<td>voor korte citaten in de lopende zin. (quote) Gebruik het attribuut cite om de bron te vermelden</td>
</tr>
<tr>
<td>

```html
<abbr></abbr>
```
</td>
<td>gebruikt voor een afkorting</td>
</tr>
<tr>
<td>

```html
<dfn></dfn>
```
</td>
<td>markeert de eerste keer dat een definitie voorkomt</td>
</tr>
<tr>
<td>

```html
<code></code>
```
</td>
<td>markeren van programma code</td>
</tr>
<tr>
<td>

```html
<time></time>
```
</td>
<td>gebruikt om een tijdstip of datum aan te duiden</td>
</tr>
<tr>
<td>

```html
<samp></samp>
```
</td>
<td>computer uitvoer</td>
</tr>
<tr>
<td>

```html
<kbd></kbd>
```
</td>
<td>gebruikersinvoer</td>
</tr>
<tr>
<td>

```html
<s></s>
```
</td>
<td>informatie die niet meer klopt (suppress)</td>
</tr>
<tr>
<td>

```html
<sub></sub>
```
</td>
<td>gebruikt voor subscript</td>
</tr>
<tr>
<td>

```html
<sup></sup>
```
</td>
<td>gebruitkt voor superscript</td>
</tr>
<tr>
<td>

```html
<mark></mark>
```
</td>
<td>markeer tekst (om tekst met speciale relevantie te markeren)</td>
</tr>
<tr>
<td>

```html
<ins></ins>
```
</td>
<td>geeft aan dat informatie is toegevoegd</td>
</tr>
<tr>
<td>

```html
<del></del>
```
</td>
<td>geeft aan dat informatie verwijderd is</td>
</tr>
<tr>
<td>

```html
<article></article>
```
</td>
<td>voor een zelfstandig stuk inhoud, dat onafhankelijk te hergebruiken is</td>
</tr>
<tr>
<td>

```html
<section></section>
```
</td>
<td>voor een onderdeel van een pagina waarvoor geen meer specifiek element is</td>
</tr>
<tr>
<td>

```html
<nav></nav>
```
</td>
<td>voor de hoofdnavigatie</td>
</tr>
<tr>
<td>

```html
<aside></aside>
```
</td>
<td>voor 'zijdelingse informatie'</td>
</tr>
<tr>
<td>

```html
<header></header>
```
</td>
<td>voor het kopgedeelte</td>
</tr>
<tr>
<td>

```html
<footer></footer>
```
</td>
<td>Voor het footer gedeelte</td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
</table>