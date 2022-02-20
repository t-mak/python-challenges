import pathlib

new_dir = pathlib.Path.home() / "images"
new_dir.mkdir(exist_ok=True)
documents_dir = pathlib.Path.home() / "documents"

for path in documents_dir.rglob("*.*"):
    if path.suffix == ".png" or path.suffix == ".gif" or path.suffix == ".jpg":
        path.replace(new_dir / path.name)

