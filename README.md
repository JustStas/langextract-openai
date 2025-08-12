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
│   └── basic_usage.py              # Basic usage demonstration
└── test_openai_provider.py         # Test script
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

# Test the providers
./run_with_venv.sh test_openai_provider.py

# Run examples
./run_with_venv.sh examples/basic_usage.py
```

**Note**: The `run_with_venv.sh` script sets up the correct Python path to use both the latest langextract and this plugin.

## Quick Start

### OpenAI

```python
import langextract as lx

# Create OpenAI model
config = lx.factory.ModelConfig(
    model_id="gpt-4o-mini",
    provider="OpenAILanguageModel",
    provider_kwargs={"api_key": "your-openai-api-key"},
)
model = lx.factory.create_model(config)

# Extract structured data
result = lx.extract(
    text_or_documents="John Smith is a software engineer at Tech Corp.",
    model=model,
    prompt_description="Extract person's name, job title, and company",
    examples=[{
        "input": "Jane Doe works as a data scientist at DataCorp.",
        "output": {"name": "Jane Doe", "job_title": "data scientist", "company": "DataCorp"}
    }]
)
```

### Azure OpenAI

```python
import langextract as lx

# Create Azure OpenAI model
config = lx.factory.ModelConfig(
    model_id="azure:your-deployment-name",
    provider="AzureOpenAILanguageModel",
    provider_kwargs={
        "api_key": "your-azure-api-key",
        "azure_endpoint": "https://your-resource.openai.azure.com",
    },
)
model = lx.factory.create_model(config)

# Use the same way as OpenAI
result = lx.extract(text_or_documents="...", model=model, ...)
```

## Environment Variables

Set these environment variables for the examples and tests:

- `OPENAI_API_KEY`: Your OpenAI API key
- `AZURE_OPENAI_API_KEY`: Your Azure OpenAI API key
- `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT`: Your Azure deployment name (optional, defaults to 'gpt-4o-mini')

## License

Apache License 2.0
