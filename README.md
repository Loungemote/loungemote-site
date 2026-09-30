# Loungemote site

The official website for Loungemote: the product home page and the public pages the App Store listing needs. It is a static Jekyll site with no theme, no JavaScript framework and no third-party requests. GitHub Pages builds it from the `main` branch.

| Page | URL | App Store Connect field |
|---|---|---|
| Home | https://loungemote.github.io/loungemote-site/ | Marketing URL |
| Support | https://loungemote.github.io/loungemote-site/support/ | Support URL |
| Privacy | https://loungemote.github.io/loungemote-site/privacy/ | Privacy Policy URL |
| Terms | https://loungemote.github.io/loungemote-site/terms/ | Link in the app description and the paywall (Terms of Use / EULA) |

The app opens the same three pages from `Links.swift`. Keep the two in step.

## Layout

```
_config.yml            site settings: email, effective date, App Store link, url and baseurl
index.html             home page (English, the default language); its text is in _data/home/en.yml
zh/ ja/ de/            translated home pages; their text is in _data/home/<i18n>.yml
_remotes/              one page per TV platform, for example /samsung-tv-remote/ (`remote` layout)
llms.txt               plain summary for AI assistants and search tools
privacy.md terms.md support.md   text pages (Markdown, `page` layout)
404.html robots.txt site.webmanifest favicon.ico favicon.svg
_layouts/              default.html (shell), page.html (text pages with a table of contents),
                       remote.html (platform pages), home-i18n.html (the home page in every language)
_includes/             head, header, footer, phone frame, App Store badge, icons, trademark line
_data/home/*.yml       home page text per language, FAQ included (it also feeds the FAQPage structured data).
                       Every language has the same sections: hero, features, how it works, devices, privacy, FAQ
_data/platforms.yml    supported platforms (home page, support page, platform pages, llms.txt)
_data/languages.yml    translated home pages (hreflang links and the footer language menu)
_data/app.yml          app features for the structured data
assets/css/main.css    all styles; tokens follow the app's design tokens (dark theme)
assets/js/main.js      menu, scroll reveal, card spotlight; the site works without it
assets/img/            app screens (WebP), icons, social image
tools/                 render_assets.py and check_site.py (not published)
```

## Before and after launch

Everything is in `_config.yml`.

- `email`: the support address. It must be a mailbox that someone reads, and it must match `supportEmail` in the app.
- `effective_date`: shown on the Privacy Policy and the Terms of Use. Change it when either page changes.
- `app_store_url`: empty until the app is live. While it is empty, the download buttons say "Coming soon to the App Store". Set it to the App Store link and they become download links.
- `app_store_id`: the numeric Apple ID. It adds Safari's Smart App Banner.

## Keep the privacy policy true

Update `privacy.md` and the App Privacy answers in App Store Connect when you:

- add an SDK (analytics, crash reporting, RevenueCat, ads),
- add a server or an account feature,
- store new kinds of data.

The app uses Google Analytics for Firebase and Firebase Crashlytics, on by default and turned off with **Settings > Privacy > Share Usage Data**. The Privacy Policy, the home page privacy section and FAQ in `_data/home/*.yml`, `support.md` and `llms.txt` describe this. Keep them in step with the app's tracking plan (`docs/analytics/tracking-plan.md` in the app repo).

The Privacy Policy also says that this website has no cookies or analytics and loads nothing from other sites. Keep that true, or change the text.

When the app adds a platform, update `_data/platforms.yml`, `_includes/trademarks.html`, `_data/app.yml`, `llms.txt` and each `_data/home/*.yml`, and add a page in `_remotes/`.

## Search and AI answers

- Titles: the home page title is `seo_title` in `index.html` (translated pages: `title` in `_data/home/<i18n>.yml`); platform pages set `seo_title` in their front matter. Keep the words close to the App Store name and subtitle (`docs/app-store/metadata.json` in the app repo).
- Platform pages state only what the app's **Supported TVs** screen says (`MoreSettings.swift`): pairing, typing, apps, inputs and casting per platform. Their `faq` front matter is also the page's FAQPage structured data.
- Translated home pages: add a language in `_data/languages.yml`, `_data/home/<i18n>.yml` and `<i18n>/index.html`. Use the app's own words for setting names (from `Localizable.xcstrings`). Legal and support pages stay in English. Change `en.yml` first and keep every language to the same sections and items.
- After launch, set `app_store_url` and `app_store_id`: the structured data then gets the download link and `sameAs`, and `llms.txt` links the App Store.
- Add the site to Google Search Console and submit `sitemap.xml`.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000/loungemote-site/.

## Checks

```bash
bundle exec jekyll build
python3 tools/check_site.py
```

`check_site.py` checks every internal link, anchor, image and script in `_site/`, the meta tags of each page, and the structured data.

## Images

The app screens, the icons and the social image are rendered from the app repo's design mockups, with the same brand-neutral text as the App Store screenshots:

```bash
python3 tools/render_assets.py ../Loungemote
```

It needs Google Chrome, `beautifulsoup4` and `Pillow`. The device frame around each screen is CSS (`.phone` in `main.css`).

## Custom domain later

Add the domain in **Settings > Pages > Custom domain**, set `url` to it and `baseurl` to `""` in `_config.yml`. Every link in the site goes through `relative_url`, so nothing else changes. GitHub Pages then redirects the `github.io` URLs to the new domain. Update the URLs in App Store Connect and in the app's `Links.swift`.
