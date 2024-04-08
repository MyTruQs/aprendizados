class Movie:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.ultimaAval = 0
        self.avalTotal = 0
        self.durationMinutes = durationMinutes
        self.avaliadores = 0
    
    def technical_sheet(self):
        print("####Dados do Filme####")
        print(f"Nome Filme: {self.name}")
        print(f"Ano Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Total de avaliações Filme: {self.ultimaAval}")
        print(f"Média de avaliações Filme: {self.avalTotal}")
        print(f"Duração Filme: {self.durationMinutes}")
        print(f"QTD Avaliadores Filme: {self.avaliadores}")
    
    def aval(self, nota):
        self.ultimaAval += nota
        self.avaliadores += 1
        # self.ultimaAval = self.ultimaAval / self.avaliadores
    
    def mediaNota(self):
        self.avalTotal = self.ultimaAval / self.avaliadores


movie = Movie("Super Mario", 2023, False, 120)

x = False

while not x:
    
    print("----MENU----")
    print("1-Informações Filmes:\n")
    print("2-Avaliar um filme:\n")
    print("3-Sair\n")
    menu = input("Escolha um dos menus acima\n")
    
    if menu == "1":
        movie.technical_sheet()
    elif menu == "2":
        print("Filmes disponiveis para avaliação:\n")
        print(f"1- {movie.name}")
        nota = float(input("Digite a nota de avaliação!\n"))
        movie.aval(nota)
        movie.mediaNota()
    elif menu == "3":
        x = True
    else:
        pass


# avaliacao = float(input("Digite a nota de avaliação\n"))
# movie.technical_sheet()
