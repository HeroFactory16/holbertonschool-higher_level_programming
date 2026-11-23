#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name:str, age:int, is_student:bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}" +
              f"\nIs Student: {self.is_student}")

    def serialize_self(self, filename:str):
        with open(file=filename, mode="w", encoding="utf-8") as file:
            pickle.dump(obj=self, file=file)

    @classmethod
    def deserialize_self(cls, filename):
        try:
            with open(file=filename, mode="r", encoding="utf-8") as file:
                return pickle.load(file=file)
        except FileNotFoundError:
            return
