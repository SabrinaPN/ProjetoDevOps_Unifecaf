variable "kubeconfig_path" {
  description = "Caminho do kubeconfig"
  type        = string
  default     = "~/.kube/config"
}

variable "namespace" {
  description = "Namespace da aplicação"
  type        = string
  default     = "loja-veloz"
}
