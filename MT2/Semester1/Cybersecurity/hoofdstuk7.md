# CYBERSECURITY : Hoofdstuk 7 - Certificaten

## Waarom nood aan certificaten?

### Problemen

- Symmetrische encryptie
    - ⚠️ Je moet fysiek afspreken om sleutel uit te wisselen
- Asymmetrische encryptie
    - ⚠️ Je moet de juiste publieke sleutel kunnen bemachtigen
    - Wat bij een MitM attack?
        - Een hacker onderschept een publieke sleutel, vervangt deze door zijn eigen publieke sleutel en stuurt deze door
        - Niemand heeft door dat een hacker de geëncrypteerde data kan aflezen
        - Hoe kunnen we garanderen dan een publieke sleutel bij een bepaalde persoon of organisatie hoort?

## Certificaten

### Certificaten: een digitaal paspoort

- Iedereen vertrouwt een 3e persoon of organisatie
    - De Certificate Authority (CA)
- Deze deelt "Identiteitskaarten" of certificaten uit
- Dankzij de identiteitskaarten/certificaten kan iemand bewijzen dat hij of zij daadwerkelijk die persoon is
- Geen geldige identiteitskaart/certificaat? Niet te vertrouwen

## Certificate Authorities

- online werken we met Certificate Authorities (CA's) als 3e vertrouwenspersoon/-organisatie
- CA genereert certificaten voor gebruikers die dit vragen
    - Gebruikers kunnen elkaar controleren via deze certificaten of ze daadwerkelijk met de gewenste persoon communiceren
    - Een certificaat koppelt een publieke sleutel van een gebruiker aan zijn identiteit.
- Certificaten aanvragen, maken en verifiëren gebeurt allemaal met asymmetrische encryptie
    - Iedereen (CA's en gebruikers) heeft dus een asymmetrisch sleutelpaar (publieke en private sleutel) nodig

### Hoe ziet een certificaat er uit?

- Een certificaat is een digitaal ondertekend tekstbestand
- De structuur van het tekstbestand is vastgelegd volgens de x.509 standaard

**Voorbeeld**:

```console
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            72:14:11:d3:d7:e0:fd:02:aa:b0:4e:90:09:d4:db:31
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, ST=Texas, L=Houston, O=SSL Corp, CN=SSL.com EV SSL Intermediate CA RSA R3
        Validity
            Not Before: Apr 18 22:15:06 2019 GMT
            Not After : Apr 17 22:15:06 2021 GMT
        Subject: C=US, ST=Texas, L=Houston, O=SSL Corp/serialNumber=NV20081614243, CN=www.ssl.com/postalCode=77098/businessCategory=Private Organization/street=3100 Richmond Ave/jurisdictionST=Nevada/jurisdictionC=US
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:ad:0f:ef:c1:97:5a:9b:d8:1e ...
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Authority Key Identifier:
                keyid:BF:C1:5A:87:FF:28:FA:41:3D:FD:B7:4F:E4:1D:AF:A0:61:58:29:BD

            Authority Information Access:
                CA Issuers - URI:http://www.ssl.com/repository/SSLcom-SubCA-EV-SSL-RSA-4096-R3.crt
                OCSP - URI:http://ocsps.ssl.com

            X509v3 Subject Alternative Name:
                DNS:www.ssl.com, DNS:answers.ssl.com, DNS:faq.ssl.com, DNS:info.ssl.com, DNS:links.ssl.com, DNS:reseller.ssl.com, DNS:secure.ssl.com, DNS:ssl.com, DNS:support.ssl.com, DNS:sws.ssl.com, DNS:tools.ssl.com
            X509v3 Certificate Policies:
                Policy: 2.23.140.1.1
                Policy: 1.2.616.1.113527.2.5.1.1
                Policy: 1.3.6.1.4.1.38064.1.1.1.5
                  CPS: https://www.ssl.com/repository

            X509v3 Extended Key Usage:
                TLS Web Client Authentication, TLS Web Server Authentication
            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://crls.ssl.com/SSLcom-SubCA-EV-SSL-RSA-4096-R3.crl

            X509v3 Subject Key Identifier:
                E7:37:48:DE:7D:C2:E1:9D:D0:11:25:21:B8:00:33:63:06:27:C1:5B
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment
            CT Precertificate SCTs:
                Signed Certificate Timestamp:
                    Version   : v1 (0x0)
                    Log ID    : 87:75:BF:E7:59:7C:F8:8C:43:99 ...
                    Timestamp : Apr 18 22:25:08.574 2019 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
        30:44:02:20:40:51:53:90:C6:A2 ...
                Signed Certificate Timestamp:
                    Version   : v1 (0x0)
                    Log ID    : A4:B9:09:90:B4:18:58:14:87:BB ...
                    Timestamp : Apr 18 22:25:08.461 2019 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
        30:45:02:20:43:80:9E:19:90:FD ...
                Signed Certificate Timestamp:
                    Version   : v1 (0x0)
                    Log ID    : 55:81:D4:C2:16:90:36:01:4A:EA ...
                    Timestamp : Apr 18 22:25:08.769 2019 GMT
                    Extensions: none
                    Signature : ecdsa-with-SHA256
        30:45:02:21:00:C1:3E:9F:F0:40 ...
    Signature Algorithm: sha256WithRSAEncryption
         36:07:e7:3b:b7:45:97:ca:4d:6c ...
```

### Certificaten aanvragen

1. De gebruiker genereert een certificate signing request (CSR)
    - bevat zijn publieke sleutel
    - bevat zijn informatie (zijn identiteit): naam, adres
2. De CA ontvangt de CSR en controleert de identiteit van de gebruiker aan de hand van de informatie in de CSR
3. De CA creëert het gevraagde certificaat en ondertekent dit met zijn private sleutel
    - Het certificaat is nu 100% zeker afkomstig van de CA
    - Indien het certificaat vervalst wordt, wordt de handtekening ongeldig (en dus ook het certificaat)

### Certificaten verifiëren

- Alice wil een geëncrypteerd bericht versturen naar Bob
- In plaats van de publieke sleutel, stuurt Bob zijn certificaat naar Alice
    - Het certificaat bevat de publieke sleutel en is ondertekend door de CA
- Het certificaat is ondertekend met de private sleutel van de CA
    - Alice kan de geldigheid dus nagaan dankzij de publieke sleutel van de CA
        - ✅ Indien geldig: de publieke sleutel in het certificaat is volgens de CA inderdaad van Bob
        - ⚠️ Indien niet geldig: Bob is niet wie hij zegt dat hij is!
            - mogelijks een MitM attack
- Alice kan nu ook indien gewenst haar certificaat geven aan Bob
    - Bob kan dan ook op dezelfde manier achterna gaan of hij daadwerkelijk met Alice praat

### De publieke sleutel van de CA

- Hoe geraken gebruikers aan de publieke sleutel van de CA?
    - Is dit ook niet onderhevig aan een mogelijke MitM attack?
- Wie ondertekent het certificaat van de CA zelf?

### Verspreiden van CA certificaten

- CA heeft zelf ook een certificaat
- CA-certificaten worden geeïnstalleerd samen met programma's die gebruik maken van certificaten
    - OS, webbrowser (HTTPS), VPN clients, SSH clients,...
- Gebruik je een eigen CA, dan moet je deze manueel toevoegen
    - Anders krijg je een gelijkaardige fout als deze:

<p align='center'><img src='src/cert_authority_invalid.png' alt='Cert Authority Invalid error' width='50%'></p>

### Wie ondertekent het CA certificaat

- CA zelf heeft ook een certificaat
    - Wie ondertekent deze?
- De CA ondertekent zelf zijn certificaat
    - **self signed certificate**
- Iedereen kan een self signed certificate genereren
    - maar geniet geen vertrouwen van een CA!
    - Word vaak gebruikt binnen een privaat netwerk (bv. om te testen)
    - geeft meestal een foutmelding

## Toepassing: HTTPS

### HTTP

- Vroeger werd al het webverkeer plaintext verstuurd via het HTTP (webverkeer) protocol
    - iedereen kon inloggegevens afluisteren (bv. op wifi)

### HTTPS

- Tegenwoordig gebruiker browsers en web servers certificaten
    - Praten zeker met de juiste gesprekpartner (geen MitM)
    - Certificaten bevatten een publieke key en zorgen voor de mogelijkheid tot encryptie
- Gebruik van certificaten gebeurt volgens TLS/SSL protocol
    - HTTP + TLS/SSL == HTTPS
- De browser vertelt je of je via HTTP of via HTTPS surft
- Websites leiden je vaak automatisch om naar `https://` als je naar de `http://` surft
    - Indien niet, geeft de browser je vaak een foutmelding ("HTTPS only mode")
        - Wil je toch doorgaan, moet je dit expliciet aanklikken

#### HTTPS is geen internetpolitie

- HTTPS beloofd enkel
    - dat er geen MitM is
    - dat de verbinding tussen client en webserver geëncrypteerd is
- HTTPS biedt geen bescherming tegen malafide websites
    - bv. https://h0g3nt.be/
        - geeft groen slot 
            - immers garantie geen MitM en encryptie
            - Wat de website voor de rest doet is niet van belang voor HTTPS

## Toepassing: VPN

- Beveiligde communicatie over publiek netwerk
- Maakt privénetwerk over het publieke internet aan tussen verschillende fysieke locaties
    - Wordt vaak voorgesteld als een geëncrypteerde tunnel
- Gebruikt voor het verbinden van verschillende geografische locaties
    - bv. 2 kantoren op verschillende geografische locaties kunnen zo via het internet op een veilige manier verbonden worden
    - bv. Verschillende campussen van Hogent op zelfde netwerk
- Gebruikers hebben het vaak niet door
- gebruikt voor work@home
    - bv. thuis verbinden met intranet school/bedrijf
- Lijkt alsof je rechtstreeks op het school/bedrijf netwerk werkt
- Gebruikt voor privacy en tegen geo-restrictions
    - bv. Belgacom/telenet mag niet zien naar wat ik surf
    - bv. websitebeheerder mag niet zien wie ik ben
    - bv. ik wil een serie bekijken op Netflix die enkel aan Amerikaanse kijkers wordt aangeboden
- Gebruikt TLS/SSL certificaten
    - Geen MitM
    - encryptie
- Er zijn ook niet TLS/SSL VPN systemen zoals IPsec
    - out of scope voor deze cursus

### VPN logging Policy

- VPN biedt geen oneindige privacy, enkel in bepaalde gevallen
    - de VPN server ziet alles
    - is eigenlijk een bewuste MitM attack
- Vertrouw jij jouw VPN provider?
    - houden ze logs bij? (logging policy)
    - wat doen ze met jouw data?
    - VPN-bedrijven zijn niet immuun voor de wet
        - sommige bedrijven bieden wel transparancy report aan (wat gebeurt ere als de rechtbank aanklopt?)

### Anonimiteit

- 🔒 Jouw ISP ziet niet wat je doet
    - Ze zien wel dat je een VPN tunnel gebruikt
- 🔒 De website waar je naartoe surft ziet niet jouw IP-adres
    - Ze zien het IP-adres van de VPN server als verzender
    - Neem een VPN server in een ander land om geo-restrictions te voorkomen