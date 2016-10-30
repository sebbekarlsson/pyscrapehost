# PyScrapeHost
> Client for talking to the scrape.host API

## Initialize
> Create the client like this:

    from pyscrapehost.SHClient import SHClient

    
    client = SHClient(token='tok123en123', host='http://scrape.host/')

## Getting scrapers
> Get a list of all your scrapers

    client.get_scrapers()

## Getting matches
> Get a list of matches from a scraper

    client.get_matches(scraper_id='23908aadfs0bb129', offset=2)

