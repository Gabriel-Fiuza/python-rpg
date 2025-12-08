⚔️ The Pythonic RPG Battle System
=================================

Um sistema de batalha por turnos desenvolvido em **Python** para aplicar e demonstrar conceitos fundamentais de **Programação Orientada a Objetos (POO)**.

O projeto simula um combate entre um Herói (com habilidades especiais) e um Monstro, gerenciando turnos, cálculo de dano, defesa e condições de vitória.

🧠 Conceitos Aplicados
----------------------

Este projeto foi desenvolvido com foco nas seguintes práticas de Engenharia de Software:

*   **Programação Orientada a Objetos (POO):** Organização do código em classes (Personagem, Hero, Monster, Battle).
    
*   **Herança:** Reutilização de código onde Hero e Monster herdam atributos e métodos da classe base Personagem.
    
*   **Encapsulamento:** Uso de atributos protegidos (ex: \_life, \_attack) para preservar a integridade do estado dos objetos.
    
*   **Lógica de Game Loop:** Implementação de um laço while para gerenciar os turnos da batalha até que uma condição de fim (HP <= 0) seja atendida.
    
*   **Polimorfismo:** Estrutura preparada para suportar diferentes comportamentos de ataque e habilidades.
    

🎮 Funcionalidades
------------------

*   **Criação de Personagens:** Atributos personalizáveis de Vida, Ataque e Defesa.
    
*   **Sistema de Habilidades:** O Herói possui habilidades únicas:
    
    *   heal: Recupera 10 pontos de vida.
        
    *   double hit: Causa o dobro de dano no turno.
        
    *   shield: Aumenta a defesa em 50% temporariamente.
        
*   **Log de Batalha:** Interface via terminal (CLI) que narra cada rodada, mostrando dano causado e vida restante.
    

🚀 Como Executar
----------------

Certifique-se de ter o Python instalado.

1.  Copie o código do jogo para um arquivo chamado main.py.
    
2.  Adicione o seguinte bloco ao final do arquivo para iniciar o jogo:
    

```bash
# Instanciando o Herói (Nome, Vida, Ataque, Defesa, Habilidade)
heroi = Hero("Aragorn", 100, 20, 5, "double hit")  
# Instanciando o Monstro (Nome, Vida, Ataque, Defesa, Tipo) 
monstro = Monster("Orc", 80, 15, 2, "Guerreiro")  
# Iniciando a Batalha      
batalha = Battle(heroi, monstro)      
batalha.start_battle()
```

1.  Em seguida, execute no terminal:
    
```
   python rpg.py
```

🛠️ Próximos Passos (Roadmap)
-----------------------------

Futuras melhorias planejadas para o projeto:

*   \[ \] Adicionar aleatoriedade (Random) para danos críticos e esquivas.
    
*   \[ \] Implementar sistema de níveis (Level Up).
    
*   \[ \] Criar inventário de itens (poções).
    
*   \[ \] Criar novos tipos de monstros com habilidades específicas.
    

_Desenvolvido para fins de estudo em Python e POO._
