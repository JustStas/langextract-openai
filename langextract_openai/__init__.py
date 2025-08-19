# Copyright 2025 [Stanislav Nosulenko]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""OpenAI and Azure OpenAI provider plugin for LangExtract."""

from langextract_openai.openai_providers import (
    AzureOpenAILanguageModel,
    OpenAILanguageModel,
)

__all__ = [
    "OpenAILanguageModel",
    "AzureOpenAILanguageModel",
]
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as pkg_version

try:
    __version__ = pkg_version("langextract-openai")
except PackageNotFoundError:
    __version__ = "0.0.0"
