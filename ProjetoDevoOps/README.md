# Loja Veloz – Projeto Completo DevOps

Este repositório contém um MVP acadêmico para o desafio **“Entrega contínua de uma plataforma de pedidos em microsserviços: do Docker Compose ao Kubernetes com observabilidade e CI/CD”**.

## Estrutura

- `services/`: microsserviços do sistema
- `docker-compose.yml`: ambiente local multi-serviço
- `k8s/base`: manifests Kubernetes
- `.github/workflows`: pipeline CI/CD
- `terraform/`: esqueleto de IaC
- `docs/`: relatórios e roteiro do pitch

## Serviços

- `api-gateway`: entrada HTTP da aplicação
- `orders`: criação e consulta de pedidos
- `payments`: autorização simulada de pagamentos
- `stock`: reserva de itens

## Como executar localmente

```bash
docker compose up --build
```

A API ficará disponível em `http://localhost:8000`.

### Teste rápido

```bash
curl -X POST http://localhost:8000/orders   -H "Content-Type: application/json"   -d '{"customer":"Gabriel","sku":"SKU-001","quantity":2,"amount":199.90}'
```

## Estratégias adotadas

- **Deploy:** Rolling Update como baseline; indicação de evolução para Canary.
- **Escala:** HPA no API Gateway por CPU.
- **Observabilidade:** proposta com métricas, logs e traces via OpenTelemetry.
- **Segurança:** usuário não-root nas imagens, Secrets/ConfigMaps, namespace dedicado e policy inicial.

## Observações

- O projeto foi simplificado para fins acadêmicos e demonstração de arquitetura.
- Os endpoints de pagamento e estoque são simulados.
- Ajustes de registry, credenciais e cluster devem ser configurados conforme o ambiente real.
