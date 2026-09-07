# CloudWatch Monitoring Design

## Metrics

Track CPU utilization, request count, latency, 5xx errors, ECS service health and deployment events.

## Alerts

Create alarms for sustained resource saturation, elevated error rates and application health degradation.

## Operational workflow

`Metric → Alarm → Notification → Investigation → Remediation → Post-incident review`

For a production implementation, connect alarms to SNS and an approved incident-management workflow.
