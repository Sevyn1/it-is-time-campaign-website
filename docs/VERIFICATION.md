# Verification — October 6, 2026

## Static checks

The standard-library audit passed for **13 maintained pages and 352 local references**. It checks referenced files, fragment anchors, unique IDs, labelled images, page titles, a single main heading, placeholder links, inline event handlers and unexpected runtime scripts/third-party embeds.

The page generator completed successfully, and JavaScript passed Node's syntax check. CI rebuilds generated pages and rejects differences so content and compiled pages stay synchronized.

## Browser smoke checks

- Desktop and 390 × 844 phone-sized homepage layouts were inspected. The temporary viewport override was reset.
- Mobile navigation expanded, exposed its links and collapsed after navigating Home.
- Topic search for `jobs` showed one matching topic; an unmatched query showed the empty state; Clear search restored all nine topics.
- The Jobs article opened with its original content and contents links; the Technology anchor resolved.
- A gallery image opened in a modal. Next and arrow-key navigation worked, including wrapping from photograph 1 to 11. Escape closed the viewer and returned focus to the triggering photograph.
- The on-demand video loaded without an error, reported its 222.506-second duration and remained paused until playback was selected. Closing the dialog paused the video. No autoplay is enabled.
- The plan PDF remains a valid local file, linked from all maintained pages. Download-link existence is audited; its historical political statements are not independently fact-checked here.

## Limits

These are static checks and browser smoke checks, not a full cross-browser, screen-reader, performance or accessibility audit. The site is local and the repository remains private. No production hosting, forms, mailing-list submission, donations or third-party services were activated. Original copy and media are archival; original authorship and rights are not reassigned by this restoration.
