⚔️ The Pythonic RPG: Survival Mode
==================================

Um sistema de batalha infinito por turnos desenvolvido em **Python**. Este projeto demonstra a evolução de conceitos de **POO**, saindo de classes básicas para o uso de **Tipagem Estrita (Enums)**, **Geração Procedural** e **Fluxo de Jogo Contínuo**.

O Herói luta contra ondas infinitas de monstros gerados aleatoriamente, acumulando experiência (XP) e utilizando habilidades especiais.

🧠 Conceitos e Tecnologias Aplicadas
------------------------------------

Este projeto vai além do básico, implementando padrões importantes de desenvolvimento:

*   **Enumerators (Enums):** Uso da biblioteca enum para criar tipos estritos (MonsterType, SkillType). Isso evita "Magic Strings" e erros de digitação, tornando o código mais seguro e profissional.
    
*   **Factory Pattern (Simplificado):** Implementação da função spawn\_monster(), que atua como uma fábrica geradora de instâncias de monstros com atributos aleatórios.
    
*   **Geração Procedural (Random):** Uso do módulo random para variar tipos de inimigos, vida, ataque e defesa a cada nova rodada.
    
*   **Sistema de Experiência (XP):** Lógica de recompensa onde diferentes tipos de monstros concedem quantidades diferentes de XP ao serem derrotados.
    
*   **Correção de Herança:** Ajuste preciso na ordem de inicialização do super().\_\_init\_\_ para garantir a integridade dos dados entre classe Mãe e Filha.
    

🎮 Novas Funcionalidades
------------------------

### 1\. Tipos de Monstros (Tipados via Enum)

O jogo agora gera três classes de inimigos, cada um valendo uma quantidade de XP:

*   🧙‍♂️ **Mage:** 50 XP
    
*   ⚔️ **Warrior:** 30 XP
    
*   👹 **Orc:** 70 XP
    

### 2\. Habilidades do Herói

O jogador pode escolher entre ações táticas baseadas em SkillType:

*   HEAL: Recupera vida.
    
*   DOUBLE\_HIT: Causa 2x o dano normal.
    
*   SHIELD: Aumenta a defesa em 50%.
    

### 3\. Loop Infinito (Survival)

Ao derrotar um monstro:

1.  O XP é creditado ao Herói.
    
2.  Um novo monstro é gerado automaticamente (spawn\_monster).
    
3.  A batalha reinicia imediatamente mantendo a vida atual do Herói.
    

🚀 Como Executar
----------------

Certifique-se de ter o Python instalado.

1.  Copie o código do github com o `git clone`.
    
2.  Execute no terminal:

```bash
python rpg-python

```
    

🛠️ Exemplo de Código (Enums)
-----------------------------

Um destaque da implementação técnica é o uso de Enums para controle de fluxo:

```bash

class MonsterType(Enum):  
    MAGE = 'Mage'     
    WARRIOR = 'Warrior'      
    ORC = 'Orc'  
    
    # No momento da criação, garantimos que o tipo é válido:  
    def spawn_monster():      
        chosen_type = random.choice([MonsterType.MAGE, MonsterType.WARRIOR, MonsterType.ORC])
        return Monster(..., type=chosen_type)

```

🔮 Roadmap (Melhorias Futuras)
------------------------------

*   \[ \] Implementar sistema de **Level Up** (Aumentar atributos quando atingir X de experiência).
    
*   \[ \] Adicionar chance de erro (Miss) nos ataques.
    
*   \[ \] Criar um Boss que aparece a cada 5 rodadas.
    
*   \[ \] Salvar o recorde de XP em um arquivo .txt.
    

_Projeto desenvolvido para estudo aprofundado de Python e Engenharia de Software._