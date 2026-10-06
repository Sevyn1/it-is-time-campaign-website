# It Is Time — Campaign Archive

A restored HTML, CSS and JavaScript campaign website with a cohesive responsive layout, nine original policy articles, the preserved biography, searchable topics, an accessible photograph viewer and an on-demand video player.

**HTML · CSS · JavaScript · Static content · Python build/check tools**

![Restored homepage](docs/preview.png)

This is historical material from the campaign for the 2023 election cycle, not an active campaign or a statement of current government policy. It is a frontend project; it does not claim Python backend, Java, React or machine-learning functionality.

## Run locally

From the repository root:

```sh
python3 -m http.server 8088 --bind 127.0.0.1
```

Open http://127.0.0.1:8088/. No API key, database or package installation is required. Port 8088 avoids the separate freight-calculator preview.

## Working flows

- Shared desktop navigation, a mobile menu with expanded-state semantics, keyboard focus styles and a skip-to-content link.
- A searchable topic index with matching counts, an empty state and a clear-search action. Search covers titles and summaries, not full article text.
- All nine original topic pages, with next/previous navigation. Longer articles and the biography include an in-page contents list.
- Eleven original photographs, opened in a modal with previous/next actions, arrow-key navigation, Escape dismissal and native focus return. Homepage photograph links open the corresponding viewer.
- The original local video opens on demand, with playback controls; it does not autoplay or download on page load. Closing the dialog pauses playback.
- Download links to the original plan PDF. File size is shown before download.
- Archive notices distinguish original campaign statements from current information. No live signup, mailing-list, contact or donation submission is provided.

## Update content

`content/archive.json` contains the preserved article HTML, biography and photograph paths. To regenerate the maintained pages:

```sh
python3 scripts/build.py
python3 scripts/check_site.py
node --check assets/site.js
```

The generator uses Python's standard library; the website itself is static. CI rebuilds the pages, rejects uncommitted generated differences, checks local resources/anchors and validates JavaScript syntax. No third-party frontend libraries, fonts, trackers or embedded services are loaded by the maintained pages.

## Review and provenance

[Verification](docs/VERIFICATION.md) records completed checks and remaining limits. [Provenance](docs/PROVENANCE.md) explains preserved material, third-party history and the restoration work.

Existing history is retained. The October 2026 design and implementation were developed with Codex assistance, directed and reviewed by Favour Ojo. Campaign copy/media and recovered third-party source are not claimed as original sole-authored work. The repository remains private; no public deployment is claimed.
