# Integrate affiliate landing pages under /aff/

Date: 2026-06-29

## Decision

Use a pure static integration. Copy approved public files from `/Users/hongc/codebuddy/job/aff/levoit`, `/Users/hongc/codebuddy/job/aff/SEESII`, and `/Users/hongc/codebuddy/job/aff/syokami` into this Hugo project's `static/aff/` directory.

Hugo will copy these files directly into the generated site. The pages will not be converted into Hugo content or templates.

## Goals

- Publish the three affiliate landing page groups under one shared path: `/aff/`.
- Preserve the original standalone HTML, CSS, and conversion layouts, except for the user-approved removal of broken Syokami `terms.html` links because no Syokami terms page exists.
- Keep brand folders lowercase in the published URL.
- Avoid publishing internal notes, repository metadata, Claude configuration, or build artifacts.
- Keep the change narrow and reversible.

## Target source directories

```text
/Users/hongc/codebuddy/job/aff/levoit
/Users/hongc/codebuddy/job/aff/SEESII
/Users/hongc/codebuddy/job/aff/syokami
```

## Target project structure

```text
static/
└── aff/
    ├── levoit/
    │   ├── contact.html
    │   ├── levoit-de-store.html
    │   ├── lvac-200.html
    │   ├── privacy-policy.html
    │   ├── terms.html
    │   └── vital200s-air-purifier.html
    ├── seesii/
    │   ├── index.html
    │   └── assets/
    └── syokami/
        ├── contact.html
        ├── privacy-policy.html
        └── steak-knives-affiliate.html
```

## URL rules

The shared prefix is `/aff/`. Brand directory names are lowercase.

Expected public URLs:

```text
/aff/levoit/contact.html
/aff/levoit/levoit-de-store.html
/aff/levoit/lvac-200.html
/aff/levoit/privacy-policy.html
/aff/levoit/terms.html
/aff/levoit/vital200s-air-purifier.html
/aff/seesii/
/aff/syokami/contact.html
/aff/syokami/privacy-policy.html
/aff/syokami/steak-knives-affiliate.html
```

`/aff/seesii/` works because `static/aff/seesii/index.html` is copied to `public/aff/seesii/index.html`.

## Syokami link adjustment

The copied Syokami `contact.html` and `privacy-policy.html` files must not retain footer links to `terms.html`, because `/Users/hongc/codebuddy/job/aff/syokami/terms.html` does not exist. Remove only the broken `terms.html` link and adjacent separator from the copied target files under `static/aff/syokami/`; do not modify the source directory.

## Files to exclude

Do not copy internal or non-public files/directories, including:

```text
.claude/
.git/
.github/
.DS_Store
README.md
CLAUDE.md
notes/
public/
```

For `SEESII`, `notes/compliance.md` stays out of `static/` because it is an internal compliance note, not a public asset.

## Architecture

This uses Hugo's static file pipeline only:

1. Source HTML and assets are stored under `static/aff/`.
2. `hugo` copies them to `public/aff/` during build.
3. Cloudflare Pages serves the generated files as static routes.

No Hugo layout, shortcode, content bundle, or menu integration is required for this version.

## Error handling and conflict rules

- If `static/aff/` already exists, inspect it before overwriting files.
- If a target file already exists and differs from the source, stop and report the conflict instead of silently replacing it.
- Do not modify `.env`, CI/CD config, deployment settings, or production deployment state as part of this change.
- Do not delete existing unrelated files.

## Validation

After implementation, run:

```bash
hugo
```

Success criteria:

- Hugo build succeeds.
- `public/aff/levoit/levoit-de-store.html` exists.
- `public/aff/levoit/lvac-200.html` exists.
- `public/aff/levoit/vital200s-air-purifier.html` exists.
- `public/aff/seesii/index.html` exists.
- `public/aff/syokami/steak-knives-affiliate.html` exists.
- `public/aff/seesii/notes/` does not exist.
- No `.claude`, `.git`, `.github`, `.DS_Store`, `README.md`, or `CLAUDE.md` files are published under `public/aff/`.

## Out of scope

- Converting pages into Hugo templates.
- Creating a public `/aff/` index page.
- Editing affiliate links or copy.
- Changing Cloudflare Pages settings.
- Deploying to production.
