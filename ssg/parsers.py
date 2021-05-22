from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions = []
    extensions: List[str]

    def valid_extension(self, extension):
        return self.extensions.contains(extension)

    def parse(path: Path, source: Path, dest: Path):
        try:
            raise NotImplementedError
        except Exception as e:

    def read(path: Path):
        with path.open() as file:
            return file.read()

    def write(path: Path, dest: Path, content, ext=".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with full_path.open() as file:
            file.write(content)

    def copy(path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / source)

class ResourceParser:
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]
    
    super(Parser, self).parse(path, source, dest):
        copy(path, source, dest)

