# NPS Portal

Internal tools portal for Power Solutions Hub.

## Structure

```
nps-portal/
├── index.html              ← shared portal home page
├── server.py               ← local dev server (Python 3, no deps)
├── README.md
└── tools/
    └── nps-calculator.html ← UPS & Battery Calculator
    └── (add new apps here)
```

## Run locally

```bash
python server.py
```

Then open http://localhost:8000

## Add a new app

1. Drop the `.html` file into `tools/`  e.g. `tools/nps-invoicing.html`
2. Add a new card in `index.html` pointing to `tools/nps-invoicing.html`
3. Change `status-soon` → `status-live` when ready

## URL pattern

| Page | URL |
|------|-----|
| Portal home | `/` |
| Calculator | `/tools/nps-calculator.html` |
| Next app | `/tools/nps-<name>.html` |
