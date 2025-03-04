"""
Web scraping utilities.

Provides functions for scraping websites and converting URLs to markdown.
"""

import xml.etree.ElementTree as ET
from app.services.document_service import DocumentService

# Create a singleton instance
document_service = DocumentService()

def read_urls_from_sitemap(sitemap_path: str) -> list[str]:
    """Read URLs from local sitemap XML file"""
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    
    # Handle namespace in sitemap
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
    
    print(f"Found {len(urls)} URLs in sitemap")
    for url in urls:
        print(f"  - {url}")
        
    return urls



def batch_convert_urls_to_markdown(urls: list[str]) -> dict[str, str]:
    """
    Convert a list of URLs to markdown using docling document converter
    
    Args:
        urls: List of URLs to convert
        
    Returns:
        Dictionary mapping URLs to their markdown content
    """
    results = {}
    
    print(f"Converting {len(urls)} URLs to markdown...")
    for url in urls:
        try:
            markdown = document_service.url_to_markdown(url)
            results[url] = markdown
            print(f"  ✓ Successfully converted {url}")
        except Exception as e:
            print(f"  ✗ Failed to convert {url}: {str(e)}")
            results[url] = None
    
    successful = sum(1 for content in results.values() if content is not None)
    print(f"\nConversion complete: {successful}/{len(urls)} URLs converted successfully")
    
    return results
