output "api_url" {
  description = "URL pública de la API desplegada en Azure"
  value       = "http://${azurerm_container_group.api.fqdn}:8000"
}

output "resource_group" {
  description = "Nombre del grupo de recursos creado"
  value       = azurerm_resource_group.rg.name
}

output "location" {
  description = "Región donde se ha desplegado la infraestructura"
  value       = azurerm_resource_group.rg.location
}