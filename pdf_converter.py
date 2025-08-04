from pathlib import Path

from docling.backend.pypdfium2_backend import PyPdfiumDocumentBackend
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableStructureOptions
from docling.document_converter import DocumentConverter, PdfFormatOption


def create_pdf_converter() -> DocumentConverter:
    return DocumentConverter(
        allowed_formats=[InputFormat.PDF],
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=PdfPipelineOptions(
                    do_ocr=False,
                    do_table_structure=False,
                    table_structure_options=TableStructureOptions(
                        do_cell_matching=False
                    ),
                ),
                backend=PyPdfiumDocumentBackend,
            )
        },
    )


def convert_to_markdown(pdf_path: Path, converter: DocumentConverter) -> str:
    document = converter.convert(pdf_path).document
    return document.export_to_markdown()
