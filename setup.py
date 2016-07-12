from setuptools import setup

setup(name='nsequoter',
      version='1.0.0',
      description='Web scraping api for the National Stock Exchange of India. Retrives quotes for equities and equity futures from the NSE website.',
	  classifires=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
      ],
      url='https://github.com/TheAdityaKedia/nsequoter',
      author='Aditya Kedia',
      author_email='kedia.aditya@gmail.com',
      license='MIT',
      packages=['nsequoter'],
	  install_requires=['requests',],
      zip_safe=False)
