import asyncio
from typing import List
from crawl4ai import *
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
import requests
from xml.etree import ElementTree

async def crawl_sequentiel(urls: List[str]):
    print("\n=== Crawl séquentiel avec session partagée ===")

    # Configuration du navigateur
    config_navigateur = BrowserConfig(
        headless=True,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )

    config_crawl = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator()
    )

    crawler = AsyncWebCrawler(config=config_navigateur)
    await crawler.start()

    try:
        session_id = "session1"
        for url in urls:
            resultat = await crawler.arun(
                url=url,
                config=config_crawl,
                session_id=session_id
            )
            if resultat.success:
                print(f"Crawl réussi : {url}")
                print(f"Taille du Markdown : {len(resultat.markdown.raw_markdown)}")
            else:
                print(f"Échec : {url} - Erreur : {resultat.error_message}")
    finally:
        await crawler.close()

def recuperer_urls():
    reponse = requests.get("https://ai.pydantic.dev/sitemap.xml")
    racine = ElementTree.fromstring(reponse.content)
    return [url.text for url in racine.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]

if __name__ == "__main__":
    urls = recuperer_urls()
    asyncio.run(crawl_sequentiel(urls))