'''
...File config os this project STOBS...
'''
import os


class Config(object):
    NAME = 'stobs'
    VERSION = '1.0.0'
    LICENSE = 'MIT'
    AUTHOR = 'Jose Segura'
    EMAIL = 'j0s3s3gur4@gmail.com'
    DESCRIPTION = '''
    stobs -> Is a CLI for generate a simple scenes collection that we using in ours streamings.
    '''
    SOCIAL_MEDIAS = {
        'medium': 'asdas',
        'github': 'https://github.com/DarkCode01/streamelopers-cli',
        'patron': 'dasdasda'
    }

    # System Configuration.
    HOME = os.environ.get('HOME')