import glob
from os import listdir, path
from os.path import isfile, join, isdir
from typing import List


def get_all_files(the_path: str) -> List[str]:
    return [f for f in listdir(the_path) if isfile(join(the_path, f))]


def get_all_dirs(the_path: str) -> List[str]:
    return [f for f in listdir(the_path) if isdir(join(the_path, f))]

def get_all_site_paths(the_path: str) -> List[str]:
    dirs = get_all_dirs(the_path)
    return list(map(lambda p: the_path + p, dirs))

def get_all_markdowns(the_path: str) -> List[str]:
    return [f for f in glob.glob(path.abspath(the_path) + '/**/*.[Mm][Dd]', recursive=True)]

def get_template_path(site_path: str) -> str:
    return site_path + '/templates'