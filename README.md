# Megatherium - Extrator de Quantitativos de Formas para Pilares e Vigas IFC

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

Ferramenta em Python para extração automatizada de quantitativos de formas (área de fôrma) para pilares e vigas de concreto armado a partir de arquivos IFC (Industry Foundation Classes).

## 📋 Sobre o Projeto

Este projeto visa automatizar o processo de extração de quantitativos de formas para elementos estruturais de concreto armado (pilares e vigas) diretamente de modelos BIM no formato IFC. A ferramenta calcula automaticamente as áreas de fôrma necessárias para execução desses elementos, gerando relatórios detalhados para orçamento e planejamento de obras.

### 🎯 Funcionalidades

- Leitura e parse de arquivos IFC (IFC2X3 e IFC4)
- Identificação automática de pilares e vigas no modelo
- Cálculo preciso da área de fôrma para cada elemento
- Suporte a diferentes geometrias e seções transversais
- Relatórios detalhados em formato CSV e Excel
- Agrupamento por pavimento/tipo de elemento
- Filtros personalizáveis por critérios específicos
- Validação de geometrias e tratamento de interseções

## 🚀 Tecnologias Utilizadas

- Python 3.8+
- [IfcOpenShell](https://ifcopenshell.org/) - Biblioteca principal para manipulação de arquivos IFC

