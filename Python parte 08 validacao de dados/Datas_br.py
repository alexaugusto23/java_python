from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def ano_cadastro(self):
        ano_cadastro = self.momento_cadastro.year
        #print(type(mes_cadastro))
        return ano_cadastro

    def mes_cadastro(self):
        # pode adicionar um valor vazio ex "" antes de janeiro para que o índice dos meses começe em 1
        # pode por -1 ex self.momento_cadastro.month -1 ou meses_do_ano[int(mes_cadastro)-1]
        meses_do_ano = ['janeiro', 'fevereiro',
                        'março', 'abril',
                        'maio', 'junho',
                        'julho','agosto',
                        'setembro', 'outubro',
                        'novembro', 'dezembro']

        mes_cadastro = self.momento_cadastro.month - 1
        #print(type(mes_cadastro))
        return meses_do_ano[mes_cadastro]

    def dia_cadastro(self):
        dia_cadastro = self.momento_cadastro.day
        #print(type(mes_cadastro))
        return dia_cadastro

    def dia_semana(self):
        dias_semana = ['segunda-feira', 'terça-feira',
                        'quarta-feira', 'quinta-feira',
                        'sexta-feira']

        dia_cadastro = self.momento_cadastro.weekday() 
        #print(type(mes_cadastro))
        return dias_semana[dia_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cad = (datetime.today() + timedelta(days=30) ) - self.momento_cadastro
        return tempo_cad

