"""Profile a data file."""
import click
import logging
import os
import pathlib
import sys

from rich.console import Console

from data_file_profiler_utils import constants
from data_file_profiler_utils.file_utils import check_infile_status
from data_file_profiler_utils.manager import Manager


DEFAULT_OUTDIR = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.splitext(os.path.basename(__file__))[0],
    constants.DEFAULT_TIMESTAMP
)


error_console = Console(stderr=True, style="bold red")

console = Console()


def validate_verbose(ctx, param, value):
    """Validate the validate option.

    Args:
        ctx (Context): The click context.
        param (str): The parameter.
        value (bool): The value.

    Returns:
        bool: The value.
    """

    if value is None:
        click.secho("--verbose was not specified and therefore was set to 'True'", fg='yellow')
        return constants.DEFAULT_VERBOSE
    return value


@click.command()
@click.option('--infile', help="The primary input file.")
@click.option('--logfile', help="The log file.")
@click.option('--outdir', help=f"The default is the current working directory - default is '{DEFAULT_OUTDIR}'.")
@click.option('--outfile', help="The output final report file.")
@click.option('--verbose', is_flag=True, help=f"Will print more info to STDOUT - default is '{constants.DEFAULT_VERBOSE}'.", callback=validate_verbose)
def main(
    infile: str,
    logfile: str,
    outdir: str,
    outfile: str,
    verbose: bool
):
    """Profile a data file."""
    error_ctr = 0

    if infile is None:
        error_console.print("--infile was not specified")
        error_ctr += 1

    if error_ctr > 0:
        click.echo(click.get_current_context().get_help())
        sys.exit(1)

    check_infile_status(infile)

    if outdir is None:
        outdir = DEFAULT_OUTDIR
        console.print(f"[yellow]--outdir was not specified and therefore was set to '{outdir}'[/]")

    if not os.path.exists(outdir):
        pathlib.Path(outdir).mkdir(parents=True, exist_ok=True)

        console.print(f"[yellow]Created output directory '{outdir}'[/]")

    if logfile is None:
        logfile = os.path.join(
            outdir,
            os.path.splitext(os.path.basename(__file__))[0] + '.log'
        )
        console.print(f"[yellow]--logfile was not specified and therefore was set to '{logfile}'[/]")

    logging.basicConfig(
        filename=logfile,
        format=constants.DEFAULT_LOGGING_FORMAT,
        level=constants.DEFAULT_LOGGING_LEVEL,
    )

    manager = Manager(
        outdir=outdir,
        verbose=verbose
    )

    manager.profile_file(
        infile=infile,
        outfile=outfile,
    )

    if verbose:
        print(f"The log file is '{logfile}'")
        console.print(f"[bold green]Execution of '{os.path.abspath(__file__)}' completed[/]")


if __name__ == "__main__":
    main()

