# Scraping-Quora-CryptoQA

## Web Scraping Description
Developed a Web scraping tool in Python that collects a number of Q&A pairs in Quora (https://www.quora.com/). Selenium was used to scrape a list of questions, as quora require manual scrolling to see more information. 

## Web Scraping Instructions
1. Run quora_scraper_questions.py to gain a list of questions and URLs
2. Run quora_scraper_answers.py to create JSON files containing multiple answers per a question and the number of upvotes

## Notes
1. Download an appropriate chromedriver
2. Better to avoid using "headless" option in quora
3. Make sure to set chrome_options.add_argument('--user-data-dir=YOUR SETTING') to keep a login status. YOUR SETTING can be seen chrome://version/ as a profile pass
