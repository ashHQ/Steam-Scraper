import os
from utils.extract import extract_full_body_html
import time
from selectolax.parser import HTMLParser
from config.tools import get_config
URL = "https://store.steampowered.com/specials"
image = "steam"
count = 0
if __name__ == "__main__":
    config = get_config()

    html = extract_full_body_html(from_url=config.get('url'),wait_for=config.get('container').get('selector'))
    tree = HTMLParser(html)
    divs = tree.css(config.get('container').get('selector'))

    for d in divs:
        title = d.css_first('div[class*=StoreSaleWidgetTitle]').text()
        thumbnail = d.css_first('img[class*="CapsuleImage"]').attributes.get("src")
        tags = [a.text() for a in d.css('div[class*="StoreSaleWidgetTags"] > a')[:5]]
        release_date = d.css_first('div[class*="WidgetReleaseDateAndPlatformCtn"] > div[class*="StoreSaleWidgetRelease"]').text()
        review_score = d.css_first('div[class*="ReviewScoreValue"] > div').text()
        reviewed_by = d.css_first('div[class*=ReviewScoreCount]').text()
        sale_price = d.css_first('div[class*="StoreSalePriceBox"]').text()
        original_price = d.css_first('div[class*="StoreOriginalPrice"]')
        attrs = {
                "title": title,
                "original_price": original_price,
                "sale_price": sale_price,
                "review_score": review_score,
                "reviewed_by": reviewed_by,
                "release_date": release_date,
                "tags": tags,
                "thumbnail": thumbnail
            }
        print(attrs)