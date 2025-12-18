from enum import Enum
import random

class MonsterType(Enum):
    MAGE = 'Mago'
    WARRIOR = 'Guerreiro'
    ORC = 'Orc'

class SkillType(Enum):
    HEAL = 'heal'
    DOUBLE_SWORD = 'double sword'
    SHIELD = 'shield'

def chose_skill():
    print("Escolha a habilidade especial do herói:")
    print("1 - Heal")
    print("2 - Double sword")
    print("3 - Shield")
    choice = input("Digite o número da habilidade escolhida: ")
    if choice == '1':
        skill_chosen = SkillType.HEAL
    elif choice == '2':
        skill_chosen = SkillType.DOUBLE_SWORD
    elif choice == '3':
        skill_chosen = SkillType.SHIELD
    return skill_chosen

def spawn_monster(dificulty):
    monster_types = [MonsterType.MAGE, MonsterType.WARRIOR, MonsterType.ORC]
    chosen_type = random.choice(monster_types)
    life = random.randint(10, 30) * dificulty
    atk = random.randint(5, 15) * dificulty
    defense = random.randint(5, 10) * dificulty
    return Monster(f'Monstro {chosen_type.value}', life, atk, defense, chosen_type)
class Personagem:
    def __init__(self, name, life, atk, defense):
        self._name = name
        self._life = life
        self._attack = atk
        self._defense = defense
        self._current_life = life
        self._crit_chance = 0.15
        self._dodge_chance = 0.05

    def is_alive(self):
        if self._current_life > 0:
            return True
        else:
            return False
    
    def damage(self, target):

        if self._attack > target._defense:
            if self._crit_chance > random.random():
                print(f'Acerto crítico de {self._name}!')
                return (self._attack * 2) - target._defense
            return self._attack - target._defense
        elif self._dodge_chance > random.random():
            print(f'{target._name} desviou do ataque!')
            return 0
        else:
            return 0
    
    def receive_damage(self, damage):
        self._current_life -= damage
        if self._current_life < 0:
            self._current_life = 0

class Hero(Personagem):
    def __init__(self, name, life, atk, defense, special: SkillType):
        super().__init__( name, life, atk, defense)
        self._special_skill = special
        self._exp = 0
        self._total_exp = 0
        self._level = 1
        self.first_level = True
        self.second_level = True
        self.third_level = True
        self._life_potion = 5
        self._coins = 0

    def level_up(self):

        xp_necessario = self._level * 40
        if self._exp >= xp_necessario:
            self._level += 1
            self._exp = 0
            self._life += 15
            self._attack += 5
            self._defense += 2
            self._current_life = self._life
            print(f'Level {self._level} alcançado!')
            print(f'O herói {self._name} subiu de nível! Vida: {self._life}, Ataque: {self._attack}, Defesa: {self._defense}')

    def show_shop(self):
        print(f'Você tem {self._coins} moedas.')
        print('1 - Poção de vida (10 moedas)')
        print('2 - Amolar espada (20 moedas)')
        print('3 - Comprar armadura (15 moedas)')
        print('4 - Sair da loja')

    def shop(self):
        print('Bem-vindo à loja!')
        self.show_shop()
        choice = input('O que você deseja comprar? ')
        while choice != '4':
            if choice == '1':
                if self._coins >= 10:
                    self._life_potion += 1
                    self._coins -= 10
                    print(' ')
                    print('Você comprou uma poção de vida!')
                    print(' ')
                    self.show_shop()
                    choice = input('O que você deseja comprar? ')
                else:
                    print(' ')
                    print('Moedas insuficientes!')
                    print(' ')
                    self.show_shop()
                    choice = input('O que você deseja comprar? ')
            elif choice == '2':
                if self._coins >= 20:
                    self._attack += 5
                    self._coins -= 20
                    print(' ')
                    print('Você amolou sua espada! Seu ataque aumentou em 5 pontos.')
                    print(' ')
                    self.show_shop()
                    choice = input('O que você deseja comprar? ')
                else:
                    print(' ')
                    print('Moedas insuficientes!')
                    print(' ')
                    self.show_shop()
                    choice = input('O que você deseja comprar? ')
            elif choice == '3':
                if self._coins >= 15:
                    self._defense += 3
                    self._coins -= 15
                    print(' ')
                    print('Você comprou uma armadura! Sua defesa aumentou em 3 pontos.')
                    print(' ')
                    self.show_shop()
                    choice = input('O que você deseja comprar? ')
                else:
                    print(' ')
                    print('Moedas insuficientes!')
                    print(' ')
                    self.show_shop()
                    choice = input('O que você deseja comprar? ')
            else:
                print(' ')
                print('Opção inválida!')
                print(' ')
                self.show_shop()
                choice = input('O que você deseja comprar? ')
        print(' ')
        print('Fechando a loja...')
        print(' ')

    def receive_exp_coin(self, exp_given):
        self._coins += exp_given
        self._exp += exp_given
        self._total_exp += exp_given

    def refresh_potion(self):
        self._life_potion += 1

    def use_potion(self):
        if (self._life_potion > 0):
            if self._current_life < self._life:
                self._current_life += 0.2 * self._life
                if self._current_life > self._life:
                    self._current_life = self._life
                print(f'O herói usou uma poção de vida e recuperou 20% da sua vida máxima. Vida atual: {self._current_life}')
            else:
                print(' ')
                print('A vida do herói já está cheia!')
                return
        else:
            print(' ')
            print('O herói não possui poções de vida!')
    
    def use_skill(self, target):
        if (self._special_skill.value == 'heal'):
            self._current_life += 10
            print(f'O herói se curou em 10 pontos de vida. Vida atual: {self._current_life}')
        elif (self._special_skill.value == 'double sword'):
            self._attack *= 2
            print(f'O herói aumentou seu ataque para {self._attack}')
        elif (self._special_skill.value == 'shield'):
            self._defense *= 1.5
            print(f'O herói aumentou sua defesa para {self._defense}')
        
    def __str__(self):
        return f'{self._name} ({self._current_life} / {self._life})'
   
class Monster(Personagem):
    def __init__(self, name, life, atk, defense, type: MonsterType):
        super().__init__(name, life, atk, defense)
        self._type = type

    def exp(self):
        if not self.is_alive():
            if self._type == MonsterType.MAGE:
                return 20
            if self._type == MonsterType.WARRIOR:
                return 15
            if self._type == MonsterType.ORC:
                return 30
        return 0

    def __str__(self):
        return f'{self._name} ({self._current_life} / {self._life})'
    
class Battle:
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster
    
    def start_battle(self):
        counter = 1
        print('')
        print(self.monster)
        print(' ')
        print(self.hero)
        print(' ')
        while self.hero.is_alive() == True:
            print(f'--------------------------Round {counter}--------------------------')
            print(' ')
            print('Turno do Herói')
            print(' ')
            input_hero = input("Selecione uma ação\n\n 1 - atacar \n 2 - usar habilidade especial \n 3 - Usar poção de vida\n\n")
            if input_hero == '1':
                print(' ')
                dano_causado = int(self.hero.damage(self.monster))
                self.monster.receive_damage(dano_causado)
                print(f'O herói {self.hero._name} deu {dano_causado} de dano ao monstro')
            elif input_hero == '2':
                self.hero.use_skill(self.monster)
            elif input_hero == '3':
                self.hero.use_potion()
                continue
            else:
                print('Entrada inválida!')
                continue
            if self.monster.is_alive() == False:
                    print('O monstro foi derrotado!')
                    exp_ganho = self.monster.exp()
                    self.hero.receive_exp_coin(exp_ganho)
                    print(' ')
                    print(f'O herói ganhou {exp_ganho} pontos de experiência.')
                    self.hero.level_up()
                    break
            print(' ')
            print('Turno do Monstro')
            print(' ')
            self.hero.receive_damage(self.monster.damage(self.hero))
            print(f'O monstro do tipo {self.monster._type.value} deu {self.monster.damage(self.hero)} de dano ao herói')
            print(' ')
            print('-------------------------------------------')
            print(f'Fim do {counter}° round')
            print('-------------------------------------------')
            print(self.hero)
            print(' ')
            print(self.monster)
            print('-------------------------------------------')
            print('')
            counter += 1
        print('-----------------------------------------------------------')

# Exemplo de uso:
hero = Hero('Fiuza', 100, 20, 25, chose_skill())
print(f'O herói {hero._name} iniciou sua jornada com a habilidade especial: {hero._special_skill.value}')
print('')
number_battle = 1
dificulty = 1
while hero.is_alive():
    time_monster = spawn_monster(dificulty)
    print(f'Um novo monstro do tipo {time_monster._type.value} level {dificulty} apareceu!')
    print('')
    print(f'Batalha {number_battle}:')
    battle = Battle(hero, time_monster)
    battle.start_battle()
    number_battle += 1
    if number_battle % 3 == 0:
        hero.refresh_potion()
        dificulty += 1
    if number_battle % 5 == 0:
        hero.shop()
xp_total = hero._total_exp
print(f'O herói acumulou um total de {xp_total} pontos de experiência.')
print('')
print(f'O herói lutou em {number_battle - 1} batalhas.')
print('')
print('------------------- O herói foi derrotado! Fim do jogo. -------------------')