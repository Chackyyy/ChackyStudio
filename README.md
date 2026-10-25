# Chacky Studio

The website for Chacky Studio, which designs and builds websites for small businesses. It's a single page with:

- the services and packages
- a request form that emails requests through Formspree
- a small game, Chacky Run

## Files

- `index.html` is the finished site. Upload this file to host it.
- `src/chacky-studio.html` is the page source.
- `build.py` turns the source into `index.html`.

## Building

After editing `src/chacky-studio.html`, rebuild the site:

```sh
python3 build.py
```

It needs Python 3 and no other packages.

## Hosting

`index.html` is self-contained, so any static host works, for example Netlify Drop or GitHub Pages.

## Request form

The form posts to the Formspree form `mwllvvyz`. The address that receives the requests is set in the Formspree dashboard, not in this code. Formspree also uses the visitor's email field as the reply-to address.
