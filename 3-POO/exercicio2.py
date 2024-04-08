class Produto:
    def __init__(self, name, valor):
        self.name = name
        self.valor = valor
      
    def __str__(self):
        return f"Produto: {self.name}, Preço: {self.valor}"
    
    def desconto(self, desc):
        self.valor = self.valor - (self.valor * (desc/100))

produto1 = Produto("Arroz", 50)
produto2 = Produto("Feijao", 10)
  
produto1.desconto(10)
produto1.desconto(50)

print(produto1)
print(produto2)