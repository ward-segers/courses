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

Probeer zoveel mogelijk `nullpointers` te vermijden door de attributen `final` te declareren.

DTO -> Verschillende type objecten kunnen via eenzelfde DTO doorgegeven worden via verschillende constructoren.

Verschillende soorten interfaces:

- Comparable interface => Altijd met methode `compareTo()` 

```java

public interface Comparable<T>{
    public int compareTo(T o);
}

//T is de de klasse waartoe we objecten gaan vergelijken
//o is het object dat we vergelijken

```

==> Voor verschillende klassen bestaan er reeds een compareTo-methode (zoals voor String)

- Comparator interface => Vergelijken tussen 2 verschillende objecten
==> Hiervoor moeten we een aparte klasse maken die de Comparator implements