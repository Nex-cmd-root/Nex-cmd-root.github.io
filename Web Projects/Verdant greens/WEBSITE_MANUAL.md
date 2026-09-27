# Verdant Greens — Website Feature Manual

> **Ndola's Greenhouse Botanical Nursery** | *Branching out into your space*  
> Official Email: ash2herbal@gmail.com  
> Orders & Payments: +260 775 971 03  
> Customer Support & Plant Doctor: +260 771 594 459  
> Facebook: [facebook.com/VerdantGreens](https://web.facebook.com/profile.php?id=61593869917364)

---

## Table of Contents

1. [Website Overview & Page Structure](#1-website-overview--page-structure)
2. [How to Update Products & Prices (`products.js`)](#2-how-to-update-products--prices-productsjs)
3. [How the Spectacle Gallery Works (`spectacles.js`)](#3-how-the-spectacle-gallery-works-spectaclesjs)
4. [How Shopping Cart & WhatsApp Checkout Works (`cart.js`)](#4-how-shopping-cart--whatsapp-checkout-works-cartjs)
5. [How the Contact Form & Email Logger Works (`contact.js`)](#5-how-the-contact-form--email-logger-works-contactjs)
6. [How Search & Filtering Works (`shop.js`)](#6-how-search--filtering-works-shopjs)
7. [How the Plant Symptom Doctor Works (`care.js`)](#7-how-the-plant-symptom-doctor-works-carejs)
8. [Light / Dark Theme System (`theme.js` & `style.css`)](#8-light--dark-theme-system-themejs--stylecss)
9. [SEO & Zambia Search Optimization](#9-seo--zambia-search-optimization)
10. [Admin: Viewing & Exporting Customer Inquiries](#10-admin-viewing--exporting-customer-inquiries)
11. [Adding New Pages or Plants](#11-adding-new-pages-or-plants)
12. [Image Folder Structure & WebP Format](#12-image-folder-structure--webp-format)

---

## 1. Website Overview & Page Structure

The Verdant Greens website is a **static HTML/CSS/JavaScript site** — no server or database is required. All pages load directly in the browser.

| Page | File | Purpose |
|------|------|---------|
| Home / Landing | `Index.html` | Main showpiece — spectacle gallery, hero, featured products, testimonials, FAQ |
| Store & Prices | `shop.html` | Full 30-item plant catalog with live search, multi-filter, quick view, and cart |
| Plant Care Guide | `care-guide.html` | Botanical symptom doctor, seasonal Zambia care tips, and watering rules |
| Contact Us | `contact.html` | Official phone/WhatsApp/email cards, interactive inquiry form, and admin leads logger |

### JavaScript Controllers

| File | Role |
|------|------|
| `products.js` | Central data source for all 30 on-sale plant items |
| `spectacles.js` | Data registry for the Home Page Spectacle Gallery images |
| `shop.js` | Search, filter, sort, and Quick View logic for the store |
| `cart.js` | Cart management, quantity editing, WhatsApp order formatting, and checkout |
| `contact.js` | Contact form validation, email logging to `localStorage`, and CSV/JSON export |
| `care.js` | Plant symptom diagnostics, symptom result cards, and seasonal tips |
| `theme.js` | Light/Dark mode detection, toggling, and `localStorage` persistence |
| `script.js` | Shared UI helpers — header scroll effects, FAQ toggles, spectacle gallery rendering |

---

## 2. How to Update Products & Prices (`products.js`)

All 30 on-sale items are defined in `products.js` as a global array `window.VG_PRODUCTS`.

### Adding a New Product

Open `products.js` and append a new object to the array:

```javascript
{
  id: 'vg-sXX',              // Unique ID (increment from last)
  name: 'Your Plant Name',   // Display name
  botanical: 'Latin Name',   // Botanical / scientific name
  price: 750,                // Price in Kwacha (number only, no K)
  image: 'images/products/your-plant-k750.webp', // WebP image path
  categories: ['indoor', 'office'],  // One or more from: statement, indoor, office, rare, succulent, bundle
  badge: 'Air Purifier',     // Short badge label displayed on card
  light: 'Bright Indirect',  // Light requirement
  water: 'Every 7 Days',     // Watering frequency
  petSafe: false,            // true or false
  size: 'Medium (55cm)',     // Physical size description
  desc: 'Short description displayed on card.',
  tags: ['keyword', 'trait', 'variety'] // Search tags
}
```

### Changing a Price

Find the plant by `id` or `name` in `products.js` and update the `price` field:
```javascript
price: 900  // Changed from 850 to 900
```

> **Note:** The WhatsApp checkout message in `cart.js` reads prices directly from `window.VG_PRODUCTS`, so the cart total updates automatically.

---

## 3. How the Spectacle Gallery Works (`spectacles.js`)

The Home Page Spectacle Gallery renders lush arrangement photos **without price tags** as pure botanical inspiration.

Data is defined in `spectacles.js` as `window.VG_SPECTACLES`. Each entry contains:
- `id`: Unique identifier
- `title`: Display title
- `image`: Path to `images/spectacles/*.webp`
- `category`: One of `bundles`, `focal`, `varieties`, `greenhouse`
- `tags`: Searchable trait tags

### Adding a New Spectacle Image

1. Place the converted `.webp` image in `images/spectacles/`
2. Add an entry in `spectacles.js`:

```javascript
{
  id: 'sp-XX',
  title: 'Your Arrangement Title',
  image: 'images/spectacles/your-image.webp',
  category: 'bundles',
  tags: ['lush', 'tropical', 'indoor']
}
```

The gallery on `Index.html` is rendered dynamically by `script.js` — no HTML changes needed.

---

## 4. How Shopping Cart & WhatsApp Checkout Works (`cart.js`)

The cart is managed entirely in the browser using `localStorage` under the key `verdant_greens_cart_v2`.

### Adding Items to Cart

Items can be added from:
- **Store grid cards** (Shop page) — `+ Add to Cart` button
- **Quick View modal** — `+ Add to Cart` button  
- **Featured product cards** (Home page) — `+ Add to Cart` button

Each button calls:
```javascript
window.vgCart.addItem('vg-s01')  // Pass the product ID from products.js
```

### Checkout via WhatsApp

When the customer clicks **"Order via WhatsApp"** in the cart:

1. Cart items, quantities, subtotal, and free delivery status are formatted into a pre-filled WhatsApp message.
2. The message is sent to **+260 775 971 03** (orders/payments line — strictly for transactions).
3. Payment instructions for Airtel Money, MTN MoMo, Zamtel Kwacha are appended.

> **Important:** The order line (+260 775 971 03) must ONLY be used for confirmed purchases and payment tracking. Support queries go to +260 771 594 459.

### Free Delivery Logic

- Orders **≥ K1,000** in Ndola: **Free delivery** automatically applied
- Orders **< K1,000**: Delivery fee discussed via WhatsApp

---

## 5. How the Contact Form & Email Logger Works (`contact.js`)

The contact form on `contact.html` collects and logs every customer inquiry to browser `localStorage` under the key `verdant_greens_inquiries_v1`.

### What Gets Logged

Each inquiry entry stores:
- Submission timestamp
- Customer name, email, phone number
- Inquiry topic and plant of interest
- Message content
- Newsletter opt-in status

### Viewing Logged Inquiries (Admin Panel)

1. Navigate to `contact.html`
2. In the footer, click **"📋 View Logged Inquiries"**
3. An admin modal will appear showing all stored customer leads

From the admin panel you can:
- **Export as CSV** — downloads a `.csv` file for use in Excel / Google Sheets
- **Export as JSON** — downloads raw JSON data
- **Clear all leads** — permanently removes logged data from browser storage

> **Note:** Because this is a static site, inquiries are stored locally in the browser. To collect leads centrally across all customers, you would need a backend service (see `HOSTING_GUIDE.md` for options like Formspree or Netlify Forms).

---

## 6. How Search & Filtering Works (`shop.js`)

The Store page provides real-time multi-facet filtering with **zero page reloads**.

### Search

The search bar (`#vg-store-search`) matches against:
- Plant display name
- Botanical name
- All tags array entries
- Category strings

Matching is **case-insensitive** and updates the visible grid instantly on every keystroke.

### Filter Categories

| Filter Pill | Matches `categories` field containing |
|-------------|--------------------------------------|
| Statement & Large | `statement` |
| Indoor Houseplants | `indoor` |
| Desk & Office | `office` |
| Rare & Flowering | `rare` |
| Succulents & Cacti | `succulent` |
| Curated Bundles | `bundle` |

### Price Range Filters

| Price Pill | Range |
|------------|-------|
| Premium Tier | K1,000 – K1,200 |
| Mid-Range | K700 – K950 |
| Starter & Budget | K400 – K650 |

### Care & Trait Filters

| Care Pill | Matches |
|-----------|---------|
| Pet-Friendly | `petSafe: true` |
| Low-Light Tolerant | tags include `low-light` |
| Bright Light / Sun | light field contains `Bright` or `Direct` |
| Air Purifying Pro | tags include `air-purifier` |

---

## 7. How the Plant Symptom Doctor Works (`care.js`)

The interactive **Plant Symptom Checker** on `care-guide.html` displays a diagnosis result card based on the selected symptom button.

### Available Symptoms

| Button | Symptom Key | Diagnosis |
|--------|-------------|-----------|
| 🍂 Yellowing Leaves | `yellow` | Overwatering, root rot, or nitrogen deficiency |
| 🥀 Brown Crispy Tips | `brown_tips` | Low humidity, fluoride in water, or sunburn |
| 🌿 Drooping Stems | `drooping` | Underwatering or root-bound condition |
| 🦟 Pests & Webbing | `pests` | Spider mites, fungus gnats, or mealy bugs |
| ☀️ Leggy & Pale Growth | `leggy` | Insufficient light — move to a brighter location |
| 🪨 White Topsoil Mold | `mold` | Overwatering or poor drainage — reduce moisture |

### Adding a New Symptom

In `care.js`, find the `VG_SYMPTOMS` object and add a new entry:
```javascript
'new_symptom': {
  title: 'Symptom Title',
  emoji: '🌿',
  causes: ['Cause 1', 'Cause 2'],
  remedies: ['Step 1: Do this', 'Step 2: Do that'],
  severity: 'moderate',  // 'mild', 'moderate', or 'urgent'
  waLink: true  // Whether to show WhatsApp Doctor CTA
}
```

---

## 8. Light / Dark Theme System (`theme.js` & `style.css`)

### How Theme Detection Works

On every page load, `theme.js` runs **before the page renders** (it's loaded in `<head>` without `defer`) to prevent flash-of-unstyled-content:

1. Checks `localStorage` for a saved preference (`verdant_greens_theme`)
2. Falls back to the OS/browser `prefers-color-scheme: dark` system setting
3. Applies the `data-theme="dark"` attribute to `<html>` immediately

### Theme Toggle Button

Every page has a `<button class="theme-toggle-btn">` in the navigation. Clicking it:
- Toggles `data-theme` between `"light"` and `"dark"` on the `<html>` element
- Saves the selection to `localStorage`
- Updates the button icon (🌙 for dark, ☀️ for light)

### CSS Variables

All colors are defined as CSS custom properties in `style.css` under `:root` (light theme) and `[data-theme="dark"]` (dark theme). To adjust any color globally, edit the relevant variable:

```css
:root {
  --verdant-primary: #2d6a4f;  /* Main jungle green */
  --verdant-accent: #74c69d;   /* Soft mint accent */
  --coral-accent: #f4845f;     /* Tropical coral */
  --cerulean-primary: #4cc9f0; /* Sky blue */
}
```

---

## 9. SEO & Zambia Search Optimization

All pages include the following SEO elements:

### Meta Tags (per page)
- `<meta name="description">` — 155-character descriptive summary
- `<meta name="keywords">` — Plant, location, and Zambia-specific terms
- `<meta name="geo.region" content="ZM-02">` — Copperbelt Province geo-tag
- `<meta name="geo.placename" content="Ndola">`

### Open Graph (Social Sharing)
- `og:locale` set to `en_ZM` for Zambian locale
- `og:image` pointing to a high-quality spectacle or product WebP
- `og:title`, `og:description`, and `og:url` per page

### Schema.org Structured Data (JSON-LD)
- `Index.html` — `Florist` with geo-coordinates, opening hours, and payment methods
- `shop.html` — `Store` with price range and address
- `care-guide.html` — `HowTo` schema for plant care steps
- `contact.html` — `ContactPage` linked to `LocalBusiness`

### Sitemap & Robots
- `sitemap.xml` — Lists all 4 pages with priority and change frequency
- `robots.txt` — Opens site to all crawlers, points to sitemap

---

## 10. Admin: Viewing & Exporting Customer Inquiries

All inquiries submitted on `contact.html` are stored locally in the browser. To access them:

1. Open `contact.html` in any browser
2. Scroll to the footer and click **"📋 View Logged Inquiries"**
3. The admin panel opens showing all collected leads with timestamps
4. Click **"Export CSV"** to download a spreadsheet-ready file
5. Click **"Export JSON"** to download raw data for developers

> **Tip:** Regularly export and back up your CSV leads file to keep a permanent record, since browser `localStorage` can be cleared by the user.

---

## 11. Adding New Pages or Plants

### Adding a New HTML Page

1. Copy the structure from an existing page (e.g., `contact.html`)
2. Update the `<title>`, meta description, and `og:url`
3. Change the `class="nav-active"` on the correct navigation link
4. Add the page to `sitemap.xml`
5. Add a `<li><a href="newpage.html">New Page</a></li>` to the footer Quick Navigation in all 4 pages

### Adding a New Product Plant

See [Section 2](#2-how-to-update-products--prices-productsjs) above.

---

## 12. Image Folder Structure & WebP Format

```
images/
├── products/           30 on-sale product photos (named: plant-name-kPRICE.webp)
│   ├── the-greenhouse-masterpiece-k1200.webp
│   ├── bamboo-palm-k600.webp
│   └── ... (28 more)
└── spectacles/         52 Home Page Spectacle arrangement photos
    ├── spectacle-main-attraction.webp
    └── ... (51 more)
```

### Converting New Images to WebP

Use the included Python script `process_images.py` (in the scratch directory) as a reference, or run:

```bash
# Install Pillow if needed
pip install Pillow

# Python one-liner to convert a single image
python -c "from PIL import Image; img = Image.open('photo.jpg'); img.save('photo.webp', 'WEBP', quality=85)"
```

### Naming Convention

Product images follow this naming pattern:
```
[plant-kebab-name]-k[PRICE].webp
```
Examples: `snake-plant-k550.webp`, `peace-lily-golden-mint-k800.webp`

---

*Last updated: September 2026 | Verdant Greens, Ndola, Copperbelt, Zambia*

