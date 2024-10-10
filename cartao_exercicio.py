meuCartao = int(input("Digite o número do seu cartão: "))

cartaoLido = 1
cartaoEncontrado_lista = False

while cartaoLido != 0 and not cartaoEncontrado_lista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        cartaoEncontrado_lista = True

if cartaoEncontrado_lista:
    print("EBAAAA!!!!")
else:
    print("CARAMBA, PERDI MEU CARTÃO!!!!!!")
