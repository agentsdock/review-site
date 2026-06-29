# Affiliate Static Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish existing affiliate landing pages from `/Users/hongc/codebuddy/job/aff/` under this Hugo site's `/aff/` URL prefix.

**Architecture:** Use Hugo's static asset pipeline only. Copy public HTML and image assets into `static/aff/`, where Hugo will copy them unchanged into `public/aff/` during build. Do not convert these pages into Hugo content, layouts, or templates.

**Tech Stack:** Hugo static site, plain HTML/CSS, shell file copy commands, `hugo` build verification.

---

## File Structure

Create these project files/directories:

```text
static/aff/levoit/contact.html
static/aff/levoit/levoit-de-store.html
static/aff/levoit/lvac-200.html
static/aff/levoit/privacy-policy.html
static/aff/levoit/terms.html
static/aff/levoit/vital200s-air-purifier.html
static/aff/seesii/index.html
static/aff/seesii/assets/images/seesii-mini-chainsaw-accessory-1.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-accessory-2.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-aplus-1.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-main.jpg
static/aff/syokami/contact.html
static/aff/syokami/privacy-policy.html
static/aff/syokami/steak-knives-affiliate.html
```

Do not create or copy:

```text
static/aff/levoit/.claude/
static/aff/seesii/CLAUDE.md
static/aff/seesii/notes/
static/aff/syokami/.claude/
```

No existing source file should be modified for the integration. `public/` is build output and must not be committed.

---

### Task 1: Prepare static affiliate directories

**Files:**
- Create directory: `static/aff/levoit/`
- Create directory: `static/aff/seesii/assets/images/`
- Create directory: `static/aff/syokami/`

- [ ] **Step 1: Confirm target does not contain conflicting files**

Run:

```bash
find static/aff -maxdepth 4 -type f 2>/dev/null | sort
```

Expected output before this integration:

```text
```

If the command prints existing files, stop and compare them to the source files before continuing. Do not overwrite existing files silently.

- [ ] **Step 2: Create the target directories**

Run:

```bash
mkdir -p static/aff/levoit static/aff/seesii/assets/images static/aff/syokami
```

Expected: command exits with no output.

- [ ] **Step 3: Verify directories exist**

Run:

```bash
find static/aff -maxdepth 3 -type d | sort
```

Expected output includes:

```text
static/aff
static/aff/levoit
static/aff/seesii
static/aff/seesii/assets
static/aff/seesii/assets/images
static/aff/syokami
```

---

### Task 2: Copy Levoit public pages

**Files:**
- Create: `static/aff/levoit/contact.html`
- Create: `static/aff/levoit/levoit-de-store.html`
- Create: `static/aff/levoit/lvac-200.html`
- Create: `static/aff/levoit/privacy-policy.html`
- Create: `static/aff/levoit/terms.html`
- Create: `static/aff/levoit/vital200s-air-purifier.html`

- [ ] **Step 1: Copy only public Levoit HTML files**

Run:

```bash
cp \
  /Users/hongc/codebuddy/job/aff/levoit/contact.html \
  /Users/hongc/codebuddy/job/aff/levoit/levoit-de-store.html \
  /Users/hongc/codebuddy/job/aff/levoit/lvac-200.html \
  /Users/hongc/codebuddy/job/aff/levoit/privacy-policy.html \
  /Users/hongc/codebuddy/job/aff/levoit/terms.html \
  /Users/hongc/codebuddy/job/aff/levoit/vital200s-air-purifier.html \
  static/aff/levoit/
```

Expected: command exits with no output.

- [ ] **Step 2: Verify copied Levoit files**

Run:

```bash
find static/aff/levoit -maxdepth 2 -type f | sort
```

Expected output:

```text
static/aff/levoit/contact.html
static/aff/levoit/levoit-de-store.html
static/aff/levoit/lvac-200.html
static/aff/levoit/privacy-policy.html
static/aff/levoit/terms.html
static/aff/levoit/vital200s-air-purifier.html
```

- [ ] **Step 3: Verify Levoit internal config was not copied**

Run:

```bash
test ! -e static/aff/levoit/.claude && echo "levoit internal files excluded"
```

Expected output:

```text
levoit internal files excluded
```

---

### Task 3: Copy SEESII public page and assets

**Files:**
- Create: `static/aff/seesii/index.html`
- Create: `static/aff/seesii/assets/images/seesii-mini-chainsaw-accessory-1.jpg`
- Create: `static/aff/seesii/assets/images/seesii-mini-chainsaw-accessory-2.jpg`
- Create: `static/aff/seesii/assets/images/seesii-mini-chainsaw-aplus-1.jpg`
- Create: `static/aff/seesii/assets/images/seesii-mini-chainsaw-main.jpg`

- [ ] **Step 1: Copy SEESII index page**

Run:

```bash
cp /Users/hongc/codebuddy/job/aff/SEESII/index.html static/aff/seesii/index.html
```

Expected: command exits with no output.

- [ ] **Step 2: Copy SEESII public image assets**

Run:

```bash
cp \
  /Users/hongc/codebuddy/job/aff/SEESII/assets/images/seesii-mini-chainsaw-accessory-1.jpg \
  /Users/hongc/codebuddy/job/aff/SEESII/assets/images/seesii-mini-chainsaw-accessory-2.jpg \
  /Users/hongc/codebuddy/job/aff/SEESII/assets/images/seesii-mini-chainsaw-aplus-1.jpg \
  /Users/hongc/codebuddy/job/aff/SEESII/assets/images/seesii-mini-chainsaw-main.jpg \
  static/aff/seesii/assets/images/
```

Expected: command exits with no output.

- [ ] **Step 3: Verify copied SEESII files**

Run:

```bash
find static/aff/seesii -maxdepth 4 -type f | sort
```

Expected output:

```text
static/aff/seesii/assets/images/seesii-mini-chainsaw-accessory-1.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-accessory-2.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-aplus-1.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-main.jpg
static/aff/seesii/index.html
```

- [ ] **Step 4: Verify SEESII internal docs were not copied**

Run:

```bash
test ! -e static/aff/seesii/CLAUDE.md && test ! -e static/aff/seesii/notes && echo "seesii internal files excluded"
```

Expected output:

```text
seesii internal files excluded
```

---

### Task 4: Copy Syokami public pages

**Files:**
- Create: `static/aff/syokami/contact.html`
- Create: `static/aff/syokami/privacy-policy.html`
- Create: `static/aff/syokami/steak-knives-affiliate.html`

- [ ] **Step 1: Copy only public Syokami HTML files**

Run:

```bash
cp \
  /Users/hongc/codebuddy/job/aff/syokami/contact.html \
  /Users/hongc/codebuddy/job/aff/syokami/privacy-policy.html \
  /Users/hongc/codebuddy/job/aff/syokami/steak-knives-affiliate.html \
  static/aff/syokami/
```

Expected: command exits with no output.

- [ ] **Step 2: Verify copied Syokami files**

Run:

```bash
find static/aff/syokami -maxdepth 2 -type f | sort
```

Expected output:

```text
static/aff/syokami/contact.html
static/aff/syokami/privacy-policy.html
static/aff/syokami/steak-knives-affiliate.html
```

- [ ] **Step 3: Remove broken Syokami Terms links from copied target files**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
for path in [
    Path('static/aff/syokami/contact.html'),
    Path('static/aff/syokami/privacy-policy.html'),
]:
    text = path.read_text()
    text = text.replace(' · <a href="terms.html">Terms</a>', '')
    text = text.replace('<a href="terms.html">Terms</a> · ', '')
    text = text.replace('<a href="terms.html">Terms</a>', '')
    path.write_text(text)
PY
```

Expected: command exits with no output.

- [ ] **Step 4: Verify Syokami Terms links are gone**

Run:

```bash
if grep -R "terms.html" static/aff/syokami; then
  exit 1
else
  echo "syokami broken terms links removed"
fi
```

Expected output:

```text
syokami broken terms links removed
```

---

### Task 5: Build and verify published paths

**Files:**
- Build output only: `public/aff/` generated by Hugo. Do not commit `public/`.

- [ ] **Step 1: Run Hugo build**

Run:

```bash
hugo
```

Expected: command exits successfully. Hugo may print normal build statistics.

- [ ] **Step 2: Verify generated affiliate pages exist**

Run:

```bash
test -f public/aff/levoit/levoit-de-store.html && \
test -f public/aff/levoit/lvac-200.html && \
test -f public/aff/levoit/vital200s-air-purifier.html && \
test -f public/aff/seesii/index.html && \
test -f public/aff/syokami/steak-knives-affiliate.html && \
echo "affiliate pages generated"
```

Expected output:

```text
affiliate pages generated
```

- [ ] **Step 3: Verify excluded files are not published**

Run:

```bash
if find public/aff -name '.claude' -o -name '.git' -o -name '.github' -o -name '.DS_Store' -o -name 'README.md' -o -name 'CLAUDE.md' -o -path '*/notes/*' | grep .; then
  exit 1
else
  echo "internal files excluded from public aff output"
fi
```

Expected output:

```text
internal files excluded from public aff output
```

- [ ] **Step 4: Check git status**

Run:

```bash
git status --short
```

Expected output includes the newly created `static/aff/` files and the docs under `docs/superpowers/`. It may also show the pre-existing `.gitignore` modification. Do not include `public/` in a commit unless the user explicitly asks to publish build output through git.

---

### Task 6: Commit source and planning files only

**Files:**
- Commit: `docs/superpowers/specs/2026-06-29-aff-static-integration-design.md`
- Commit: `docs/superpowers/plans/2026-06-29-aff-static-integration.md`
- Commit: `static/aff/`
- Do not commit: `public/`
- Do not commit: unrelated pre-existing `.gitignore` change unless the user explicitly confirms it belongs to this task.

- [ ] **Step 1: Stage only relevant files**

Run:

```bash
git add docs/superpowers/specs/2026-06-29-aff-static-integration-design.md \
  docs/superpowers/plans/2026-06-29-aff-static-integration.md \
  static/aff
```

Expected: command exits with no output.

- [ ] **Step 2: Review staged files**

Run:

```bash
git diff --cached --name-only
```

Expected output:

```text
docs/superpowers/plans/2026-06-29-aff-static-integration.md
docs/superpowers/specs/2026-06-29-aff-static-integration-design.md
static/aff/levoit/contact.html
static/aff/levoit/levoit-de-store.html
static/aff/levoit/lvac-200.html
static/aff/levoit/privacy-policy.html
static/aff/levoit/terms.html
static/aff/levoit/vital200s-air-purifier.html
static/aff/seesii/assets/images/seesii-mini-chainsaw-accessory-1.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-accessory-2.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-aplus-1.jpg
static/aff/seesii/assets/images/seesii-mini-chainsaw-main.jpg
static/aff/seesii/index.html
static/aff/syokami/contact.html
static/aff/syokami/privacy-policy.html
static/aff/syokami/steak-knives-affiliate.html
```

If `.gitignore` or `public/` appears, unstage it before committing.

- [ ] **Step 3: Commit relevant files**

Run:

```bash
git commit -m "feat: add affiliate static pages"
```

Expected: git creates a commit containing only the plan, spec, and `static/aff/` source files.

---

## Self-Review

Spec coverage:

- `/aff/` shared path is implemented by `static/aff/` in Tasks 1-4.
- Lowercase brand directories are implemented in Tasks 1-4.
- Public Levoit, SEESII, and Syokami files are copied in Tasks 2-4.
- User-approved removal of broken Syokami `terms.html` links is covered in Task 4.
- `SEESII/notes/`, `CLAUDE.md`, `.claude`, and other internal files are excluded and verified in Tasks 2, 3, and 5.
- Hugo build validation is covered in Task 5.
- `public/` is treated as build output and excluded from commit in Task 6.

Placeholder scan: no placeholders remain.

Type/path consistency: all paths match the design spec and source inventory.
