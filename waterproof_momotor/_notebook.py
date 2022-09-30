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

    def __eq__(self, other):
        """
        Check if two blocks are equal.
        """
        return (
            (self.block_type == other.block_type)
            and (self.text == other.text)
            and self.start == other.start
        )
        # not checking id

    def copy(self):
        """
        Returns a (deep) copy of the block.
        """
        return Block(self.block_type, text=self.text, start=self.start, id=self.id)


class Notebook:
    """
    A list of Block objects
    """

    blocks: List[Block]

    def __init__(self, blocks):
        """
        Construct a notebook from a list of Block objects.
        """
        self.blocks = blocks
        self._validate()

    def _validate(self):
        """
        Validate notebook integrity.
        """
        assert isinstance(self.blocks, list)
        for b in self.blocks:
            assert isinstance(b, Block)

    def code_blocks(self):
        """
        Returns all code blocks.
        """
        return [block.text for block in self.blocks if block.block_type == "code"]

    def input_code(self) -> List[str]:
        """
        Concatenates code blocks from input blocks.

        Returns
        -------
        blocks : List[str]
            A list of strings, wherein the n-th index contains the code of the
            n-th input block.
        """
        blocks = []
        in_input_block = False
        code = []
        for block in self.blocks:
            if block.block_type == "input":
                in_input_block = block.start
                if block.start == False:
                    blocks.append("\n".join(code))
                    code = []
            elif block.block_type == "code":
                if in_input_block:
                    code.append(block.text)
        return blocks

    def non_input_blocks(self):
        """
        Returns all blocks that are not within an input block and are not an input block.
        """
        blocks = []
        in_input_block = False
        for block in blocks:
            if block.block_type == "input":
                in_input_block = block.start
            if not in_input_block or block.block_type == "input":
                blocks.append(block)
        return blocks

    def non_input_equals(self, other):
        """
        Returns true if and only if all the non-input-blocks are equal.
        """
        self_blocks = self.non_input_blocks()
        other_blocks = other.non_input_blocks()
        if len(self_blocks) != len(other_blocks):
            return False
        return all(a == b for a, b in zip(self_blocks, other_blocks))

    def copy(self):
        """
        Returns a deep copy of the notebook.
        """
        blocks_copy = [block.copy() for block in self.blocks]
        return Notebook(blocks_copy)

    def replace_input_code(self, i, code):
        """
        Replace the contents of the i-th input cell.
        """
        ith_input_idx = None
        input_counter = 0
        for block_idx, block in enumerate(self.blocks):
            if block.block_type == "input":
                if block.start == True:
                    if input_counter == i:
                        ith_input_idx = block_idx
                        break
                    input_counter += 1
        if ith_input_idx is None:
            raise ValueError(f"Index {i} not found")

        while self.blocks[ith_input_idx + 1].start != False:
            self.blocks.pop(ith_input_idx + 1)

        self.blocks.insert(ith_input_idx + 1, Block("code", code))
