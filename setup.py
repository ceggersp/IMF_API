from setuptools import setup

setup(
    name='PyIMF',
    version='0.0.1',
    license='MIT',
    author="Carlos Eggers P.",
    author_email='ceggers@fen.uchile.cl',
    package_dir={'': 'src'},
    url='https://github.com/ceggersp/IMF_API',
    keywords='IMF API',
    install_requires=[
          'pandas',
          'numpy'
      ],
)