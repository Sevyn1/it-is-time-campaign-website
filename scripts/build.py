"""Render the maintained static site from the preserved campaign content."""
from pathlib import Path
import json,html,re
ROOT=Path(__file__).resolve().parent.parent
DATA=json.loads((ROOT/'content/archive.json').read_text())
esc=html.escape

def page(title,body,active='home',nested=False,description='Explore the preserved It Is Time campaign archive: biography, original policy topics and photographs.'):
 p='../' if nested else ''
 links=[('home','Home','index.html'),('biography','Biography','itistime/biography.html'),('plan','The plan','plan.html'),('gallery','Gallery','gallery.html')]
 nav=''.join(f'<a href="{p}{url}"'+(' aria-current="page"' if key==active else '')+f'>{label}</a>' for key,label,url in links)
 rendered=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{esc(description,quote=True)}"><meta name="theme-color" content="#123e2e"><title>{esc(title)} · It Is Time Archive</title><link rel="icon" href="{p}itistime/Images/logo6.png"><link rel="stylesheet" href="{p}assets/site.css"><script src="{p}assets/site.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><div class="archive-banner"><div class="wrap"><span>2023 CAMPAIGN ARCHIVE</span><span>Historical material · Not an active campaign</span></div></div>
<header class="site-header"><div class="wrap header-row"><a class="wordmark" href="{p}index.html" aria-label="It Is Time archive home">IT IS TIME<span>.NG</span></a><button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav">Menu <span aria-hidden="true">☰</span></button><nav id="main-nav" aria-label="Main navigation">{nav}<a class="nav-download" href="{p}itistime/plan.pdf" download>Download plan <span aria-hidden="true">↓</span></a></nav></div></header>
<main id="main" tabindex="-1">{body}</main><footer class="site-footer"><div class="wrap footer-grid"><div><a class="wordmark" href="{p}index.html">IT IS TIME<span>.NG</span></a><p>A preserved campaign website.<br>Original material, presented as an archive.</p></div><nav aria-label="Footer navigation">{nav}</nav><div><p>Browse the original document.</p><a href="{p}itistime/plan.pdf" download>Download the plan (PDF, 13 MB) ↓</a><p class="small">Campaign photographs and copy retain their original provenance.</p></div></div><div class="wrap footer-bottom"><span>Campaign archive · 2023</span><a href="#main">Back to top ↑</a></div></footer></body></html>'''
 return '\n'.join(line.rstrip() for line in rendered.splitlines())+'\n'

def cards(p=''):
 return ''.join(f'''<a class="topic-card" href="{p}itistime/{t['slug']}.html" data-topic data-search="{esc(t['title']+' '+t['summary'],quote=True)}"><span class="topic-number">{i+1:02}</span><h3>{esc(t['title'])}</h3><p>{esc(t['summary'])}</p><span class="card-link">Read the original topic <span aria-hidden="true">↗</span></span></a>''' for i,t in enumerate(DATA['topics']))

def video(p=''):
 return f'''<dialog id="film-dialog" class="media-dialog" aria-labelledby="film-title"><div class="dialog-heading"><h2 id="film-title">Archived campaign film</h2><button type="button" data-close-dialog>Close ×</button></div><video controls playsinline preload="none" poster="{p}itistime/Images/prof9.jpg" data-video-src="{p}itistime/MAN WITH THE PEOPLE.mp4"></video><p>Original campaign footage. Video loads only when opened.</p></dialog>'''

home=f'''<section class="wrap hero"><div class="hero-copy"><p class="eyebrow">THE ORIGINAL CAMPAIGN · PRESERVED</p><h1>IT IS<br><span>TIME.</span></h1><p class="hero-intro">Discover the campaign’s original ideas, the person behind them and the moments captured along the way.</p><div class="actions"><a class="button" href="plan.html">Explore the plan <span aria-hidden="true">↗</span></a><button class="button button-light" type="button" data-open-film>Watch the film <span aria-hidden="true">▷</span></button></div><p class="hero-note">Yemi Osinbajo · 2023 presidential campaign archive</p></div><figure class="hero-media"><img src="itistime/Images/prof9.jpg" alt="Yemi Osinbajo seated at a desk in an archived photograph" fetchpriority="high" width="754" height="667"><figcaption><span>FROM THE ARCHIVE</span><span>Ideas. Leadership. People.</span></figcaption></figure></section>
<section class="topic-band"><div class="wrap section-heading"><div><p class="eyebrow">THE ORIGINAL PLATFORM</p><h2>Nine topics.<br>One place to explore.</h2></div><p>Read the campaign’s original proposals in full. This material reflects the campaign period.</p></div><div class="wrap topic-grid">{cards()}</div></section>
<section class="wrap about-strip"><img src="itistime/Images/prof5.jpg" alt="Archived portrait of Yemi Osinbajo" width="398" height="739" loading="lazy"><div><p class="eyebrow">THE BIOGRAPHY</p><h2>Meet the person<br>behind the campaign.</h2><p>The original biography covers education, professional life and public service, as described in the campaign archive.</p><a class="text-link" href="itistime/biography.html">Read the biography ↗</a></div></section>
<section class="wrap gallery-preview"><div class="section-heading"><div><p class="eyebrow">CAMPAIGN MOMENTS</p><h2>A look through the lens.</h2></div><a class="text-link" href="gallery.html">Explore all photographs ↗</a></div><div class="preview-grid">'''+''.join(f'<a href="gallery.html#photo-{i+1}" aria-label="View archived photograph {i+1}"><img src="{src}" alt="Archived campaign photograph {i+1}" loading="lazy"></a>' for i,src in enumerate(DATA['gallery'][:3]))+f'</div></section>{video()}'
(ROOT/'index.html').write_text(page('Home',home))
plan=f'''<section class="wrap page-intro"><p class="eyebrow">THE ORIGINAL PLATFORM</p><h1>Explore the plan.</h1><p>Nine policy topics, preserved from the original campaign website.</p><div class="search-row"><label for="topic-search">Find a topic<input type="search" id="topic-search" placeholder="Search topic titles and summaries…" autocomplete="off"></label><a class="button button-light" href="itistime/plan.pdf" download>Full plan · PDF ↓</a></div><p id="search-status" role="status" aria-live="polite">9 topics</p></section><section class="wrap topic-grid plan-grid" aria-label="Policy topics">{cards()}</section><div class="wrap empty-state" id="no-topics" hidden><h2>No topics match that search.</h2><p>Try another word, or clear your search to see all topics.</p><button class="button button-light" type="button" id="clear-search">Clear search</button></div>'''
(ROOT/'plan.html').write_text(page('The plan',plan,'plan'))

def article_body(source):
 counter=0;toc=[]
 def heading(match):
  nonlocal counter
  counter+=1;level=match.group(1);text=match.group(2);slug=f'section-{counter}';plain=re.sub('<[^>]+>','',text).strip()
  toc.append(f'<li><a href="#{slug}">{plain}</a></li>');return f'<h{level} id="{slug}">{text}</h{level}>'
 body=re.sub(r'<h([234])>(.*?)</h\1>',heading,source,flags=re.S)
 return body,toc

for i,t in enumerate(DATA['topics']):
 body,toc=article_body(t['html']);side='<aside class="article-nav"><p class="eyebrow">IN THIS ARTICLE</p><nav aria-label="Article contents"><ol>'+''.join(toc)+'</ol></nav></aside>' if toc else ''
 prev=DATA['topics'][(i-1)%len(DATA['topics'])];nxt=DATA['topics'][(i+1)%len(DATA['topics'])]
 content=f'''<section class="wrap article-heading"><a class="back-link" href="../plan.html">← All topics</a><p class="eyebrow">ORIGINAL CAMPAIGN PLATFORM · {i+1:02} / 09</p><h1>{esc(t['title'])}</h1><p class="archive-note">Preserved campaign proposals. These are historical statements, not current government commitments.</p></section><div class="wrap article-layout">{side}<article class="prose">{body}<div class="article-next"><a href="{prev['slug']}.html">← {esc(prev['title'])}</a><a href="{nxt['slug']}.html">{esc(nxt['title'])} →</a></div></article></div>'''
 (ROOT/'itistime'/f"{t['slug']}.html").write_text(page(t['title'],content,'plan',True,t['summary']))
body,toc=article_body(DATA['biography'])
bio=f'''<section class="wrap article-heading"><a class="back-link" href="../index.html">← Home</a><p class="eyebrow">FROM THE ORIGINAL CAMPAIGN</p><h1>The biography.</h1><p class="archive-note">The biography below is preserved from the campaign website. Titles, accomplishments and descriptions reflect its original publication period.</p></section><div class="wrap article-layout"><aside class="article-nav"><p class="eyebrow">IN THIS BIOGRAPHY</p><nav aria-label="Biography contents"><ol>{''.join(toc)}</ol></nav><button class="button button-light" type="button" data-open-film>Watch the archived film ▷</button></aside><article class="prose">{body}<a class="text-link" href="../plan.html">Explore the original platform ↗</a></article></div>{video('../')}'''
(ROOT/'itistime/biography.html').write_text(page('Biography',bio,'biography',True))
gallery='''<section class="wrap page-intro"><p class="eyebrow">CAMPAIGN MOMENTS</p><h1>From the archive.</h1><p>Original photographs from the campaign website. Open any image for a closer look.</p></section><section class="wrap gallery-grid" aria-label="Campaign photographs">'''+''.join(f'''<button class="gallery-item" type="button" id="photo-{i+1}" data-photo="{src}" data-photo-index="{i}" aria-label="Open archived photograph {i+1}"><img src="{src}" alt="Archived campaign photograph {i+1}" loading="lazy"><span><span>PHOTOGRAPH {i+1:02}</span><span aria-hidden="true">↗</span></span></button>''' for i,src in enumerate(DATA['gallery']))+'''</section><dialog class="media-dialog photo-dialog" id="photo-dialog" aria-labelledby="photo-title"><div class="dialog-heading"><h2 id="photo-title">Archived campaign photograph</h2><button type="button" data-close-dialog>Close ×</button></div><img id="expanded-photo" alt="Selected archived campaign photograph"><div class="photo-controls"><button class="button button-light" type="button" id="previous-photo" aria-label="Previous photograph">← Previous</button><p id="photo-count" role="status" aria-live="polite"></p><button class="button button-light" type="button" id="next-photo" aria-label="Next photograph">Next →</button></div></dialog>'''
(ROOT/'gallery.html').write_text(page('Gallery',gallery,'gallery'))
print('Rendered home, topic index, gallery, biography and 9 original topics.')
