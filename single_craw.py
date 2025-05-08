import asyncio
from crawl4ai import *


async def main():
    async with AsyncWebCrawler() as crawler:
        resultat = await crawler.arun(
            url="https://ai.pydantic.dev/",
        )

        print(resultat.markdown)


if __name__ == "__main__":
    asyncio.run(main())