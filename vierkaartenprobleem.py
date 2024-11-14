# https://dodona.be/nl/courses/4195/series/46782/activities/1345385696


zijde=input()
inhoud=input()
resultaat=input()

if zijde == 'waarde':
    if int(inhoud) % 2 != 0 and resultaat == 'ja':
        print(f'Fout: kaarten met waarde {inhoud} moeten niet gedraaid worden.')
    elif int(inhoud) % 2 == 0 and resultaat == 'ja':
        print(f'Juist: kaarten met waarde {inhoud} moeten gedraaid worden.') 
    elif int(inhoud) % 2 != 0 and resultaat == 'nee':
        print(f'Juist: kaarten met waarde {inhoud} moeten niet gedraaid worden.')
    elif int(inhoud) % 2 == 0 and resultaat == 'nee':
        print(f'Fout: kaarten met waarde {inhoud} moeten gedraaid worden.')     
if zijde == 'kleur':
    if inhoud == 'bruin' and resultaat == 'ja':
        print(f'Juist: kaarten met kleur {inhoud} moeten gedraaid worden.')
    elif inhoud == 'bruin' and resultaat == 'nee':
        print(f'Fout: kaarten met kleur {inhoud} moeten gedraaid worden.')
    elif inhoud == 'rood' and resultaat == 'nee':
        print(f'Juist: kaarten met kleur {inhoud} moeten niet gedraaid worden.')
    elif inhoud == 'rood' and resultaat == 'ja':
        print(f'Fout: kaarten met kleur {inhoud} moeten niet gedraaid worden.')
    elif inhoud != 'bruin' and resultaat == 'nee':
        print(f'Fout: kaarten met kleur {inhoud} moeten gedraaid worden.')
    elif inhoud != 'bruin' and resultaat == 'ja':
        print(f'Juist: kaarten met kleur {inhoud} moeten gedraaid worden.')