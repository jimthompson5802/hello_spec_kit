import sys
from pathlib import Path

import pytest

# Ensure repository `src/` is importable when running tests from the repo root
ROOT = Path(__file__).resolve().parents[1]
# Add repository root to sys.path so `import src.app` resolves to `./src`
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.fixture
def client():
    # Import inside fixture so sys.path modifications above take effect and
    # to avoid module-level import side-effects that ruff flags as E402.
    from src.app import app as flask_app

    flask_app.config.update({"TESTING": True})
    with flask_app.test_client() as client:
        yield client
