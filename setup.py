from setuptools import setup


EXTENSIONS = {
    'Click',
    'colorama'
}


setup(
    name='StOBS',
    version='1.0.0',
    author='Jose Segura',
    author_email='j0s3s3gur4@gmail.com',
    packages='srobs',
    license='MIT',
    include_package_data=True,
    long_description=open('README.md').read(),
    install_requires=['Click', 'colorama'],
    entry_points={
        'console_scripts': [
            'stobs = stobs.__main__:main',
        ]
    }
)