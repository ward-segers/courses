# CYBERSECURITY : Hoofdstuk 5 - Integrity

## Digitale handtekening

- Aan bestanden kan een **digitale handtekening** toegevoegd worden voor het verzekeren van de **integriteit**
- Hiermee kunnen twee zaken gecontroleerd worden:
    - het bestand is **niet gewijzigd** nadat de handtekening is gegenereerd
    - het bestand is daadwerkelijk **afkomstig van de persoon** die de handtekening geeft gegenereerd, en niet van iemand anders.
- Om dit te realiseren wordt een **asymmetrisch algoritme** gebruikt

### Hoe werkt het?

- Asymmetrische encryptie genereert een **publiek** en **private** sleutel per persoon? Deze sleutels zijn wiskundig aan elkaar gelinkt.

<p align='center'>
    <img src='src/bob.png' alt='' width='25%'>
    <img src='src/alice.png' alt='' width='25%'>
</p>

1. Alice voegt een digitale handtekening toe aan haar bericht, versleuteld met haar **private** sleutel
2. De **publieke** sleutel van Alice kan gebruikt worden om de handtekening te decrypteren. Zo wordt het volgende gecontroleerd
    - Het bericht niet is gewijzigd
        - De handtekening wordt immers ongeldig zodra er iets wijzigt in het bericht
    - Afkomstig is van Alice
        - Enkel Alice heeft immers de private sleutel om de handtekening te maken

> Dit garandeert **geen vertrouwelijkheid**, daarvoor kan het bericht na ondertekening worden versleuteld met de publieke sleutel van Bob.

#### Voorbeeld sleutelpaar

- Normaal gebruik je hiervoor software op jouw eigen computer (GPG)
- onderstaand voorbeeld zijn geen geldige sleutels

> Genereer nooit sleutels via een website voor echt gebruik!

<table>
<tr>
<td>

```console
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: OpenPGP v2.0.8

793hZyatESpYcgQplSrDXBBc9MZGRE9fvZE8Qvscr9kpf7BLJ
YU5xKVFkFuaSTx2k6Mwd2F6Mo9OoNcAdeS9vALjvtyD8TEGoPRq
SQ1rbQfIi814JW7unXg...
=bGdt
-----END PGP PUBLIC KEY BLOCK-----
```

</td>
<td>

```console
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: OpenPGP v2.0.8

xcaGBF9fhEBEADkw2xYivAYznxkZM3Rv0U0gyqj9gDbVmPloQ9f
3F0B9Tmtwht3Z8JmwPJ1GUUnT03mMlGYKtblVYPX1uAQItIaBN
CykwZ4T16g3rSa...
=UmmP
-----END PGP PRIVATE KEY BLOCK-----
```

</td>
</tr>
</table>

## Hashing algoritmes

### Een hash als integriteitscontrole

- Om te controleren dat een bestand of bericht niet gewijzigd is, kan een **hashing algoritme** of **hashfunctie** gebruikt worden
    - hierbij wordt een bepaalde waarde (**hash**) berekend en toegevoegd aan het bestand of bericht
- op een later moment kan de hashfunctie opnieuw uitgevoerd worden, en zou de **hashwaarde niet gewijzigd** mogen zijn.

#### Hashing algoritme

- Vormt een reeks van bits om naar een reeks van een vast aantal bits (alles in IT kan voorgesteld worden in bits)
- Het is een **wiskundige eenrichtingsfunctie**. Het is in de ene richting makkelijk te berekenen, maar onmogelijk in de andere richting
- Je kan dit vergelijken met het vermalen van koffiebonen. Het vermalen van bonen tot gruis is gemakkelijk, maar het terug samen plakken van gruis tot bonen is onmogelijk.
- Een andere voorbeeld is het controlecijfer in een bankrekeningnummer. Hierbij worden de 2 cijfers na de landcode van een IBAN bankrekeningnummer berekend aan de hand van de bankcode en de resterende getallen. Zo kunnen we controleren of het nummer geldig is (bv BE**68** 5390 0754 7034)


*Eigenschappen*:

- De input kan uit om het even welk aantal bits bestaan
- De output heeft steeds hetzelfde aantal bits (ongeacht het aantal bits van de input)
- De hashfunctie is een eenrichtingsfunctie en is onmogelijk om te keren
- Twee verschillende inputwaarden zullen steeds een verschillende outputwaarde geven

*MD5 en SHA*

- het **Message Digest 5 Algoritme** (MD5): ontwikkeld door Ron Rivest en geeft 128-bits output terug
- het **Secure Hash Algorithm** (SHA): ontwikkeld door NIST (National Institute of Standards and Technology)
    - Verschillende varianten afhankelijk van het aantal gewenste output bits:
        - SHA-224 (224 bits), SHA-256 (256 bits), SHA-384 (394 bits), SHA-512 (512 bits)
- uiteraard zijn er nog andere hashing algoritmes

### Botsingen

- Hashing algoritmes moeten in theorie altijd een andere output hebben voor verschillende inputs
- In de praktijk is dit niet steeds mogelijk, er zijn immers veel meer mogelijke inputs dan outputs (met vast aantal bits)
- Wanneer je voor 2 verschillende inputs dezelfde output waarde krijgt, spreekt men van een **botsing of collision**
- Een hashing algoritme verliest zijn nut als botingen bewust veroorzaakt kunnen worden

```console
password                hash
Hash(qwertyqwerty)  ==  548defa8
Hash(ietsAnders)    ==  548defa8
```

### Sterke en zwakke algoritmes

Hashing algoritmes kunnen onderverdeeld worden in zwakke en sterke hashing algoritmes
- **MD5** en **SHA-1** zijn zwakke algoritmes waarbij botsingen bewust veroorzaakt kunnen worden.

> Zwakke algoritmes zijn niet (meer) bruikbaar voor cybersecurity doeleinden

- **SHA-2** en **SHA-3** zijn **sterke algoritmes** die wel nog gebruikt worden voor cybersecurity doeleinden

## Toepassingen van hashing algoritmes

- controle op fouten in data
- Het veilig bewaren en controleren van wachtwoorden
- Identificeren van data aan de hand van een kleinere waarde (hash als fingerprint)
- Efficiënte opslag van data in hashtabellen 

### Controle op fouten

- Via een hashing algoritme kan je van een digitaal bestand de hashwaarde berekenen en dit toevoegen aan het bestand of publiceren op een website
- De hashwaarde kan op een later moment opnieuw berekend worden, bv. na downloaden van het bestand van een server
- Indien de nieuwe hashwaarde verschillend is, is het bestand gewijzigd en dus mogelijks onbruikbaar (bv. door een fout tijdens de download)

### Veilig bewaren van wachtwoorden

- Gebruikersnaam en wachtwoord worden vaak bewaard in databanken
- Databanken zijn een efficiënte manier om data op te slaan, analyseren en op te vragen
- Databanken zijn een gewild doelwit van cybercriminelen
- Een gelekte hoeveelheid gegevens uit een databank noemt men een **Data Breach**
- Als een datalek gebruikersnamen en wachtwoorden bevat, zullen cybercriminelen die uittesten op andere websites
    - dit is een grote oorzaak van hacks
- Gebruik bij voorkeur een wachtwoordmanageren maak een uniek wachtwoord per website

*Poging 1*: we slaan de gebruikersnaam en het wachtwoord gewoon op in de databank, bij het inloggen moeten we dan het volgende controleren:
- Ingevulde gebruikersnaam == gebruikersnaam in databank?
- Ingevulde wachtwoord == wachtwoord in databank?

Dit noemen we ookwel **plaintext** opslag
- eenvoudig
- iemand met toegang tot de databank kan alle wachtwoorden uitlezen. ⚠️ GEVAARLIJK!

<table>
<tr>
<th>Gebruikersnaam</th>
<th>Paswoord</th>
</tr>
<tr>
<td>tom@gmail.com</td>
<td>

`Dit is een ST3rk Paswoord!`

</td>
</tr>
<tr>
<td>hanne@outlook.com</td>
<td>

`zwakpaswoord`

</td>
</tr>
</table>

*Poging 2*: we slaan de gebruikersnaam en de **hashwaarde van het wachtwoord** op in de databank. Bij inloggen moeten we het volgende controleren:
- Ingevulde gebruikersnaam == gebruikersnaam in databank?
- Hash(Ingevulde wachtwoord) == hashwaarde in databank?

- iets complexer, maar hashwaarden kunnen snel berekend worden
- Het plaintext wachtwoord wordt nooit opgeslagen
- iemand met (al dan niet geautoriseerde) toegang tot de databank kan de wachtwoorden NIET uitlezen: ✅ VEILIG!

<table>
<tr>
<th>Gebruikersnaam</th>
<th>Paswoord</th>
</tr>
<tr>
<td>tom@gmail.com</td>
<td>

`b30ead2d465295bd47ki4lkyu3a8cvzxd6g84`

</td>
</tr>
<tr>
<td>hanne@outlook.com</td>
<td>

`78062a5218ad971fb4m44io997zdfgzs321jk`

</td>
</tr>
</table>

#### Salting

- Wanneer 2 gebruikers hetzelfde wachtwoord gebruiken, zal voor beiden dezelfde hashwaarde worden opgeslagen
    - hierdoor weten aanvallers dat ze door 1 wachtwoord te kraken 2 vliegen in 1 klap slaan
- **Salting** is een extra maatregel om hashing veiliger te maken
    - Een random reeks bits (**salt**) die wordt toegevoegd aan het wachtwoord voordat de hash berekend wordt
- Hetzelfde wachtwoord geeft zo een verschillende hash: ✅✅ VEILIG!

```console
     password       salt         hash
Hash(qwertyqwerty + 4g74e57q) == 8fg41jk3235e4wr48
Hash(qwertyqwerty + avb7d2fs) == wqrhjk485s6ef8gfg
```

#### Samenvatting

- Plaintext : ⚠️ GEVAARLIJK
- Hash wachtwoord: ✅ MATIG VEILIG. Dezelfde paswoorden geven dezelfde hashwaarden, dit kan misbruikt worden door cybercriminelen.

<table>
<tr>
<th>Gebruikersnaam</th>
<th>Paswoord</th>
</tr>
<tr>
<td>tom@gmail.com</td>
<td>

`b30ead2d465295bd47ki4lkyu3a8cvzxd6g84`

</td>
</tr>
<tr>
<td>hanne@outlook.com</td>
<td>

`78062a5218ad971fb4m44io997zdfgzs321jk`

</td>
</tr>
</table>

- Hash + salt : ✅✅ EXTRA veilig

<table>
<tr>
<th>Gebruikersnaam</th>
<th>Salt</th>
<th>Paswoord</th>
</tr>
<tr>
<td>tom@gmail.com</td>
<td>

`D;%yL9TS:5PalS/d89`

</td>
<td>

`b30ead2d465295bd47ki4lkyu3a8cvzxd6g84`

</td>
</tr>
<tr>
<td>hanne@outlook.com</td>
<td>

`)<,s-<U(jLezy4j>\*`

</td>
<td>

`78062a5218ad971fb4m44io997zdfgzs321jk`

</td>
</tr>
</table>

## Kraken van hashing

- Bij het kraken van hashing probeer je voor een gekende hashwaarde (output) een overeenkomstige input te vinden
- vanuit een hashwaarde de oorspronkelijke input berekenen is zo goed als onmogelijk (eenrichtingsfunctie!)
- Een mogelijkheid is om van elke mogelijke inputwaarde de hashwaarde te berekenen tot je dezelfde hash hebt (bruteforce attack) eventueel met een dictionary

### Rainbow Tables

- Je kan ook van verschillende inputs de hash berekenen, tot je een lijst hebt met alle mogelijke hashwaarden en de input
- Deze lijst kan gesorteerd worden op basis van de hashwaarde, zodat je snel input voor een hash kan vinden

> Een dergelijke lijst noemen we **een Rainbow Table**

- Het opstellen van een rainbow table moet maar 1 keer gebeuren: je kan dezze dus downloaden van het internet
- Het toevoegen van een salt aan een wachtwoord maakt Rainbow Tables onbruikbaar voor het kraken!

### Vertragende hashing algoritmes

- om te vermijden dat er veel pogingen worden gedaan om een hash te kraken of een collision te vinden wordt er vaak gebruik gemaakt van vertragende hashing algoritmes
- Een aanvaller met meer rekenkracht moet zo toch nog steeds lang wachten om de hashwaarde te kraken
- Bekende voorbeelden:
    - PBKDF2
    - bcrypt
    - Argon2

## HMAC

### Hashing met symmetrische encryptie

- om integriteit en authenticiteit te garanderen van een bericht kunnen we hashing combineren met symmetrische encryptie
- hash-based message authentication (**HMAC**) is een hashfunctie die naast de input ook gebruik maakt van een symmetrische sleutel voor de berekening van de hashwaarde
- Dit lijkt goed op digitale handtekeningen, maar bij digitale handtekeningen wordt asymmetrische encryptie gebruikt

### Werking HMAC

- Alice (verzender):
    1. Berekent de hashwaarde van het (versleuteld) bericht via HMAC met behulp van de gedeelde geheime sleutel
    2. Voegt deze waarde (HMAC digest of vingerafdruk) toe aan het bericht en stuurt dit naar Bob

<p align='center'><img src='src/hmac.png' alt='HMAC' width='50%'></p>

- Bob (ontvanger):
    1. Berekent na ontvangen van het bericht zelf de hashwaarde via HMAC met dezelfde sleutel
    2. Vergelijkt deze waarde met de waarde die Alice toevoegde aan het bericht
    3. Indien beide waarden overeenkomen weet Bob dat het bericht niet gewijzigd is, en dat het afkomstige is van Alice.

### Nut van HMAC

- HMAC biedt dus bescherming tegen een Man-in-the-Middle attack: via gewone hashing zou een aanvaller een nieuwe hash kunnen berekenen na aanpassing van het bericht
- Bij HMAC is de symmetrische sleutel geheim, en dus enkel gekend door de zender en ontvanger van het bericht
- HMAC garandeert dus integriteit (bericht is niet gewijzigd) nen authenticiteit (afkomstig van Alice)