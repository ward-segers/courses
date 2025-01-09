# FUNCTIONAL ANALYSIS - Oefening 3

## USE CASE : Inloggen gebruiker

**Primary actor:** Gebruiker(Administrator, Aanbieder, Vrager)

**Stakeholders:** Eigenaar applicatie

**Precondities:** Gebruiker is geregistreerd in het systeem

**Postcondities:** Gebruiker wordt correct aangemeld en het juist overzichtscherm volgens rol wordt getoond. Aanmeld resultaat wordt weggeschreven in log.

**Normal verloop:**

1. De Gebruiker wenst in te loggen
2. Systeem valideert de gegevens volgens DR_LOGIN
3. Systeem valideert de rol volgens DR_ROL

**Alternatief verloop:**

- 2A - Systeem detecteert dat DR_LOGIN faalt
    - 2A1 - Systeem toont een gepaste melding
    - 2A2 - Systeem keert terug naar stap 1 in het normaal verloop

- 3A - Systeem detecteert dat DR_ROL faalt
    - 3A1 - Systeem keert terug naar stap 1 in het normaal verloop

**Domeinregels:**

- DR_LOGIN
    Logingegevens worden gecontrolleerd a.d.h.v. de opgeslagen gegevens in de database. Validatie gebeurd door de "Forms based Authentication"
- DR_ROL
    Een gebruiker kan enkel één van volgende rollen hebben: Administrator, Aanbieder, Vrager

**Op te klaren punten:**

- /