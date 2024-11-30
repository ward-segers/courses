# Databases : Hoofdstuk 1 - Inleiding

## Databanken inleiding

Enkele voorbeelden van het gebruik van databases in het dagelijks leven:
- Betalen aan de kassa: De barcode van producten wordt gescand en in de databank wordt de prijs van het product opgezocht. Bij het kopen van het product wordt ook de stock-lijst met 1 verminderd.
- Bibliotheek: houdt een databank bij met de details van boeken, lezers, reservaties,... 
- Bankautomaat: Wanneer je geld opvraagt moet er nagegaan worden of je nog genoeg geld hebt. Wanneer je genoeg hebt staan moet er aan de databank doorgegeven worden welk bedrag er moet aangepast worden.

### Gegevensmanagement via bestanden

Vroeger werd data opgeslagen in bestanden.

> Deze aanpak is grotendeels verouderd. Enkele databankmanagement systemen maken hiervan nog gebruik. (bv. Enscribe, gebruikt door HP-NonStop mainframe)

In een bestandsgebaseerde oplossing, definieert elke toepassing zijn eigen bestanden. We gebruiken dus verschillende bestanden zonder relaties tussen deze bestanden. 

Stel we hebben een traditionele facturatie-applicatie en CRM systeem en een GIS toepassing die elk gebruik maken van informatie zoals klantnummer, klantnaam, postcode,... Wanneer deze gegevens opgenomen worden in afzonderlijke gegevensbestanden zal deze benadering voor problemen zorgen. (Elke wijziging moet op 3 verschillende locaties uitgevoerd worden.)

#### Nadelen gegevensmanagement via bestanden

##### 1. Verspreiding en isolatie van gegevens


