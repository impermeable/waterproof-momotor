import re
from typing import Dict, List
from ._notebook import Notebook

"""
Format that is expected:
we don't use marker lines, but use the lemma names themselves
Only keep characters that are utf8
"""
_LEMMA_FORMAT = r"Lemma (\w+) ?:"


def wp_formatter(notebook: Notebook, post_amble: str = "") -> str:
    """
    Concatenates the code blocks from the notebook, and adds a post amble.
    """
    code_blocks = notebook.code_blocks()
    string = "\n".join(code_blocks)
    string + "\n" + post_amble + "\n"  # I hope \n is ok and \r\n is not necessary?
    return string


def lemma_names(string) -> List[str]:
    """
    Finds the Lemma names using RegExp.
    """
    return re.findall(_LEMMA_FORMAT, string)


def lemmas(string) -> Dict[str, str]:
    """
    Finds the Lemma names using RegExp.
    """
    # TODO end of lemma will be indicated with Qed or Admitted?
    prev_name_index = 0
    lemma_names = []
    lemma_start_idx = []
    for match in re.finditer(_LEMMA_FORMAT, string):
        name_index = match.start()
        start_lemma_index = string.rfind("Lemma", prev_name_index, name_index)
        lemma_names.append(match.group(1))
        lemma_start_idx.append(start_lemma_index)
    lemma_start_idx.append(len(string))
    lemmas_extracted = dict()
    for i, lemma in enumerate(lemma_names):
        lemmas_extracted[lemma] = string[lemma_start_idx[i] : lemma_start_idx[i + 1]]
    return lemmas_extracted


def insert_lemma(code: str, lemma_name: str, lemma_code: str):
    """
    Replace lemma code. Lemma must end with Admitted. or Qed.
    """
    start_lemma_index = code.index("Lemma " + lemma_name)
    endings = []
    for ending in ("Admitted.", "Qed."):  # TODO remove Coq comments
        try:
            ending_index = code.index(ending, start_lemma_index)
            endings.append(ending_index)
        except ValueError:
            pass
    assert len(endings) > 0
    end_lemma_index = min(endings)
    end_lemma_index = code.index(".", end_lemma_index) + 1

    return code[:start_lemma_index] + lemma_code + code[end_lemma_index:]
