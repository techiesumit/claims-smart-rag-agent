# Claims‑Smart RAG Agent – Progress Tracker

Use this file to **track daily progress** across the 24‑week plan.  
Check the box when a task is done and use the **Notes** column for freeform updates. [web:66][web:70]

---

## Legend

- **☐** `- [ ]` – not started
- **☑** `- [x]` – completed
- **Notes** – any freeform text (what you did, blockers, ideas)

Most Markdown renderers (GitHub, VS Code with Markdown preview) will let you **click the checkboxes** interactively; the underlying Markdown updates when you edit the file. [web:66][web:64]

---

## Week 1 – RAG Fundamentals & Project Setup

| Day | Task | Links | Done | Notes |
| --- | ---- | ----- | ---- | ----- |
| Day 1 | Create GitHub repo, initialize project, push first commit | [GitHub New Repo](https://github.com/new) | - [ ] |  |
| Day 1 | Enroll in RAG course, watch intro lesson | [RAG Course](https://learn.deeplearning.ai/courses/retrieval-augmented-generation/information) | - [ ] |  |
| Day 2 | Finish Week 1 videos (RAG overview & basic pipeline) | [RAG Course](https://learn.deeplearning.ai/courses/retrieval-augmented-generation/information) | - [ ] |  |
| Day 2 | Write 1–2 paragraphs of RAG notes in `docs/notes-week1.md` |  | - [ ] |  |
| Day 3 | Finalize repo structure (`src`, `docs`, `tests`, `PLAN.md`) |  | - [ ] |  |
| Day 3 | Capture open questions about RAG & your domain (claims) |  | - [ ] |  |

---

## Week 2 – Data Ingestion Pipeline

| Day | Task | Links | Done | Notes |
| --- | ---- | ----- | ---- | ----- |
| Day 4 | Implement basic PDF → text extraction (PyPDF / OCR) |  | - [ ] |  |
| Day 4 | Save raw text to files/DB, add small sample dataset |  | - [ ] |  |
| Day 5 | Refine extraction for CMS‑style docs (headers, fields) |  | - [ ] |  |
| Day 5 | Document ingestion flow in `docs/ingestion.md` |  | - [ ] |  |
| Day 6 | Add simple ingestion tests (happy path + bad file) |  | - [ ] |  |
| Day 6 | Commit & push with clear message |  | - [ ] |  |

---

## Week 3 – Chunking & Vector Store

| Day | Task | Links | Done | Notes |
| --- | ---- | ----- | ---- | ----- |
| Day 7 | Implement fixed‑size chunking (by chars/tokens) |  | - [ ] |  |
| Day 7 | Stand up vector DB (PGVector/Weaviate/Pinecone) | [Pinecone RAG](https://www.pinecone.io/learn/retrieval-augmented-generation/) | - [ ] |  |
| Day 8 | Implement section‑aware chunking |  | - [ ] |  |
| Day 8 | Index chunks into vector DB |  | - [ ] |  |
| Day 9 | Add CLI or script to rebuild index from raw docs |  | - [ ] |  |
| Day 9 | Update `docs/ingestion.md` with chunking strategies |  | - [ ] |  |

---

## Week 4 – Baseline Retrieval & QA API

| Day | Task | Links | Done | Notes |
| --- | ---- | ----- | ---- | ----- |
| Day 10 | Implement dense retriever (top‑k search) | [RAG Concepts](https://www.databricks.com/blog/what-is-retrieval-augmented-generation) | - [ ] |  |
| Day 10 | Quick manual sanity checks on retrieval |  | - [ ] |  |
| Day 11 | Build minimal FastAPI/Flask endpoint: `POST /ask` |  | - [ ] |  |
| Day 11 | Wire retrieval + LLM into endpoint |  | - [ ] |  |
| Day 12 | Add basic logging and error handling |  | - [ ] |  |
| Day 12 | Update README with simple usage example |  | - [ ] |  |

---

## Week 5 – RAG Evaluation & Metrics

| Day | Task | Links | Done | Notes |
| --- | ---- | ----- | ---- | ----- |
| Day 13 | Create small evaluation set of Q/A pairs |  | - [ ] |  |
| Day 13 | Write script to run eval set through RAG pipeline |  | - [ ] |  |
| Day 14 | Log retrieval hit rate & answer quality (manual tags) | [Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | - [ ] |  |
| Day 14 | Store results in `docs/evaluation.md` |  | - [ ] |  |
| Day 15 | Tune top‑k / prompts and re‑run eval |  | - [ ] |  |
| Day 15 | Commit changes with summary of improvements |  | - [ ] |  |

---

## Week 6 – ML Refresher (scikit‑learn)

| Day | Task | Links | Done | Notes |
| --- | ---- | ----- | ---- | ----- |
| Day 16 | Build simple classifier with `scikit-learn` (claim type) | [ML Frameworks](https://learningactors.com/the-ultimate-guide-to-machine-learning-frameworks/) | - [ ] |  |
| Day 16 | Evaluate on small labeled dataset |  | - [ ] |  |
| Day 17 | Wrap classifier as a callable service or function |  | - [ ] |  |
| Day 17 | Add tests for classifier pipeline |  | - [ ] |  |
| Day 18 | Document how classifier could be an agent tool |  | - [ ] |  |
| Day 18 | Commit & push |  | - [ ] |  |

---

## Week 7 – NLP Fundamentals with PyTorch

| Day | Task | Links | Done | Notes |
| --- | ---- | ----- | ---- | ----- |
| Day 19 | Start PyTorch NLP tutorial (tokenization, embeddings) | [PyTorch NLP](https://docs.pytorch.org/tutorials/beginner/nlp/index.html) | - [ ] |  |
| Day 19 | Run first tutorial example end‑to‑end |  | - [ ] |  |
| Day 20 | Implement simple NLP model (e.g., sentiment) |  | - [ ] |  |
| Day 20 | Integrate model as a tool in project |  | - [ ] |  |
| Day 21 | Notes on where to use custom models vs LLMs |  | - [ ] |  |
| Day 21 | Commit & push |  | - [ ] |  |

---

## Week 8 – Hybrid Retrieval

| Day | Task | Links | Done | Notes |
| --- | ---- | ----- | ---- | ----- |
| Day 22 | Add BM25/keyword retriever |  | - [ ] |  |
| Day 22 | Implement hybrid retrieval (keyword + vector) | [RAG Concepts](https://www.databricks.com/blog/what-is-retrieval-augmented-generation) | - [ ] |  |
| Day 23 | Compare dense vs BM25 vs hybrid on eval set |  | - [ ] |  |
| Day 23 | Document results in `docs/evaluation.md` |  | - [ ] |  |
| Day 24 | Clean up code, add tests for hybrid retriever |  | - [ ] |  |
| Day 24 | Commit & push |  | - [ ] |  |

---

## Later Weeks

For Weeks 9–24 (multi‑agent, security, observability, ADK), follow the same pattern:

- **One section per week** with ~5–6 rows:
  - Design tasks
  - Coding tasks
  - Docs/tests
  - Links to specific docs/courses (ADK, security, observability)  
- Keep **checkboxes** and **freeform Notes** column to track progress and blockers. [web:66][web:70]

You can copy one of the week tables above, paste it, and edit **Week X / Day Y** and the task text for each future week.

---

## Summary

- This `TRACKER.md` gives you **interactive checkboxes** (in GitHub/VS Code) + **links + notes** for each day. [web:66][web:64]  
- Extend the same pattern for Weeks 9–24 to cover the whole 6‑month plan.  
- You can now drive your execution by just opening `TRACKER.md` and ticking off tasks.

Would you like me to also generate a **short PowerShell script** that copies `PLAN.md` → `TRACKER.md` scaffold and opens it in VS Code automatically so you don’t have to create it by hand?
