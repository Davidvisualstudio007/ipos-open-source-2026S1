# Architecture

Some intro paragraph here explaining the architecture...

## System Diagram

```mermaid
graph LR
    HumanClient["Human Client<br/>Browser, curl, Postman"]
    AIClient["AI Client<br/>Gemini, MCP Inspector"]
    Gemini["Gemini API<br/>External<br/>PLANNED"]

    subgraph AgServer ["Agriculture MCP Server (localhost:8003)"]
        FastAPI["FastAPI Layer<br/>HTTP routes, JSON<br/>BUILT"]
        MCP["MCP Layer<br/>Tools, Resources, Prompts<br/>BUILT"]
    end

    Service["Service Layer<br/>TaskService<br/>PLANNED"]

    HumanClient -->|HTTP request| FastAPI
    AIClient -->|MCP request| MCP

    FastAPI -.->|calls service| Service
    MCP -.->|calls service| Service
    MCP -.->|natural language| Gemini

    style Service stroke-dasharray: 5 5
    style Gemini stroke-dasharray: 5 5
```

## Legend

- **Solid border** = built today (as of 05/24/2026)
- **Dashed border** = planned, not yet built

(...more content like the folder map table...)