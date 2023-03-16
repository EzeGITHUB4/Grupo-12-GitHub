class adviento():
    Month = "Febrero"
    Year =  2023
    
    def __init__ (self, Dia, Hora):
        self.Dia = Dia
        self.Hora = Hora
        
        def calendario(adviento):
            Premio = ["Peluche de oso", "Cepillo de pelo", "Remera", "Stickers", "Hamburguesa", "Gorra", "Chocolate", "Perfume"]
            
            if (Year == 2023 and Month == "Febrero"):
                Eldia = int(input("Decime el día en numero: "))
                for Eldia in Premio:    
                    print(Eldia.Premio - 1)
                    
            elif (Year < 2023 and Month != "Febrero"):
                print("Todavia falta para que se inicie el calendario")
            
            elif (Year > 2023 and Month != "Febrero"):
                print("Ya paso la fecha del calendario de adviento")
            
            else:
                print("Busca la fecha de hoy")
                