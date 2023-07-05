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
        """ Return objects dictionary """
        return self.__objects

    def new(self, obj):
        """ a new dictionary """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ saves the data """
        json_data = json.dumps(self.__objects)
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            file.write(json_data)

    def reload(self):
        """ Tries reloading """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as json_file:
                json_object = json.load(json_file)
                for key, attributes_dict in json_object.items():
                    class_type = eval(attributes_dict["__class__"])
                    obj = class_type(**attributes_dict)
                    self.new(obj)
        except FileNotFoundError:
            pass