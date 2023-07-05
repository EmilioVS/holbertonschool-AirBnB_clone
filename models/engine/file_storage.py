#!/usr/bin/python3
""" serializes and deserializes instances from and to JSON file """
import json


class FileStorage():
    """TestFileStorage test of suits for the engine
    testing save, all, reload and new methods
    Args:
        unittest (): Propertys for unit testing
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        __objects[key] = obj

    def save(self):
        json_data = json.dumps(self.__objects)
        with open(self.__file_path, 'w') as file:
            file.write(json_data)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    class_ = eval(class_name)
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass