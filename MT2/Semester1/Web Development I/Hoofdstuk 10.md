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
verplaatsen in de X- en Y-richting
</td>
<td>

```css
transform: translate(100px, 200px);
```
</td>
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

#### `translate()`

```css
div{transform: translate(100px, 100px);}
```

Verplaatst het element 100px in de X- en de Y-richting. De X-richting is horizontaal naar rechts en de Y-richting is verticaal naar beneden.

## CSS animations

- Bij een CSS transition konden we enkel een begin- en eindtoestand opgeven. Bij **CSS animations** zullen we meer toestanden zgn. keyframes kunnen opgeven en zullen we bijvoorbeeld ook de animatie een aantal keren kunnen herhalen.
- In animatie-terminologie is een **keyframe**, een frame waar je veranderingen in de animatie definieert
- Een CSS animation kan automatisch starten bij het laden van de webpagina. Dit is zelfs de default. Je kan ze ook starten via JavaScript of met behulp van :hover.

### opbouwen animatie

- STAP 1: definiëren animatie

Definieer de animatie door middel van keyframes.
```css
@keframes at-rule
```
De browser zal bij het afspelen van de animatie de tussenliggende waarden tussen de opeenvolgende keyframes automatisch genereren.

- STAP 2: afspelen van de animatie op een bepaald element

properties `animation-name`, `animation-duration`, `animation-timing-function`, ... shorthand `animation`

**Voorbeeld:**

```css
div{
    animation-name: my-animation;
    animation-duration: 2s;
}

@keyframes my-animation{
    0% {transform: translate(0, 0);}
    50% {transform: translate(100px, 0);}
    100% {transform: translate(100px, 100px);}
}
```

### CSS animation properties

Een CSS animation kan uit de volgende properties bestaan:
- het `@keyframes` statement
- De shorthand property `animation`
- De 8 long hand properties met hun beginwaarden:
    - `animation-name: none;`
    - `animation-duration: 0s;`
    - `animation-delay: 0s;`
    - `animation-fill-mode: none;`
    - `animation-iteration-count: 1;`
    - `animation-timing-function: ease;`
    - `animation-direction: normal;`
    - `animation-play-state: running;`

#### `animation-name`

De naam van de `@keyframe` animation die moet afgespeeld worden

#### `animation-duration`

De lengte van de animatie. Analoog als bij `transition-duration` kan je hier waarden opgeven zoals 1s voor 1 seconde of 300ms voor driehonderd milliseconden.

#### `animation-delay`

- Is vergelijkbaar met **transition-delay**. We kunnen deze property gebruiken om een wachttijd op te geven vooraleer de animatie start. Dit is vooral nuttig in situaties waarbij er verschillende animaties tegelijkertijd worden afgespeeld.

- Als de animatie een aantal keren herhaald wordt, wordt de wachttijd niet bij elke herhaling toegepast, maar enkel bij de start van de animatie (om de animatie te pauzeren zie het @keyframe voorbeeld verderop)

#### `animation-fill-mode`

Standaard zal een animatie nadat deze beëindigd is terugkeren naar haar begintoestand. Maar kan je deze bevriezen op haar eindpunt door gebruik te maken van de `animation-fill-mode` property

#### `animation-iteration-count`

Aantal keren dat de animatie afgespeeld wordt. Standaard wordt ze één keer afgespeeld. Je kan als waarde een getal opgeven of de waarde **infinite**, als je de animatie continu wilt afspelen.

#### `animation-timing-function`

- Bij een CSS animation kan je bij elk keyframe een timing function opgeven. (in het @frame statement) en je kan hiervoor dezelfde waarden gebruiken als bij `transition-timing-function`
- Ook als je slechts één enkele animation-timing-function opgeeft bij het element, zal de timing function toegepast worden op elk keyframe afzonderlijk en niet op de volledige animatie. Dit betekent dat in het voorbeeld de animatie snel start dan vertraagt bij 25% om daarna weer te versnellen en terug te vertragen bij 50% en weer te versnellen enz. 

> het is daarom dat we de timing function voor een animation meestal op **linear** plaatsen.

#### `animation-direction`

- Met deze property controleer je de richting van de animatie
- CSS animations beginnen normaal bij 0% en eindigen bij 100%
- De mogelijke waarden voor `animation-direction` zijn:
    - `normal` (default)
    - `reverse` 
    - `alternate`
    - `alternate-reverse`
- Bij `alternate` speelt de animatie van 0% naar 100% bij de eerste iteratie en bij de tweede terug van 0%, enz...

#### `animation-play-state`

Met deze property kan je een animatie pauzeren of hervatten. De default is `running`

#### Voorbeelden

```css
div{
    ...
    animation-timing-function: linear;
}
@keyframes to-right{
    ...
    75% {
        ...
        animation-timing-function: ease-out;
    }
    ...
}
```

```css
.bounce {
    animation: 2s my-bounce 2; /* duration name iteration-count */
}
@keyframes my-bounce {
    /* de animatie pauzeert van 0% tot 20% */
    0%, 20% {transform: translateY(0);}
    40% {transform: translateY(-30px);}
    50% {transform: translateY(0);}
    60% {transform: translateY(-15px);}
    /* de animatie pauzeert van 80% tot 100% */
    80%, 100% {transform: translateY(0);}
}
```

>[!tip]
> Opmerkingen:

- Je kan een animatie ook starten met :hover
```css
a:hover {
    animation: bounce 400ms;
}
```
- Gebruik `overflow: hidden` om ongewenste schuifbalken bij het afspelen van animaties te verbergen
- Je kan een volledig element transparant maken met de animatable CSS property `opacity`