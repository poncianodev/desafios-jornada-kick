# Faça um programa no qual o usuário precisa cadastrar as informações de um produto:
# código, nome, quantidade e preço. No final o programa deve mostrar as informações cadastradas e exibir o valor total da compra.

productCode = int(input('Código do produto: '));
productName = input('Nome do produto: ');
quantity = int(input('Quantidade do produto: '));
price = float(input('Preço do produto: '));
totalPrice = price * quantity;

print(f'O código do produto é: {productCode}, nome do produto: {productName}, quantidade do produto: {quantity}, preço do produto: {price}, total da compra é: {totalPrice}');