from import_MRP import __fix_import__
__fix_import__()

from pathlib import Path
import os



PIPELINES_BASEPATH: str = str(Path('./pipelines').resolve())
if not os.path.exists(PIPELINES_BASEPATH):
        Path(PIPELINES_BASEPATH).mkdir(parents=True, exist_ok=True)
print(PIPELINES_BASEPATH)
READINGS_BASEPATH: str = str(Path('../readings').resolve())


import typer




#load_dotenv()
app = typer.Typer(add_completion=True)
app.add_typer(udpp_pipeline.app, name="pipeline")








@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass





if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()