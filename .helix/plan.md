# Automated MEP construction estimation workflow with price validation

**Kind:** feature  
**Reference:** doc at `Requirements from IT expert - DDC CWICR database, OpenTakeoff MCP, OpenConstructionERP`  
**Standards enforced:** CLAUDE.md, docs/architecture.md  
**Behavior harness:** `python -m pytest tests/`  
**Autonomy:** supervised  

## Open questions (answer before approving)

- What are the exact Qdrant collection dimensions for DDC CWICR?
- What is the OpenTakeoff MCP API specification?
- What Python orchestration framework to use (LangGraph, CrewAI, custom)?

---

## Sequence

| # | Checkpoint | Builder | Gates | Status |
|---|---|---|---|---|
| 1 | Environment setup and dependency installation | opus | behavior → adversarial → human | planned |
| 2 | Takeoff integration - PDF/BIM quantity extraction | opus | behavior → adversarial → human | planned |
| 3 | Cost database vector search interface | opus | behavior → adversarial → human | planned |
| 4 | LLM orchestration layer | opus | behavior → adversarial → human | planned |
| 5 | Price validation and sanity checking | opus | behavior → adversarial → human | planned |
| 6 | Output generation - BOQ and reports | opus | behavior → adversarial → human | planned |
| 7 | Integration testing with real drawings | opus | behavior → adversarial → human | planned |

---

### 1. Environment setup and dependency installation

**Done when:**
- Python virtual environment created with Qdrant and OpenTakeoff MCP installed
- DDC CWICR Qdrant snapshot loaded with 55K+ work items

**Tests:**
- qdrant collection count matches DDC CWICR spec (55K+ work items)
- OpenTakeoff MCP server responds to ping

---

### 2. Takeoff integration - PDF/BIM quantity extraction

**Done when:**
- OpenTakeoff MCP extracts quantities (length, area, volume, count)
- Output in standardized format for downstream processing

**Tests:**
- Sample PDF with known quantities produces correct measurements
- Output JSON matches expected schema

---

### 3. Cost database vector search interface

**Done when:**
- Qdrant collection indexed with DDC CWICR data with vector search
- Search interface provides work item IDs and resource mappings

**Tests:**
- Search for common MEP item returns expected results
- Results include required fields (work_id, resource_id, unit_cost)

---

### 4. LLM orchestration layer

**Done when:**
- Agent coordinates takeoff → database search → cost calculation flow
- Error handling for missing database entries with confidence scoring

**Tests:**
- Full pipeline produces estimate for sample input
- Missing item triggers fallback logic

---

### 5. Price validation and sanity checking

**Done when:**
- ±20% benchmark validation implemented with productivity checks
- Cross-database sanity comparisons enabled

**Tests:**
- Estimate 20% below benchmark flagged as invalid
- Productivity check rejects impossible values

---

### 6. Output generation - BOQ and reports

**Done when:**
- Verified BOQ generated in standard format with confidence ranges
- Cost report with line-item breakdown produced

**Tests:**
- BOQ contains all required fields and totals
- Report format matches industry standard

---

### 7. Integration testing with real drawings

**Done when:**
- End-to-end test with sample construction drawing validates accuracy
- Performance metrics captured and documented

**Tests:**
- Full pipeline runs without errors on test drawing
- Estimated costs within acceptable margin of known values

---

## Status: approved: None