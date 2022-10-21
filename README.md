# russian_uncensor

Sample text

## Installation
You can find [this project on PyPi](https://pypi.org/project/russian-uncensor/)

To install using pip:
`pip install russian_uncensor`

Or just clone project repository:
```
git clone https://github.com/AlexKly/russian_uncensor 
python setup.py develop
```

## Usage
Supported main functions:
- extract from dict of the obscene words and get n-grams
- perform uncensoring of the masked obscene words in sentence
- perform uncensoring of the splitted obscene words in sentence

Example how to use it is [here](https://github.com/AlexKly/russian_uncensor/blob/master/example.py)

### Quickstart
If you want to run uncensor quickly and use it with default settings, you need to import Uncensor and 
use following functions:
```
# Import uncensor:
from russian_uncensor import uncensored

text = 'obscene_word'
# Call uncensor and find suitable variants of obscene word:
uncensor = uncensored.Uncensor()
uncensored_masked = uncensor.uncensor_masked(text)
uncensored_splitted = uncensor.uncensor_splitted(text)

print('Uncensored in masked word: ', uncensored_masked)
print('Uncensored in splitted word: ', uncensored_masked)
```


## N-grams and WordStats
Sample text

## Uncensor
Sample text

## Documentation
