from ..ingestion_daemon import config as cfg
from ..file_parser.parser_factory import FileParserFactory

pdf_file_parser = FileParserFactory.instance(
    "application/pdf", cfg.get_config("PDF_PARSER", "tika"),
)
html_file_parser = FileParserFactory.instance(
    "text/html", cfg.get_config("HTML_PARSER", "tika"),
)
