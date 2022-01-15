import json
import os
from tkinter import *
from functools import partial

from file_handler import FileHandler


class Form:
    form_title = 'Teaser creator'
    form_size = '400x150'
    blueprint_file = "./form_construction.json"
    blueprint = []

    def __init__(self):
        # window
        self.tkWindow = Tk()
        self.tkWindow.geometry(self.form_size)
        self.tkWindow.title(self.form_title)

        self.create()

    def load_blueprint(self):

        if not os.path.exists(self.blueprint_file):
            print("not found " + self.blueprint_file)
            exit(0)

        with open(self.blueprint_file, encoding='utf-8') as data_file:
            self.blueprint = json.loads(data_file.read())

    def save_form(self, submit_data):
        d = {}
        for n in submit_data:
            d[n] = submit_data[n].get()
        fh = FileHandler()
        fh.add_to_json_file(d)
        print("saved " + d['headline'])
        return

    def create(self):
        self.load_blueprint()
        row_counter = 0
        element_inputs = {}
        for element in self.blueprint:
            Label(self.tkWindow, text=element['label']).grid(row=row_counter, column=0)
            element_inputs[element['name']] = StringVar()
            Entry(self.tkWindow, textvariable=element_inputs[element['name']]).grid(row=row_counter, column=1)
            row_counter = row_counter + 1

        form_fields = partial(self.save_form, element_inputs)
        Button(self.tkWindow, text="Add", command=form_fields).grid(row=row_counter, column=0)

    def run(self):
        self.tkWindow.mainloop()


f = Form()
f.run()
