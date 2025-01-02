import yaml
import json

class Config:
    def __init__(self):
        
        self.__config_file = self.__load_config()
        self.screen = self.__config_file['screen']
        self.s_width, self.s_height = self.screen['size']
        self.color = self.__config_file['color']
        self.font = self.__config_file['font']
        self.w_scale,self.h_scale = self.font['scale']

    def __load_config(self):
        yaml.add_constructor("!tup", lambda loader, node: tuple(loader.construct_sequence(node)))
        with open('config.yaml') as f:
            return yaml.load(f, Loader=yaml.FullLoader)