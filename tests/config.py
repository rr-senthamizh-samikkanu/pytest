class Config:
    def __init__(self, env):

        # SUPPORTED_ENVS = ["dev", "qa"]

        # if env.lower() not in SUPPORTED_ENVS:
        #     raise Exception(f'{env} is not supported. Use : {SUPPORTED_ENVS}')
        
        self.base_url = {
            'dev': 'https://mydev-env.com',
            'qa': 'https://myqa-env.com',
            'staging': 'staging'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80,
            'staging': 8088
        }[env]
        
