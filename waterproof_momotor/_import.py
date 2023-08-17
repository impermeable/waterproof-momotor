from ._notebook import Notebook, Block
import json
import re


def load_file(file, extention="auto") -> Notebook:
    """
    Load a waterproof notebook/exercisesheet or .v or .mv file into a Notebook object.

    Parameters
    ----------
    file : file object, Path, str
        Reads content of file object or reads concent at string location
    extention : {"auto", "wpn", "wpe", "v", "mv"}
        The extention of the file. If not auto, this ensures a certain type is expected.
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

        with open(file, "r", encoding="utf8", errors="ignore") as file_object:
            content = file_object.read()

    if extention == "v":
        return _load_file_v(content)
    if extention == 'mv':
        return _load_file_mv(content)
    elif extention in ["wpn", "wpe"]:
        return _load_file_wp(content)
    else:
        raise ValueError(f"Extention {extention} not supported.")


def _load_file_wp(txt):
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
        # FIXME hint blocks may change in waterproof?
        blocks.append(block)
    nb = Notebook(blocks)
    return nb


def _load_file_v(txt):
    # TODO implement as it is not (yet?) needed.
    raise NotImplementedError()

def _load_file_mv(txt):
    input_blocks = re.split('(```coq.*?```|<input-area>|</input-area>)', txt, flags=re.DOTALL)
    blocks = []
    id = 1
    for input_block in input_blocks:
        if input_block == '<input-area>':
            block = Block(
                block_type = "input",
                start = True,
                id = id
            )
        elif input_block == '</input-area>':
            block = Block(
                block_type = "input",
                start = False,
                id = id
            )
            id+=1
        else:
            my_match = re.match('```coq(.*?)```', input_block, flags=re.DOTALL)
            if my_match:
                block = Block(
                    block_type = "code",
                    text = my_match.group(1)
                )
            else:
                block = Block(
                    block_type = "text",
                    text = input_block
                )
        blocks.append(block)
    nb = Notebook(blocks)
    return nb
