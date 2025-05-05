import xml.etree.ElementTree as ET
from docling.document_converter import DocumentConverter

class SitemapService:
    def __init__(self):
        self.converter = DocumentConverter()
        
    def read_urls_from_sitemap(self, sitemap_path: str) -> list[str]:
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
    
    def url_to_markdown(self, url: str):
        """Convert a URL to markdown."""
        return self.converter.url_to_markdown(url)
    
    def batch_convert_urls_to_markdown(self, urls: list[str]) -> dict[str, str]:
        """Convert URLs to markdown"""
        results = {}
        
        print(f"Converting {len(urls)} URLs to markdown...")
        for url in urls:
            try:
                markdown = self.converter.url_to_markdown(url)
                results[url] = markdown
                print(f"  ✓ Successfully converted {url}")
            except Exception as e:
                print(f"  ✗ Failed to convert {url}: {str(e)}")
                results[url] = None
        
        successful = sum(1 for content in results.values() if content is not None)
        print(f"\nConversion complete: {successful}/{len(urls)} URLs converted successfully")
        
        return results

