'''
Conjunto de Funções que processa os metadados dos acervos.
'''
import json
import os

from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional, Tuple


_DATA_DIR = Path(".semantica")
_INDEX_FILE_PATH = _DATA_DIR / "index_acervos.json"

def load_index() -> Dict:
    """Lê o arquivo de índice JSON. Se o arquivo não existir, retorna um dicionário vazio."""
    
    try:
        content = _INDEX_FILE_PATH.read_text(encoding='utf-8')
        return json.loads(content)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"Aviso: O arquivo de índice em \"{_INDEX_FILE_PATH}\" está corrompido ou vazio. Um novo será criado.")
        return {}

def save_index(data: Dict[str, Any]) -> None:
    """Salva o dicionário de índice fornecido no arquivo JSON. Cria o diretório de dados se ele não existir."""
    # Garante a existência do diretório
    _DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Cria um json com o índice atualizado
    content = json.dumps(data, indent=4, ensure_ascii=False)
      
    _INDEX_FILE_PATH.write_text(content, encoding='utf-8')

