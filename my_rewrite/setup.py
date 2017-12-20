from setuptools import setuptools

setup(
    name='jpglitch',
    version='0.2',
    py_modules=['jpglitch'],
    install_requires=[
        'Click',
        'Pillow',
    ],
    entry_poinsts='''
        [console_scipts]
        jpglitch=jpglitch:cli
        ''',
)