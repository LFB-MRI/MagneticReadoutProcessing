import os
from pathlib import Path

PIPELINES_FOLDER: str = str(Path(str(os.path.dirname(__file__))).parent.joinpath("pipelines"))
TMP_FOLDER: str = str(Path(PIPELINES_FOLDER).joinpath("generated/"))
STATIC_FOLDER: str = str(Path(str(os.path.dirname(__file__))).joinpath("static"))
TEMPLATE_FOLDER: str = str(Path(str(os.path.dirname(__file__))).joinpath("templates"))