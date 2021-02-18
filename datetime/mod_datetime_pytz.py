# Trabalhando com pytz para fuso horários: pip install pytz
from datetime import datetime
from pytz import timezone
import pytz


def mod_datetime():
    data_e_hora_atuais = datetime.now()
    print(data_e_hora_atuais)
    # Códigos de formatação para strftime() e strptime()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y - %H:%M')
    print(data_e_hora_em_texto)

    print("-"*30)
    
    fuso_horario = timezone('America/Sao_Paulo')
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('fuso horário:'+'%d/%m/%Y %H:%M')
    print(data_e_hora_sao_paulo_em_texto) 

if __name__ == "__main__":
    mod_datetime()
    for tz in pytz.all_timezones:
        print(tz)

