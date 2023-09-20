from pathlib import Path
import os



PIPELINES_BASEPATH: str = str(Path('./pipelines').resolve())
if not os.path.exists(PIPELINES_BASEPATH):
        Path(PIPELINES_BASEPATH).mkdir(parents=True, exist_ok=True)
print(PIPELINES_BASEPATH)
READINGS_BASEPATH: str = str(Path('../readings').resolve())