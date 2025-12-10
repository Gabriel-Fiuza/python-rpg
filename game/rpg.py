from enum import Enum
import random

class MonsterType(Enum):
    MAGE = 'Mage'
    WARRIOR = 'Warrior'
    ORC = 'Orc'

class SkillType(Enum):
    HEAL = 'heal'
    DOUBLE_HIT = 'double hit'
    SHIELD = 'shield'

def spawn_monster():
    monster_types = [MonsterType.MAGE, MonsterType.WARRIOR, MonsterType.ORC]
    chosen_type = random.choice(monster_types)
    life = random.randint(20, 50)
    atk = random.randint(5, 15)
    defense = random.randint(1, 10)
    return Monster('Orc', life, atk, defense, chosen_type)
class Personagem:
    def __init__(self, name, life, atk, defense):
        self._name = name
        self._life = life
        self._attack = atk
        self._defense = defense
        self._current_life = life
        self._exp = 0

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
        self.special_skill = special

    def receive_exp(self, exp_given):
        self._exp += exp_given
    
    def use_skill(self, target):
        if (self.special_skill.value == 'heal'):
            self._current_life += 10
            print(f'O herói se curou em 10 pontos de vida. Vida atual: {self._current_life}')
        elif (self.special_skill.value == 'double hit'):
            attack_damage = self.damage(target) * 2
            target.receive_damage(attack_damage)
        elif (self.special_skill.value == 'shield'):
            self._defense *= 1.5
            print(f'O herói aumentou sua defesa para {self._defense}')
        
    def __str__(self):
        return f'Hero ({self._current_life} / {self._life})'
   
class Monster(Personagem):
    def __init__(self, name, life, atk, defense, type: MonsterType):
        super().__init__(name, life, atk, defense)
        self._type = type

    def exp(self):
        if not self.is_alive():
            if self._type == MonsterType.MAGE:
                return 50
            if self._type == MonsterType.WARRIOR:
                return 30
            if self._type == MonsterType.ORC:
                return 70
        return 0

    def __str__(self):
        return f'Orc ({self._current_life} / {self._life})'
    
class Battle:
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster
    
    def start_battle(self):
        counter = 1
        while self.hero.is_alive() == True:
            print(f'--------------------------Round {counter}--------------------------')
            print(' ')
            print('Turno do Herói')
            print(' ')
            input_hero = input("Selecione uma ação\n\n 1 - atacar \n 2 - usar habilidade especial\n\n")
            if input_hero == '1':
                dano_causado = int(self.hero.damage(self.monster))
                self.monster.receive_damage(dano_causado)
                print(f'O herói {self.hero._name} deu {dano_causado} de dano ao monstro')
            elif input_hero == '2':
                self.hero.use_skill(self.monster)
            else:
                print('Entrada inválida!')
                continue
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
            if self.monster.is_alive() == False:
                print('O monstro foi derrotado!')
                exp_ganho = self.monster.exp()
                self.hero.receive_exp(exp_ganho)
                print(f'O herói ganhou {exp_ganho} pontos de experiência!')
                Battle(hero, spawn_monster()).start_battle()
        print('--------------------------Fim de jogo--------------------------')

# Exemplo de uso:
hero = Hero('Aragorn', 100, 20, 10, SkillType.HEAL)
battle = Battle(hero, spawn_monster())
battle.start_battle()