#Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
seconds = 1000
days = seconds // (24 * 3600)
seconds %= 24 * 3600
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f'{days}:{hours}:{minutes}:{seconds}')
