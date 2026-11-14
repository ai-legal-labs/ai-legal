# AI Legal — AILL LLC

Static editorial website for AI Legal, the DBA of AILL LLC, United States. Recreated from the public ai.legal website with four original essays, a research lab, selected speaking entries, and company, contact, privacy and terms pages.

## Build and check

Python 3.12+, no third-party dependencies:

```sh
python scripts/build.py
python scripts/check.py
```

`dist/` is the publishable website. Content is readable without JavaScript. Internal links use relative paths and work at a project subpath or a custom domain. No trackers, external font requests, forms, payments, document uploads or AI backend are included.

Edit the essays in `content/essays.json`, page content in `scripts/build.py` and the design in `assets/style.css`. The original essays remain dated historical commentary, with a note about changes to law and guidance.

## GitHub Pages

1. Merge this branch into `main` when ready to release. The previous repository version remains available in Git history.
2. In repository **Settings → Pages → Build and deployment**, select **GitHub Actions**. An owner with Pages administration access must do this; the connected GitHub tool cannot change Pages settings.
3. Run **Build and deploy website** under Actions, or push a change to `main`. Pull requests build and check without production deployment.
4. Check the staging URL reported by the deployment, normally `https://ai-legal-labs.github.io/ai-legal/`. Confirm all pages before changing the production domain. Canonical URLs intentionally point to the eventual `https://ai.legal` domain.
5. In Pages settings, add `ai.legal` as the custom domain, verify domain ownership if prompted and configure HTTPS. Use GitHub's current custom-domain documentation for the exact DNS records. Preserve existing MX, email authentication and other verification records. The `www` host should be configured consistently.
6. When the custom domain is connected, set `PAGES_BASE_PATH=/` for the build in the workflow so the 404 page also uses the domain root. Normal pages already support both deployments. Add `dist/CNAME` containing `ai.legal` if using branch-based Pages instead of the supplied Actions workflow.
7. Confirm HTTPS, both root and www host behaviour, legacy essay paths, RSS and sitemap. Leave Vercel available until the new site and DNS are verified. This change does not cancel or delete any Vercel project or paid subscription.

GitHub Pages has usage restrictions: this version is an informational research publication. It is not a checkout, transactional business application or commercial SaaS host. Reassess hosting before adding paid transactions, accounts or hosted AI tools.

## Business Hub preparation

`business-hub-profile.json` contains proposed profile copy and a separate list of unresolved items. It is preparation, not a submitted or verified profile. Use the actual options offered by Business Hub; a suggested category is descriptive, not a promised platform taxonomy.

The owner supplied the company name, trade name, country and email. State of registration, public mailing address, entity registration details, any DBA registration, business hours and phone have not been verified or invented. Use exact official records for verification. No claim of professional licensing, regulatory approval, OpenAI endorsement or guaranteed compliance is made.

Official guidance checked 14 November 2026:

- https://help.openai.com/en/articles/20001635-setting-up-your-business-on-chatgpt
- https://openai.com/policies/businesses-in-chatgpt/
- https://openai.com/policies/business-agents-policy/
- https://openai.com/policies/businesses-in-chatgpt-terms/
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits

OpenAI requires claim approval and Persona identity verification for profile updates. A website cannot guarantee approval. An agent, if desired, has separate availability and policy requirements. No business agent, product feed or fabricated product catalogue is included. Review actual offerings and data practices before enabling any future features or submitting profile copy. Legal notices reflect this static website and direct email correspondence; they must be revisited when processing practices change.

## Validation limits

The build checks local links, anchors, assets, page metadata, structured data, RSS and sitemap. This workspace did not expose the managed browser QA interface, so visual browser QA and production DNS/HTTPS verification remain to be completed in the hosted environment.
