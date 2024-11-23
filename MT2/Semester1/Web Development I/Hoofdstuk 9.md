# Web Development 1 : Hoofdstuk 9 - Layout - Responsive

## Inleiding

***Waarom responsive design?***

- beter user experience
- meer bezoekers
- hogere SE ranking
- betere laadtijden
- beheersbare ontwikkeling & onderhoud
    - geen aparte ontwikkeling voor verschillende devices

***Hoe?***

- HTML en CSS gebruiken om pagina's geschikt te maken voor alle soorten schermen en devices.
    - Lay-out van pagina kan wijzigen
    - inhoud kan verborgen/getoond worden
    - elementen kunnen anders getoond worden
        - menu's, buttons, tekst,...

***Mobile first***

- Start de ontwikkeling met focus op mobile experience
    - minimaal, maar bevat alle belangrijke elementen
    - focus op inhoud
- geleidelijk opschalen voor grotere schermen
    - meer mogelijkheden voor extra inhoud
    - meer toeters en bellen

## De viewport

> A **viewport** representts the part of the document you are viewing

- op grotere schermen komt dit overeen met de grootte van het browser venster
- op mobile devices kom de viewport overeen met het volledig scherm
    - de grootte van het browser venster kan op een mobiel niet aangepast worden.

- mobiel: **visual & layout viewport**
    - *visual viewport*: bevat het gedeelte van de pagina dat momenteel op het scherm wordt getoond
    - *layout viewport*: is groter dan de visual viewport en bevat de layout van de volledige pagina. (css werkt met deze afmetingen)

    - De *visual viewport* toont een deel van wat beschikbaar is in de *layout viewport*
    - Door te zoomen (in/uit), te 'pannen', portrait/landscape mode te gebruiken breng je een ander deel van de *layout viewport* in de *visual viewport*

- De grootte van de viewport wordt bepaald door de fabrikant van de browser
- Bij volledig uitzoomen komt de volledige viewport in de visual viewport
- Probleem:
    - pagina wordt gebouwd tov de layout viewport breedte
        - uitgedrukt in DIP - Device independent pixels
    - Bij het openen van de pagina gaat de browser uitzoomen om je de volledige pagina te tonen in de **visual viewport**

- via de *viewport meta tag* wordt het mogelijk de viewport width gelijk te stellen aan de device width

>[!important]
> Het is belangrijk steeds de viewport width gelijk te stellen aan de device width bij 'Responsive Web Design'

- **width = device-width**
    - breedte waarop we werken is de breedte van het device in DIP 
- **initial-scale = 1.0**
    - 1 DIP = 1 CSS pixel

```html
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

> [!tip]
> Maak gebruik van de responsive web developer tools in de browsers

## Media Queries

> A **media query** is a method of testing certain aspects of the user agent or device that the document is being displayed in.

- `@media`
- aspecten: **media type & media features**
    - logische expressie die *true* of *false* is
    - afhankelijk van het resultaat van de tekst kan bepaalde opmaak al dan niet toegepast worden.

**voorbeeld:**

```css
@media screen and (min-width: 800px){
    p {
        background-color: chocolate;
        color: lightyellow;
    }
}
```

Als het venster waarin de pagina bekeken wordt een breedte heeft die groter of gelijk aan 800px is, dan krijgen p-elementen een 'chocolate' achtergrondkleur en 'lightyellow' gekleurde tekst.

- De user agent gaat media queries automatisch her-evalueren indien relevante eigenschappen wijzigen. (bv. bij het wijzigen van het venster)

>[!important]
> De volgorde waarin de media queries geplaatst worden is belangrijk

**media type**

- *all*: komt overeen met eender welk device
- *print*: komt overeen met printers en devices in een modus om te printen (bv. een browser in print-preview modus)
- *screen*: komt overeen met alles dat niet overeen komt met print

**media features**

- *viewport/page afmetingen*
    - bv. width, height, aspect-ratio, orientation
- *kwaliteit*
    - bv. via resolution kan je queriesz maken die rekening houden met de resolutie van het device
- *kleur*
    - bv. via color kan je queries maken die rekening houden met de kleurdiepte van het device
- *interactie*
    - bv. via pointer kan je queries maken die rekening houden met de accuraatheid van het pointing device (touchscreen vs muis/touchpad)

Voorbeelden:

```css
@media (min-width: 500px){
    /* CSS toepassen wanneer viewport width >= 500px */
}
@media (max-width: 50em){
    /* CSS toepassen wanneer viewport width <= 50em */
}
@media (min-aspect-ratio: 1/1){
    /* CSS toepassen wanneer viewport width >= viewport height */
}
@media screen and (min-width: 500px) and (max-width:= 800px){
   /* CSS toepassen wanneer viewport size >= 500px EN viewport size <= 800px is */
}
@media screen and (min-width: 500px), screen and (max-width:800px) {
/* CSS toepassen wanneer viewport size >= 500px OF viewport size <= 800px */
}
@media not print {
/* CSS toepassen voor non-printing */
}
@media screen and (orientation:landscape) {
/* CSS toepassen wanneer viewport width >= viewport height*/
}
/* at time of writing this works only in FireFox! */
@media screen and (height>500px) {
/* CSS toepassen wanneer viewport height >= 500px*/
}
```

### breakpoints

> het punt waarop we layout kenmerken van een pagina gaan wijzigen noemen we een breakpoint

>[!tip]
> **Keuze van breakpoints:**
<table align="center">
<tr>
<td>320px-480px</td>
<td>Mobile devices</td>
</tr>
<tr>
<td>481px-768px</td>
<td>iPads, Tablets</td>
</tr>
<tr>
<td>769px-1024px</td>
<td>Small screens, laptops</td>
</tr>
<tr>
<td>1025px-1200px</td>
<td>Desktops, large screens</td>
</tr>
<tr>
<td>1201px and more</td>
<td>Extra large screens, TV</td>
</tr>
</table>

**Laat je vooral leiden door de inhoud van de pagina om 'jouw' breakpoints te vinden**

>[!tip]
> - zorg voor een **tap-area** van minstens 45 op 45 pixels voor buttons links, ... op schermen zonder accuraat pointing device (= gem afdruk vinger)
> - maak minimaal gebruik van absolute waarden in CSS maak gebruik van relatieve waarden (%, vw, em, rem)
> - gebruik `max-width: 100%` op img elementen zodat de afbeelding niet uit hun container kunnen vloeien
> - layout is geen exacte wetenschap, gebruik tips, baseer je op best practices, maar gebruik ook je gevoel om te beslissen of iets al dan niet OK oogt. 