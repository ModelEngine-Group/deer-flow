# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import enum
import os

import requests
from dotenv import load_dotenv

from src.config.loader import get_str_env

load_dotenv()


class SearchEngine(enum.Enum):
    TAVILY = "tavily"
    DUCKDUCKGO = "duckduckgo"
    BRAVE_SEARCH = "brave_search"
    ARXIV = "arxiv"
    SEARX = "searx"
    WIKIPEDIA = "wikipedia"


def get_search_engine():
    search_engine = os.getenv("SEARCH_API")

    datamate_backend_url = get_str_env("DATAMATE_BACKEND_URL", "http://datamate-backend:8080")
    response = requests.get(datamate_backend_url + "/api/sys-param/list")
    if response.status_code == 200:
        content = response.json().get("data", [])
        sys_param = {}
        for c in content:
            sys_param[c.get("id")] = c.get("paramValue")
        if "SEARCH_API" in sys_param:
            search_engine = sys_param.get("SEARCH_API")
            if search_engine == SearchEngine.TAVILY.value:
                os.environ["TAVILY_API_KEY"] = sys_param.get("TAVILY_API_KEY")
            elif search_engine == SearchEngine.BRAVE_SEARCH.value:
                os.environ["BRAVE_SEARCH_API_KEY"] = sys_param.get("BRAVE_SEARCH_API_KEY")
            elif search_engine == SearchEngine.SEARX.value:
                os.environ["SEARX_HOST"] = sys_param.get("SEARX_HOST")
        if "JINA_API_KEY" in sys_param:
            os.environ["JINA_API_KEY"] = sys_param.get("JINA_API_KEY")
    return search_engine


class RAGProvider(enum.Enum):
    DIFY = "dify"
    RAGFLOW = "ragflow"
    VIKINGDB_KNOWLEDGE_BASE = "vikingdb_knowledge_base"
    MOI = "moi"
    MILVUS = "milvus"
    QDRANT = "qdrant"


SELECTED_RAG_PROVIDER = os.getenv("RAG_PROVIDER")
