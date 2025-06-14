
# Drawing Checker API (QA Module)

A FastAPI backend for processing DXF/PDF metadata and running 30-point QA checks, designed for use with Custom GPT tools.

## Endpoints

### POST /qa_check
Send JSON with drawing metadata to receive structured QA results.

## Deployment

Use `render.yaml` to deploy to [Render.com](https://render.com).

## Example Start

```bash
uvicorn app.main:app --reload
```
