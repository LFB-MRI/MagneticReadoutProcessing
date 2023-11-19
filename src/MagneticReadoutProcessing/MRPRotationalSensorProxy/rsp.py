import typer
from MRPRotationalSensorProxy import rsp_proxy



#load_dotenv()
app = typer.Typer(add_completion=True)
app.add_typer(rsp_proxy.app_typer, name="proxy")






@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass


def run():
    app()




if __name__ == "__main__":
    run()