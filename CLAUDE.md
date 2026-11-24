# MEP AI Estimation Pipeline - Development Instructions

## Project Overview

This is an automated construction estimation workflow for MEP (Mechanical, Electrical, Plumbing) projects. It combines open-source quantity takeoff with a local cost database for price validation.

## Working Guidelines

- **Use helix-plan checkpoints**: Each task follows the 7 checkpoints in `.helix/plan.json`
- **TDD approach**: Write tests first, prove they fail, then implement
- **Data licensing**: USCCDB is CC BY 4.0 (commercial OK); internal rates are proprietary
- **No MCP servers yet**: We need to research and install OpenTakeoff MCP, Qdrant will be set up locally

## Environment Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Start Qdrant (when implemented)
# qdrant --config /path/to/config.yaml
```

## Development Workflow

1. **Check `STATUS.md`** for current checkpoint progress
2. **Read `.helix/plan.md`** for checkpoint acceptance criteria
3. **Write test first** in `tests/` directory
4. **Implement code** to pass the test
5. **Validate** against acceptance criteria
6. **Update STATUS.md** when done

## Key Design Decisions

- **Orchestration**: Using LangGraph for agent coordination
- **Vector search**: Qdrant for cost database similarity search
- **Input formats**: PDF and BIM (IFC) files
- **Output**: Standard BOQ format with confidence scoring

## Data Sources

| Source | Records | License | Usage |
|--------|---------|---------|-------|
| USCCDB | 2.85M | CC BY 4.0 | Open data, commercial use OK |
| Dupras Ledoux | ~10K | Proprietary | Internal Montreal projects |

## Next Steps

1. Install Qdrant and load USCCDB data
2. Research OpenTakeoff MCP API
3. Build the takeoff extraction module
4. Create vector search interface