"""Provider-neutral incident summarization interface.

Connect this module to an approved LLM provider and sanitized CloudWatch/log input.
Never send credentials, secrets, tokens or customer data to the model.
"""

from dataclasses import dataclass


@dataclass
class Incident:
    service: str
    severity: str
    symptoms: str
    recent_changes: str


def build_prompt(incident: Incident) -> str:
    return f"""Summarize this DevOps incident for an engineer.
Service: {incident.service}
Severity: {incident.severity}
Symptoms: {incident.symptoms}
Recent changes: {incident.recent_changes}
Return: impact, likely causes, evidence to inspect, and safe next steps.
"""


if __name__ == "__main__":
    print(build_prompt(Incident("ecs-service", "high", "elevated 5xx", "new deployment")))
