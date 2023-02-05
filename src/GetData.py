import jsonschema

from src.Auth import Auth


class GetData(Auth):
    SCHEMA_FILE = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "items": {
                "type": "array",
                "items": {},
                "additionalItems": True
            },
            "limit": {
                "type": "integer"
            },
            "offset": {
                "type": "integer"
            }
        },
        "required": [
            "items",
            "limit",
            "offset"
        ]
    }
    SCHEMA_DIR = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "_embedded": {
                "type": "object",
                "properties": {
                    "sort": {
                        "type": "string"
                    },
                    "items": {
                        "type": "array",
                        "items": {}
                    },
                    "limit": {
                        "type": "integer"
                    },
                    "offset": {
                        "type": "integer"
                    },
                    "path": {
                        "type": "string"
                    },
                    "total": {
                        "type": "integer"
                    }
                },
                "required": [
                    "sort",
                    "items",
                    "limit",
                    "offset",
                    "path",
                    "total"
                ]
            },
            "name": {
                "type": "string"
            },
            "exif": {
                "type": "object"
            },
            "resource_id": {
                "type": "string"
            },
            "created": {
                "type": "string"
            },
            "modified": {
                "type": "string"
            },
            "path": {
                "type": "string"
            },
            "comment_ids": {
                "type": "object"
            },
            "type": {
                "type": "string"
            },
            "revision": {
                "type": "integer"
            }
        },
        "required": [
            "_embedded",
            "name",
            "exif",
            "resource_id",
            "created",
            "modified",
            "path",
            "comment_ids",
            "type",
            "revision"
        ]
    }

    def list_file(self):
        res = self.get_file().json().get('items')
        list_file = []
        for i in res:
            list_file.append(i.get('name'))
        return list_file

    def list_dir(self, path_base="disk:/"):
        res = self.get_dir(path_base).json().get('_embedded').get('items')
        list_dir = []
        if res is not None:
            for i in res:
                if i.get('type') == "dir":
                    dir_name = i.get('name')
                    path = i.get('path')
                    list_dir.append(dir_name)
                    self.list_dir(path)
                    list_dir.extend(self.list_dir(path))
            return list_dir

    def print_list(self, *args):
        print()
        for i in args:
            for k in i:
                print(k)

    def validation_json_schema(self, res, schema):
        try:
            jsonschema.validate(instance=res.json(), schema=schema)
            result = True
        except jsonschema.ValidationError:
            result = False
        return result
