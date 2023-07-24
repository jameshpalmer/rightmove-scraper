# Rightmove-Scraper

## About

This is a simple scraper for Rightmove. Users can easily set up property searches, and shortly after§ a new property is listed that matches the search criteria, a notification will get sent to a notifications channel on notify-run.

## Installation and Setup

1. Clone the repository

```bash
git clone https://github.com/jameshpalmer/rightmove-scraper.git
```

2. Install the requirements

```bash
pip install -r requirements.txt
```

3. Set up a notify-run channel

```bash
notify-run register
```

This will give you a URL to visit. Visit it, and you will be given a channel ID. Copy this ID. Visit the url or scan the QR code on any device you wish to receive notifications on, and allow notifications.

If you wish to set up different notifications channels for different searches, you can repeat this step for each channel you wish to set up.

4. Set up a `data/input/searches.csv` file, following the format of `data/input/searches.example.csv`. This is where you will set up your searches and the corresponding notify-run channel IDs you wish to send notifications to.

| Channel Id                           | Name                                   | Url                              |
| ------------------------------------ | -------------------------------------- | -------------------------------- |
| ID of relevant notifications channel | Name of search (used for notification) | Url of relevant rightmove search |

## Usage

To run the scraper, simply run the following command:

```bash
python main.py
```

Please note that on the first run, all properties will be sent to the notifications channel. This is to ensure that the scraper is working correctly. After this, only new properties will be sent to the notifications channel.
