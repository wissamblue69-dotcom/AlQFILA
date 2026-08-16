variable "project_id" {
  description = "Google Cloud project ID."
  type        = string
  default     = ""
}

variable "region" {
  description = "Google Cloud region for regional resources."
  type        = string
  default     = "europe-west1"
}

variable "network_name" {
  description = "Name of the Qafila VPC network."
  type        = string
  default     = "qafila-vpc"
}

variable "subnet_cidr" {
  description = "CIDR range for the initial subnet."
  type        = string
  default     = "10.10.0.0/24"
}

variable "enable_vpc" {
  description = "Create the VPC and subnet only when explicitly enabled."
  type        = bool
  default     = false
}
