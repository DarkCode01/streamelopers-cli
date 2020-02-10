from libs import config

def _info():
    _config = config._config()

    print(f'''
    Medium: {_config.get('medium')}
    Github: {_config.get('github')}
    Github (Streamelopers): {_config.get('github (Stremelopers)')}
    Patron: {_config.get('patron')}
    ''')

def version():
    _config = config._config()
    print(f'Streamelopers Generator (v{_config.get("version")})')
