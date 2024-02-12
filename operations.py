from mongo_db import search_item
from random import randint


def calculate_damage(n_dices,  weapon, modifier, advantage):
    weapon_search = search_item(weapon)
    dado = weapon_search['damage_dice']
    arma = weapon_search['weapon']
    total = 0
    valor_dado = []

    message = f'Rolando {n_dices}d{dado} + {modifier} para {arma}...\n\n'

    if advantage == "vantagem":
        rolls = []

        for i in range(2):
            total = 0
            valor_dado = []

            for n in range(n_dices):
                if arma in ["Espada Grande", "Malho"]:
                    valor_dado.append(randint(1, dado) + randint(1, dado))

                valor_dado.append(randint(1, dado))
                # print(f'Dado {n + 1}: {valor_dado[n]}')

            total = sum(valor_dado)
            rolls.append(total + modifier)

            message += f'Rolagem {i + 1} (sem modificador): {total}\n'

        rolls.sort(reverse=True)
        return message + f'\nDano total com vantagem: {rolls[0]}'
    elif advantage == "desvantagem":
        rolls = []

        for i in range(2):
            total = 0
            valor_dado = []

            for n in range(n_dices):
                if arma in ["Espada Grande", "Malho"]:
                    valor_dado.append(randint(1, dado) + randint(1, dado))

                valor_dado.append(randint(1, dado))
                # print(f'Dado {n + 1}: {valor_dado[n]}')

            total = sum(valor_dado)
            rolls.append(total + modifier)

            message += f'Rolagem {i + 1} (sem modificador): {total}\n'

        rolls.sort()
        return message + f'\nDano total com desvantagem: {rolls[0]}'
    else:
        message += 'Rolagem: '
        for n in range(n_dices):
            if arma in ["Espada Grande", "Malho"]:
                valor_dado.append(randint(1, dado) + randint(1, dado))

            valor_dado.append(randint(1, dado))
            message += f'{valor_dado[n]}'

            if n < n_dices - 1:
                message += ' + '

        total = sum(valor_dado) + modifier

        return message + f'\n\nDano total: {total}'
