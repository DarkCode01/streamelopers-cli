import setuptools

from sdcli.config import Config


EXTENSIONS = {
    'Click',
    'colorama'
}


setuptools.setup(
    name=Config.NAME,
    version=Config.VERSION,
    author=Config.AUTHOR,
    author_email=Config.EMAIL,
    packages=setuptools.find_packages(),
    license=Config.LICENSE,
    description=Config.DESCRIPTION,
    long_description=open('README.md').read(),
    install_requires=['Click', 'colorama'],
    python_requires='>=3.7',
    platforms=['linux', 'macos'],
    entry_points={
        'console_scripts': [
            'sdcli = sdcli.__main__:main',
        ]
    },
    project_urls={
        'Code': Config.SOCIAL_MEDIAS['github']
    }
)