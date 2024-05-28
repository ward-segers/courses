# Les 6

Aantal subnets == aantal subnet bits ^ 2
Magic number => Plaats mints significante bit.

10.0.0.0/28 => Splitsen in 4 gelijke delen.
=> 4 gelijke delen => 2 bits nodig

nnnnnnnn.nnnnnnnn.nnnnnnnn.nnnnsShh

=> Magic number op plaats van 4 (hoofdletter S)

=> Subnetten:


10.0.0.0/30 (/ +2 => 2 bits gebruikt)

10.0.0.4/30

10.0.0.8/30

10.0.0.12/30

Waar eindigt de subnet berekening met magic number? 

Zet alle subnet bits op 1.

VLSM => Subnetten, niet gelijke subnetwerken

LET OP => Hostbits verdelen => ALTIJD NETW EN BROADCAST BIJ TELLEN