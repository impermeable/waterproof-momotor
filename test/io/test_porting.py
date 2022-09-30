from waterproof_momotor._import import load_file

import pytest
from pathlib import Path
import os

test_path = Path(__file__).parent / 'test_porting'
test_files = [str(test_path / file) for file in os.listdir(test_path)]
test_names = set([".".join(name.split('.')[:-1]) for name in test_files])
# test_names are the names with extention

def test_load_file():
    notebook = load_file(test_path / 'tutorial.wpe')
    assert len(notebook.blocks) == 233
