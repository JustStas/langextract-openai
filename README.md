# LangExtract OpenAI Plugin

OpenAI and Azure OpenAI provider plugin for LangExtract that enables structured data extraction using OpenAI's language models.

## Features

- **OpenAI Support**: Direct integration with OpenAI's API
- **Azure OpenAI Support**: Full support for Azure OpenAI deployments
- **Structured Output**: JSON and YAML format support
- **Parallel Processing**: Efficient batch processing with configurable concurrency
- **Plugin System**: Seamless integration with LangExtract's provider system

## Structure

```
langextract-openai/
├── pyproject.toml                    # Package configuration and metadata
├── README.md                         # This file
├── langextract_openai/              # Package directory
│   ├── __init__.py                  # Package initialization and exports
│   └── openai_providers.py         # OpenAI and Azure OpenAI providers
├── examples/                        # Usage examples
│   └── usage_examples.ipynb        # Jupyter notebook with examples
└── LICENSE
```

## Provider Implementations

- **OpenAI** (`OpenAILanguageModel`): Direct OpenAI API integration
- **Azure OpenAI** (`AzureOpenAILanguageModel`): Azure OpenAI service integration (inherits OpenAI implementation)

### Package Configuration (`pyproject.toml`)

```toml
[project.entry-points."langextract.providers"]
openai = "langextract_openai:OpenAILanguageModel"
azure_openai = "langextract_openai:AzureOpenAILanguageModel"
```

This entry point allows LangExtract to automatically discover your provider.

## Installation

### Prerequisites

First install the latest LangExtract from source:

```bash
git clone https://github.com/google/langextract.git
cd langextract
pip install -e .
```

### Install Plugin

```bash
# Clone this plugin
git clone <this-repo-url>
cd langextract-openai

# Install in development mode
pip install -e .

# Run the example notebook
# (ensure you have Jupyter installed: pip install jupyter)
jupyter notebook examples/usage_examples.ipynb
```

## Quick Start

### OpenAI

```python
import langextract as lx

# Extract structured data with OpenAI
result = lx.extract(
    text_or_documents="John Smith is a software engineer at Tech Corp.",
    model_id="gpt-4o-mini",
    api_key="your-openai-api-key",
    prompt_description="Extract person's name, job title, and company",
    examples=[{
        "input": "Jane Doe works as a data scientist at DataCorp.",
        "output": {"name": "Jane Doe", "job_title": "data scientist", "company": "DataCorp"}
    }]
)

# Tip: If there are multiple providers matching your model_id in your environment,
# you can disambiguate by explicitly specifying the provider name:
# result = lx.extract(
#     text_or_documents="...",
#     model_id="gpt-4o-mini",
#     api_key="...",
#     provider="OpenAILanguageModel",
#     prompt_description="...",
# )
```

### Azure OpenAI

```python
import langextract as lx

# Extract with Azure OpenAI
result = lx.extract(
    text_or_documents="John Smith is a software engineer at Tech Corp.",
    model_id="azure:your-deployment-name",
    api_key="your-azure-api-key",
    azure_endpoint="https://your-resource.openai.azure.com",
    prompt_description="Extract person's name, job title, and company",
)
```

## Environment Variables

Set these environment variables for the examples and tests:

- `OPENAI_API_KEY`: Your OpenAI API key
- `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
- `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT`: Your Azure deployment name (optional, defaults to 'gpt-4o-mini')

## Release

1. Bump version in `pyproject.toml` under `[project] version`.

2. Build and upload to PyPI:

```bash
python -m pip install --upgrade build twine
rm -rf dist build *.egg-info
python -m build
twine upload dist/*
```

Optional: Upload to TestPyPI first:

```bash
twine upload --repository testpypi dist/*
```

Optional: Tag the release in git:

```bash
git tag vX.Y.Z
git push origin vX.Y.Z
```

Notes:
- Use a PyPI API token (username: `__token__`, password: your token), or configure `~/.pypirc`.
- Ensure you have a clean tree and tests/examples pass before publishing.

## License

Apache License 2.0
