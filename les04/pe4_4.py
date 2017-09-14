def new_password(oldpassword, newpassword, repeatpassword):
    if oldpassword != newpassword:
        if len(newpassword) >= 6 :
            if has_numbers(nieuw_wachtwoord):
                if newpassword == repeatpassword:
                    return True
                else:
                    print('De wachtwoorden komen niet overeen.')
            else:
                print('Het wachtwoord moet een cijfer bevatten.')
                return False
        else:
            print('Het wachtwoord moet langer dan 5 karakters zijn.')
            return False
    else:
        print('U heeft een oud wachtwoord gebruikt.')
        return False


def has_numbers(wachtwoord):
    return any(char.isdigit() for char in wachtwoord)

password_changed = False

oud_wachtwoord = input('Oud wachtwoord: ')
nieuw_wachtwoord = input('Nieuw wachtwoord: ')
herhaal_wachtwoord = input('Herhaal nieuw wachtwoord: ')

if new_password(oud_wachtwoord, nieuw_wachtwoord, herhaal_wachtwoord):
    print('Uw wachtwoord is gewijzigd')

