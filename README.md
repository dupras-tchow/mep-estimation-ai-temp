# MEP AI Estimation Pipeline

Automated construction estimation workflow combining open-source quantity takeoff with local cost database for MEP (Mechanical, Electrical, Plumbing) projects.

## Overview

This project implements an end-to-end automated construction estimation workflow:

1. **Quantity Takeoff** - Extract quantities from PDFs and BIM models using OpenTakeoff MCP
2. **Cost Database** - USCCDB (2.85M cost observations) + Dupras Ledoux internal rates in Qdrant vector database
3. **LLM Orchestration** - Agent coordinates takeoff → database search → cost calculation
4. **Price Validation** - ±20% benchmarking, productivity checks, cross-database sanity comparisons
5. **Output** - Verified BOQ and cost reports with confidence ranges

## Data Sources

- **USCCDB v1.0** - 2.85M cost observations from 2,375 US public sources (CC BY 4.0 - commercial use OK)
- **Dupras Ledoux Internal Rates** - Historical Montreal project unit rates

## Quick Start

```bash
# Clone and setup
git clone https://github.com/dupras-tchow/mep-estimation-ai.git
cd mep-estimation-ai
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Initialize Qdrant with USCCDB data
python scripts/load_costs.py

# Run estimation pipeline
python -m estimation.pipeline --input drawing.pdf
```

## Architecture

See [docs/architecture.md](docs/architecture.md) for detailed system design.

## Development

Follow the helix checkpoint plan in [.helix/plan.json](.helix/plan.json).

```bash
# Run tests
python -m pytest tests/

# Run specific checkpoint
python -m pytest tests/checkpoint_01_environment.py -v
```

## License

- USCCDB data: CC BY 4.0
- Dupras Ledoux internal rates: Proprietary
- Code: MIT