# tdias_dataforge – Scrapy Optimized Crawler ![Python](https://img.shields.io/badge/python-3.11-blue.svg) ![CI/CD](https://github.com/tdiasnet/tdias_dataforge/actions/workflows/ci.yml/badge.svg)

🔍 This branch demonstrates a minimalist crawler, built with pure Python using requests, BeautifulSoup, and optional aiohttp. It is designed for low-cost, low-complexity scraping tasks where dependencies must be minimal, and deployment must be fast and lightweight.

    🧰 Perfect for bootstrapping prototypes, testing pipelines, or performing targeted data collection in small-scale applications.

    ⚠️ This is a portfolio branch. Sensitive data, credentials, and full-scale production logic are intentionally omitted to highlight only the technical structure, modularity, and best practices.
---

## 📁 Project Structure

```plaintext
tdias_dataforge/
├── simple_crawler/
│   ├── __init__.py
│   ├── http_crawler.py
│   └── parser.py
├── data/                 # Raw collected data
├── output/               # Cleaned or processed data
├── .env.example          # Template for environment configuration
├── requirements.txt      # Lightweight dependencies
├── Dockerfile            # Containerization config
└── .github/
    └── workflows/
        └── ci.yml        # GitHub Actions pipeline
```

⚙️ Core Features

    Built with only essential Python libraries

    Modular separation of crawler logic and parsing

    .env-driven configuration for portability

    Simple output writing to JSON/CSV/local disk

    Fully dockerized and CI/CD-ready

🧠 Why This Matters (For Recruiters)

This branch illustrates:

    🪶 Lightweight, dependency-minimal scraping workflows

    🛠️ Clean code organization with separation of crawler logic, parsing, and data storage

    ⚙️ Infrastructure readiness (Docker + CI/CD) even in small-scale solutions

    📈 Scalable foundation for more complex systems later

🛠 Technologies Used

    Python 3.11

    Requests + BeautifulSoup (or AIOHTTP)

    Docker

    GitHub Actions

    dotenv config pattern

## 👤 Author

**Thiago Dias Joaquim**  
📧 thiago@tdias.net  
📞 +55 19 99962-0662  
🔗 [LinkedIn](https://www.linkedin.com/in/tdiasnet/)

---

👉 Check other branches for different approaches:

- [`main`](https://github.com/tdiasnet/tdias_dataforge/tree/main) – Complex modular crawler architecture (inspired by Big Tech).
- [`simple_http_crawler`](https://github.com/tdiasnet/tdias_dataforge/tree/simple_http_crawler) – Minimal crawler for simple or resource-limited scenarios.
