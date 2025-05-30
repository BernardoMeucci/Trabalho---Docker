import datetime
novo_local = datetime.datetime.now(datetime.timezone.utc).astimezone()
data_hora_formatada = novo_local.strftime('%d/%m/%Y %H:%M:%S')
print(f"A data e hora atuais são: {data_hora_formatada}")