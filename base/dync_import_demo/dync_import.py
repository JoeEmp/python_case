import importlib
import logging


class dync_hander():
    def __init__(self, filename, func_name, func_args=[], func_kwargs={}, class_args=[], class_kwargs={}):
        module_path = '.'.join(filename.split('/')[1:])
        module_obj = dync_import(module_path)
        if '.' in func_name:
            class_name, func_name = func_name.split('.')
            return module_obj.class_func(
                class_name, func_name, class_args, class_kwargs, func_args, func_kwargs)
        else:
            return module_obj.func(func_name, *func_args, **func_kwargs)


class dync_import():
    def __init__(self, module_path):
        self.imp_module = importlib.import_module(module_path)

    def get_object(self, obj_name, imp_module=None, *args, **kwargs):
        imp_module = imp_module or self.imp_module
        imp_obj = getattr(imp_module, obj_name)
        return imp_obj(*args, **kwargs)

    def class_func(self, class_name, func_name, class_args=[], class_kwargs={}, func_args=[], func_kwargs={}):
        imp_module = self.get_object(class_name, *class_args, **class_kwargs)
        return self.get_object(func_name, imp_module=imp_module, *func_args, **func_kwargs)

    def func(self, func_name, *args, **kwargs):
        return self.get_object(func_name, *args, **kwargs)

if "__name__" ==  __name__:
    import os
    os.chdir(__file__)
    dync_hander('call.py')