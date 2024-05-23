TIP lagen:

Please -> Physcal
Do -> Data Link
Not -> Network
Tell -> Transport
Secret -> Session
Password (to) -> Presentation
Anyone -> Application


Frame verandert niet als de hop binnen L2 toestellen blijven
=> Van een L3 naar L2 wordt het frame aangepast

Ethernet is bijna altijd full-duplex

Wifi => nog vaak half-duplex

#### EXAMEN

CSMA/CD (enkel half-duplex)
CSMA/CA (enkel half-duplex)

Carrier Sense => Voelen aan de kabel 
Multiple Access => meerdere toegang
=> Voelen aan de kabel of hij vrij is

Collision Detection => (vaak door lengte of CRC merken we dat er een collision is)
Collision Avoidance => Randomise wanneer na een collision opnieuw gestuurd wordt

!! Frame start en stop worden niet meegerekend in frame size
Adressen vooraan => Zo rap mogelijk weten wanneer door te sturen

Ethernet is slechts een implementatie van Media Access Control protocol

Taak datalink laag:

- Van de ene toestel naar het andere geraken
- Zorgen dat we op de kabel mogen spreken
- Klein beetje error detectie