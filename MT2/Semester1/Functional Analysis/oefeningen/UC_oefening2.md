# FUNCTIONAL ANALYSIS - Oefening 2

## USE CASE : Registratie Aanbieder

**Primary actor:** Aanbieder

**Stakeholders:** Eigenaar opleidingsplatform

**Precondities:** /

**Postcondities:** Systeem registreert Aanbieder

**Normal verloop:**

1. Aanbieder wenst zicht te registreren
2. Systeem laad de pagina
3. Aanbieder vervolledigt en voltooid de registratie
4. Systeem valideert volges DR_VELDEN
5. Systeem valideert volgens DR_WACHTWOORD
6. Systeem stuurt bevestigingsmail
7. Systeem toont bevestigingsmelding
8. Aanbieder bevestigt de regstratie

**Alternatief verloop:**

- 4A - Systeem detecteert dat DR_VELDEN faalt
    - 4A1 - Systeem toont een melding
    - 4A2 - Systeem keert terug naar stap 3 in het normaal verloop

- 5A - Systeem detecteert dat DR_WACHTWOORD faalt
    - 5A1 - Systeem toont een melding
    - 5A2 - Systeem keert terug naar stap 3 in het normaal verloop

**Domeinregels:**

- DR_VELDEN
    Alle velden mogen niet leeg zijn
- DR_WACHTWOORD
    Beide ingegeven wachtwoorden moeten dezelfde zijn.

**Op te klaren punten:**

- #
- #