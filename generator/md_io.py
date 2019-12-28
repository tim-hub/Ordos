from os import listdir, path
from os.path import isfile, join, isdir
import glob
from typing import List

def get_all_files(the_path:str) -> List[str]:
    return [f for f in listdir(the_path) if isfile(join(the_path, f))]

def get_all_dirs(the_path:str) -> List[str]:
    return [f for f in listdir(the_path) if isdir(join(the_path, f))]

def get_all_markdowns(the_path:str) -> List[str]:
    return [f for f in glob.glob(path.abspath(the_path) + '/**/*.[Mm][Dd]', recursive=True)]

def save_all_htmls(html: List[str]) -> None:
    return