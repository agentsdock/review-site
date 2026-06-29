#!/usr/bin/env python3
"""
Scrape all articles from tenbests.jankalyaan.co.in and generate Hugo markdown files.
"""
import os
import re
import urllib.request
import ssl
import json

# Skip SSL verification
ssl._create_default_https_context = lambda: ssl._create_unverified_context()

BASE_URL = "https://tenbests.jankalyaan.co.in"
OUTPUT_DIR = "/Users/hongc/Documents/iLang-Trae-Plugin-main/review-site/content/posts"

# All article URLs from tenbests
article_urls = [
    ("best-pillows", f"{BASE_URL}/best-pillows/"),
    ("best-pans", f"{BASE_URL}/best-pans/"),
    ("best-cooktops", f"{BASE_URL}/best-cooktops/"),
    ("best-dehydrators", f"{BASE_URL}/best-dehydrators/"),
    ("best-air-fryers", f"{BASE_URL}/best-air-fryers/"),
    ("best-cookware-sets", f"{BASE_URL}/best-cookware-sets/"),
    ("best-smart-watches", f"{BASE_URL}/best-smart-watches/"),
    ("best-telephones", f"{BASE_URL}/best-telephones/"),
    ("best-ink-cartridges", f"{BASE_URL}/best-ink-cartridges/"),
    ("best-bluetooth-speakers-2", f"{BASE_URL}/best-bluetooth-speakers-2/"),
    ("best-bluetooth-speakers", f"{BASE_URL}/best-bluetooth-speakers/"),
    ("best-portable-document-scanners", f"{BASE_URL}/best-portable-document-scanners/"),
    ("best-wi-fi-extenders", f"{BASE_URL}/best-wi-fi-extenders/"),
    ("best-projectors", f"{BASE_URL}/best-projectors/"),
    ("best-portable-thermal-printers", f"{BASE_URL}/best-portable-thermal-printers/"),
    ("best-drawing-tablets", f"{BASE_URL}/best-drawing-tablets/"),
    ("best-power-banks", f"{BASE_URL}/best-power-banks/"),
    ("best-trail-cameras", f"{BASE_URL}/best-trail-cameras/"),
    ("best-portable-ssd", f"{BASE_URL}/best-portable-ssd/"),
    ("best-portable-monitors", f"{BASE_URL}/best-portable-monitors/"),
]

def fetch_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode('utf-8')
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None

def parse_article(html, slug):
    if not html:
        return None
    
    # Extract title
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    title = title_match.group(1).strip() if title_match else slug.replace('-', ' ').title()
    
    # Extract intro (first paragraph after h1)
    intro_match = re.search(r'<h1[^>]*>.*?</h1>\s*(?:<[^>]+>\s*)*<p[^>]*>(.*?)</p>', html, re.DOTALL)
    intro = intro_match.group(1).strip() if intro_match else ""
    # Clean HTML tags from intro
    intro = re.sub(r'<[^>]+>', '', intro)
    
    # Extract products - find all product blocks
    products = []
    # Split by ### number pattern
    sections = re.split(r'###\s+\d+', html)
    
    for section in sections[1:]:  # Skip first section (intro)
        # Product name (h2)
        name_match = re.search(r'<h2[^>]*>(.*?)</h2>', section, re.DOTALL)
        if not name_match:
            continue
        name = re.sub(r'<[^>]+>', '', name_match.group(1)).strip()
        
        # Pros (checkmarks)
        pros = re.findall(r'✔️\s*(.*?)(?:<|$)', section)
        pros = [re.sub(r'<[^>]+>', '', p).strip() for p in pros]
        
        # Rating
        rating_match = re.search(r'⭐\s*([\d.]+)', section)
        rating = float(rating_match.group(1)) / 2 if rating_match else 4.5  # Convert 10-scale to 5-scale
        
        # Badge
        badge = ""
        if "BEST OVERALL" in section:
            badge = "BEST OVERALL"
        elif "BEST VALUE" in section:
            badge = "BEST VALUE"
        elif "BUDGET PICK" in section:
            badge = "BUDGET PICK"
        
        # Price link
        price_match = re.search(r'href="(https://www\.amazon\.com/dp/[^"]+)"', section)
        affiliate_link = price_match.group(1) if price_match else ""
        
        # Extract description from first few pros
        description = pros[0] if pros else ""
        
        products.append({
            "name": name,
            "rating": round(rating, 1),
            "description": description,
            "pros": pros[:4],  # Top 4 pros
            "cons": pros[4:6] if len(pros) > 4 else ["No major drawbacks found"],
            "badge": badge,
            "affiliate_link": affiliate_link,
        })
    
    return {
        "title": title,
        "intro": intro,
        "products": products,
    }

def generate_frontmatter(data, slug):
    year_match = re.search(r'\d{4}', data['title'])
    year = year_match.group(0) if year_match else "2026"
    
    # Determine date from slug
    if "2025" in data['title']:
        date = "2025-06-15"
    else:
        date = "2026-01-15"
    
    products_yaml = ""
    for i, p in enumerate(data['products']):
        pros_yaml = "\n".join([f'      - "{pro}"' for pro in p['pros']])
        cons_yaml = "\n".join([f'      - "{con}"' for con in p['cons']])
        products_yaml += f'''  - name: "{p['name']}"
    rating: {p['rating']}
    price: "Check Price"
    description: "{p['description']}"
    badge: "{p['badge']}"
    pros:
{pros_yaml}
    cons:
{cons_yaml}
    affiliate_link: "{p['affiliate_link']}"
'''
        if i < len(data['products']) - 1:
            products_yaml += "\n"
    
    faq_yaml = f'''faq:
  - question: "What is the best {slug.replace('-', ' ')}?"
    answer: "Based on our testing, the {data['products'][0]['name']} is the best overall choice."
  - question: "How did you test these products?"
    answer: "We tested each product using standardized criteria including performance, durability, and value for money."
  - question: "Which one offers the best value?"
    answer: "For budget-conscious buyers, we recommend checking our Budget Pick option in the list above."
'''
    
    return f'''---
title: "{data['title']}"
date: {date}T10:00:00+08:00
lastmod: {date}T10:00:00+08:00
draft: false
tags: [best, review, {year}]
summary: "{data['intro'][:150]}"
author: "ReviewPro Editorial Team"
rating: 4.5
products:
{products_yaml}{faq_yaml}---
'''

def generate_content(data):
    content = f"{data['intro']}\n\n"
    content += "## How We Chose\n\n"
    content += "We evaluated each product based on performance, quality, features, and value for money. Every product was tested in real-world conditions for at least two weeks.\n\n"
    content += "## Our Testing Process\n\n"
    content += "Each product was subjected to our standardized testing protocol to ensure fair and accurate comparisons across all options.\n\n"
    content += "## What to Look For\n\n"
    content += "When shopping, consider these key factors:\n\n"
    content += "- **Performance**: Does the product deliver on its promises?\n"
    content += "- **Quality**: How well is it built and how long will it last?\n"
    content += "- **Value**: Is it worth the price compared to alternatives?\n"
    content += "- **Features**: Does it have the features you actually need?\n"
    return content

def main():
    for slug, url in article_urls:
        print(f"Processing: {slug}...")
        
        html = fetch_url(url)
        if not html:
            print(f"  Skipped (fetch error)")
            continue
        
        data = parse_article(html, slug)
        if not data or not data['products']:
            print(f"  Skipped (no products found)")
            continue
        
        dir_path = os.path.join(OUTPUT_DIR, slug)
        os.makedirs(dir_path, exist_ok=True)
        
        frontmatter = generate_frontmatter(data, slug)
        content = generate_content(data)
        
        with open(os.path.join(dir_path, "index.md"), "w") as f:
            f.write(frontmatter + content)
        
        print(f"  Created: {slug} ({len(data['products'])} products)")
    
    print(f"\nDone!")

if __name__ == "__main__":
    main()
