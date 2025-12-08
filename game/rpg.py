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
        self._current_life -= (damage)
        if self._current_life < 0:
            self._current_life = 0

class Hero(Personagem):
    def __init__(self, name, life, atk, defense, special):
        super().__init__(name, life, atk, defense)
        self.special_skill = special
    
    def use_skill(self, target):
        if (self.special_skill == 'heal'):
            self._current_life += 10
            print(f'O herói se curou em 10 pontos de vida. Vida atual: {self._current_life}')
        elif (self.special_skill == 'double hit'):
            attack_damage = self.damage(target) * 2
            target.receive_damage(attack_damage)
        elif (self.special_skill == 'shield'):
            self._defense *= 1.5
            print(f'O herói aumentou sua defesa para {self._defense}')
        
    def __str__(self):
        return f'Hero ({self._current_life} / {self._life})'
   
class Monster(Personagem):
    def __init__(self, name, life, atk, defense, type):
        super().__init__(name, life, atk, defense)
        self._type = type

    def __str__(self):
        return f'Orc ({self._current_life} / {self._life})'
    
class Battle:
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster
    
    def start_battle(self):
        counter = 1
        while self.hero.is_alive() == True and self.monster.is_alive() == True:
            print(f'--------------------------Round {counter}--------------------------')
            print(' ')
            print('Turno do Herói')
            print(' ')
            input_hero = input("Selecione uma ação\n\n 1 - atacar \n 2 - usar habilidade especial\n\n")
            if input_hero == '1':
                dano_causado = self.hero.damage(self.monster)
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
            print(f'O monstro do tipo {self.monster._type} deu {self.monster.damage(self.hero)} de dano ao herói')
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
            if self.hero.is_alive() == False:
                print('O herói foi derrotado!')
            elif self.monster.is_alive() == False:
                print('O monstro foi derrotado!')
        print('--------------------------Fim de jogo--------------------------')

hero = Hero('Gabriel', 10, 15, 10, 'shield')
monster = Monster('Orc', 30, 15, 10, 'fogo')
battle = Battle(hero, monster)
battle.start_battle()
