import time
from datetime import datetime
from data.models import Property, Search
from data.database import session
from notify_run import Notify
from data.setup import search_setup, create_tables
from data.scrape import get_search_results


def process_properties(search: Search, properties: list):
    """
    Processes the properties returned from the search.

    Args:
        search (Search): The search to process
        properties (list): The properties to process
    """

    notify = Notify(endpoint=f"https://notify.run/{search.notification_channel_id}")
    new = False
    for property in properties:
        if session.get(Property, property["id"]) is None:
            property_record = Property(
                id=property["id"],
                search_id=search.id,
                url="https://www.rightmove.co.uk" + property["propertyUrl"],
                bedrooms=property["bedrooms"],
                bathrooms=property["bathrooms"],
                summary=property["summary"],
                address=property["displayAddress"],
                longitude=property["location"]["longitude"],
                latitude=property["location"]["latitude"],
                price=property["price"]["amount"],
                letting_agent=property["customer"]["branchDisplayName"],
            )
            session.add(property_record)
            session.commit()

            # Action is the url to open when the notification is clicked
            notify.send(
                f"New property found in {search.name} for {property['price']['amount']}!",
                action="https://www.rightmove.co.uk" + property["propertyUrl"],
            )

            print(
                f"\nNew property found in {search.name} for {property['price']['amount']}!"
            )
            new = True

    if not new:
        print(
            f"No new properties found in {search.name} at {datetime.now()}",
            end="\r",
        )


if __name__ == "__main__":
    create_tables()
    search_setup()

    while True:
        for search in session.query(Search).all():
            try:
                time.sleep(5)
                properties = get_search_results(search)
                process_properties(search, properties)
            except KeyboardInterrupt:
                print("Exiting...")
                exit()
            except Exception as e:
                print(f"Error in {search.name}: {e}")
