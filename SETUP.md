# Development Setup

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

## Installation Steps

1. Clone the repository
   ```bash
   git clone <repo-url>
   cd dprs
   ```

2. Create a virtual environment (recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Verify setup
   ```bash
   python -m pytest tests/ -v       # Tests are empty in Sprint 0
   python -m cli.main --help        # Should show argparse help
   ```

## Project Structure

See [ARCHITECTURE.md](ARCHITECTURE.md) for module responsibilities.

## Running Tests

```bash
pytest tests/ -v                              # Run all tests
pytest tests/test_processor.py -v            # Run specific test file
pytest --cov=core --cov=reporting --cov=cli  # Run with coverage
```

## Running the Application

```bash
# From the dprs/ directory:
python -m cli.main --help
python -m cli.main load --file input/sample_data.csv
python -m cli.main summary
```

## Troubleshooting

**"ModuleNotFoundError: No module named 'core'"**
- Make sure you're running from the `dprs/` directory
- Check that all `__init__.py` files exist in each package

**"FileNotFoundError: config.json"**
- Ensure `config.json` is in the root directory where you run the CLI

**Tests won't run**
- Install pytest: `pip install pytest pytest-cov`
- Run from root directory: `pytest tests/`
