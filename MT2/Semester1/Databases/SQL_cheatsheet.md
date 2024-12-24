# SQL Cheatsheet

<table>
<thead>
<tr>
<th>SQL</th>
<th>Beschrijving</th>
</tr>
</thead>
<tbody>
<tr>
<td>

```sql
SELECT *
FROM Werknemer
```

</td>
<td>

Selecteert alle gegevens uit de tabel Werknemers
> Na ' * ' worden de specifieke kolommen vermeld die we willen selecteren. ' * ' wijst op alle kolommen.

> Na FROM specifieren we uit welke tabel er geselecteerd moet worden.

</td>
</tr>
<tr>
<td>

```sql
SELECT *
FROM Werknemer
WHERE AfdNr='D11'
```

</td>
<td>

Selecteert alle gegevens uit de tabel Werknemer waar het AfdNr D11 is.
> We noemen dit het maken van een subset (door WHERE te gebruiken) van de volledige tabel

</td>
</tr>
<tr>
<td>

```sql
SELECT Nr, Fnaam, Afd
FROM Werknemer
```

</td>
<td>

We selecteren slechts een beperkt aantal kolommen uit de tabel Werknemer.
> Ook hier maken we een subset, door het specifiëren na de SELECT Tag

</td>
</tr>
<tr>
<td>

```sql

```

</td>
<td>



</td>
</tr>
</tbody>
</table>