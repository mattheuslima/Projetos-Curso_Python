def voto(age):
    from datetime import date
    this_year = date.today().year
    player_age=this_year-age
    if (this_year-age)<16:
        return f'Você tem {player_age} anos.\nVocê ainda não tem idade para votar.'
    elif (this_year-age)>18:
        return f'Você tem {player_age} anos. \nVocê já tem idade para votar.'
    else:
        return f'Você tem {player_age} anos.\nVocê tem idade para votar, porém seu voto é OPCIONAL.'


#Main program
idade = int(input('Em que ano você nasceu? '))
print(voto(idade))
