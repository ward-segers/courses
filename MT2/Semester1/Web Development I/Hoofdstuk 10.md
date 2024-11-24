# Web Development 1 : Hoofdstuk 10 - Animaties

> Animatie is de illusie van beweging door het na elkaar afspelen van verschillende stilstaande beelden, zogenaamde *frames*

Er zijn twee manieren om animaties toe te voegen aan een webpagina met behulp van CSS. **CSS transitions** en **CSS animations**

## CSS transitions

- Normaal zal als je de waarde wijzigt van een CSS property de webpagina onmiddelijk bijgewerkt worden met de nieuwe waarde.
- Met een CSS transition kan je ervoor zorgen dat als de waarde van een CSS property wijzigt, de overgang van de oude naar de nieuwe waarde geleidelijk verloopt over een zekere tijdsperiode. De browser zal hierbij automatisch de tussenliggende beelden (frames) tekenen ne zo een animatie creëren.

**Voorbeeld:**

```css
#my-div{
    ...
    width: 100px;
    /* CSS transition:
    om een transitie-effect te bekomen
    moeten we minimaal de transition-duration instellen */
    transition-duration: 2s;
}
```

De transitie kunnen we activeren door bv. op button1 te klikken en de breedte te wijzigen naar 300px

```javascript
button1.onclick() = () => myDiv.style.width = '300px';
```

- In plaats van de breedte van het div-element te wijzigen met javascript kunnen we de breedte ook wijzigen met CSS door gebruik te maken van de `:hover` pseudo class.
- Als we de breedte van het div-element wijzigen naar 300px als er gehoverd wordt over het element, dan zal deze wijziging opnieuw onmiddelijk gebeuren, tenzij we een CSS transition instellen.

**Voorbeeld:**

```css
div{
    ...
    width: 100px;
    /* CSS transition:
    om een transitie-effect te bekomen
    moeten we minimaal de transition-duration instellen */
    transition-duration: 2s;
}
/* als er gehoverd wordt over het div-element wijzigen we zijn breedte. */
div:hover{
    width: 300px;
}
```

### CSS transition properties

- De CSS properties die je kan instellen voor een transition, met hun beginwaarden zijn:
    - `transition-property: all;`
        - stelt in voor welke CSS properties een transitie-effect moet toegepast worden.
        - standaardwaarde is *all*, zodat het effect op alle CSS properties wordt toegepast.
    - `transition-duration: 0s;`
        - deze property definieert de duur van de transitie uitgedrukt in milliseconden of seconden.
        - de standaard waarde is 0s, wat wil zeggen dat de transitie onmiddelijk gebeurd. Deze property moeten we dus minstens instellen om de transitie te kunnen zien.
        - **best practice om de transition-duration property in te stellen**
    - `transition-timing-function: ease;`
        - het is belangrijk om de snelheid waarmee een waarde wijzigt te kunnen controleren. Hiervoor gebruiken we de *transition-timing-function*. Het definieert een `<easing-function>` die de versnellingscurve bepaald.
        - de standaardwaarde is *ease* en definieert een meer natuurlijke beweging dan de waarde *linear*.
    - `transition-delay: 0s;`
        - bepaalt hoe lang er moet gewacht worden met het starten van het transitie-effect nadat de waarde van een property gewijzigd is.
        - De standaardwaarde is 0s en betekent dat het transitie-effect onmiddelijk start nadat de property gewijzigd is.

#### easing functions

- Meer geanvanceerde timing functions kunnen gemaakt worden aan de hand van een *cubiv-bezier* function.

```css
transition-timing-function: cubic-bezier(0.99, 0.21, 0, 0.85);
```

- Je kan een cubic-bezier function visualiseren en eventueel aanpassen met de Chrome of Firefox Dev Tools.
    - Stel een waarde voor de **transition-timing-function** in.
    - Open de **Chrome Dev Tools** en selecteer het element met de transition
    - Klik op het icoontje bij de **transition-timing-function** om de cubic bezier editor te openen
    - Kies een andere waarde of gebruik de hendels om de curve aan te passen.

### meerdere transities instellen

Als we meerdere CSS properties wijzigen dan kunnen we voor elke CSS propety apart de transition properties instellen. Standaard zullen alle transities dezelfde waarden gebruiken.

```css
div{
    transition-property: opacity, height;
    transition-duration: 3s, 5s;
}
```

### de transition shorthand

```css
div{
    transition: opacity 3s, height 5s;
}
```

### transitions op element en element:hover

- Wanneer je een transition instelt op de element selector, dan wordt bij het hoveren de transitie zowel voorwaarts (bij het overgaan) als achterwaards (bij het verlaten) toegepast.
- Wanner je de transition instelt op de element:hover selector, dan wordt de transitie enkel voorwaarts toegepast. Bij het verlaten keert het element onmiddelijk terug naar zijn begintoestand.
- Het is ook mogelijk om verschillende 'transition-*' properties in te stellen voor de voorwaartse en achterwaartse transitie. De 'transition-*' properties voor de voorwaartse transitie stel je dan in op element:hover en deze voor de achterwaartse op het element zelf.

**Voorbeeld:**

```css
div {
...
width: 100px;
/* Achterwaartse transitie */
transition: width 200ms;
}
div:hover {
/* Voorwaartse transitie */
transition: width 2s;
width: 300px;
}
```

### Animatable CSS properties

Je kan **transition** niet bij elke CSS property gebruiken. Zie MDN

> Om waarden te wijzigen zonder gebruik te make van JavaScript hebben we steeds :hover gebruikt, maar je kan hiervoor ook andere pseudo classes gebruiken zoals :focus en :checked.

## CSS 2D transform

- Een property die veel gebruikt wordt bij CSS transitions (en CSS animations) is de **transform** property en de bijhorende **transform-origin**
- Met de **transform** property kan je een element schalen (scale), roteren (rotate), scheef maken (skew) en verplaatsen (translate)

**Voorbeeld:**

```css
/* Het tweede div-element 300px naar
rechts verschuiven en 30 graden roteren. */
div:nth-of-type(2) {
transform: translateX(300px) rotate(30deg);
}
```

- `transform`
    - mogelijke waarden:
        - **none** (initiële waarde = geen transformatie)
        - één of meerdere van de CSS transform functions

    ```css
    transform: rotate(20deg) translateX(50px);
    ```
- `tranform-origin`
    - Stelt de oorsprong in. De initiële waarde is `transform-origin: center center;` (komt overeen met `transform-origin: 50% 50%;`) = oorsprong ligt standaard in het middelpunt van het element
    ```css
    transform-origin: 0% 0%; /* x-offset y-offset */
    ```

### CSS 2D transform functions

<table>
<tr>
<th>2D transform function</th>
<th>Beschrijving</th>
<th>Voorbeeld</th>
</tr>
<tr>
<td>

`rotate()`
</td>
<td>roteren</td>
<td>

```css
transform: rotate(45deg);
```
</td>
</tr>
<tr>
<td>

`scale()`
</td>
<td>schalen</td>
<td>

```css
transform: scale(1.2);
```
</td>
</tr>
<tr>
<td>

`translateX()`
</td>
<td>verplaatsen in de X-richting</td>
<td>

```css
transform: translateX(50%);
```
</td>
</tr>
<tr>
<td>

`translateY()`
</td>
<td>verplaatsen in de Y-richting</td>
<td>

```css
transform: translateY(200px);
```
</td>
</tr>
<tr>
<td>

`translate()`
</td>
<td>

```css
transform: translate(100px, 200px);
```
</td>
<td></td>
</tr>
<tr>
<td>

`skew()`
</td>
<td>scheef maken</td>
<td>

```css
transform: skew(10deg, 10deg);
```
</td>
</tr>
</table>