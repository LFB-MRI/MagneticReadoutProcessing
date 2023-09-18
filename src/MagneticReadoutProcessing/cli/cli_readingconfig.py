import typer
import cli_helper
import cli_datastorage
import os

app = typer.Typer()

BASEPATH = os.path.dirname(__file__)+'/'


@app.command()
def setup(ctx: typer.Context):
    cfg = cli_datastorage.CLIDatastorage()


    print("CONFIGURE READING")

    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX)
    resp = typer.prompt("READING-NAME:", curr)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX, resp)

    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER)
    if len(curr) <= 0:
        curr = BASEPATH
    resp = typer.prompt("OUTPUT-FOLDER", curr)

    if len(curr) <= 0:
        print("user response empty: so setting the default path")
        resp = BASEPATH

    if not os.path.exists(resp):
        print("note folder does not exists: {}. please create first before running a measurement cycle".format(BASEPATH))
    if not os.path.exists(resp):
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER, resp)



    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT)
    if len(curr) <= 0:
        curr = 1
    resp = int(typer.prompt("NUMBER DATAPOINTS:", curr))
    if resp <= 0:
        print("invalid number for datapoints to collect: minimum is 1".format(1))
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT, "1")
    else:
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT, str(resp))



    curr = cfg.get_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT)
    if len(curr) <= 0:
        curr = 1
    resp = int(typer.prompt("NUMBER AVERAGE READINGS PER DATAPOINT:", curr))
    if resp <= 0:
        print("invalid number for number readings per datapoint : minimum is 1".format(1))
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT, "1")
    else:
        cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT, str(resp))



@app.command()
def reset(ctx: typer.Context):
    cfg = cli_datastorage.CLIDatastorage()
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_PREFIX, "")
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_OUTPUT_FOLDER, BASEPATH)
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_DATAPOINT_COUNT, "1")
    cfg.set_value(cli_datastorage.CLIDatastorageEntries.READING_AVERAGE_COUNT, "1")
    print("READING CONFIG RESET SUCCESS")




@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    ctx.obj = cli_datastorage.Common()






if __name__ == "__main__":
    cli_helper.__fix_import__fix_import()
    app()