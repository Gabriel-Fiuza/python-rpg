⚔️ The Pythonic RPG: Legacy Edition
===================================

Um RPG de texto robusto e infinito desenvolvido em **Python**. Este projeto simula um sistema de batalha completo com mecânicas de RPG clássico, focado na aplicação prática de **Programação Orientada a Objetos (POO)** e lógica de sistemas.

🌟 Sobre o Projeto
------------------

O objetivo deste projeto foi criar um motor de jogo escalável onde um Herói enfrenta ondas infinitas de monstros. A cada batalha, a dificuldade aumenta, exigindo que o jogador gerencie recursos (ouro e poções), melhore seus atributos na loja e tome decisões estratégicas.

🚀 Funcionalidades Principais (v3.0)
------------------------------------

### 🗡️ Sistema de Combate Avançado

*   **RNG (Random Number Generation):** Implementação de chances de **Crítico** (Dano x2) e **Esquiva** (Dano 0).
    
*   **Skills Táticas:**
    
    *   Heal: Cura instantânea.
        
    *   Double Sword: Ataque devastador.
        
    *   Shield: Buff defensivo.
        
*   **Inimigos Dinâmicos:** Monstros (Mage, Warrior, Orc) gerados proceduralmente com atributos baseados na dificuldade atual.
    

### 💰 Economia e Loja (Novo!)

*   **Sistema de Moedas:** Monstros dropam ouro ao morrer.
    
*   **Loja Interativa:** O jogador pode acessar um menu de compra a cada 5 rodadas para:
    
    *   Comprar Poções de Vida.
        
    *   Afiar a Espada (Aumento permanente de Ataque).
        
    *   Reforçar Armadura (Aumento permanente de Defesa).
        

### 📈 Progressão Infinita

*   **Level Up:** O Herói acumula XP e sobe de nível, restaurando vida e aumentando status base.
    
*   **Survival Mode:** O jogo não tem fim. A dificuldade escala infinitamente até o jogador ser derrotado.
    

🛠️ Tecnologias e Conceitos
---------------------------

O código foi estruturado seguindo boas práticas de Engenharia de Software:

*   **Orientação a Objetos:** Uso intensivo de Classes, Herança (Hero herda de Personagem) e Polimorfismo.
    
*   **Encapsulamento:** Proteção de atributos sensíveis (\_life, \_coins) com métodos de acesso controlados.
    
*   **Enums:** Uso da biblioteca enum para tipagem estrita de Habilidades e Monstros, evitando erros de string.
    
*   **Game Loop:** Controle de fluxo robusto que gerencia turnos, spawn de monstros e condições de vitória/derrota sem estourar a pilha de memória.
    

💻 Como Executar
----------------

### Passo a Passo

1.  git clone https://github.com/SEU\_USUARIO/python-rpg.git
    
2.  cd python-rpg
   
3.  cd game   
    
4.  python rpg.py
    

🎨 Exemplo de Gameplay
----------------------

```bash
--------------------------Round 3--------------------------

Turno do Herói

Selecione uma ação

 1 - atacar
 2 - usar habilidade especial
 3 - Usar poção de vida

1

O herói Fiuza deu 34 de dano ao monstro
O monstro foi derrotado!

O herói ganhou 30 pontos de experiência.
-----------------------------------------------------------
Bem-vindo à loja!
Você tem 105 moedas.
1 - Poção de vida (10 moedas)
2 - Amolar espada (20 moedas)
3 - Comprar armadura (15 moedas)
4 - Sair da loja
O que você deseja comprar?

```

🧠 Trecho de Código (Destaque)
------------------------------

Exemplo da lógica de dano com implementação de sorte (RNG):

```bash
def damage(self, target):
    # Cálculo de Crítico
    if self._attack > target._defense:
        if self._crit_chance > random.random():
            print(f'Acerto crítico de {self._name}!')
            return (self._attack * 2) - target._defense
        return self._attack - target._defense
    
    # Cálculo de Esquiva
    elif self._dodge_chance > random.random():
        print(f'💨 {target._name} desviou do ataque!')
        return 0
    return 0
```

🔮 Próximos Passos
------------------

*   \[ \] Adicionar persistência de dados (Salvar/Carregar jogo em JSON).
    
*   \[ \] Implementar Boss Battles a cada 10 rodadas.
    
*   \[ \] Criar interface gráfica com Pygame ou Web.
    

Desenvolvido com 🐍 por **\[Gabriel Fiuza\]**.
