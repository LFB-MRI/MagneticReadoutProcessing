import typer
from MRPproxy import proxy



#load_dotenv()
app = typer.Typer(add_completion=True)
app.add_typer(proxy.app_typer, name="proxy")






@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    pass


def run():
    app()




if __name__ == "__main__":
    run()