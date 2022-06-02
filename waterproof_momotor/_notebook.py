from typing import List

class Block:
    """
    Represents a waterproof block.
    """
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
    """
    A list of Block objects
    """
    blocks: List[Block]

    def __init__(self, blocks):
        self.blocks = blocks
        self._validate()

    def _validate(self):
        assert isinstance(self.blocks, list)
        for b in self.blocks: assert isinstance(b, Block)

    def code_blocks(self):
        return [block.text for block in self.blocks if block.block_type == "code"]

