# EKS delivery and operations model

## Delivery

Build an immutable image, scan it, attach provenance, render a reviewed manifest/Helm release, and commit the desired state. A GitOps controller should reconcile only protected branches/environments. The admission checks in this repository are a small CI gate, not an in-cluster admission controller. Roll back by the last known-good image digest and manifest revision; do not retag a mutable image.

## Signals and incident response

Track API error/latency/saturation, pod readiness/restarts, node pressure, autoscaling events, deployment progression, cluster audit logs, container logs and AWS control-plane events. Establish SLOs with the owning service team before paging. Triage begins with scope and recent change; pause rollout if it increases impact. Escalate identity/network boundary changes and security events. Avoid logging credentials, tokens or customer payloads.

## Backup, recovery and cost

Test recovery of workload configuration, persistent data and IAM dependencies against approved RTO/RPO targets. EKS cluster recreation is not data recovery. Attribute cloud cost by environment/workload; review right-sizing, autoscaling and egress before changing availability-critical capacity. Use a remote, encrypted Terraform state backend with locking in an actual organization; none is configured here.
