# tdias_dataforge – Scrapy Optimized Crawler ![Python](https://img.shields.io/badge/python-3.11-blue.svg) ![CI/CD](https://github.com/tdiasnet/tdias_dataforge/actions/workflows/ci.yml/badge.svg)

🚀 **This branch showcases a Scrapy-based crawler**, optimized for production-level reliability, extensibility, and speed. It is part of the [`tdias_dataforge`](https://github.com/tdiasnet/tdias_dataforge) portfolio project, which demonstrates how modular, scalable crawlers can be built using modern open-source technologies.

> 🔄 **Scrapy** is ideal for structured crawling, automatic request scheduling, throttling, retries, and extensible item pipelines — making it a powerful tool for building robust crawlers.

> 💡 This is a **portfolio branch**. Sensitive logic, credentials, and full-scale orchestration are intentionally omitted. The goal is to demonstrate architectural design, tool mastery, and code hygiene.

---

## 📁 Project Structure

```plaintext
tdias_dataforge/
├── scrapy_project/
│   ├── scrapy.cfg
│   └── tdias_spider/
│       ├── __init__.py
│       ├── items.py
│       ├── middlewares.py
│       ├── pipelines.py
│       ├── settings.py
│       └── spiders/
│           └── example_spider.py
├── data/
├── output/
├── .env.example
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── ci.yml
```


## 🕸 Features

- Built with Scrapy 2+
- Clean separation of concerns with:
  - Custom item pipeline
  - Middleware for headers/user-agent rotation
  - Configurable output handling
- Follows best practices for Python packaging and version control
- Easily deployable via Docker

## 🔧 Technologies Used

- Python 3.11
- Scrapy Framework
- Docker
- GitHub Actions
- dotenv + modular configuration

## ✅ Why This Matters (For Recruiters)

This crawler demonstrates:

- 🛠️ Ability to architect and implement maintainable, scalable web scraping systems
- 🚀 CI/CD fluency for automated testing and deployment
- 🧱 Code modularity and best practices in real-world applications
- 📊 Preparation for larger data pipelines (e.g., for NLP or ML training)

## 👤 Author

**Thiago Dias Joaquim**  
📧 thiago@tdias.net  
📞 +55 19 99962-0662  
🔗 [LinkedIn](https://www.linkedin.com/in/tdiasnet/)

---

👉 Check other branches for different approaches:

- [`main`](https://github.com/tdiasnet/tdias_dataforge/tree/main) – Complex modular crawler architecture (inspired by Big Tech).
- [`simple_http_crawler`](https://github.com/tdiasnet/tdias_dataforge/tree/simple_http_crawler) – Minimal crawler for simple or resource-limited scenarios.
