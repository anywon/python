import os, sys

class Setting_config():

    __Setting_config = None

    @staticmethod
    def get_instance():
        if Setting_config.__Setting_config== None:
            Setting_config()
        return Setting_config.__Setting_config

    def __init__(self):
        if Setting_config.__Setting_config is None:
            Setting_config.__Setting_config = self
