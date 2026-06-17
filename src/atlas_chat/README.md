# atlas-chat - Core Package

Main agentic workflow package containing agents, services, and orchestration logic.

## Installation

```bash
pip install atlas-chat
```

## Usage

See main project README at repository root for complete documentation.

## Package Contents

- **atlas_chat/agents/** - Agent classes and canonical `*.prompt.yaml` files
- **atlas_chat/graphs/** - Workflow orchestration (deprecated programmatic path)
- **atlas_chat/schemas/** - JSON schemas (source of truth for data models)
- **atlas_chat/services/** - LLM and API integration layer
- **atlas_chat/utils/** - Supporting utilities
- **atlas_chat/validation/** - Cross-cutting validations (report checker)

## Development

This package is part of a UV workspace. See repository root for development instructions.
