# Descrição do problema
Você está organizando um hub para participr do CodeHash e deseja pedir pizza para os participantes do seu hub. Felizmente, há uma pizzaria nas proximidades com uma pizza muito boa.
A pizzaria possui diferentes tipos de pizza e mantém os alimentos disponíveis para o seu hub, você só pode pedir no máximo uma pizza de cada tipo. Em particular, existem
muitos tipos de pizza para escolher!
Cada tipo de pizza tem um tamanho específico: o tamanho corresponde ao número de fatias nessa pizza.
Você estimou o número máximo de fatias de pizza que deseja pedir para o seu
hub com base no número de participantes registrados. Para reduzir o desperdício de alimentos,
seu objetivo é pedir o maior número possível de fatias de pizza, mas sem ultrapassar o
número máximo.

## Dataset de entrada 
### Formato de arquivo
Cada conjunto de dados de entrada é fornecido em um arquivo de texto sem formatação que contém exclusivamente caracteres ASCII com linhas terminadas com um único caractere '\n' (finais de linha no estilo UNIX). Quando uma única linha contém vários elementos, eles são separados por espaços únicos.

A primeira linha do dataset contém os seguintes dados:
  - um inteiro M ( 1 ≤ M ≤ 10 9 ) – o número máximo de fatias de pizza para pedir
  - um inteiro N ( 1 ≤ N ≤ 10 5 ) – o número de diferentes tipos de pizza

A segunda linha contém N inteiros - o número de fatias de pizza em cada tipo de pizza, em ordem não decrescente:
  - 1 ≤ S0 ≤ S1 ≤ ... ≤ S(N-1) <= M