# qa-automation-showcase
# QA Automation Showcase 🚀

Este repositório é uma demonstração rápida de arquitetura de automação de testes, focada em manutenibilidade e resiliência, dividida em duas frentes principais: Automação Web (UI) e Validação de APIs.

## 1. Web UI Testing (Selenium + POO)
**Qual:** Padrão Page Object Model (POM).
**Por que:** Para separar a lógica da página (elementos e interações) da lógica de teste. Isso garante que, se a interface mudar, a manutenção seja feita em apenas um lugar, evitando a quebra de múltiplos testes.
**Vamos:** Implementação de uma classe base simulando o login no site de testes Sauce Demo, utilizando Esperas Explícitas (WebDriverWait) para evitar falsos-positivos (Flaky Tests) causados por atrasos na renderização.

## 2. API Testing (Testes de Resiliência)
**Qual:** Validação de rotas de backend utilizando a biblioteca `requests` do Python.
**Por que:** O backend deve atuar como o principal filtro de segurança do sistema. Além do "caminho feliz" (Status 200), é crucial validar como a API se comporta com dados incorretos ou rotas inexistentes (Status 404), garantindo o tratamento adequado de exceções.
