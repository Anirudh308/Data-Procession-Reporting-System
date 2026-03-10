# Data Processing & Reporting System (DPRS)

> A production-ready Python CLI application under active development.

## Overview

DPRS is a command-line application that processes structured data files in CSV and JSON formats. It validates data against a configurable schema, computes statistical summaries (mean, median, min, max, count), and generates formatted reports in both text and JSON formats. Built with a clean modular architecture, the system enforces professional development practices including comprehensive logging, custom error handling, and full unit test coverage.

## Status

🚧 **Under Development** — Sprint 0 (Foundation) complete. Sprints 1–5 in progress.

## Project Structure

```
dprs/
├── core/          # Data loading, processing, validation, exceptions
├── reporting/     # Report generation (text + JSON)
├── cli/           # CLI entry point and argument parsing
├── utils/         # Logging and configuration management
├── tests/         # Unit tests
├── input/         # Input data files
├── output/        # Generated reports (auto-populated)
├── logs/          # Application logs (auto-populated)
├── config.json    # Application configuration
└── requirements.txt
```

## Quick Start

See [SETUP.md](SETUP.md) for full installation instructions.

```bash
python -m cli.main --help
```

## Tech Stack

- **Language:** Python 3.9+
- **Testing:** pytest + pytest-cov
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Data Formats:** CSV, JSON (standard library only)

## Team

Built by a 3-intern team as a 30-day Agile project.
