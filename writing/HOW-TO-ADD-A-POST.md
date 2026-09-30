# Adding a post

1. Write it in Markdown (start with the first paragraph, not a title; the page adds the title) and save it as `writing/posts/<slug>.md` (slug = short-lowercase-name, e.g. `ornithopter`).
2. Add an entry to `writing/posts.json`:

```json
{ "slug": "ornithopter", "title": "Building an ornithopter", "date": "2019-04-01", "summary": "One line about it." }
```

For a post that lives elsewhere (Medium, LinkedIn, Substack), skip the .md file and add `"url": "https://..."` instead.
Posts sort newest first. Images go in `writing/posts/img/` and are referenced as `img/name.jpg`.
