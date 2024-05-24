# Notities Computer Networks - Les 5

192.168.10.1 => Dotted decimal notatie
Van 0 tot en met 255 => 8 bits => 1 byte => In totaal 4 bytes

8 host bits => 0 tem 255 => 256 mogelijkheden (netwerkadres en Broadcastadres included) => Uiteindelijk 254 mogelijke adressen
netwerkadres => hostbits allemaal op 0
Broadcastadres => hostbits allemaal op 1

Netwerkgedeelte in het IP-adres kan ook verzet worden:
nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnnhhhh
netwerk                        | hosts
=> 4 host bits => 4*2 => 16 mogelijke hosts (0 -> 15) - netwerkadres en - Broadcastadres => 14 mogelijke toestellen

=> Uit dotted decimal notatie kunnen we het netwerk gedeelte niet afleiden.
==> Hiervoor hebben we het subnetmask nodig.

Subnetmask : 255.255.255.0
=> Vertalen naar binair om het masker af te kunnen leiden

==> 11111111.11111111.11111111.00000000 <br>
==> nnnnnnnn.nnnnnnnn.nnnnnnnn|hhhhhhhh <br>
Ip-adres: 192.168.10.1 <br>
==> 11000000.10101000.00001010.00000001 <br>
==> 11111111.11111111.11111111.00000000 <br>
Netwerkadres bepalen we door logical AND op de subnetmask en het ipadres uit te voeren <br>

==> 11000000.10101000.00001010.00000000

>[EXAMEN] <br>
>Gegeven: <br>
>netwerkmask: 255.255.255.240 <br>

=> Binair: <br>
240 - 128 - 64 - 32 - 16 = 0 => 11110000 <br>
11111111.11111111.11111111.1111 |0000 <br>
                                |4 host bits => 16 toestellen (incl netwerk en broadcast)

Broadcastadres: <br>
11000000.10101000.00001010.0000 |1111
192.168.10.15

>[EXAMEN] <br>
>Gegeven: <br>
>PC1 IP: 192.168.22.155 (netwerkmask) 255.255.248.0 <br>
>PC2 IP: 192.168.30.1 (netwerkmask) 255.255.248.0 <br>
>Vraag: Zitten deze hosts op hetzelfde netwerk?

STAP 1: omzetten naar binair: <br>
PC1: 11000000.10101000.00010110.10011011 <br>
netw mask: 11111111.11111111.11111|000.00000000 <br>
netw adres= 11000000.10101000.00010|000.00000000 <br>
Decimaal netw adres: 192.168.16.0

PC2 IP: 192.168.30.1 <br>
11000000.10101000.00011110.00000001 <br>
netw mask: 11111111.11111111.11111|000.00000000 <br>
netw adres: 11000000.10101000.00011|000.00000000 <br>
Decimaal: 192.168.24.0 <br>

=> Netw adres van PC1 en PC2 is verschillend

>[EXAMEN] <br>
>Gegeven: <br>
>PC1 IP: 10.0.55.9 (netwerkmask) 255.240.0.0 <br>
>Wat is het eerste (bruikbare) adres
>Wat is het netw adres
>Wat is het broadcast adres
>Hoeveel host maximaal

IP Binair: <br>
00001010.00000000.00110111.00001001 <br>
Mask binair: <br>
11111111.11110000.00000000.00000000 <br>
AND (netwerkadres): <br>
00001010.00000000.00000000.00000000 <br>
Binair: 10.0.0.0 <br>
Eerst mogelijke (bruikbare) adres: 10.0.0.1 <br>
#mogelijke hosts? <br>
broadcast: <br>
00001010.00000000.00000000.00000000 <br>
AND <br>
11111111.11110000.00000000.00000000 <br>
00001010.00001111.11111111.11111111 <br>
10.15.255.255 (broadcast) <br>
range: tussen: <br>
10.0.0.0 en 10.15.255.255 <br>
Gemakkelijkst binair te berekenen: <br>
Aantal 0 bits in het netwerkmask => 20 => 20 bits <br>
Aantal mogelijkheden => 2^20 => 1048576 - 1 - 1 => 1048574

>[!important]
>Veel nullen in een netwerkmask => groot netwerk

==> /24 => Netwerkmask staat op 24e bit <br>
==> 255.255.255.0

### Hulptabel subnetmasks: (noteren op examen)
/8 => 11111111.00000000.00000000.00000000 <br>
=> Hoeveel hosts? (maximaal) => 2^24 (aantal nullen) -1 -1 = 16777214 - 1 -1 = 16777212 
/16 => 11111111.11111111.00000000.00000000 <br>
/25 => 11111111.11111111.11111111.10000000 <br>
/26 => 11111111.11111111.11111111.11000000 <br>
/27 => 11111111.11111111.11111111.11100000 <br>
/28 => 11111111.11111111.11111111.11110000 <br>
/29 => 11111111.11111111.11111111.11111000 <br>
/30 => 11111111.11111111.11111111.11111100 <br>

| Prefix-lengte (/) | subnetmask | # hosts |
| ----------------- | ---------- | ------- |
| /8 | 255.0.0.0 | 2^24 -2 |
| /16 | 255.255.0.0 | 2^16 -2 |
| /24 | 255.255.255.0 | 2^8 -2 |
| /25 | 255.255.255.128 | 2^7 -2 = 126 |
| /26 | 255.255.255.192 | 2^6 -2 = 62 |
| /27 | 255.255.255.224 | 2^5 -2 = 30 |
| /28 | 255.255.255.240 | 2^4 -2 = 14|
| /29 | 255.255.255.248 | 2^3 -2 = 6 |
| /30 | 255.255.255.252 | 2^2 -2 = 2 |

Waarom NAT => Network Adress Translation? <br>
=> Te weinig beschikbare IP adressen voor aantal devices <br>
==> Router zorgt intern voor een vertaalslag op de private IP-adresses => Ranges te kennen voor EXAMEN

IPv6 => Vergroten aantal beschikbare addressen => 2^64

NAT valt weg bij IPv6

=> Private adressen range van buiten kennen

