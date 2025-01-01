import yaml

class Config:
    def __init__(self):
        
        self.__config_file = self.__load_config()
        self.config_window = self.__config_file['window']
        self.config_color = self.__config_file['color']

    def __load_config(self):
        yaml.add_constructor("!tup", lambda loader, node: tuple(loader.construct_sequence(node)))
        with open('config.yaml') as f:
            return yaml.load(f, Loader=yaml.FullLoader)