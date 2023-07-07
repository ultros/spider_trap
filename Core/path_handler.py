import Core.settings as settings
import random


class PathHandler:
    def __init__(self) -> None:
        self._charspace = settings.Settings.CHARSPACE

    def generate_path_strings(self) -> list:
        '''
        Generate a list of paths based on the character list self._charspace.
        :return:
        path_list - List of paths.
        '''
        path_list = []

        for i in range(5):
            value = random.choices(self._charspace, k=10)
            path = ''.join(value)
            path_list.append(path)

        return path_list
