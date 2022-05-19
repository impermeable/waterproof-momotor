from typing import List

class Block:
    block_type: str
    text: str
    start: bool
    id: str

    def __init__(self, block_type, text=None, start=None, id=None):
        self.block_type = block_type
        self.text = text
        self.start = start
        self.id = id

class Notebook:
    blocks: List[Block]

    def __init__(self, blocks):
        self.blocks = blocks
        self._validate()

    def _validate(self):
        assert isinstance(self.blocks, list)

    def code_blocks(self):
        return [block.text for block in self.blocks if block.block_type == "code"]

