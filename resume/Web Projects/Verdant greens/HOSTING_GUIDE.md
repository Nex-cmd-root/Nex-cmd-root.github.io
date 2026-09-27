# Verdant Greens — Website Hosting Guide

> **For:** Verdant Greens Botanical Nursery, Ndola, Zambia  
> **Site Type:** Static HTML/CSS/JavaScript (no server-side code)  
> **Goal:** Make the site live and accessible to customers across Zambia

---

## Table of Contents

1. [Quick Answer: Best Option for Verdant Greens](#1-quick-answer-best-option-for-verdant-greens)
2. [Cloudflare Pages (Recommended — Free & Fast)](#2-cloudflare-pages-recommended--free--fast)
3. [Netlify (Excellent Alternative)](#3-netlify-excellent-alternative)
4. [GitHub Pages (Free & Simple)](#4-github-pages-free--simple)
5. [Vercel (Fast & Developer-Friendly)](#5-vercel-fast--developer-friendly)
6. [Firebase Hosting (Google's Free Tier)](#6-firebase-hosting-googles-free-tier)
7. [Side-by-Side Comparison Table](#7-side-by-side-comparison-table)
8. [Getting a Zambian Domain Name (.zm / .co.zm)](#8-getting-a-zambian-domain-name-zm--cozm)
9. [Connecting a Custom Domain (Step-by-Step)](#9-connecting-a-custom-domain-step-by-step)
10. [Contact Form Backend Options (For Lead Collection)](#10-contact-form-backend-options-for-lead-collection)
11. [After Going Live: Essential SEO Checks](#11-after-going-live-essential-seo-checks)

---

## 1. Quick Answer: Best Option for Verdant Greens

> **Recommended:** **Cloudflare Pages** + **`verdantgreens.co.zm`** domain

| What you need | Our pick |
|--------------|---------|
| Free, fast hosting with global CDN | Cloudflare Pages |
| Zambian `.co.zm` domain | ZAMNIC / Zain Zambia registrars |
| Free contact form backend | Formspree (10 free submissions/month) or Netlify Forms |

**Total cost estimate:**
- Hosting: **FREE** (Cloudflare Pages free tier is very generous)
- `.co.zm` domain: ~**K300 – K500/year** through ZAMNIC
- Contact form: **FREE** (Formspree free tier = 50 submissions/month)

---

## 2. Cloudflare Pages (Recommended — Free & Fast)

### Why Cloudflare Pages?

- ✅ **Completely free** for static sites with unlimited bandwidth
- ✅ **Global CDN** — site loads fast from Ndola, Lusaka, Kitwe, and internationally
- ✅ Built-in **SSL/HTTPS** (secure padlock) — free and automatic
- ✅ Supports **custom domains** including `.co.zm`
- ✅ Automatic deployments from GitHub

### Step-by-Step Deployment

#### Option A: Deploy via GitHub (Easiest Long-Term)

1. **Create a free GitHub account** at [github.com](https://github.com)
2. Create a **new repository** called `verdant-greens-website`
3. Upload all website files (drag and drop the entire `Verdant greens` folder)
4. Go to [pages.cloudflare.com](https://pages.cloudflare.com)
5. Sign in / create a free Cloudflare account
6. Click **"Create a project"** → **"Connect to Git"**
7. Select your GitHub repository
8. Build settings: leave blank (static site — no build command needed)
9. Click **"Save and Deploy"**

Your site will be live at: `https://verdant-greens-website.pages.dev`

#### Option B: Direct Upload (No GitHub Needed)

1. Go to [pages.cloudflare.com](https://pages.cloudflare.com)
2. Click **"Create a project"** → **"Direct Upload"**
3. Drag and drop your entire `Verdant greens` folder
4. Name your project and click **"Deploy site"**

---

## 3. Netlify (Excellent Alternative)

### Why Netlify?

- ✅ Free tier includes **100GB bandwidth/month** and unlimited deployments
- ✅ Easiest drag-and-drop upload interface
- ✅ **Netlify Forms** — free backend to collect contact form submissions without any extra setup
- ✅ Built-in SSL, custom domain support
- ✅ Branch previews for testing changes before going live

### Step-by-Step Deployment

1. Go to [netlify.com](https://www.netlify.com) and create a free account
2. On the dashboard, find the **"Deploy manually"** box
3. Drag your entire `Verdant greens` folder onto the deploy box
4. Your site is live instantly at: `https://random-name-abc123.netlify.app`
5. In **Site Settings → Domain Management** → add your custom `.co.zm` domain

### Using Netlify Forms (Free Contact Form Backend)

Add `netlify` attribute to your form tag in `contact.html`:
```html
<form id="vg-contact-form" name="verdant-contact" netlify>
```

Netlify will automatically capture all form submissions and send them to your email. **No backend code needed.**

---

## 4. GitHub Pages (Free & Simple)

### Why GitHub Pages?

- ✅ Completely free forever
- ✅ Tight integration with GitHub version control
- ✅ Good for sharing a portfolio or getting started quickly

### Limitations

- ❌ Slower CDN compared to Cloudflare Pages
- ❌ Custom domain setup is slightly more manual
- ❌ No built-in form handling

### Step-by-Step

1. Create a GitHub account at [github.com](https://github.com)
2. Create repository named `verdant-greens` (or `yourusername.github.io`)
3. Upload all files from the `Verdant greens` folder
4. Go to **Settings → Pages**
5. Source: **"Deploy from a branch"** → select `main` branch → `/ (root)`
6. Your site will be live at: `https://yourusername.github.io/verdant-greens/`

---

## 5. Vercel (Fast & Developer-Friendly)

### Why Vercel?

- ✅ Extremely fast global CDN
- ✅ Free tier with generous bandwidth limits
- ✅ Clean dashboard and great performance analytics

### Deployment

1. Go to [vercel.com](https://vercel.com) and sign up
2. Click **"New Project"** → Import from GitHub or drag-and-drop
3. No build settings needed for a static site
4. Click **"Deploy"**

---

## 6. Firebase Hosting (Google's Free Tier)

### Why Firebase?

- ✅ Google-backed CDN
- ✅ Free Spark plan includes 10GB storage and 360MB/day bandwidth
- ✅ Easy custom domain setup
- ✅ Good if you plan to add a Firestore database later

### Deployment

Requires the Firebase CLI (Node.js):

```bash
npm install -g firebase-tools
firebase login
firebase init hosting
firebase deploy
```

---

## 7. Side-by-Side Comparison Table

| Feature | Cloudflare Pages | Netlify | GitHub Pages | Vercel | Firebase |
|---------|-----------------|---------|-------------|--------|----------|
| **Price** | Free | Free | Free | Free | Free |
| **Bandwidth** | Unlimited | 100GB/mo | Soft limit | 100GB/mo | 360MB/day |
| **Custom Domain** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **SSL/HTTPS** | ✅ Auto | ✅ Auto | ✅ Auto | ✅ Auto | ✅ Auto |
| **Global CDN Speed** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Form Backend** | ❌ Needs 3rd party | ✅ Built-in | ❌ Needs 3rd party | ❌ Needs 3rd party | ❌ Needs 3rd party |
| **Ease of Use** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Best For** | Production site | Quick launch + forms | Portfolio | Fast deploy | Google ecosystem |

---

## 8. Getting a Zambian Domain Name (.zm / .co.zm)

A `.co.zm` domain gives Verdant Greens a strong **local Zambian identity** and boosts local SEO rankings in Google Zambia.

### Recommended Zambian Domain Registrars

#### Option A: ZAMNIC (Official Zambian Registry)
- **Website:** [zamnic.zm](https://www.zamnic.zm)
- **Price:** ~K350–K500/year for `.co.zm`
- **Process:** Online application with business registration details

#### Option B: Zain Zambia Digital Solutions
- Offers domain registration bundled with data packages
- Contact via your local Zain business center

#### Option C: International Registrars with .zm Support
- **Namecheap** — Check if `.co.zm` is available at [namecheap.com](https://www.namecheap.com)
- **GoDaddy** — International option with good support

### Ideal Domain Names to Register
In order of preference:
1. `verdantgreens.co.zm` ← **Best choice** — clear, professional, local
2. `verdantgreens.zm`
3. `verdant-greens.co.zm`

---

## 9. Connecting a Custom Domain (Step-by-Step)

Once you have your domain (e.g., `verdantgreens.co.zm`) and hosting (e.g., Cloudflare Pages):

### On Cloudflare Pages

1. In your Cloudflare Pages dashboard, click your project
2. Go to **Settings → Custom Domains**
3. Click **"Set up a custom domain"**
4. Enter `verdantgreens.co.zm`
5. Cloudflare will show you **DNS records** to configure

### At Your Domain Registrar (ZAMNIC)

1. Log into your ZAMNIC account
2. Go to DNS Management for `verdantgreens.co.zm`
3. Add a **CNAME record**:
   - **Name:** `www`
   - **Value:** `verdant-greens.pages.dev` (your Cloudflare Pages URL)
4. For the root domain (`@`), add an **A record** pointing to Cloudflare's IP as instructed

DNS changes typically take **5 minutes to 24 hours** to propagate.

---

## 10. Contact Form Backend Options (For Lead Collection)

The current site logs inquiries to the **browser's localStorage** only (visible only on the device that submitted). For real email delivery:

### Option A: Formspree (Recommended — Free Tier)

1. Create a free account at [formspree.io](https://formspree.io)
2. Create a new form and get your unique form endpoint URL (e.g., `https://formspree.io/f/xabcdefg`)
3. In `contact.js`, update the form submission to POST to that endpoint:
   ```javascript
   const response = await fetch('https://formspree.io/f/xabcdefg', {
     method: 'POST',
     body: new FormData(formElement),
     headers: { 'Accept': 'application/json' }
   });
   ```
4. Submissions arrive at `ash2herbal@gmail.com` automatically

**Free tier:** 50 submissions/month — ideal for getting started.

### Option B: Netlify Forms (If Hosted on Netlify)

Just add `netlify` attribute to your form tag. **Zero additional setup.** Notifications go directly to your email.

### Option C: EmailJS (Client-Side Email)

[emailjs.com](https://www.emailjs.com) — Send emails directly from JavaScript without a server. Free tier: 200 emails/month.

---

## 11. After Going Live: Essential SEO Checks

Once the site is hosted at your domain, complete these steps to maximize Zambian search visibility:

### 1. Submit to Google Search Console
1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Add your property (`verdantgreens.co.zm`)
3. Submit `sitemap.xml` URL: `https://verdantgreens.co.zm/sitemap.xml`

### 2. Create a Google Business Profile
1. Visit [business.google.com](https://business.google.com)
2. Add **Verdant Greens** with:
   - Address: Ndola, Copperbelt, Zambia
   - Phone: +260 775 971 03
   - Category: Florist / Plant Nursery
   - Website: `https://verdantgreens.co.zm`
3. This makes the nursery appear in Google Maps and local search results

### 3. Update Sitemap Domain

Open `sitemap.xml` and replace `https://verdantgreens.com/` with your live domain:
```xml
<loc>https://verdantgreens.co.zm/</loc>
```

### 4. Submit to Bing Webmaster Tools
- [bing.com/webmasters](https://www.bing.com/webmasters) — submit sitemap for Bing/DuckDuckGo coverage

---

*Prepared for Verdant Greens Botanical Nursery — Ndola, Copperbelt, Zambia*  
*Questions? Email: ash2herbal@gmail.com | WhatsApp: +260 771 594 459*

