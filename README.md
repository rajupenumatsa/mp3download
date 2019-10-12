# mp3download
Scraper to crawl and download all latest Telugu mp3 songs from internet. Please note that this application is created just for fun and to learn python, scrapy and other tools in the area of data collection from web. This is not intended for any production use. 

# Description
It is a Telugu mp3 albums scraper from naasongs.com website. It navigates to the recently published albums list page and checks if any downloadable zip version is available and download them to the local disk. It also automatically unzip content to the local drive.

It checks if any of the available album is alredy captured previously and ignores it in that case.

We can either run it individually using scrapy crawl commands or we can deploy it in scrapyd to run as daemon and schedule it as needed.

# Installation and run steps
Local environment:
- Clone it from Git 
- Navigate to the project root directory in terminal
- Change FILES_STORE value in settings.py file available in <<project-root-dir>>/mp3download/settings.py to your desired local drive path where you would like to scrape all the albums.
- Run command 'scrapy crawl mp3scrapper'
- You will see nice log in console with the necessary details and stats. You can verify the files downloaded in the FILES_STORE path that you configured.

It is recommended to deploy it using Scrapyd as we can schedule it as job and run it as needed. It also supports monitoring it through web interface.
- Install scrapyd and scarpyd-client using pip. Make sure to install same server and client versions.
- Start scrapyd as daemon
- Navigate to project root folder in terminal and deploy the project egg using scapyd-deploy tool.
- Schedule a job to run the mp3scraper to see the results.
- Monitor the job status and log files using scrapyd web interface runs at 6800 port(default).
- Create a cron job(Linux) and schedule it to run this job as needed.

# Configuration
Update the FILES_STORE value to the desired path to store downloaded files to local drive. You can find it at <<project-root-dir>>/mp3download/settings.py

# Further extensions planned
- Capture additional meta data of album.
- Store the metadata and files to a database. 
- Pull metadata from DB to check if we already downladed the album previously.