output "network_id" {
  description = "ID of the Qafila VPC network."
  value       = google_compute_network.qafila.id
}

output "subnetwork_id" {
  description = "ID of the Qafila private subnet."
  value       = google_compute_subnetwork.qafila_private.id
}
