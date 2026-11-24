# MEP AI Estimation Pipeline - Architecture

## System Overview

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Input Drawing  │────▶│  OpenTakeoff    │────▶│  Quantity Data  │
│  (PDF/BIM)      │     │  MCP Server     │     │  (Length,Area,  │
└─────────────────┘     └─────────────────┘     │  Volume, Count) │
                                                 └────────┬────────┘
                                                          │
                                                          ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Cost Database  │◀────│  Qdrant Vector  │◀────│  USCCDB + DL     │
│  (Unit Rates)   │     │  Database       │     │  Internal Rates  │
└─────────────────┘     └────────┬────────┘     └─────────────────┘
                                  │                (2.85M + 10K recs)
                                  │
                                  ▼
┌─────────────────┐     ┌─────────────────┐
│  Validation     │────▶│  Output         │
│  Engine         │     │  (BOQ Report)   │
│  (±20% check,   │     │                 │
│   Productivity) │     │                 │
└─────────────────┘     └─────────────────┘
```

## Components

### 1. Quantity Takeoff (OpenTakeoff MCP)
- **Purpose**: Extract construction quantities from PDFs and BIM models
- **Output**: Standardized JSON with measurement types:
  - Length (feet/meters)
  - Area (sq ft/sq m)
  - Volume (cubic ft/cubic m)
  - Count (item counts)

### 2. Cost Database (Qdrant)
- **Purpose**: Vector similarity search for unit rates
- **Sources**:
  - USCCDB: 2.85M cost observations
  - Dupras Ledoux: 10K+ internal Montreal rates
- **Schema**: {work_id, resource_id, unit_cost, description, vector_embedding}

### 3. Orchestration Layer (LangGraph)
- **Purpose**: Coordinate workflow between components
- **Flow**: Takeoff → DB Search → Cost Calculation → Validation → Output
- **Error handling**: Fallback logic for missing database entries

### 4. Validation Engine
- **±20% Benchmark**: Compare against regional benchmarks
- **Productivity Checks**: Reject physically impossible values
- **Cross-DB Sanity**: Compare USCCDB vs internal rates

## Data Flow

1. **Input**: PDF drawing or BIM model
2. **Takeoff**: OpenTakeoff extracts quantities
3. **Match**: Vector search finds similar items in cost database
4. **Calculate**: Apply unit rates to quantities
5. **Validate**: Check against benchmarks and constraints
6. **Output**: BOQ (Bill of Quantities) with confidence ranges

## API Endpoints

### Takeoff Service
```
POST /takeoff
{
  "file": "drawing.pdf",
  "categories": ["electrical", "plumbing", "mechanical"]
}
→ {"measurements": [...]}
```

### Cost Search Service
```
POST /search
{
  "item": "conduit 1 inch PVC",
  "region": "Montreal",
  "limit": 5
}
→ {"results": [{work_id, resource_id, unit_cost, similarity}]}
```

### Estimate Service
```
POST /estimate
{
  "quantities": [...],
  "region": "Montreal",
  "validate": true
}
→ {"total_cost": 125000, "confidence": 0.85, "breakdown": [...]}
```