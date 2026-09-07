import logging


def configurar_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s"
    )