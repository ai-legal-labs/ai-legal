"""Check the built public site for broken links and misleading infrastructure claims."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
errors=[]

class Document(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.schemas=[];self.schema=False;self.buffer='';self.h1=0;self.lang=None;self.canonical=None;self.description=None;self.title=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if 'id' in a:self.ids.add(a['id'])
        if tag=='meta' and a.get('name')=='description':self.description=a.get('content')
        if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
        if tag in ('a','link','img'):
            url=a.get('href') or a.get('src')
            if url:self.links.append(url)
        if tag=='img' and 'alt' not in a:errors.append('Image missing alt')
        if tag in ('form','iframe'):errors.append('Unexpected form or embedded service')
        if tag=='script':
            if a.get('type')!='application/ld+json':errors.append('Unexpected executable script')
            else:self.schema=True;self.buffer=''
        if tag in ('input','textarea'):errors.append('Unexpected data collection field')
    def handle_data(self,data):
        if self.schema:self.buffer+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.schema:self.schemas.append(json.loads(self.buffer));self.schema=False

documents={}
for path in DIST.rglob('*.html'):
    d=Document();text=path.read_text();d.feed(text);documents[path.resolve()]=d
    for ok,label in [(d.h1==1,'one h1'),(d.lang=='en','language'),(bool(d.description),'description'),(bool(d.canonical),'canonical'),(d.title,'title'),(bool(d.schemas),'structured data'),('AILL LLC' in text,'legal entity'),('milos@ai.legal' in text,'contact'),('id="main"' in text,'skip target')]:
        if not ok:errors.append(f'{path.relative_to(DIST)}: missing {label}')
    if 'TODO' in text or 'PLACEHOLDER' in text:errors.append(f'{path}: placeholder')

for path,d in documents.items():
    if path.name=='404.html':continue  # Pages injects arbitrary request path; separately built with configured base.
    for url in d.links:
        parsed=urlsplit(url)
        if parsed.scheme or parsed.netloc:continue
        target=(DIST/parsed.path.lstrip('/') if parsed.path.startswith('/') else path.parent/unquote(parsed.path)).resolve() if parsed.path else path
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{path.relative_to(DIST)}: broken {url}')
        elif parsed.fragment and target in documents and parsed.fragment not in documents[target].ids:errors.append(f'{path.relative_to(DIST)}: missing anchor {url}')

for f in ('sitemap.xml','feed.xml'):ET.parse(DIST/f)
sitemap=ET.parse(DIST/'sitemap.xml')
assert len(sitemap.getroot())==13
assert len(list(DIST.rglob('*.html')))==14
assert len(json.loads((ROOT/'content/essays.json').read_text()))==4
assert not (DIST/'CNAME').exists(), 'Production domain should be connected after staging verification.'
if errors:raise SystemExit('\n'.join(errors))
print(f'Passed: {len(documents)} HTML documents, all local links/assets/anchors, metadata, structured data, sitemap, RSS, and static privacy constraints.')
