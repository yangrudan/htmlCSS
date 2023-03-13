# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _stru_stru
else:
    import _stru_stru

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class Student(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    age = property(_stru_stru.Student_age_get, _stru_stru.Student_age_set)
    score = property(_stru_stru.Student_score_get, _stru_stru.Student_score_set)

    def __init__(self):
        _stru_stru.Student_swiginit(self, _stru_stru.new_Student())
    __swig_destroy__ = _stru_stru.delete_Student

# Register Student in _stru_stru:
_stru_stru.Student_swigregister(Student)

class School(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    class_num = property(_stru_stru.School_class_num_get, _stru_stru.School_class_num_set)
    studentObj = property(_stru_stru.School_studentObj_get, _stru_stru.School_studentObj_set)

    def __init__(self):
        _stru_stru.School_swiginit(self, _stru_stru.new_School())
    __swig_destroy__ = _stru_stru.delete_School

# Register School in _stru_stru:
_stru_stru.School_swigregister(School)


def create():
    return _stru_stru.create()

def new_StudentArray(nelements):
    return _stru_stru.new_StudentArray(nelements)

def delete_StudentArray(ary):
    return _stru_stru.delete_StudentArray(ary)

def StudentArray_getitem(ary, index):
    return _stru_stru.StudentArray_getitem(ary, index)

def StudentArray_setitem(ary, index, value):
    return _stru_stru.StudentArray_setitem(ary, index, value)
class StudentClass(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _stru_stru.StudentClass_swiginit(self, _stru_stru.new_StudentClass(nelements))
    __swig_destroy__ = _stru_stru.delete_StudentClass

    def __getitem__(self, index):
        return _stru_stru.StudentClass___getitem__(self, index)

    def __setitem__(self, index, value):
        return _stru_stru.StudentClass___setitem__(self, index, value)

    def cast(self):
        return _stru_stru.StudentClass_cast(self)

    @staticmethod
    def frompointer(t):
        return _stru_stru.StudentClass_frompointer(t)

# Register StudentClass in _stru_stru:
_stru_stru.StudentClass_swigregister(StudentClass)

def StudentClass_frompointer(t):
    return _stru_stru.StudentClass_frompointer(t)



