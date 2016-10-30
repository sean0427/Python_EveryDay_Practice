#!/usr/bin/env python
# -*- conding: utf-8 -*- 

from subject import Subject

class Observer:

    def __init__(self, subject, name=None):
        self.name = name
        self.subject = subject

    def update(self):
        print('update observer {}'.format(self.name))

if __name__ == "__main__":
    subject = Subject()
    subject.attach(Observer(subject, 'A'))
    subject.notify()
