An extremely fast Python package and project manager, written in Rust.
https://github.com/astral-sh/uv

### Help:

### Installing uv:
PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

- irm is a built-in PowerShell alias for the cmdlet Invoke-RestMethod.
- iex is a built-in PowerShell alias for the cmdlet Invoke-Expression.

### uv-managed project
uv init YOUR_PROJECT_NAME
cd YOUR_PROJECT_NAME

### Add dependencies 
uv add NAME
