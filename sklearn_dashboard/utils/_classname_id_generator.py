from typing import Optional
import string

def classname_id_generator(prefix: string = None, label: string = None):
    if label is not None:
        if prefix is None:
            classname = label.strip().replace(' ', "_").lower()
            return classname
        return prefix + "_" + label.strip().replace(' ', "_").lower()
    raise ValueError





