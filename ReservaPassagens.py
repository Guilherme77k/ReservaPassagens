class CompanhiaAerea:
    def __init__(self):
        self.voos = {
            101: {"origem": "Seattle", "destino": "Los Angeles", "lugares": 50},
            102: {"origem": "New York", "destino": "Chicago", "lugares": 10},
            103: {"origem": "New York", "destino": "Chicago", "lugares": 1},
            104: {"origem": "New York", "destino": "Chicago", "lugares": 1},
            105: {"origem": "New York", "destino": "Chicago", "lugares": 16},
            106: {"origem": "New York", "destino": "Chicago", "lugares": 100},
            107: {"origem": "New York", "destino": "Chicago", "lugares": 13333},
            108: {"origem": "New York", "destino": "Chicago", "lugares": 12},
            109: {"origem": "New York", "destino": "Chicago", "lugares": 133},
            110: {"origem": "New York", "destino": "Chicago", "lugares": 444},
            111: {"origem": "New York", "destino": "Chicago", "lugares": 6},
            112: {"origem": "New York", "destino": "Chicago", "lugares": 72},
        }

    def consultar_por_numero(self, numero_voo):
        if numero_voo in self.voos:
            voo = self.voos[numero_voo]
            print(f"Voo {numero_voo}: Origem: {voo['origem']}, Destino: {voo['destino']}, Lugares disponíveis: {voo['lugares']}")
        else:
            print("Voo inexistente.")

    def consultar_por_origem(self, origem):
        for numero_voo, voo in self.voos.items():
            if voo["origem"].lower() == origem.lower():
                print(f"Voo {numero_voo}: Origem: {voo['origem']}, Destino: {voo['destino']}, Lugares disponíveis: {voo['lugares']}")

    def consultar_por_destino(self, destino):
        for numero_voo, voo in self.voos.items():
            if voo["destino"].lower() == destino.lower():
                print(f"Voo {numero_voo}: Origem: {voo['origem']}, Destino: {voo['destino']}, Lugares disponíveis: {voo['lugares']}")

    def efetuar_reserva(self, numero_voo):
        if numero_voo in self.voos:
            voo = self.voos[numero_voo]
            if voo["lugares"] > 0:
                voo["lugares"] -= 1
                print("Reserva confirmada. Assento reservado.")
                self.consultar_por_numero(numero_voo)
            else:
                print("Voo lotado. Não há lugares disponíveis.")
        else:
            print("Voo inexistente.")

    def menu_principal(self):
        while True:
            print("\nMenu Principal:")
            print("1. Consultar")
            print("2. Efetuar Reserva")
            print("3. Sair")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                self.menu_consulta()
            elif opcao == 2:
                numero_voo = int(input("Digite o número do voo desejado: "))
                self.efetuar_reserva(numero_voo)
            elif opcao == 3:
                print("Encerrando o programa. Obrigado!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_consulta(self):
        print("\nMenu de Consulta:")
        print("1. Por Número de Voo")
        print("2. Por Origem")
        print("3. Por Destino")
        consulta_opcao = int(input("Escolha uma opção de consulta: "))

        if consulta_opcao == 1:
            numero_voo = int(input("Digite o número do voo: "))
            self.consultar_por_numero(numero_voo)
        elif consulta_opcao == 2:
            origem = input("Digite a origem desejada: ")
            self.consultar_por_origem(origem)
        elif consulta_opcao == 3:
            destino = input("Digite o destino desejado: ")
            self.consultar_por_destino(destino)
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    companhia = CompanhiaAerea()
    companhia.menu_principal()
