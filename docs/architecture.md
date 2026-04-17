```mermaid
flowchart TD
    subgraph Client
        A[User Request] --> B[API Gateway]
    end

    subgraph Security
        B --> C[Auth/JWT Validation]
        C --> D[RBAC & Input Sanitization]
        D --> E[PII Filtering / Redaction]
    end

    subgraph Ingestion
        E --> F[Claims Data Store]
        F --> G[Chunking Service]
        G --> H[Vector DB]
    end

    subgraph RAG_Agents
        E --> I[Researcher Agent]
        H --> I
        I --> J[Critic Agent]
        J --> K[Policy‑Checker Agent]
        K --> L[Summarizer Agent]
        L --> M[Final Answer]
    end

    subgraph Observability
        A --> N[Request Logging]
        I --> N
        J --> N
        K --> N
        L --> N
        N --> O[Tracing IDs]
        O --> P[Metrics: latency, errors]
        P --> Q[Alerts on SLOs]
    end

    subgraph Edge_Cases
        I --> R{Docs Found?}
        R -- No --> S[Return fallback / escalation]
        R -- Yes --> I

        K --> T{Policy Compliant?}
        T -- No --> U[Reject + route to Reviewer]
        T -- Yes --> K

        H --> V[Vector DB Unavailable]
        V --> W[Graceful degradation: keyword‑only retrieval]

        P --> X{High Error Rate?}
        X -- Yes --> Y[Alert / Backoff / Retry]
    end

    M --> Z[User Response]
    ...
```
```mermaid
sequenceDiagram
    participant User
    participant Gateway
    participant Auth
    participant Agents
    participant VectorDB
    participant Storage
    participant Metrics

    User->>Gateway: POST /ask
    Gateway->>Auth: Validate JWT
    Auth-->>Gateway: Auth OK
    Gateway->>Agents: Start Researcher
    Agents->>VectorDB: Query chunks
    VectorDB-->>Agents: Retrieved chunks
    Agents->>Agents: Critic refines
    Agents->>Agents: Policy‑Checker validates
    Agents->>Agents: Summarizer formats
    Agents-->>Gateway: Final answer
    Gateway-->>User: JSON response
    Gateway->>Metrics: Log request + latency
    ...
```