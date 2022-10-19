'''
from datetime import datetime
from vk_parser import VkParser
from n_grams import WordStats
from uncensored import Uncensor

__author__ = 'Alex Klyuev'

neg_words = f'/home/alexkly/data/dict/words_neg.txt'
PIPEPLINE_PARTS = {
    'vk_parser': False,
    'n_grams': False,
    'uncencor': True,
}

if __name__ == '__main__':
    """
    Run VK parser:
    For example use MVD Dota 2 VK group to parse comments.
    Use this site to know VK groud ID using VK group link: https://regvk.com/id/
    """
    if PIPEPLINE_PARTS['vk_parser']:
        VkParser(phone='+79*********', password='************', group_id='56333679', date=datetime(2020, 1, 1),
                 progress_bar=True).parse_comments(filename='comments.txt')
    """
    Run Word Stats to get n-grams:
    As result of execution you will get list of the most frequent russian letter in words, bi-grams and tri-grams.
    """
    if PIPEPLINE_PARTS['n_grams']:
        ngrams = WordStats(debug=True).save_n_grams()

    """
    Uncensor text and try to find bad words in the string:
    There is two method in the Uncensor class:
    * uncensor_splitted - try to find bad words in separated particles.
    * uncensor_masked - try to find bad words in 
    """
    if PIPEPLINE_PARTS['uncencor']:
        variants = Uncensor().uncensor_splitted(sentence='п и зда к')
        print(variants)
        example = Uncensor().uncensor_masked(word='п*зд*к')
        print(example)
'''