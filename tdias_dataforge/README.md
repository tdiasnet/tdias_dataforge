# tdias_dataforge – Complex Crawler System ![Python](https://img.shields.io/badge/python-3.11-blue.svg) ![CI/CD](https://github.com/tdiasnet/tdias_dataforge/actions/workflows/ci.yml/badge.svg)

🚀 **This repository showcases a portfolio project** that demonstrates the architecture and implementation of a scalable, modular, and production-ready crawler system. Inspired by the infrastructure used by large tech companies for web-scale data collection (e.g., for NLP training), this system is designed to be easily extended and automated.

> 🔎 You can explore additional crawler examples in these branches:
> - [`scrapy_optimized`](https://github.com/tdiasnet/tdias_dataforge/tree/scrapy_optimized) – More robust, production-friendly crawler using Scrapy framework.
> - [`simple_http_crawler`](https://github.com/tdiasnet/tdias_dataforge/tree/simple_http_crawler) – Lightweight crawler for simple or cost-sensitive use cases.

> ⚠️ _This is a **public version** meant only to showcase my skills for portfolio purposes. Sensitive data, credentials, and full production logic are **intentionally omitted**._

---

## 📁 Project Structure

tdias_dataforge/
├── main.py
├── pipelines/
│   └── crawler_pipeline.py
├── utils/
│   └── helpers.py
├── storage/
│   └── save_to_disk.py
├── data/                # Collected datasets
├── input/               # Input seed URLs, rules, etc.
├── output/              # Processed or filtered results
├── .env.example         # Environment config template
├── Dockerfile           # Docker container setup
├── requirements.txt     # Python dependencies
└── .github/
    └── workflows/
        └── ci.yml       # GitHub Actions CI/CD workflow


## 🔧 Technologies Used

- Python 3.11
- Docker
- GitHub Actions (CI/CD)
- Requests / BeautifulSoup / AIOHTTP
- Modular design with scalable architecture

## 🔐 Disclaimer

This project avoids including real data or infrastructure configurations for privacy and security reasons.

## 👤 Author

**Thiago Dias Joaquim**  
📧 thiago@tdias.net  
📞 +55 19 99962-0662  
🔗 [LinkedIn](https://www.linkedin.com/in/tdiasnet/)