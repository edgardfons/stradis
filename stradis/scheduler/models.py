from django.db import models

class Teacher:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return self.name

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Classroom:
    def __init__(self, id, number):
        self.id = id
        self.number = number

class Timezone:
    def __init__(self, id, start, end, weekdays):
        self.id = id
        self.start = start
        self.end = end
        self.weekdays = weekdays
