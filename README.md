#  Carbon-14 Dating Calculator (C14)

Este script em Python permite estimar a idade de uma amostra orgânica com base na porcentagem de Carbono-14 remanescente, utilizando o modelo de decaimento exponencial radioativo.

 **Baseado em:** *S. J. Chapman — MATLAB for Engineers, pág. 66*

---

##  Descrição

A datação por Carbono-14 é amplamente utilizada para estimar a idade de artefatos arqueológicos, fósseis e múmias, como o famoso **Homem de Gelo (Ötzi)**. 
Este script aplica a fórmula clássica do decaimento exponencial para converter a porcentagem de C-14 restante em anos.


##  Exemplo de uso

```bash
# O CRC handbook of chemistry and physics estabelece que a meia vida do carbono-14
# é de 5730 anos, portanto a saida do programa esta correta.
# No caso do "Homem de Gelo" Ötzi, a famosa múmia natural encontrada nos Alpes entre a Áustria e a Itália em 1991
# os cientistas utilizaram datação por carbono-14 para estimar sua idade
# a porcentagem de carbono-14 remanescente no corpo de Ötzi é de aproximadamente 52,7% do original.
# ou seja, cerca de 5.300 anos atrás.
