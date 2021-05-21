import typer
import Site from ssg.site

source = "content"
dest = "dist"

def main(source, dest):
    config = {
        "source":"source",
        "dest":"dest"
    }
    site = Site(**config)
    site.build()

typer.run(main)

