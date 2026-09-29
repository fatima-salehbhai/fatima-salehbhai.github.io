# fatima-salehbhai.github.io

Personal site. Single static page, no build step.

- `index.html` — the page
- `photo.jpg` — headshot
- `resume.html` + `resume.enc` — password-protected resume. The PDF is AES-256-GCM encrypted in the browser with a PBKDF2-derived key; the plaintext PDF is never committed.
- `encrypt_resume.py` — re-run with the password whenever `../Fatima_Salehbhai_Resume.pdf` changes: `python3 encrypt_resume.py '<password>'`

Deployed via GitHub Pages from `main`.
