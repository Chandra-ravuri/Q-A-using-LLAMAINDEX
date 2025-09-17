# Q-A-using-LLAMAINDEX

Professional README

Project summary
- **Purpose:** A question-and-answer assistant built on top of LlamaIndex (formerly GPT-Index) to ingest and query documents and web pages.
- **Primary components:** code to load webpages and documents, a small runner script (`webpagereader.py`), and environment configuration for reproducible development.

Quick start
1. Activate the project environment (this repo uses a conda environment at `./venv`):

```bash
# make conda available in the shell, then activate
source /opt/conda/etc/profile.d/conda.sh
conda activate /workspaces/Q-A-using-LLAMAINDEX/venv
```

2. Install Python dependencies (if not already installed):

```bash
pip install -r requirements.txt
# or install individual packages used in the examples
pip install "llama-index==0.5.9" langchain==0.0.27 python-dotenv
```

3. Run the example script (reads a webpage and runs a small query):

```bash
python webpagereader.py
```

Project structure
- `webpagereader.py` — example script that demonstrates loading a web page with LlamaIndex and querying it.
- `requirements.txt` — project dependency list (update as you stabilize versions).
- `.env` — environment variables (API keys, etc.).

Notes on compatibility and troubleshooting
- LlamaIndex and LangChain evolve quickly and change public APIs. If you see import errors like `No module named 'langchain.chains.prompt_selector'` or pydantic errors, it's typically due to incompatible package versions.
- Known working pair used while developing this project:
  - `llama-index==0.5.9`
  - `langchain==0.0.27`
  - `pydantic==1.10.12` (downgraded when necessary for compatibility)

- If you want to use the latest `llama-index` (0.8.x) you must use a newer `langchain` (>=0.0.303) and Python >= 3.8.1 (many modern langchain versions require >= 3.9). In that case create a fresh environment with Python 3.10 and install:

```bash
conda create -p /path/to/env python=3.10 -y
conda activate /path/to/env
pip install --upgrade pip
pip install "langchain>=0.0.303" "llama-index==0.8.42" python-dotenv
```

- If you encounter `conda activate` errors, run:

```bash
source /opt/conda/etc/profile.d/conda.sh
conda activate /path/to/env
```

- If `from dotenv import load_dotenv` fails, install `python-dotenv`:

```bash
pip install python-dotenv
```

Security and API keys
- Store API keys in `.env` and never commit them to source control. Example `.env`:

```env
OPENAI_API_KEY=sk-...
```

Development notes and next steps
- Consider adding a `requirements.txt` or `pyproject.toml` with pinned versions for reproducibility.
- Add tests and a small example notebook demonstrating query workflows.
- Replace local manual shims with proper version alignment when moving to production.

Contact
- For questions about this repo, you can send me an emial to chandra.r0723@gmail.com.
