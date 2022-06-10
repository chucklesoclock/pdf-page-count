import pathlib
import sys
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
import logging

import click
from rich.console import Console
from rich.table import Table
from rich.text import Text

logging.basicConfig(
    filename="pdf_page_counter.log",
    filemode="w",
    format="%(levelname)s:%(message)s",
    level=logging.DEBUG,
)


def count_pages(path: pathlib.Path) -> int:
    try:
        with open(path.resolve(), mode="rb") as f:
            reader = PdfReader(f)
            num_pages = len(reader.pages)
        logging.info(f'"{path.name}":pages={num_pages}')
        return num_pages
    except PdfReadError as e:
        logging.error(f'"{path.name}":{e}:could not be read as PDF')
        return 0
    except Exception as e:
        print(
            f"ERROR: Unhandled exception, check log file for details. Exiting...",
            file=sys.stderr,
        )
        logging.critical(f'"{path.name}":{e}', exc_info=True)
        sys.exit()


@click.command()
@click.argument(
    "dir_path",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
    default=pathlib.Path(),
)
@click.option(
    "-r",
    "--recursive",
    is_flag=True,
    default=False,
    help="recursive search; count all pdfs in all subdirectors of DIR_PATH",
)
@click.option(
    "-t",
    "--table",
    is_flag=True,
    default=False,
    help="print a table to terminal using rich library",
)
def count(dir_path, recursive, table):
    """
    Count all the PDFs in the directory DIR_PATH.

    "1, 2, 3 PDFs do I see, HA HA HA"

        -- Count von Count, Seasame Street
    """
    pdf_path_gen = getattr(dir_path, "rglob" if recursive else "glob")("*.pdf")

    if not table:
        total_pages = sum(count_pages(p) for p in pdf_path_gen)
        print(total_pages)
    else:
        print()
        table = Table(title="Count of PDF Pages", show_edge=True)
        table.add_column(
            Text.from_markup("PDF Path", justify="center"),
            Text.from_markup("[u]Total Pages", justify="right", style="red"),
            style="cyan",
            justify="left",
        )
        table.add_column("Pages", str(0), justify="right", style="magenta")
        total_pages = 0
        for pdf_path in pdf_path_gen:
            pages = count_pages(pdf_path)
            table.add_row(str(pdf_path), str(pages))
            total_pages += pages
        table.show_footer = True
        table.footer_style = "red"
        table.columns[1].footer = f"[u]{total_pages}"
        console = Console()
        console.print(table)
        print()

    logging.info(f"TOTAL_PAGE_COUNT={total_pages}")


if __name__ == "__main__":
    count()
