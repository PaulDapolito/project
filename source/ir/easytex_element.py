__author__ = 'Paul Dapolito'

from abc import ABCMeta, abstractmethod


class EasyTeXElement(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __eq__(self, other):
        pass