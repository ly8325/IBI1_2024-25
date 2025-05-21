import xml.dom.minidom as dom
import xml.sax
from datetime import datetime
from collections import defaultdict

# ======================== DOM Parser ========================
def dom_parser(xml_file):
    start_time = datetime.now()
    
    max_counts = {
        'molecular_function': {'id': '', 'count': 0},
        'biological_process': {'id': '', 'count': 0},
        'cellular_component': {'id': '', 'count': 0}
    }
    
    doc = dom.parse(xml_file)
    terms = doc.getElementsByTagName('term')
    
    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].firstChild.data
        if namespace not in max_counts:
            continue
        
        term_id = term.getElementsByTagName('id')[0].firstChild.data
        is_a_count = len(term.getElementsByTagName('is_a'))
        
        if is_a_count > max_counts[namespace]['count']:
            max_counts[namespace]['id'] = term_id
            max_counts[namespace]['count'] = is_a_count
    
    return max_counts, datetime.now() - start_time

# ======================== SAX Parser ========================
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.namespace = ""
        self.term_id = ""
        self.is_a_count = 0
        self.max_counts = defaultdict(lambda: {'id': '', 'count': 0})
    
    def startElement(self, tag, attrs):
        self.current_data = tag
        if tag == 'term':
            self.namespace = ""
            self.term_id = ""
            self.is_a_count = 0
    
    def characters(self, content):
        if self.current_data == 'namespace':
            self.namespace = content.strip()
        elif self.current_data == 'id':
            self.term_id = content.strip()
    
    def endElement(self, tag):
        if tag == 'term':
            if self.namespace in ['molecular_function', 'biological_process', 'cellular_component']:
                current_max = self.max_counts[self.namespace]
                if self.is_a_count > current_max['count']:
                    current_max['id'] = self.term_id
                    current_max['count'] = self.is_a_count
        elif tag == 'is_a':
            self.is_a_count += 1
        self.current_data = ""

def sax_parser(xml_file):
    start_time = datetime.now()
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    return handler.max_counts, datetime.now() - start_time

# ======================== Main Execution ========================
if __name__ == "__main__":
    xml_file = "go_obo.xml"
    
    # DOM Processing
    dom_results, dom_time = dom_parser(xml_file)
    
    # SAX Processing
    sax_results, sax_time = sax_parser(xml_file)
    
    # Print Results
    print("=== DOM Results ===")
    for ns, data in dom_results.items():
        print(f"{ns.replace('_', ' ').title()}: Term {data['id']} has {data['count']} is_a relationships")
    
    print("\n=== SAX Results ===")
    for ns, data in sax_results.items():
        print(f"{ns.replace('_', ' ').title()}: Term {data['id']} has {data['count']} is_a relationships")
    
    # Time Comparison
    print(f"\nDOM Processing Time: {dom_time.total_seconds():.4f} seconds")
    print(f"SAX Processing Time: {sax_time.total_seconds():.4f} seconds")
    print("# SAX was faster" if sax_time < dom_time else "# DOM was faster")