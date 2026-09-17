terraform { required_version = ">= 1.6.0" }
variable "name" { type = string }
variable "vpc_id" { type = string }
variable "private_subnet_ids" { type = list(string) }

resource "aws_cloudwatch_log_group" "eks" { name = "/aws/eks/${var.name}/cluster" retention_in_days = 30 }
resource "aws_iam_role" "workload" {
  name_prefix = "${var.name}-workload-"
  assume_role_policy = jsonencode({Version="2012-10-17",Statement=[{Effect="Allow",Principal={Service="ecs-tasks.amazonaws.com"},Action="sts:AssumeRole"}]})
}
resource "aws_security_group" "workload" {
  name_prefix = "${var.name}-workload-"
  vpc_id = var.vpc_id
  egress { from_port=443 to_port=443 protocol="tcp" cidr_blocks=["0.0.0.0/0"] }
}
