# Architecture

Some intro paragraph here explaining the architecture...

## System Diagram

```mermaid
graph TD
    HumanClient["Human ClientBrowser,<br/> curl, Postman"]
    AIClient["AI ClientGemini,<br/>MCP Inspector"]
    Gemini["Gemini APIExternalPLANNED"]

    subgraph AgServer ["Agriculture MCP Server (localhost:8003)"]
        FastAPI["FastAPI LayerHTTP routes, JSONBUILT"]
        MCP["MCP LayerTools, Resources, PromptsBUILT"]
    end

    Service["Service LayerTaskServicePLANNED"]
    Storage[("In-Memory StorageList + ID lookup mapPLANNED")]

    HumanClient -->|HTTP request| FastAPI
    AIClient -->|MCP request| MCP

    FastAPI -.->|calls service| Service
    MCP -.->|calls service| Service
    MCP -.->|natural language| Gemini

    Service -.->|reads / writes| Storage

    style Service stroke-dasharray: 5 5
    style Storage stroke-dasharray: 5 5
    style Gemini stroke-dasharray: 5 5
```

## Legend

- **Solid border** = built today (as of 05/24/2026)
- **Dashed border** = planned, not yet built

(...more content like the folder map table...)