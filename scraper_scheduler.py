import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scraper import scrape_allevents_sydney  # your scraper function

def start_scheduler():
    scheduler = AsyncIOScheduler()
    # Run scrape every 6 hours
    scheduler.add_job(lambda: asyncio.run(scrape_allevents_sydney()), 'interval', hours=6)
    scheduler.start()
    print("Scheduler started, scraping every 6 hours.")

if __name__ == "__main__":
    start_scheduler()
    # Keep script alive
    try:
        import asyncio
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
