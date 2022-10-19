from russian_uncensor import n_grams
from russian_uncensor import uncensored


# Print n-grams and save them to default path: ./data/ngrams/
ws = n_grams.WordStats()
print(ws.get_n_grams())
ws.save_n_grams()

# Check uncensor using prepared ngrams
uc = uncensored.Uncensor()
print(uc.uncensor_masked('Х*й'))
print(uc.uncensor_splitted('Х у й'))
