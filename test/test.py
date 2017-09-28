# -*- coding:utf-8 -*-
import unittest
import re

class JsonValidateCase(unittest.TestCase):

    def setUp(self):
        json_data_file_path = './data/events.json'
        json_schema_file_path = './test/json-schema.json'

        import json
        self.json_data = json.loads(self.get_json_from_file(json_data_file_path))
        self.json_schema = json.loads(self.get_json_from_file(json_schema_file_path))

    def get_json_from_file(self, path):
        with open(path, 'r') as f:
            return self.clean_json(f.read())


    def clean_json(self, string):
        string = re.sub(",[ \t\r\n]+}", "}", string)
        string = re.sub(",[ \t\r\n]+\]", "]", string)
        return string


    def test_data_json(self):
        from jsonschema import validate, ValidationError
        try:
            validate(self.json_data, self.json_schema)
        except Exception as e:
            self.fail(str(e))

if __name__ == '__main__':
    unittest.main()
