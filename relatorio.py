

class Relatorio:
    @staticmethod
    def gerar_relatorio(hotel):
        print("\n----- Relatório Geral do Hotel -----")
        
        
        print("\n--- Quartos Cadastrados ---")
        if hotel.quartos:
            for quarto in hotel.quartos:
                print(quarto.informacoes_quarto())
                print('---------------------------------')
        else:
            print("Não há quartos cadastrados.")
        
        
        print("\n--- Clientes Registrados ---")
        if hotel.clientes:
            for cliente in hotel.clientes:
                cliente.informacoes_cliente()
                print('---------------------------------')
        else:
            print("Não há clientes registrados.")
        
        
        print("\n--- Reservas Realizadas ---")
        if hotel.reservas:
            for reserva in hotel.reservas:
                print(reserva.informacoes())
                print('---------------------------------')
        else:
            print("Não há reservas registradas.")
        
        print("\n----- Fim do Relatório -----")
