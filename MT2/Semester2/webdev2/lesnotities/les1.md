# Les 1 & 2 & 3: introductie in Javascript

- JS Strict mode

--> Zorgt ervoor dat sommige oude features niet meer uitgevoerd worden.

`'use strict';`

Zorgt bv dat variabelen eerst moeten gedefiniëerd worden.

- Variabelen worden gedeclared:

```javascript
let message; // kan veranderen
let user, age;

const admin; // constante variabele
```

- alert() -> Opent alert window

>[!important]
>Gebruik zoveel mogelijk const, enkel let wanneer nodig

- type checken van een object

```javascript
typeof(object)
```

- loosely typed

```javascript
const test = 10 + true + false; // zal waarde van 11 hebben (waarde true = 1, waarde false = 0)
```

- controleren of iets niet een nummer is 

```javascript
isNaN(number);
```

- conversie

```javascript
parseInt();
parseFloat();
number.toString(); // omvormen naar een string -> aanroepen op de variabele
```

- template literal

```javascript
console.log(`Fifteen is ${a + b}`)
```

- Wrapper objecten met properties/methodes

```javascript
Number.toFixed(); // can op elk Number type aangeroepen worden
Number.toString(2);  // can op elk Number type aangeroepen worden (met 2 tussen haakjes -> binair getal)

... // zie oefeningen
```

- Datum

```javascript
const today = new Date(); // verschillende methodes mogelijk
```

- nullish operator

```javascript
a??b; // als a bestaat gebruik die -> anders de volgende
```

- Hoisting:

Defenitie van functies wordt eerst uitgevoerd.
> We kunnen dus een functie aanroepen voor deze gedefiniëerd is.

Enkel geldig voor functies => niet voor variabelen of functie declaraties

- destructuring

```javascript
const pizzas = ['funghi','margaritta','barbecue'];
const [pizza1, ,pizza2] = pizzas;

//pizza1 = funghi, pizza2 = barbecue
```

- modules: importeren van andere bestanden in JS.
    - let op de extensie!

- Object chaining > propertie van een object in een object opvragen

```javascript
object.object.property;
```

- Destructuring objecten:

```javascript
const {name, gender: sex} = myObject; // gender passen we toe aan de variabele sex
```

- Objecten die aangepast worden in een beperkte scope worden ook buiten de scope aangepast

- In methodes steeds gebruik maken van `this`-keyword om properties van het object te refereren

- In een object kunnen we geen arrow-functies gebruiken -> `this` verwijst naar `Window`-object

- window.onload -> event bij het laden van de pagina
    - Gebruiken we om de eventhandlers in te stellen

- Bij een event de functie als variabele toewijzen, de functie moet niet direct uitgevoerd worden, maar gekoppeld worden aan het even

