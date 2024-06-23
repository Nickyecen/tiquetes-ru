# Tiquetes RU
Programa destinado a buscar os tíquetes do RU da UFRGS de forma rápida por meio de um script em python.
## Modo de funcionamento
O programa vai ler o arquivo .credentials na mesma pasta em que ele está, que deve conter seu cartão UFRGS com os zeros na frente na primeira linha e sua senha na segunda. Ele utiliza essas credenciais para acessar sua conta e imprime todos os tíquetes disponíveis para uso em sua conta.

### Exemplo de arquivo .credentials:
```
00999999
senha muito difícil de acertar _123
```
