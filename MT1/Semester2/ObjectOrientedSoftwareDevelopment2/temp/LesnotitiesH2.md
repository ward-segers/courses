# OOSD II - Hoofdstuk 2 - Polymorfisme en interfaces

Upcasting: Variabele van de superklasse verwijst naar een variabele van het subklasse

Downcasting: Variabele van de superklasse doen verwijzen naar subklasse bv:

```java
Rechthoek r2 = new Vierkant();

if(r2 instanceof Vierkant v){
    //het element van de klasse Rechthoek wordt gedowncast automatisch 
    //via instanceof Vierkant naar een element v van de klasse Vierkant
}
```
