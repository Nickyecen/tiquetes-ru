# Tiquetes RU
Programa destinado a buscar os tíquetes do RU da UFRGS de forma rápida por meio de um script em python.

## Como utilizar
O programa vai ler o arquivo .credentials na mesma pasta em que ele está, que deve conter seu cartão UFRGS com os zeros na frente na primeira linha e sua senha na segunda. Ele utiliza essas credenciais para acessar sua conta e pegar os 20 primeiros tíquetes disponíveis e usados.

### Exemplo de arquivo .credentials:
```
00579107
BRT_dm 092004
```

## Funcionamento
O programa vai carregar as informações de tíquetes e te apresentar com diferentes opções de acesso para as informações de seus tíquetes. Mais de uma opção pode ser utilizada por execução, desde que o caracter da opção esteja na chamada, ela aparecerá.

### t (padrão): Pegar um tíquete disponível
O programa exibe apenas o tíquete mais recente. Essa é a opção padrão, ou seja, caso nada seja informado no input, essa opção será executada.

### d: Ver últimos 20 tíquetes disponíveis
O programa exibe os últimos 20 tíquetes disponíveis para uso. Caso haja apenas *n* tíquetes disponíveis tal que *n < 20*, imprimirá apenas esses últimos n tíquetes.

### u: Ver últimos 20 tíquetes usados
O programa exibe os últimos 20 tíquetes utilizados. Caso haja apenas *n* tíquetes utilizados tal que *n < 20*, imprimirá apenas esses últimos n tíquetes.

### D: Ver informação completa dos últimos 20 tíquetes disponíveis
Mesmo que *d*, mas também exibe valor, data de liberação e vínculo utilizado para cada tíquete.

### U: Ver informação completa dos últimos 20 tíquetes usados
Mesmo que *u*, mas também exibe valor, tipo, data de liberação, vínculo utilizado, data de consumo e restaurante utilizado para cada tíquete.

