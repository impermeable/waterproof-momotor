from .._notebook import Notebook, Block
import json


def read(file, extention="auto") -> Notebook:
    """
    Read and parse a waterproof notebook/exercisesheet or .v file.

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
        return _read_v(content)
    elif extention in ["wpn", "wpe"]:
        return _read_wp(content)
    else:
        raise ValueError(f"Extention {extention} not supported.")


def _read_wp(txt):
    JSON = json.loads(txt)
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
        # FIXME hint interpreted correctly? Shouldn't matter right.
        blocks.append(block)
    nb = Notebook(blocks)
    return nb


def _read_v(txt):
    # TODO interpret notebook?
    return txt
