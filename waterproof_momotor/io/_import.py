from .._notebook import Notebook, Block
import json


def load_file(file, extention="auto") -> Notebook:
    """
    Load and parse a waterproof notebook/exercisesheet or .v file.

    Parameters
    ----------
    file : file object, Path, str
        reads content of file object or reads concent at string location
    """
    if hasattr(file, "read"):
        content = file.read()  # we didn't open it, so we don't close it.
        # FIXME infer extention of file
    else:
        file = str(file)  # to remove Path wrapper
        if extention == "auto":
            if "." not in file:
                raise ValueError(
                    f"File location {file} has no file extention, so you must provide this"
                )
            extention = file.split(".")[-1]

        with open(file, 'r', encoding="utf8", errors='ignore') as file_object:
            content = file_object.read()

    if extention == "v":
        return _load_file_v(content)
    elif extention in ["wpn", "wpe"]:
        return _load_file_wp(content)
    else:
        raise ValueError(f"Extention {extention} not supported.")


def _load_file_wp(txt):
    JSON = json.load_files(txt)
    blocks = []
    for json_block in JSON["blocks"]:
        if json_block["type"] == "input":
            block = Block(
                block_type=json_block["type"],
                start=json_block["start"],
                id=json_block["id"],
            )
        else:
            block = Block(block_type=json_block["type"], text=json_block["text"])
        # FIXME hint blocks may change in waterproof?
        blocks.append(block)
    nb = Notebook(blocks)
    return nb


def _load_file_v(txt):
    # TODO interpret notebook?
    raise NotImplementedError()
