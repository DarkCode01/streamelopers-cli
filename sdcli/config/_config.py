'''
...File config os this project STOBS...
'''
import os


class Config(object):
    NAME = 'sdcli'
    VERSION = '1.2.0'
    LICENSE = 'MIT'
    AUTHOR = 'Jose Segura'
    EMAIL = 'j0s3s3gur4@gmail.com'
    DESCRIPTION = '''
    sdcli -> Is a CLI for generate a simple scenes collection that we using in ours streamings.
    '''
    SOCIAL_MEDIAS = {
        'medium': '...',
        'github': 'https://github.com/DarkCode01/streamelopers-cli',
        'patron': '...'
    }

    # System Configuration.
    HOME = os.environ.get('HOME')