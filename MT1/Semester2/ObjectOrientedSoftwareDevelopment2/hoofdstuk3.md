# OOSD II - Hoofdstuk 2 - Lambda Expressies

## Functionele Interfaces

>**Een functionele interface** is een interface met exact één abstracte methode. 

*De abstracte methode in een functionele interface kan je aanzien als een contract van een methode handtekening die je later met een lambda expressie of methode referentie kan implementeren.*

### Functionele interface uit de JavaAPI

```java
Interface Comparator<T>
```

Deze *functionele interface* heeft enkel de volgende abstracte methode:

```java
int     compare(T o1, To2)          //compares its two arguments for order
```

:arrow_right: de equals-methode overschrijft een public methode uit Object, en telt daarvoor niet als een abstracte methode.

### Zelfgedefinieerde functionele interface

Om een functionele interface gebruiken we best de annotatie `@FunctionalInterface` dit helpt op het moment van compilatie de IDE nagaan of alles correct geparemetreerd is.

```java
@FunctionalInterface
public interface HelloWorld{
    void greetSomeone(String someone);
}
```

## Anonieme innerklasse

> **Een anonieme innerklasse** is een klasse die gedefinieerd en geïnstantieerd wordt in hetzelfde statement, waarbij het geen naam krijgt.

**Syntax**:

```java
new ClassOrInterfaceName(){
    //class body
};
```

Een anonieme innerklasse kan gebruikt worden voor de implementatie van een interface of een abstracte klasse.

```java
public class EnglishGreeting{
    public void speakEnglish(){
        HelloWorld englishGreeting = new HelloWorld(){
            @Override
            public void greetSomeone(String someone){
                System.out.println("Hello" + someone);
            }
        };
        englishGreeting.greetSomeone("world3");
    }
}
```

## Lambda Expressies

In Java kunnen we een lambda expressie gebruiken om de implementatie van een functionele interface doormiddel van een anonieme innerklasse, verkort te schrijven.

**Syntax**:

```java
(parameterlijst) -> {statement}
```

>Java beschikt over 'variable type reference' waardoor de compiler vaak uit de context het type van de parameters kan afleiden. We kunnen dus meestal het type weglaten bij de parameters. Indien er maar één parameter is kunnen we ook de haakjes weglaten.

```java
public class EnglishGreeting{
    public void speakEnglish(){
        HelloWorld englishGreeting = someone -> System.out.println("Hello" + someone);
        englishGreeting.greetSomeone("world4");
    }
}
```

>[!caution]
>**Lambda expressies** kunnen enkel gebruikt worden om *functionele interfaces* te implementeren.

Met Lambda expressies zet Java een stap richting **functioneel programmeren**:
- *Declaratief programmeren*: je schrijft code die 'declareert' wat je wil doen. (geen nadruk op de implementatie)
- *Imperatief programmeren*: lijn per lijn instructies schrijven die beschrijven hoe ik iets wil bereiken.

## Methode referenties

In sommige gevallen is het enige wat een lambda expressie doet, een andere methode aanroepen. In zulke gevallen kunnen we dit nog korter en leesbaarde schrijven door te refereren naar die methode die de lambda expressie aanroept.

>**Methode referenties** laten je toe om te refereren naar een bestaande methode gebruik makende van zijn naam. Op die manier zijn methode referenties compacte en eenvoudig leesbare lambda expressies voor methodes die al een naam hebben.

```java
// voorbeeld met een static methode reference

public class EnglishGreeting{
    public void speakEnglish(){
         HelloWorld englishGreeting = EnglishGreeting::printGreeting;
    }
    private static void printGreeting(String str){
        System.out.println("Hello" + str);
    }
}
```

>[!caution]
>Merk op dat het return type en de parameterlijst van de referentie methode exact gelijk moet zijn aan deze van de abstracte methode gedeclareerd in de functionele interface!

```java
// voorbeeld met een non-static methode reference

public class EnglishGreeting{
    public void speakEnglish(){
         HelloWorld englishGreeting = new EnglishGreeting()::printGreeting;
    }
    private static void printGreeting(String str){
        System.out.println("Hello" + str);
    }
}
```

### Soorte methode referenties

<table>
<tr>
<th>Soort</th>
<th>Voorbeeld</th>
</tr>
<tr>
<td>

Een referentie naar een klasse methode `static methode`

</td>
<td>

```java
ContainingClass::staticMethodName
```

</td>
</tr>
<tr>
<td>Een referentie naar een instantie methode van een specifiek object. De instantie methode van dat object zal aangeroepen worden, het lambda argument wordt als argument doorgegeven</td>
<td>

```java
containingObject::instanceMethodeName
```

</td>
</tr>
<tr>
<td>Een referentie naar een instantie methode van een arbitrair object van een speciek type. De instantie methode zal aangeroepen worden op het lambda argument.</td>
<td>

```java
ContainingType::methodName
```

</td>
</tr>
<tr>
<td>Een referentie naar een constructor. Dit creëert een lambda die de default constructor van de gespecifieerde klasse aanroept.</td>
<td>

```java
ClassName::new
```

</td>
</tr>
</table>