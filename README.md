# AWS EKS Platform Engineering Reference — Infoplus application

A compact, inspectable reference for an AWS platform delivery path: Terraform guardrails, a deployment-admission policy, and an EKS operational runbook. Prepared by Rahul H Bhatia for the Senior Cloud/DevOps role at Infoplus Technologies UK Limited. It is a portfolio project, not an Infoplus environment or a production deployment.

## Reviewer guide

| Role theme | Evidence |
| --- | --- |
| AWS, VPC, IAM and security | `terraform/platform.tf` declares a VPC input boundary, workload TLS egress, cluster-log destination and a workload IAM role boundary. |
| Terraform / IaC | Small composable Terraform baseline plus deterministic guardrail tests. |
| Docker, Kubernetes/EKS and CI/CD | `app/admission.py` validates deployment metadata before rollout; CI runs the tests. |
| Reliability, monitoring and incident work | `docs/eks-operations.md` covers rollout, signals, backup/DR decisions and escalation. |
| GitOps / Argo CD / Helm | The runbook describes the expected reconciliation and rollback behavior; no Argo CD or Helm cluster is claimed as deployed. |

## Run

```bash
python -m unittest discover -s tests -v
terraform -chdir=terraform init
terraform -chdir=terraform validate
```

CI does not apply Terraform or connect to AWS. The Terraform is illustrative and deliberately incomplete: a real deployment needs an organization-owned account/VPC CIDRs, KMS keys, IAM boundaries, EKS version/add-ons, private endpoint decision, NAT/egress design, tags, policy-as-code, state backend, and approvals.

## Scope and honesty

Rahul’s experience includes AWS/GCP, Terraform/CloudFormation, EKS/Kubernetes, GitOps, CI/CD, monitoring/observability, cloud security and production operations, plus AWS GenAI/RAG application deployment. This artifact does not claim a specific number of years, an Infoplus production system, active AWS credentials, an Azure deployment, or SRE certification.

## Contact

Rahul H Bhatia · +91 9884541449 · rahulbhatia1998@gmail.com  
[LinkedIn](https://www.linkedin.com/in/rahul-h-bhatia/) · [Portfolio](https://rahulhbhatia.vercel.app) · [Credly](https://www.credly.com/users/rahul-h-bhatia/badges)
