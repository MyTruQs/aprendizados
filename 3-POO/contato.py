class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Nome: {self.name}, Telefone: {self.phone}, Email:{self.email}"
    
class ContactBook:
    def __init__(self):
        self.contatos = []

    def add_contato(self, contatos):
        self.contatos.append(contatos)
    
    def remover_contato(self, contatos):
        self.contatos.remove(contatos)
    
    def listar_contatos(self):
        for x in self.contatos:
            print(x)
        
    def buscar_contato(self, name):
        for x in self.contatos:
            if x.name.lower() == name.lower():
                print(x)
                return x

        print("Contato inexistente")


# book = ContactBook()
# raul = Contact("Raul", "9999", "raul@gmail.com")
# abner = Contact("Abner", "9999", "abner@gmail.com")

# book.add_contato(raul)
# book.add_contato(abner)

# book.buscar_contato("teste")

# book.listar_contatos()
