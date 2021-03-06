from setuptools import setup, find_packages

setup(
    name='reelSRCH',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/jackokeeffe/reelSRCH',
    license='',
    author="Jack O'Keeffe",
    author_email='okeeffe.jpo@gmail.com',
    description='Search for information on any movie',
    install_requires=['pysimplegui', 'imdbpy'],
)
