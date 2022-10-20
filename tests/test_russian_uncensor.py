import unittest
from russian_uncensor.uncensored import Uncensor as U

u = U()


def test_uncensored_masked(text, referance):
    text = text.replace(',', '')
    text = text.split(' ')
    res_text = ''
    for word in text:
        uncensored_vars = u.uncensor_masked(word=word)
        if uncensored_vars[0]:
            for uncensored_word in uncensored_vars[1]:
                if uncensored_word in referance:
                    res_text += uncensored_word + ' '
        else:
            res_text += uncensored_vars[1] + ' '
    print(res_text)

    assert res_text[:-1] == referance, 'Not matched'


def test_uncensored_splitted(text, referance):
    uncencored_vars = u.uncensor_splitted(sequence=text)
    res = [word for word in uncencored_vars for ref in referance if word == ref]
    print(res)

    assert res == referance, 'Not matched'


class TestRussianUncensor(unittest.TestCase):
    def test_t_u_m_u0(self): test_uncensored_masked(text='Иди нах*й, п*д*рас еб*нный', referance='иди нахуй пидорас ебанный')   # Succes
    def test_t_u_m_u1(self): test_uncensored_masked(text='Иди нах**', referance='иди нахуй')    # Success
    def test_t_u_m_u2(self): test_uncensored_masked(text='Иди на***', referance='иди нахуй')    # Success
    def test_t_u_m_u3(self): test_uncensored_masked(text='Иди н****', referance='иди нахуй')    # Fail
    def test_t_u_m_u4(self): test_uncensored_masked(text='Иди *а***', referance='иди нахуй')    # Success
    def test_t_u_s_u0(self): test_uncensored_splitted(text='на х уй', referance=['нахуй'])  # Success
    def test_t_u_s_u1(self): test_uncensored_splitted(text='н а х у й', referance=['нахуй'])    # Success
    def test_t_u_s_u2(self): test_uncensored_splitted(text='на хуй', referance=['нахуй'])   # Success
    def test_t_u_s_u3(self): test_uncensored_splitted(text='на|х!уй', referance=['нахуй'])  # Success
