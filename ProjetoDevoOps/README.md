# Loja Veloz – Plataforma de Pedidos em Microsserviços com DevOps

## Sobre o Projeto

Este repositório apresenta a implementação de um MVP (Minimum Viable Product) desenvolvido para o desafio acadêmico **"Entrega Contínua de uma Plataforma de Pedidos em Microsserviços: do Docker Compose ao Kubernetes com Observabilidade e CI/CD"**.

A solução foi projetada com base nos princípios de arquitetura de microsserviços e práticas DevOps modernas, contemplando conteinerização, integração contínua, entrega contínua, escalabilidade, observabilidade e infraestrutura como código.

O objetivo do projeto é demonstrar todo o ciclo de vida de uma aplicação distribuída, desde sua execução em ambiente local até sua implantação automatizada em um cluster Kubernetes.

---

## Arquitetura da Solução

A plataforma é composta por quatro microsserviços independentes, cada um responsável por uma funcionalidade específica do sistema:

| Serviço     | Responsabilidade                       |
| ----------- | -------------------------------------- |
| API Gateway | Ponto de entrada das requisições HTTP  |
| Orders      | Gerenciamento e consulta de pedidos    |
| Payments    | Simulação de autorização de pagamentos |
| Stock       | Controle e reserva de itens em estoque |

Essa divisão promove desacoplamento, escalabilidade e facilidade de manutenção da aplicação.

---

## Estrutura do Projeto

```text
.
├── services/
│   ├── api-gateway/
│   ├── orders/
│   ├── payments/
│   └── stock/
│
├── docker-compose.yml
├── k8s/
│   └── base/
│
├── terraform/
├── .github/
│   └── workflows/
│
└── docs/
```

### Diretórios Principais

* **services/**: código-fonte dos microsserviços.
* **docker-compose.yml**: ambiente local integrado para desenvolvimento e testes.
* **k8s/base/**: manifests Kubernetes da aplicação.
* **.github/workflows/**: pipeline de Integração Contínua e Entrega Contínua (CI/CD).
* **terraform/**: estrutura inicial de Infraestrutura como Código (IaC).
* **docs/**: documentação técnica e materiais de apresentação.

---

## Execução em Ambiente Local

Para iniciar todos os serviços localmente, execute:

```bash
docker compose up --build
```

Após a inicialização, a aplicação estará disponível em:

```text
http://localhost:8000
```

---

## Teste da API

Exemplo de criação de pedido:

```bash
curl -X POST http://localhost:8000/orders \
-H "Content-Type: application/json" \
-d '{
  "customer": "Sabrina",
  "sku": "SKU-001",
  "quantity": 2,
  "amount": 199.90
}'
```

---

## Práticas DevOps Implementadas

### Conteinerização

* Dockerfile individual para cada microsserviço.
* Imagens otimizadas utilizando multi-stage build.
* Execução com usuário não privilegiado (non-root).
* Isolamento e padronização dos ambientes.

### Kubernetes

* Namespace dedicado.
* Deployments e Services.
* ConfigMaps e Secrets.
* Health Checks (Readiness e Liveness Probes).
* Horizontal Pod Autoscaler (HPA).
* Network Policies.

### Integração e Entrega Contínua

Pipeline automatizado utilizando GitHub Actions com etapas de:

* Testes automatizados;
* Build das imagens;
* Geração de artefatos;
* Preparação para publicação e deploy.

### Observabilidade

A solução foi planejada considerando os três pilares fundamentais da observabilidade:

* **Métricas:** latência, throughput, utilização de CPU e memória;
* **Logs:** registros estruturados para análise operacional;
* **Tracing:** rastreamento distribuído utilizando OpenTelemetry.

### Escalabilidade

Foi implementado um Horizontal Pod Autoscaler (HPA) no API Gateway, permitindo o aumento automático da quantidade de réplicas conforme a demanda da aplicação.

### Segurança

Foram adotadas medidas básicas de segurança, incluindo:

* Execução dos containers com usuário não-root;
* Utilização de Secrets e ConfigMaps;
* Namespace dedicado;
* Configuração inicial de Network Policies.

---

## Infraestrutura como Código

O diretório `terraform/` contém a estrutura inicial para gerenciamento da infraestrutura utilizando Terraform.

A proposta é permitir, futuramente, o provisionamento automatizado de recursos Kubernetes, componentes de observabilidade, ingressos de rede e mecanismos adicionais de segurança.

---

## Considerações Finais

Este projeto demonstra a aplicação prática de conceitos amplamente utilizados em ambientes corporativos modernos, combinando microsserviços, Docker, Kubernetes, CI/CD, observabilidade e escalabilidade em uma única solução.

Embora desenvolvido para fins acadêmicos, o MVP reproduz elementos essenciais presentes em arquiteturas cloud-native utilizadas no mercado, proporcionando uma visão completa do ciclo de desenvolvimento e entrega contínua de software.


## Observações

- O projeto foi simplificado para fins acadêmicos e demonstração de arquitetura.
- Os endpoints de pagamento e estoque são simulados.
- Ajustes de registry, credenciais e cluster devem ser configurados conforme o ambiente real.
