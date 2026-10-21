terraform {
  required_version = ">= 1.0.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# 1. Resource Group for Dubai Smart Grid MLOps
resource "azurerm_resource_group" "rg" {
  name     = "rg-dubai-smart-grid-mlops"
  location = "East US"  # Ya aap UAE North bhi rakh sakti hain
}

# 2. Azure Kubernetes Service (AKS) Cluster for FastAPI & MLOps deployment
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "dubai-smart-grid-aks"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "dubai-smart-grid-dns"

  default_node_pool {
    name       = "defaultpool"
    node_count = 2
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Production"
    Project     = "Dubai Smart Grid MLOps"
    Owner       = "Anam Parwez"
  }
}

output "kube_config" {
  value     = azurerm_kubernetes_cluster.aks.kube_config_raw
  sensitive = true
}

output "cluster_endpoint" {
  value = azurerm_kubernetes_cluster.aks.kube_config.0.host
}
