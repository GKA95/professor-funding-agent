# Professor Funding Agent

A zero-budget starter for researching graduate professors, scoring fit, preparing personalized outreach, and scheduling email delivery.

## Architecture
- GitHub Actions = cloud scheduler/runner
- Python = automation
- Google Sheets = persistent queue/log
- Gmail = email delivery
- Botpress = optional control/interface layer

## Important
This repository is a starter. It does NOT send email until you configure credentials/secrets and explicitly enable the send workflow.

## Repository structure
```text
.github/workflows/
  research.yml
  send_emails.yml
config/profile.json
src/
  models.py
  researcher.py
  scorer.py
  queue.py
  email_generator.py
  send_emails.py
requirements.txt
```

## Local test
```bash
pip install -r requirements.txt
python -m src.scorer
```

## GitHub setup
1. Create a GitHub repository named `professor-funding-agent`.
2. Upload these files.
3. Add required secrets only after the research/scoring tests work.
4. Keep the repository public only if no secrets or private data are committed.

The workflow currently runs in DRY RUN mode. Change `DRY_RUN` to `false` only after Gmail authentication is configured and tested.
