# LuckyRoller
Lucky Roller é um bot para Discord para rolagem de dados no RPG Dungeons &amp; Dragons.

- Projeto pessoal utilizando pela primeira vez MongoDB e Discord bot.

Primeira versão de um bot para o discord para rolagem de dano no RPG de mesa D&amp;D
- Requirements:
  - discord.py
  - Pymongo

O bot é simples, com apenas 3 comandos (com a possibilidade de expandir em versões futuras):
- **/ajuda**: Mostra a lista de comandos e como utiliza-los
- **/armas**: Mostra uma lista de armas em PT-BR disponíveis para utilizar. É a mesma lista presente no Livro do Jogador.
- **/roll**: Comando para a rolagem respeitando o formato _quantidade de dados + arma + modificador + vantagem/desvantagem/normal_
  - **quantidade de dados**: número de dados na rolagem
  - **arma**: o nome da arma, não é _case sensitive_. Ou seja, pode ser 'machado grande', 'Machado Grande' ou 'MACHADO GRANDE'. A única restrição é que digite o nome correto e em PT-BR
  - **modificador**: o valor a ser somado na rolagem de dano (modificador de força, destreza...)
  - **vantagem/desvantagem/normal**: se a rolagem será normal, com vontagem ou desvantagem
 
#### MongoDB
A utilização do Mongo é opcional, a lista de armas pode ser mantida em um dicionário. Pretende-se adicionar mais armas em versões futuras.
