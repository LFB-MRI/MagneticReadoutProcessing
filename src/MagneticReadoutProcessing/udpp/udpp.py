from pathlib import Path
import os
from import_MRP import __fix_import__

import udpp_pipeline
import udpp_editor
import typer




#load_dotenv()
app = typer.Typer(add_completion=True)
app.add_typer(udpp_pipeline.app, name="pipeline")
app.add_typer(udpp_editor.app_typer, name="editor")






@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass





if __name__ == "__main__":
    __fix_import__()
    app()