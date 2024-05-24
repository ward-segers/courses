# Notities Computer Networks - Les 4

Opname - 00:05:11 - Overzicht lagen => Theoretisch lagen model noemen we OSI model

Default Gateway op de router, weg naar buiten op de router

Netwerk tussen routers => WAN
Kan ook wel point to point => P2P 

Adressering van de end devices => Eind bestemming van de end devices

Source en Destination staan omgekeerd in de IP tabel tov. de Ethernet tabel
=> In de ip-tabel is het niet belangrijk om te checken of the pakket al dan niet voor ons is. Het moet zowieso volledige uitgelezen worden. In de ethernet tabel is dit wel belangrijk.

>[EXAMEN] => Wat is het verschil tussen het type veld van ethernet tabel en het protocol veld van IP-tabel
>Type bepaald niveau van de derde laag (IP) protocol bepaald het niveau van de vierde laag (UDP/TCP)

SEL ==> Instellen Default Gateway

ARP: Address Resolution Protocol (Neighbor Discovery is ARP voor IPv6)
==> ARP tussen laag 2 en Laag 3 => GEEN Laag 3 protocol
==> ARP gebroadcast naar ff:ff:ff:ff:ff:ff
==> Antwoord is een unicast terug naar zender