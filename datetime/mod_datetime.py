from datetime import datetime, timedelta, timezone

def mod_datetime():
    data_e_hora_atuais = datetime.now()
    print(data_e_hora_atuais)
    # Códigos de formatação para strftime() e strptime()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y - %H:%M')
    print(data_e_hora_em_texto)

    # timezione e timedelta

    diferenca = timedelta(hours = -3)
    print(diferenca)

    fuso_horario = timezone(diferenca)
    print(fuso_horario)

    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('fuso horário: %d/%m/%Y %H:%M')
    print(data_e_hora_sao_paulo_em_texto)


if __name__ == "__main__":
    mod_datetime()