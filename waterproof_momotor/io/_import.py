from .._notebook import Notebook

def read(file, extention='auto') -> Notebook:
    """
    Read and parse a waterproof notebook/exercisesheet or .v file.

    Parameters
    ----------
    file : file object, Path, str
        reads content of file object or reads concent at string location
    """
    if hasattr(file, 'read'):
        content = file.read() # we didn't open it, so we don't close it.
        # FIXME infer extention of file
    else:
        file = str(file) # to remove Path wrapper
        if extention == 'auto':
            if '.' not in file:
                raise ValueError(f"File location {file} has no file extention, so you must provide this")
            extention = file.split('.')[-1]

        with open(file) as file_object:
            content = file_object.read()

    if extention == 'v':
        return _read_v(content)
    elif extention in ['wpn', 'wpe']:
        return _read_wp(content)
    else:
        raise ValueError(f"Extention {extention} not supported.")

def _read_wp(txt):
    return

def _read_v(txt):
    return