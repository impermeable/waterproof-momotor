import re
from typing import Dict, List
"""
Format that is expected:
we don't use marker lines, but use the lemma names themselves
Only keep characters that are utf8
"""
_LEMMA_FORMAT = r'Lemma (\w+) ?:'

def wp_formatter(notebook, post_amble = ""):
    code_blocks = notebook.code_blocks()
    string = "\n".join(code_blocks)
    string + "\n" + post_amble + "\n" # I hope \n is ok and \r\n is not necessary?
    return string

def lemma_names(notebook) -> List[str]:
    code_blocks = notebook.code_blocks()
    string = "\n".join(code_blocks)
    return re.findall(_LEMMA_FORMAT, string)

def lemmas(notebook) -> Dict[str, str]:
    code_blocks = notebook.code_blocks()
    string = "\n".join(code_blocks)
    prev_name_index = 0
    lemma_names = []
    lemma_start_idx = []
    for match in re.finditer(_LEMMA_FORMAT, string):
        name_index = match.start()
        start_lemma_index = string.rfind('Lemma', prev_name_index, name_index)
        lemma_names.append(match.group(1))
        lemma_start_idx.append(start_lemma_index)
    lemma_start_idx.append(len(string))
    lemmas_extracted = dict()
    for i, lemma in enumerate(lemma_names):
        lemmas_extracted[lemma] = string[lemma_start_idx[i]:lemma_start_idx[i+1]]
    return lemmas_extracted
    

