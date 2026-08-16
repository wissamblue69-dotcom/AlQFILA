variable "project_id" {
  description = "Google Cloud project ID."
  type        = string
}

variable "region" {
  description = "Google Cloud region for regional resources."
  type        = string
  default     = "europe-west1"
}

variable "subnet_cidr" {
  description = "CIDR range for the private subnet."
  type        = string
  default     = "10.0.1.0/24"
}
