from setuptools import setup, find_packages


setup(
    
    name='PyIMF',
    version='1.0.0',
    license='MIT',
    author="Carlos Eggers",
    author_email='ceggers@fen.uchile.cl',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/ceggersp/IMF_API',
    keywords='IMF API',
    install_requires=[
          'scikit-learn',
          'pandas',
          'numpy'
      ],

)