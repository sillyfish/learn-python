try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'lpthw',
    'author': 'Yiming.Deng',
    'url': 'URL to get it at',
    'download_url': 'Where to download it.',
    'author_email': 'sillyfish87@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47', 'ex48'],
    'scripts': [],
    'name': 'lpthw'
}

setup(**config)
