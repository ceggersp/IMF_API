from setuptools import setup, find_packages

setup(

    name='PyIMF',
    version='1.0.1',
    license='MIT',
    author="Carlos Eggers",
    author_email='ceggers@fen.uchile.cl',
    packages=find_packages(where = 'PyIMF'),
    #package_dir={'': 'PyIMF'},
    url='https://github.com/ceggersp/IMF_API',
    keywords='IMF API',
    install_requires=[
          'pandas',
          'numpy'
      ],

)