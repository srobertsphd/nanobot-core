from app.config.settings import settings

from pathlib import Path
from docling_core.types.doc import ImageRefMode, PictureItem, TableItem
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter, PdfFormatOption

OUTPUT_DIR = str(settings.file_paths.get_converted_docs_path())


input_doc_path = "https://docs.google.com/document/d/1YGpHp7avHQMojJRbkAyP8io0ZqarRvMKm_ulQ6dYq0g/export?format=pdf"
output_dir = Path(OUTPUT_DIR)

# Important: For operating with page images, we must keep them, otherwise the DocumentConverter
# will destroy them for cleaning up memory.
# This is done by setting PdfPipelineOptions.images_scale, which also defines the scale of images.
# scale=1 correspond of a standard 72 DPI image
# The PdfPipelineOptions.generate_* are the selectors for the document elements which will be enriched
# with the image field

IMAGE_RESOLUTION_SCALE = 2.0
pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
pipeline_options.generate_page_images = True
pipeline_options.generate_picture_images = True


doc_converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)

conv_res = doc_converter.convert(input_doc_path)

type(conv_res)
conv_res.model_dump()

output_dir.mkdir(parents=True, exist_ok=True)
doc_filename = "test_sop"
table_dir = output_dir / doc_filename / "tables"
picture_dir = output_dir / doc_filename / "pictures"
page_dir = output_dir / doc_filename / "pages"
table_dir.mkdir(parents=True, exist_ok=True)
picture_dir.mkdir(parents=True, exist_ok=True)
page_dir.mkdir(parents=True, exist_ok=True)


# Save page images
for page_no, page in conv_res.document.pages.items():
    page_no = page.page_no
    page_image_filename = output_dir / page_dir / f"page-{page_no}.png"
    with page_image_filename.open("wb") as fp:
        page.image.pil_image.save(fp, format="PNG")

# Save images of figures and tables
table_counter = 0
picture_counter = 0
for element, _level in conv_res.document.iterate_items():
    if isinstance(element, TableItem):
        table_counter += 1
        element_image_filename = output_dir / table_dir / f"table-{table_counter}.png"
        with element_image_filename.open("wb") as fp:
            element.get_image(conv_res.document).save(fp, "PNG")

    if isinstance(element, PictureItem):
        picture_counter += 1
        element_image_filename = (
            output_dir / picture_dir / f"picture-{picture_counter}.png"
        )
        with element_image_filename.open("wb") as fp:
            element.get_image(conv_res.document).save(fp, "PNG")

# Save markdown with embedded pictures
md_filename = output_dir / doc_filename / f"{doc_filename}-with-images.md"
conv_res.document.save_as_markdown(md_filename, image_mode=ImageRefMode.EMBEDDED)

# Save markdown with externally referenced pictures
md_filename = output_dir / doc_filename / f"{doc_filename}-with-image-refs.md"
conv_res.document.save_as_markdown(md_filename, image_mode=ImageRefMode.REFERENCED)

# Save HTML with externally referenced pictures
html_filename = output_dir / doc_filename / f"{doc_filename}-with-image-refs.html"
conv_res.document.save_as_html(html_filename, image_mode=ImageRefMode.REFERENCED)

#################################

for element, level in conv_res.document.iterate_items():
    # print(f"Level {level}: {type(element).__name__}")

    if type(element).__name__ == "TextItem":
        print("\nTextItem Properties:")
        print(f"  Label: {element.label}")
        print(f"  Content Layer: {element.content_layer}")
        print(f"  Self Ref: {element.self_ref}")
        print(f"  Parent: {element.parent}")
        print(f"  Children: {len(element.children)}")

        # Print provenance information if available
        if hasattr(element, "prov") and element.prov:
            print("\nProvenance Information:")
            for prov in element.prov:
                print(f"  Page Number: {prov.page_no}")
                if hasattr(prov, "bbox"):
                    print(
                        f"  Bounding Box: left={prov.bbox.l}, top={prov.bbox.t}, right={prov.bbox.r}, bottom={prov.bbox.b}"
                    )

        # Print the actual text content
        if hasattr(element, "text"):
            print(
                f"\nText Content: {element.text[:100]}..."
                if len(element.text) > 100
                else f"\nText Content: {element.text}"
            )

        print("\n" + "-" * 50 + "\n")

document = conv_res.document

if hasattr(document, "furniture"):
    furniture = document.furniture

    # You can then inspect the furniture object
    print(f"Furniture object type: {type(furniture).__name__}")

dump = conv_res.model_dump()
if isinstance(dump, dict):
    print("Keys:", list(dump.keys()))

# Get the top-level dump
dump = conv_res.model_dump()


# Function to safely print nested structures
def print_nested_dict(d, indent=0):
    indent_str = "  " * indent
    for key, value in d.items():
        if isinstance(value, dict):
            print(f"{indent_str}{key}:")
            print_nested_dict(value, indent + 1)
        elif isinstance(value, list):
            print(f"{indent_str}{key}: List with {len(value)} items")
            if value and len(value) > 0:
                print(f"{indent_str}  First item type: {type(value[0]).__name__}")
        else:
            print(f"{indent_str}{key}: {type(value).__name__}")


# Look at each top-level key
for key in dump.keys():
    print(f"\n=== {key.upper()} ===")
    value = dump[key]

    if isinstance(value, dict):
        print("Dictionary contents:")
        print_nested_dict(value)
    elif isinstance(value, list):
        print(f"List with {len(value)} items")
        if value:
            print(f"First item type: {type(value[0]).__name__}")
            # If it's a list of dictionaries, show the keys of the first item
            if isinstance(value[0], dict):
                print("Keys in first item:", list(value[0].keys()))
    else:
        print(f"Value type: {type(value).__name__}")
        print(f"Value: {value}")

# You can also access specific keys directly
print("\n=== SPECIFIC KEY EXAMPLES ===")

# Look at input details
if "input" in dump:
    print("\nInput details:")
    print_nested_dict(dump["input"])

# Look at status details
if "status" in dump:
    print("\nStatus details:")
    print_nested_dict(dump["status"])

# Look at document structure
if "document" in dump:
    print("\nDocument structure:")
    print_nested_dict(dump["document"])

# Look at pages
if "pages" in dump:
    print("\nPages structure:")
    if isinstance(dump["pages"], list):
        print(f"Number of pages: {len(dump['pages'])}")
        if dump["pages"]:
            print("First page keys:", list(dump["pages"][0].keys()))
