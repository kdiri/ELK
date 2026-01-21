# Migrate from Poetry to uv

This PR migrates the project from Poetry to [uv](https://github.com/astral-sh/uv) for faster and simpler dependency management.

## Changes
- Updated `pyproject.toml` to use standard PEP 621 format
- Removed `poetry.lock`
- Dependencies remain the same: Flask and Loguru

## Migration Steps
After merging, run:
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Run the app
uv run python -m flask run
```

## Benefits
- 10-100x faster dependency resolution
- Single binary tool
- Standard `pyproject.toml` format
- Simpler workflow
