# Модуль конфигурации

## 1. <a name="contents">Оглавление</a>
1. [Оглавление](#contents)
2. [О проекте](#about)
3. [Быстрый запуск](#quick_start)

## 2. <a name="about">О проекте</a>
Модуль позволяет собирать конфиги из директорий и читать их в удобный формат. Работает с конфигами типа `json` и `yaml`.
Читается только конфиг с наивысшим уровнем окружения, если не указан параметр `env`.

Ответственный: @komarnitsky

## 3. <a name="quick_start">Запуск</a>
#### Формат конфига
Конфиги задаются в виде файлов типа `json` или `yaml`.  
Имя файла имеет формат `config_name.env.json` или `config_name.env.yaml`,  
где `env` - один из `["deploy", "test", "dev"]`


#### Чтение конфига
```python
from dp_python_helper.config_module import Configuration

# В качестве аргументов принимает в себя kwargs для задания стартового конфига
cfg = Configuration()
# Прочитать все `json` конфиги из директории `configs`
cfg.read_json("configs")
# Прочитать все `yaml` конфиги в коружении "deploy" из директории `cfg`
cfg.read_yaml("cfg", env="deploy") 
```

#### Получение данных
Пусть у нас имеются конфиги `json_cfg.dev.json` и `yaml_cfg.deploy.yml`  

JSON-конфиг
```json
{
  "field1": "foo",
  "field2": "bar"
}
```  
  
YAML-конфиг
```yaml
field1: 123
field2: 
    field21: hello
    field22: world
```

```python
cfg.json_cfg.field1
# foo
cfg.json_cfg["field1"]
# foo

cfg.yaml_cfg.field2
# Configuration{
#   "filed21": "hello",
#   "field22": "world"
# }
```