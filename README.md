# Web Scraper

A simple Python-based web scraper that collects article previews from **nature.com** and saves them as text files.

The scraper navigates through multiple pages, filters articles by type (e.g. *News*), and stores the preview content locally for later analysis.

The project is fully containerized with Docker and runs without requiring any local Python setup.

---

## Features

- Scrapes multiple pages from nature.com  
- Filters articles by article type  
- Extracts and saves article preview texts  
- Outputs results as `.txt` files  
- Fully Dockerized for reproducible execution  

---

## Technologies

- Python  
- Requests  
- BeautifulSoup  
- Docker  

---

## How It Works

1. Sends HTTP requests to nature.com article listing pages  
2. Parses HTML content using BeautifulSoup  
3. Filters articles based on their type  
4. Extracts preview text  
5. Saves each preview as a separate `.txt` file  

---

## Run with Docker

```bash
docker run -it bediravsardev/web-scraper
```

After execution, scraped article previews will be available inside the container output directory.
