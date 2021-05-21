from pathlib import Path
source = ""
dest = ""

class Site:

    __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / relative_to(self.source)
        mkdir(parents=True, exist_ok=True)

    def build():
        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*")
            if (path.isdir()):
                create_dir(path)

