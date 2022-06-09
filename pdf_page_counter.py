import pathlib
import sys
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
import logging

logging.basicConfig(
    filename="pdf_page_counter.log",
    filemode="w",
    format="%(levelname)s:%(message)s",
    level=logging.DEBUG,
)


def count_page(path: pathlib.Path) -> int:
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


def main():
    total_pages = sum(
        count_page(p) for p in pathlib.Path().iterdir() if p.suffix.lower() == ".pdf"
    )
    logging.info(f"TOTAL_PAGE_COUNT={total_pages}")
    print(total_pages)


if __name__ == "__main__":
    main()
