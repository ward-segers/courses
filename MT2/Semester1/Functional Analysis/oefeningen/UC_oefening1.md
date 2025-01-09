# FUNCTIONAL ANALYSIS - Oefening #1

## USE CASE : Registratie Vrager

**Primary actor:** Vrager

**Stakeholders:** Eigenaar applicatie

**Precondities:** /

**Postcondities:** Systeem registreert vrager

**Normal verloop:**

1. Vrager wenst zicht te registreren
2. Systeem toont de pagina
3. Vrager vervolledigt en voltooid de registratie
4. Systeem valideert volgens DR_VELDEN
5. Systeem valideert volgens DR_WACHTWOORD
6. Systeem verstuurd bevestigingsmail
7. Systeem toont bevestiginsmelding

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