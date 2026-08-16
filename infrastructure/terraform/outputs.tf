output "network_id" {
  description = "ID of the Qafila VPC when enable_vpc is true."
  value       = var.enable_vpc ? google_compute_network.qafila[0].id : null
}

output "subnetwork_id" {
  description = "ID of the initial Qafila subnet when enable_vpc is true."
  value       = var.enable_vpc ? google_compute_subnetwork.qafila[0].id : null
}
