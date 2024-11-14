class Relatorio:
    def __init__(self, id_relatorio, tipo_relatorio, data_geracao, dados):
     self.id_relatorio = id_relatorio
     self.tipo_relatorio = tipo_relatorio
     self.data_geracao = data_geracao
     self.dados = dados

    def gerar_relatorio(self):
        # Cria o conteúdo do relatório formatado
        conteudo = f"Relatório ID: {self.id_relatorio}\n"
        conteudo += f"Tipo de Relatório: {self.tipo_relatorio}\n"
        conteudo += f"Data de Geração: {self.data_geracao}\n"
        conteudo += "Dados:\n"
        
        # Adiciona os dados formatados
        for chave, valor in self.dados.items():
            conteudo += f"  - {chave}: {valor}\n"

        # Exibe o relatório no console
        print(conteudo)

        # Salva o relatório em um arquivo de texto
        with open(f"relatorio_{self.id_relatorio}.txt", "w") as arquivo:
            arquivo.write(conteudo)
        print(f"Relatório {self.id_relatorio} salvo em relatorio_{self.id_relatorio}.txt")

