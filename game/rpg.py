from enum import Enum
import random

class MonsterType(Enum):
    MAGE = 'Mago'
    WARRIOR = 'Guerreiro'
    ORC = 'Orc'

class SkillType(Enum):
    HEAL = 'heal'
    DOUBLE_HIT = 'double hit'
    SHIELD = 'shield'

def chose_skill():
    print("Escolha a habilidade especial do herói:")
    print("1 - Heal")
    print("2 - Double Hit")
    print("3 - Shield")
    choice = input("Digite o número da habilidade escolhida: ")
    if choice == '1':
        skill_chosen = SkillType.HEAL
    elif choice == '2':
        skill_chosen = SkillType.DOUBLE_HIT
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

    def is_alive(self):
        if self._current_life > 0:
            return True
        else:
            return False
    
    def damage(self, target):
        if self._attack > target._defense:
            return self._attack - target._defense
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

    def level_up(self):
        if self.first_level == True and self._exp >= 50:
            self._life += 10
            self._attack += 5
            self._defense += 2
            self._current_life = self._life
            self.first_level = False
            self._level += 1
            print(f'Level {self._level} alcançado!')
            print(f'O herói {self._name} subiu de nível! Vida: {self._life}, Ataque: {self._attack}, Defesa: {self._defense}')
        elif self.second_level == True and self._exp >= 100:
            self._life += 15
            self._attack += 7
            self._defense += 3
            self._current_life = self._life
            self._exp = 0
            self._level += 1
            print(f'Level {self._level} alcançado!')
            self.second_level = False
            print(f'O herói {self._name} subiu de nível! Vida: {self._life}, Ataque: {self._attack}, Defesa: {self._defense}')
        elif self.third_level == True and self._exp >= 150:
            self._life += 20
            self._attack += 10
            self._defense += 5
            self._current_life = self._life
            self._exp = 0
            self._level += 1
            print(f'Level {self._level} alcançado!')
            print(' ')
            self.third_level = False
            print(f'O herói {self._name} subiu de nível! Vida: {self._life}, Ataque: {self._attack}, Defesa: {self._defense}')
        elif self._exp >= 200:
            self._life += 25
            self._attack += 12
            self._defense += 6
            self._current_life = self._life
            self._exp = 0
            self._level += 1
            print(f'Level {self._level} alcançado!')
            print(f'O herói {self._name} subiu de nível! Vida: {self._life}, Ataque: {self._attack}, Defesa: {self._defense}')
        else:
            None

    def receive_exp(self, exp_given):
        self._exp += exp_given
        self._total_exp += exp_given
    
    def use_skill(self, target):
        if (self._special_skill.value == 'heal'):
            self._current_life += 10
            print(f'O herói se curou em 10 pontos de vida. Vida atual: {self._current_life}')
        elif (self._special_skill.value == 'double hit'):
            attack_damage = self.damage(target) * 2
            print(f'O herói usou Double Hit e causou {attack_damage} de dano ao monstro')
            target.receive_damage(attack_damage)
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
            input_hero = input("Selecione uma ação\n\n 1 - atacar \n 2 - usar habilidade especial\n\n")
            if input_hero == '1':
                print(' ')
                dano_causado = int(self.hero.damage(self.monster))
                self.monster.receive_damage(dano_causado)
                print(f'O herói {self.hero._name} deu {dano_causado} de dano ao monstro')
            elif input_hero == '2':
                self.hero.use_skill(self.monster)
            else:
                print('Entrada inválida!')
                continue
            if self.monster.is_alive() == False:
                    print('O monstro foi derrotado!')
                    exp_ganho = self.monster.exp()
                    self.hero.receive_exp(exp_ganho)
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
hero = Hero('Fiuza', 50, 20, 10, chose_skill())
print(f'O herói {hero._name} iniciou sua jornada com a habilidade especial: {hero._special_skill.value}')
print('')
number_battle = 1
dificulty = 1
while hero.is_alive():
    print(f'Um novo monstro do tipo {spawn_monster(dificulty)._type.value} level {dificulty} apareceu!')
    print('')
    print(f'Batalha {number_battle}:')
    battle = Battle(hero, spawn_monster(dificulty))
    battle.start_battle()
    number_battle += 1
    if number_battle % 3 == 0:
        dificulty += 1
xp_total = hero._total_exp
print(f'O herói acumulou um total de {xp_total} pontos de experiência.')
print('')
print(f'O herói lutou em {number_battle - 1} batalhas.')
print('')
print('------------------- O herói foi derrotado! Fim do jogo. -------------------')