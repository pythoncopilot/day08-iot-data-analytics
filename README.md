## GitHub Actions (CI Pipeline)

This project uses GitHub Actions to automatically validate Python code on every push.

### Workflow Steps:
1. GitHub detects push to main branch
2. Creates a fresh Linux runner
3. Installs Python 3.11
4. Runs compile check on all Python files

### What it checks:
- Python syntax errors
- File structure validity
- Basic code integrity

### What it does NOT check:
- Runtime execution
- Database connections
- API responses
- UI behavior

### Why CI is important:
- Prevents broken code from being merged
- Provides instant feedback after commits
- Ensures code quality consistency
- Simulates real production pipelines

### View results:
Go to the "Actions" tab in GitHub repository.
Each push generates a new workflow run.