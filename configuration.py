import json
import logging
import os
from typing import Optional

import yaml


class Configuration(dict):
    def __init__(self, **kwargs):
        super(Configuration, self).__init__(**kwargs)
        for k, v in kwargs.items():
            if isinstance(v, dict):
                self[k] = Configuration(**v)
            else:
                self[k] = v

    def read_yaml(self, cfg_dir: str = "configs", env: Optional[str] = None) -> None:
        """
        Читает yaml конфиги из директории и записывает его в объект
        :param cfg_dir: Директория с конфигами
        :param env: [Optional] Конкретное окружение конфига
        :return:
        """
        self.__read_dir(cfg_dir, "yaml", env)

    def read_json(self, cfg_dir: str = "configs", env: Optional[str] = None) -> None:
        """
        Читает все json конфиги из директории
        :param cfg_dir: Директория с конфигами
        :param env: [Optional] Конкретное окружение конфига
        :return:
        """
        self.__read_dir(cfg_dir, "json", env)

    def __read_dir(self, cfg_dir: str, filetype: str, env: str) -> None:
        """
        Читает конфиги определенного типа из директории
        :param cfg_dir: Директория с конфигами
        :param filetype: Тип файлов конфигурации
        :return:
        """
        env_order = [".deploy.", ".test.", ".dev."] if env is None else [f".{env}."]
        funcs = {"yaml": self.__read_yaml, "json": self.__read_json}
        endings = {"yaml": (".yml", ".yaml"), "json": ".json"}
        if not os.path.exists(cfg_dir):
            raise ConfigException("Config dir does not exist")
        files = list(filter(lambda x: x.endswith(endings[filetype]), os.listdir(cfg_dir)))
        for file in files:
            for env in env_order:
                if env in file:
                    cfg_name = file.split(env)[0]
                    self[cfg_name] = Configuration(**(funcs[filetype](cfg_dir, file)))
                    break
            else:
                logging.warning(f"Config '{file}' doesn't match the environment")
                continue

    def __read_yaml(self, cfg_dir: str, filename: str) -> dict:
        """
        Читает конкретный yml файл конфигурации
        :param cfg_dir: Папка с конфигами
        :param filename: Имя файла конфига
        :return: Прочитанный конфиг в виде словаря
        """
        try:
            with open(os.path.join(cfg_dir, filename), encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except Exception as e:
            raise ConfigException(f"Config '{filename}' is broken, {e}")
        return data

    def __read_json(self, cfg_dir: str, filename: str) -> dict:
        """
        Читает конкретный json файл конфигурации
        :param cfg_dir: Папка с конфигами
        :param filename: Имя файла конфига
        :return: Прочитанный конфиг в виде словаря
        """
        try:
            with open(os.path.join(cfg_dir, filename), encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            raise ConfigException(f"Config '{filename}' is broken, {e}")
        return data

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Configuration, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Configuration, self).__delitem__(key)
        del self.__dict__[key]

    def __str__(self):
        return f"Configuration{json.dumps(self, indent=2, ensure_ascii=False)}"


class ConfigException(BaseException):
    pass
