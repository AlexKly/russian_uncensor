from setuptools import find_packages, setup

setup(
    name='russian_uncensor',
    version='0.0.1',
    description='Uncensor for russian masked or separated obscene words based on frequent letters, bi- and tri-grams analysis',
    long_description='',
    author='Alex Klyuev',
    author_email='Klyukvanstalker@gmail.com',
    license='MIT',
    keywords='uncensor obscene swear words n-grams',
    url='https://github.com/AlexKly/russian_uncensor',
    download_url='',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
    ]
)