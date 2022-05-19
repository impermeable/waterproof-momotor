from waterproof_momotor.io._import import read

import pytest
from pathlib import Path
import os

test_path = Path(__file__).parent / 'test_porting'
test_files = [str(test_path / file) for file in os.listdir(test_path)]
test_names = set([".".join(name.split('.')[:-1]) for name in test_files])
# test_names are the names with extention

@pytest.mark.parametrize("file_name", test_names)
def test_import_export(file_name):
    files = [file for file in test_files if file_name in file]
    v_file, wpn_file, wpe_file = [(file_name + '.' + extention) if ((file_name + '.' + extention) in files) else None for extention in ['v', 'wpn', 'wpe']]

    # TODO for now, just check v <-> wpn
    assert wpn_file is None

    # EXPORT TEST
    # TODO is this necessary?
    # expect notebook.to_v == v

    # IMPORT TEST
    v = read(v_file)
    wpe = read(wpe_file)
    # TODO
    # assert v == wpe
    # waterproof's testcase:
    # expect imported v == json spul in .wpn:
    # const blocks = coqToWp(v);
    #         expect(blocks.length).to.equal(notebook.blocks.length);
    #         for (let j = 0; j < blocks.length; j++) {
    #             const a = blocks[j];
    #             const b = notebook.blocks[j];
    #             expect(a.type).to.equal(b.type);
    #             if (b.text !== undefined) {
    #             expect(a.text).to.equal(b.text.trim());
    #             }
    #             expect(a.start).to.equal(b.start);
    #             //  expect(a.id).to.equal(b.id);
