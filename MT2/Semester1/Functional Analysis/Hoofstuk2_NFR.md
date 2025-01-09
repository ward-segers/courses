# FUNCTIONAL ANALYSIS - Hoofdstuk 2 - NFR

## Soorten NFR volgens ISO 25010:2011 standaard

> Te vermelden bij Categorie NFR

- Functional Suitability
    - > = Functionele geschikheid
    - Subsoorten: 
        - > te vermelden bij indicator
        - Functionele compleetheid
            - bv. ERP moet minstens aan 75% van de functionele requirements voldoen
        - Functionele correctheid
            - bv. Loonadmin moet de lonen naar de juiste rekeningnr. overmaken
        - Functionele toepasselijkheid
            - bv. GPS-systeem moet gebruiker in minstens 9/10 gevallen naar de juiste locatie brengen

- Performance efficiency
    - > = Prestatie efficiëntie
    - Subsoorten:
        - Snelheid
            - bv. Het systeem moet 90% van de pagina's binnen de 1 second laden. De overige pagina's mogen max 3 seconden duren.
        - Middelenbeslag
            - bv. Het systeem mag niet meer dan 1MB netwerkcapaciteit en 100GB opslagcapaciteit innemen
        - Capaciteit
            - bv. Het systeem moet 1200 gebruikers aankunnen met een piek van 2500 gebruikers op de eerste dag van de maand. Tijdens de piek mag de snelheid maar 20% dalen.

- Compatibility
    - > = uitwisselbaarheid
    - Subsoorten:
        - Beïnvloedbaar
            - bv. Het systeem moet de snelheid van de taken op de achtergrond vertragen wanneer de servercapaciteit voor meer dan 80% bereikt is.
        - Koppelbaarheid
            - bv. Het datawarehouse mag mas 1 op de 100.000 berichten verkeerd geïnterpreteerd hebben

- Usability
    - > = Bruikbaarheid
    - Subsoorten:
        - Herkenbare geschiktheid
            - bv. De eerste keer dat iemand de app opent moet hij binnen de 3sec kunnen bepalen indien die voldoet aan zijn behoeft, zonder de app store te raadplegen
        - Leerbaarheid
            - bv. 95% van de beginnende studenten moet zijn oplossing op Chamilo zelfstandig kunnen indien, ookal werken ze de eerste keer met Chamilo
        - Bedienbaarheid
            - bv. Een ervaren internetgebruiker moet op basis van zijn selectiecriteria binnen de 2min zijn hotel kunnen boeken, zonder onze site voordien gebruikt te hebben. 
        - Voorkomen gebruikersfouten
            - bv. Het boekhoudpakket moet altijd voorkomen dat er door foutieve invoer onjuiste boekhoudkundige journaalposten ontstaan. De gebruiker moet gewaarschuwd worden
        - Volmaaktheid gebruikersinteractie
            - bv. Het datawarehouse mag max 1 op de 100.000 berichten vanop het verkoopsysteem verkeerd interpreteren. 
        - Toegankelijkheid
            - bv. Het in- en uitchecken via een abonnementskaart (openbaar vervoer) moet ook mogelijk zijn voor reizigers met een beperking

-  Security
    - > = beveiligbaarheid
    - Subsoorten:
        - Vertrouwelijkheid
            - bv. De geldautomaten moeten afdwingen, dat bij het aanvullen van bankbiljetten steeds geautoriseerde medewerkers aanwezig zijn.
        - Integriteit
            - bv. Het systeem kan aantonen dat een transactie geautoriseerd door Jan, effectief door Jan werd ingevoerd
        - Onweerlegbaarheid
            - bv. Het systeem moet onvervalsbaar bewijs kunnen leveren van de ontvangst van ieder order.
        - Verantwoording
            - bv. Het klantbedieningssysteem moet voor medewerker vastleggen dat die met de klant gecommuniceerd heeft
        - Authenticiteit
            - bv. Het systeem moet de identiteit van de kassière vastleggen voordat de geldlade opengaat

- Maintainability
    - > = onderhoudbaarheid
    - Subsoorten:
        - Modulariteit
            - bv. 98% van de functionele wensen moet te realiseren zijn met code aanpassingen in basismodule en/of max 1 andere module
        - Herbuikbaarheid
            - bv. Minstens een derde van de code moet herbruikbaar zijn voor andere systemen
        - Analyseerbaarheid
            - bv. Als het systeem geen elektronische berichten meer krijgt, moet de systeembeheerder binnen de 10 min dat hij hiervan op de hoogte is, de oorzaak van de fout gevonden hebben. 
        - Wijzigbaarheid
            - bv. De bankbediende moet zelf binnen de 10 minuten eenvoudige wijzigingen in het systeem kunnen aanbrengen.
        - Testbaarheid
            - bv. De beoogde werking van een nieuwe release, moet binnen de 24h gevalideerd zijn. Bij een spoedrelease binnen de 2h.

- Reliability
    - > = Betrouwbaarheid
    - Subsoorten:
        - Volwassenheid
            - bv. De spraakherkinningsoftware moet van de 5000 meest gebruikte NL woorden 89% juiste verstaan hebben
        - Beschikbaarheid
            - bv. De webshop mag niet meer dan 1 keer per half jaar 2 minuten uitliggen tussen 08:00 en 20:00
        - Foutbestendigheid
            - bv. Het boekhoudkundig systeem mag niet uitvallen door foutief ingegeven gegevens (bv. deling door 0)
        - Herstelbaarheid
            - bv. Wanneer het loonverwerkingssysteem in de week dat de lonen uitgekeerd worden uitvalt. Moet het binnen de 4h terug operationeel zijn

- Portability
    - > = Overdraagbaarheid
    - Subsoorten:
        - Aanpasbaarheid
            - bv. Desktopapplicatie moet in 2 maanden kunnen overgezet worden naar Android 10.0
        - Installeerbaarheid
            - bv. De klant moet de software (gedownload van internet) binnen 3 klikken kunnen installeren
        - Herbruikbaarheid
            - bv. Het nieuwe agendaprogramma, moet MS Outlook zonder enig probleem kunnen vervangen en gegevens ervan kunnen importeren.