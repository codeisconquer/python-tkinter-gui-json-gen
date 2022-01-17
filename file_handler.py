import json
import os


class FileHandler:
    json_file_name = "./list_of_teasers.json"

    def add_to_json_file(self, new_entry):
        lod = self.read_json_file()
        lod.append(new_entry)

        with open(self.json_file_name, 'w') as fout:
            json.dump(lod, fout)

    def read_json_file(self):
        lod = []
        if not os.path.isfile(self.json_file_name):
            return lod

        with open(self.json_file_name, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            lod = data
        return lod
