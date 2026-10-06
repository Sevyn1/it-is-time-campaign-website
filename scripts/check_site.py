"""Audit maintained pages for broken local resources, anchors and obsolete embeds."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,sys
ROOT=Path(__file__).resolve().parent.parent
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=set();self.links=[];self.errors=[];self.title=False;self.main=False;self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get('id'):
   if a['id'] in self.ids:self.errors.append('duplicate id '+a['id'])
   self.ids.add(a['id'])
  if tag=='title':self.title=True
  if tag=='main':self.main=True
  if tag=='h1':self.h1+=1
  if tag=='img' and not a.get('alt'):self.errors.append('image has no descriptive alt text')
  if any(key.startswith('on') for key in a):self.errors.append('inline event handler')
  for attribute in ('href','src','poster','data-video-src','data-photo'):
   if attribute in a:self.links.append((tag,attribute,a[attribute]))
  if tag=='script' and a.get('src') not in ('assets/site.js','../assets/site.js'):self.errors.append('unexpected runtime script')
  if tag=='iframe':self.errors.append('unexpected third-party embed')

data=json.loads((ROOT/'content/archive.json').read_text())
paths=[ROOT/'index.html',ROOT/'plan.html',ROOT/'gallery.html',ROOT/'itistime/biography.html']+[ROOT/'itistime'/f"{t['slug']}.html" for t in data['topics']]
pages={}
for path in paths:
 parser=Page();parser.feed(path.read_text());pages[path.resolve()]=parser
errors=[];references=0
for path,parser in pages.items():
 for message in parser.errors:errors.append(f'{path.relative_to(ROOT)}: {message}')
 if not parser.title or not parser.main or parser.h1!=1:errors.append(f'{path.relative_to(ROOT)}: missing title/main or not exactly one h1')
 for tag,attribute,url in parser.links:
  references+=1;parts=urlsplit(url)
  if parts.scheme or parts.netloc:errors.append(f'{path.relative_to(ROOT)}: unexpected external reference {url}');continue
  if not url or url=='#':errors.append(f'{path.relative_to(ROOT)}: placeholder reference');continue
  target=(path.parent/unquote(parts.path)).resolve() if parts.path else path
  if not target.is_relative_to(ROOT) or not target.is_file():errors.append(f'{path.relative_to(ROOT)}: missing local file {url}')
  elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:errors.append(f'{path.relative_to(ROOT)}: missing anchor {url}')
if errors:
 print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(pages)} maintained pages; {references} references; local files and anchors resolve, labelled images, one main heading, no legacy scripts or external embeds.')
