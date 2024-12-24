# SQL Cheatsheet

<table>
<thead>
<tr>
<th>SQL</th>
<th>Beschrijving</th>
</tr>
</thead>
<tbody>
<tr>
<td>

```sql
SELECT *
FROM Werknemer
```

</td>
<td style="min-width: 250px;">

Selecteert alle gegevens uit de tabel Werknemers
> Na ' * ' worden de specifieke kolommen vermeld die we willen selecteren. ' * ' wijst op alle kolommen.

> Na FROM specifieren we uit welke tabel er geselecteerd moet worden.

</td>
</tr>
<tr>
<td>

```sql
SELECT *
FROM Werknemer
WHERE AfdNr='D11'
```

</td>
<td>

Selecteert alle gegevens uit de tabel Werknemer waar het AfdNr D11 is.
> We noemen dit het maken van een subset (door WHERE te gebruiken) van de volledige tabel

</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, Fnaam, Afd
FROM Werknemer
```

</td>
<td>

We selecteren slechts een beperkt aantal kolommen uit de tabel Werknemer.
> Ook hier maken we een subset, door het specifiëren na de SELECT Tag

</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, Fnaam, Afd
FROM Werknemer
WHERE AfdNr='D11'
```

</td>
<td>

Combineert beide subsets, we selecteren een beperkt aantal kolommen waar de waarde AfdNr D11 is uit de tabel Werknemer.

>[!important]
>Vraag enkel die kolommen en rijen op die je nodig hebt.

</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, VNaam, Fnaam, Afd
FROM Werknemer
WHERE Fnaam LIKE 'P%' AND Afd 
    LIKE 'D_1'
```

</td>
<td>

In SQL kunnen we karakterstrings opsporen. We gebruiken de kernwoorden `LIKE` en `NOT LIKE`. 
- een '%'- teken stelt om het even welke string van 0 of meer karakters voor:
    - string beginnend met P: 'P%'
    - string eindigend op P: '%P'
    - string beginnend met ABC: 'ABC%'
    - string eidigend op ABC: '%ABC'
    - string beginnend met A en eidigend op B: 'A%B'
    - string die ABC bevat: '%ABC%'
- een '_'-teken stelt in een string 1 enkel karakter voor
    - naam van 5 karakters beginnend met P: 'P____'
    - telefoonnummer van 5 cijfers met op de middelste plaats een 8: ' 8 '

> Indien je wildcard-symbolen wil opsporen dien je deze vooraf te laten gaan door een '.'

In het voorbeeld selecteren we het nummer, naam en afdelingsnummer van alle werknemers waarvan de familienaam start met een P en die in een afdeling werk beginnend met D en als 3<sup>de</sup> karakter een 1 hebben. 

</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, Vnaam, FNaam
FROM Werknemer
WHERE Afd='D11' AND Code=56
```

</td>
<td>

Selecteert het nummer, de voornaam, familienaam van de werknemers met een jobcode 56 uit de afdeling D11

</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, Vnaam, Fnaam
FROM Werknemer
WHERE (Afd='D11' OR Afd='D21') 
    AND (Code>54 OR Niv>15)
```

</td>
<td>

Selecteert werknemers die ofwel in afdeling D11 of D21 werken en met een code groter dan 54 of een opleidingsniveau hoger dan 15

</td>
</tr>
<tr>
<td>

```sql
SELECT Vnaam, FNaam, Afd, Niv
FROM Werknemer
WHERE Code=54 AND NOT(AFD='D11')

SELECT Vnaam, FNaam, Afd, Niv
FROM Werknemer
WHERE Code=54 AND (AFD<>'D11')
```

</td>
<td>

Geeft op twee verschillende manieren de werknemers met code 54 die in een willekeurige afdeling werken met uitsluiting van afdeling D11


</td>
</tr>
<tr>
<td colspan="2">

> [!important]
> SQL evalueert eerst de `NOT`, dan de `AND` en dan de `OR`. We kunnen de verwerkingsvolgorde wijzigen door haakjes te gebruiken. 

> Vermijd het gebruik van de `NOT` operator, dit vereist het doorzoeken van alle rijen uit de tabel.

</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, Vnaam, Fnaam, Afd
FROM Werknemer
WHERE Nr BETWEEN '100' AND '230'
```

</td>
<td>

Geeft het nummer, de naam en het afdelingsnummer van alle werknemers met een nummer tussen 100 en 200

> [!note]
> `BETWEEN` of `NOT BETWEEN` impliceert een gesloten interval (inclusief de grenzen)
</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, Vnaam, Fnaam, Niv
FROM Werknemer
WHERE Niv IN(16,18,20)
```

</td>
<td>

Geeft het nummer, de naam en het opleidingsniveau van werknemers met niveau 16,18 of 20

> Door `IN` kunnen we de inhoud van een veld vergelijken met een lijst van waarden

</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, VNaam, FNaam
FROM Werknemer
WHERE Code IS NULL
```

</td>
<td>

Selecteert alle Werknemers met als jobcode `NULL`
> `NULL` is met geen enkele vergelijking mogelijk. We moeten hier dus `IS` schrijven en niet vergelijken met '='

> `NULL` is een speciale waarde: ofwel bestaat de informatie niet ofwel is de informatie nog onbekend.

`NULL`-waarden komen voor wanneer er bij input in een bepaalde kolom geef waarde werd ingebracht en geen default waarde werd voorzien.


</td>
</tr>
<tr>
<td>

```sql
SELECT FNaam, Code, Niv, Salaris, 
    Afd
FROM Werknemer
WHERE (Afd='D11' OR Afd='E21')
    AND Niv IN (12,14,16,18)
    AND Salaris BETWEEN 15600 
        AND 23700
    AND (Fnaam NOT LIKE 'P%' 
        OR FNaam LIKE '%DE%')
    AND Code IS NOT NULL
```

</td>
<td>

Een voorbeeld van gecombineerde predicaten

</td>
</tr>
<tr>
<td>

```sql
SELECT Fnaam, Afd, Salaris/12
FROM Werknemer
WHERE Afd='A00' OR Afd='B01' 
    OR Afd='C01' OR Afd='D01'
ORDER BY Afd, 3 DESC
```

</td>
<td>

Geeft alle Werknemers uit de afdelingen A00, B01, C01, D01, geordend volgens afdelingsnummer. Binnen een afdeling moeten de rijen geordend zijn in afdalende volgorde van het maandelijks salaris.

`ORDER BY`:

- ASC (default) / DESC (oplopend vs. aflopend)
- kolom-specificatie: dit kan de kolomnaam zijn of een nummer (nummer van de kolom in het SELECT-commando)

</td>
</tr>
<tr>
<td>

```sql
SELECT DISTINCT Fnaam
FROM Werknemer
WHERE Fnaam='De Bruyn'
```

</td>
<td>

Geeft alle "unieke" Werknemers waarbij de familienaam De Bruyn is.

`DISTINCT` zorgt ervoor dat dubbele rijen (waar de Fnaam 2x gelijk is) niet worden weergegeven.


</td>
</tr>
<tr>
<td>

```sql
SELECT DISTINCT VNaam AS 'Voornaam', 
    Fnaam AS 'FamilieNaam'
FROM Werknemer
WHERE FNaam='De Bruyn'
```

</td>
<td>

Standaard worden de kolomnamen, zoals ingesteld bij de creatie van de tabel, gebruikt. Via `AS` kunnen we een andere naam specifiëren voor de kolommen in het `SELECT` commando.

> Deze aliassen kunnen we overigens ook gebruiken in de `ORDER BY`

</td>
<tr>
<td>

```sql
SELECT Vnaam + ""+ Fnaam AS werknemer, 
    Salaris*12 AS 'JaarSalaris'
FROM Werknemer
WHERE (salaris*12) > 12000
ORDER BY jaarsalaris
```

</td>
<td>

Geeft de naam en voornaam van een werknemer in 1 kolom weer als werknemers. We berekenen het jaarsalaris ipv het maandsalaris. En tonen enkel de rijen waarvoor het jaarsalaris > 12000 is en sorteren dit alls op jaarsalaris

</td>
<tr>
<td colspan=2>

### Enkele uitgeschreven functies in SQL

</td>
</tr>
<tr>
<td>

```sql

```

</td>
<td>

*Enkele bestaande functie*

</td>
<tr>
<td>

```sql

```

</td>
<td>



</td>
<tr>
<td>

```sql

```

</td>
<td>



</td>
</tr>
</tbody>
</table>