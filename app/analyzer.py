from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Finding:
    severity: str
    category: str
    message: str


def analyze_event(event: str) -> list[Finding]:
    text = event.lower()
    findings: list[Finding] = []

    if "failed login" in text or "authentication failure" in text:
        findings.append(Finding("MEDIUM", "AUTH_FAILURE", "Authentication failure detected."))

    if "admin" in text and ("login" in text or "authentication" in text):
        findings.append(Finding("HIGH", "PRIVILEGED_ACCOUNT", "Privileged account activity detected."))

    if re.search(r"\b(?:password|credential|secret)\b", text):
        findings.append(Finding("HIGH", "CREDENTIAL_ACTIVITY", "Credential-related activity detected."))

    if not findings:
        findings.append(Finding("LOW", "INFO", "No high-confidence security pattern detected."))

    return findings
