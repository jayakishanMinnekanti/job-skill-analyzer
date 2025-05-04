# 🔐 Security Policy

## 🛡 Supported Versions

We currently support **only the latest version** of this repository.

| Version | Supported? |
|---------|------------|
| Latest  | ✅ Yes      |
| Older   | ❌ No       |

---

## 📣 Reporting a Vulnerability

If you discover a security vulnerability, please help us protect the community by following these steps:

1. **Do not open public issues or pull requests.**
2. Report the vulnerability **privately** via email to:

   📧 [contact@jayakishan.com](mailto:contact@jayakishan.com)

3. Include the following details:
   - A clear description of the issue
   - Reproduction steps (if applicable)
   - Any potential impact or affected modules

We will respond within **48 hours** and begin triaging immediately.

---

## 🔍 Code & Dependency Security

We use the following libraries and best practices to ensure security and integrity:

- **Trusted Libraries**  
  All packages listed in [`requirements.txt`](./requirements.txt) are widely used and regularly updated (e.g., `scikit-learn`, `pandas`, `numpy`).

- **`.gitignore` Protection**  
  Sensitive model artifacts and local environment files are excluded from the repository:
  - `models/*.pkl`
  - `.idea/`, `.vscode/`, `*.log`, `.ipynb_checkpoints/`

- **No Secrets in Code**  
  This repository contains **no hardcoded API keys or credentials**. If secrets are accidentally pushed, GitHub Secret Scanning will flag them.

---

## 🤝 Responsible Disclosure

We follow responsible disclosure practices. Any reported issues will remain **confidential** until they are resolved and patched. We appreciate your help in keeping this project secure and reliable.

---

Thanks for supporting the security of **Job Skill Analyzer**! 💙