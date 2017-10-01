gebruiker = input('Geef je naam: ')
beginstation = input('Wat is je beginstation: ')
eindstation = input('Wat is je eindstation: ')
aanelkaar = gebruiker + beginstation + eindstation


def code(invoerstring):
    code = ""
    for i in invoerstring:
        code += chr(ord(i) + 3)
    print(code)


code(aanelkaar)
