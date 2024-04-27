# OOSD II - Hoofdstuk 3 - Lambda Expressies

Bij een functionele interface kan je als annotaties voor de definitie van de interface @FunctionalInterface plaatsen

Bij compilatie wordt er dan berekend indien alles correct ingesteld is voor de interface

```java
@FunctionalInterface
public interface Beheerskost{
    double geefJaarlijkseKost(double basisKost);
}
```

> Een functionele interface kan overigens maar 1 abstracte methode hebben

Verschillende manieren om een implementatie van een interface toe te passen.
- Innerklassen
- Lambda Expressies
- Methode referenties

Anonieme innerklasse:

```java
new ClassOrInterfaceName()
{
    //class body
};
```
>[!tip]
>`CTRL + a` en `CTRL + i` pas indentatie voor het volledige document toe.