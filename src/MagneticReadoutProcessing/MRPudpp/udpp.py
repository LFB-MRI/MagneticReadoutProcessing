from MRPudpp import udpp_pipeline, udpp_config, udpp_editor
import typer




#load_dotenv()
app = typer.Typer(add_completion=True)
app.add_typer(udpp_pipeline.app, name="pipeline")
app.add_typer(udpp_editor.app_typer, name="editor")




@app.callback(invoke_without_command=True)
def main(ctx: typer.Context, basepath: str = ""):
    if basepath is not None and len(basepath) > 0:

        udpp_config.UDPPConfig.set_base_folder(basepath)

        print(f"set pipeline folder to: {udpp_config.UDPPConfig.get_pipeline_folder()}")
        print(f"set result folder to : {udpp_config.UDPPConfig.get_tmp_folder()}")


def run():
    app()




if __name__ == "__main__":
    run()