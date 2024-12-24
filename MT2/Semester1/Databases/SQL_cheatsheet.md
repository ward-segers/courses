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
CURDATE()
```

</td>
<td>

geeft de huidige datim in formaat 'JJJJ-MM-DD'

</td>
<tr>
<td>

```sql
CURTIME()
```

</td>
<td>

geeft het huidig tijdstip in formaat 'UU-MM-SS'

</td>
<tr>
<td>

```sql
DATEDIFF(expr1,expr2)
```

</td>
<td>

geeft het verschil tussen expr1 - expr2 in aantal dagen

</td>
</tr>
<tr>
<td>

```sql
DATE_FORMAT(datum,format)
```

</td>
<td>

geeft de datum weer volgens de formaatspecificaties.

</td>
</tr>
<tr>
<td>

```sql
DAY()
```

</td>
<td>

is synomiem voor `DAYOFMONTH()` en geeft de dag van de maand weer als getal tussen 1 en 31

</td>
</tr>
<tr>
<td>

```sql
DAYOFWEEK(datum)
```

</td>
<td>

geeft het dagnummer van de week van de datum (1=zondag, ..., 7=zaterdag)

</td>
</tr>
<tr>
<td>

```sql
NOW()
```

</td>
<td>

geeft de huidige datum en tijd in het formaat 'JJJJ-MM-DD HH-MM-SS'

</td>
</tr>
<tr>
<td>

```sql
CONCAT(str1,str2,...)
```

</td>
<td>

geeft een string weer bestaande ui de concatenatie van alle argument

</td>
</tr>
<tr>
<td>

```sql
LEFT(str, len)
```

</td>
<td>

geeft een string bestaande uit de eerste *len*-tekens van str

</td>
</tr>
<tr>
<td>

```sql
LENGTH(str)
```

</td>
<td>

geeft de lengte van de string *str* in bytes

</td>
</tr>
<tr>
<td>

```sql
MID(str, pos, len)
```

</td>
<td>

is een synoniem voor `SUBSTRING(str, pos, len)` en geeft de substring van *str* vanaf positie *pos* met lengte *len*

</td>
</tr>
<tr>
<td>

```sql
RIGHT(str,len)
```

</td>
<td>

geeft de laatste *len* karakters van de string *str*

</td>
</tr>
<tr>
<td>

```sql
STRCMP(str1,str2)
```

</td>
<td>

geeft 0 indien beide gelijk zijn, -1 indien de eerste string kleiner is dan de tweede volgens de gehanteerde sorteringscode, zoniet is het resultaat +1

</td>
</tr>
<tr>
<td>

```sql
SELECT
    CASE
        WHEN price IS NULL THEN
            'Not yet priced'
        WHEN price<10 THEN
            'Very Reasonable Title'
        WHEN price>=10 AND 
            price<10 THEN
            'Coffee Table Title'
        ELSE 'Expensive book!'
    END AS "Price Category", 
        CONVERT(varchar(20), title)
        AS "Shortened Title"
FROM pubs.dbo.titles
ORDER BY price
```

</td>
<td>

`CASE` kan gebruikt worden wanneer we een kolom willen toevoegen gebaseerd op de waarden van een andere kolom. 

In het voorbeeld voegen we een kolom "Shortened Title" toe gebaseerd op de waarde van de kolom price
</td>
</tr>
<tr>
<td>

```sql
IF(expr1,expr2, expr3)
```

</td>
<td>

geeft expr2 indien expr1 waar is (en verschillend van 0), zoniet is het resultaat expr3

</td>
</tr>
<tr>
<td>

```sql
IFNULL(expr1,expr2)
```

</td>
<td>

geeft expr2 indien expr2 `NULL` is, zoniet geeft het expr1

</td>
</tr>
<tr>
<td>

```sql
NULLIF(expr1,expr2)
```

</td>
<td>

geeft `NULL` indien expr1 = expr2, zoniet geeft het expr1

</td>
</tr>
<tr>
<td>

```sql
CEIL(x)
```

</td>
<td>

synoniem van CEILING(x), geeft het kleinste geheel getal niet kleiner dan x.

</td>
</tr>
<tr>
<td>

```sql
FLOOR(x)
```

</td>
<td>

geeft het grootste geheel getal niet groter dan x

</td>
</tr>
<tr>
<td>

```sql
POWER(x,y)
```

</td>
<td>

synomiem voor POW(x,y) geeft x tot de macht y

</td>
</tr>
<tr>
<td>

```sql
ROUND(x)
```

</td>
<td>

geeft het geheel getal afgerond volgens de klassieke regels

</td>
</tr>
<tr>
<td>

```sql
CAST(expr AS type)
CONVERT(expr, type)
```

</td>
<td>

Beide functies zetten de expr om volgens het gespecifieerde type

</td>
</tr>
<tr>
<td>

```sql
AVG() -- berekent het gemiddelde
SUM() -- berekent de som
MIN() -- bepaald het minimum
MAX() -- bepaald het maximum
COUNT() -- bepaald aantal rijen/kolommen

-- voorbeeld:

SELECT COUNT(*), AVG(Salaris), 
    MIN(Salaris), MAX(Salaris),
    COUNT(DISTINCT Code), SUM(Salaris)
FROM Werknemer
WHERE Afd='D11'
```

</td>
<td>

Statische functies die gebruikt kunnen worden in het `SELECT`-commando. Ze houden met uitzondering van `COUNT` geen rekening met `NULL`-waarden.

- `AVG()` en `SUM()` kunnen enkel op numerieke kolommen toegepast worden
- `AVG(DISTINCT item)` of `SUM(DISTINCT item)` tellen de duplicaten niet mee.
- `COUNT(*)` - telt totaal aantal rijen (`NULL`-waarden included)
- `COUNT(kolomnaam)` - telt het aantal velden in een kolom, incl. duplicaten, `NULL`-waarden worden niet meegerekend
- `COUNT(DISTINCT kolomnaam)` - telt het aantal verschillende velden in een kolom, zonder de `NULL`-waarden

Voorbeeld: Telt het aantal Werknemers uit de afdeling D11 en geeft het maximum, minimum en gemiddelde salaris, alsook de verschillende jobcodes voor deze afdeling.

> Deze functies mogen niet voorkomen in de `WHERE`of `GROUP BY` clausule. Wel in de `HAVING` clausule

> Wanneer we functies in het `SELECT`-clausule gebruiken moeten alle kolommen een argument van een functie zijn.

</td>
</tr>
<tr>
<td>

```sql
SELECT Afd, MAX(Salaris), MIN(Salaris), 
    AVG(Salaris)
FROM Werknemer
GROUP BY Afd
```

</td>
<td>

Geeft het maximum, het minimum en het gemiddeld salaris van alle werknemers per afdeling.

Het resultaat is hier gegroupeerd in een rij per afdeling.

</td>
</tr>
<tr>
<td>

```sql
SELECT Afd, Gesl, COUNT(*)
FROM Werknemer
GROUP BY Afd, Gesl
ORDER BY Afd, Gesl DESC
```

</td>
<td>

Telt per afdeling het aantal mannen en vrouwen en sorteert oplopend de afdeling en afdalend het geslacht.

</td>
</tr>
<tr>
<td>

```sql
SELECT Afd, MAX(Salaris), MIN(Salaris), 
    AVG(Salaris)
FROM Werknemer
WHERE Geslacht='M'
GROUP BY Afd
```

</td>
<td>

Het maximum, minumum en gemiddeld loon wordt berekend voor alle mannelijke werknemers per afdeling

</td>
</tr>
<tr>
<td>

```sql
SELECT Afd, MAX(Salaris), MIN(Salaris), 
    AVG(Salaris)
FROM Werknemer
WHERE Geslacht='M'
GROUP BY Afd
HAVING COUNT(*)>2 AND MAX(Salaris)>2
    *MIN(Salaris)
```

</td>
<td>

Geeft een lijst die per afdeling het afdelingsnummer, het maximum, het minimum en het gemiddelde salaris bevat van de mannelijke werknemers.

Een afdeling komt enkel voor afdruk in aanmerking, indien ze meer dan 2 mannelijke werknemers heeft en indien het maximum mannelijk salaris meer dan 2 maal het minimum mannelijk salaris overtreft.

> `HAVING` komt steeds voor samen met `GROUP BY` en selecteert of verwerpt groepen.

</td>
</tr>
<tr>
<td>

```sql

```

</td>
<td>



</td>
</tr>
<tr>
<td>

```sql

```

</td>
<td>



</td>
</tr>
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