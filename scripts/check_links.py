from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
root = Path(__file__).resolve().parents[1]
errors = []
class Checker(HTMLParser):
    def handle_starttag(self, tag, attributes):
        for name, value in attributes:
            if name not in ('src','href') or not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (root / unquote(url.path).lstrip('/')) if url.path.startswith('/') else self.page.parent / unquote(url.path)
            if not target.exists():
                errors.append(f'{self.page.relative_to(root)}: {value}')
checker = Checker()
pages = [root/'index.html', root/'gallery.html', *(root/'itistime').glob('*.html')]
for page in pages:
    checker.page = page
    checker.feed(page.read_text(errors='replace'))
for error in errors:
    print(error)
print(f'{len(pages)} pages checked; {len(errors)} broken local references')
raise SystemExit(bool(errors))
