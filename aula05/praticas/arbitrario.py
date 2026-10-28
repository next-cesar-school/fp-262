def pedido_acai(*complementos):
    print(':: PEDIDO DE AÇAÍ ::')
    for ingrediente in complementos:
        print(f'- {ingrediente}')
    print("-"*10)


pedido_acai('granola', 'leite em pó')
pedido_acai('banana', 'chocobol', 'jujuba', 'ovomaltine', 'paçoca')
pedido_acai('banana')
pedido_acai('banana', 'granola')