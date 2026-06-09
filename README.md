# Prótese funcional de pé-tornozelo articulada (impressa em 3D, baixo custo)

**Disciplina:** Dispositivos de Reabilitação — Eng. Biomédica, FUMEC
**Entrega:** 22/06/2026 — produto físico + relatório técnico + apresentação formal
**Natureza:** trabalho dedicado e independente (só compartilha a disciplina com os demais)

> ⚠️ Dispositivo de demonstração acadêmica. **Não é para uso clínico real.** Uma prótese
> de pé-tornozelo é estrutural e crítica em segurança; nenhum protótipo FDM deste trabalho
> deve receber carga corporal real sem validação mecânica e avaliação de protético certificado.

---

## Decisões de projeto (travadas em 06/06)

| Eixo | Decisão | Razão |
|---|---|---|
| Origem do design | **Remixar open-source** | Prazo de 16 dias; partir de base comprovada e justificar mudanças é mais defensável que do zero |
| **Design-base** | **A — Make3D "Prosthetic Foot Prototype" (Printables #293133)** | Votado pelo grupo em 08/06; maior score (4,2/5), single-axis direto, conector de pylon integrado. Arquivos em `cad/A_make3d_293133/` |
| Alvo dimensional | **Genérico adulto padrão** | Sem dependência de medir paciente; protótipo demonstrativo |
| Articulação | **Single-axis (dorsi/plantarflexão)** | Mais simples de modelar e imprimir; clássico e suficiente para "funcional" |
| Régua de avaliação | **Briefing livre → régua proposta abaixo** | Não há enunciado escrito do professor |

---

## Requisitos / especificações alvo

Usuário de projeto: **adulto ~70 kg, pé ~26–27 cm (BR 40–41)**.

| Requisito | Valor alvo | Observação |
|---|---|---|
| Carga estática de projeto | ≥ 1,5 × peso corporal ≈ **1030 N** | Pico de heel-strike na marcha normal é ~1,2–1,5× BW |
| Fator de segurança | **2–3** → dimensionar p/ ~2–3 kN | Literatura: FEA achou tensão máx. **15 MPa no heel-strike a 150% BW** |
| ADM dorsiflexão | **10–15°** | Limitada por batente elástico anterior |
| ADM plantarflexão | **15–20°** | Limitada por batente elástico posterior |
| Conexão proximal | Adaptador de pylon padrão (pirâmide 30 mm) ou simplificado | Depende do que o design-base oferece |
| Custo de material | **< R$ 200** | Filamento + parafuso/bucha + TPU. Comparar com prótese comercial (US$ 5k–50k) |
| Massa | minimizar (alvo informativo) | Trade-off com rigidez |

### Materiais previstos
- **Estrutura/keel:** PETG (tenaz, melhor fadiga/impacto que PLA) ou PLA-CF (mais rígido). **Evitar PLA puro** sob carga cíclica — frágil, falha por fadiga.
- **Eixo da articulação:** parafuso de aço M8 + bucha (nylon/bronze).
- **Batentes (bumpers) dorsi/plantar:** TPU ~95A — definem a ADM e amortecem.
- **Orientação de impressão (CRÍTICO):** carga principal deve solicitar o **mínimo possível** a adesão entre camadas (eixo Z é o ponto fraco do FDM). Imprimir o keel deitado.

---

## Régua de avaliação (proposta — briefing livre)

Como não há enunciado, esta é a régua que vou usar para guiar o relatório/apresentação. Ajuste se o professor sinalizar critério diferente.

1. **Produto físico funcional** — articulação se move na ADM alvo e suporta a carga de demonstração. *(peso maior)*
2. **Relatório técnico completo** — ver `RELATORIO.md`.
3. **Fundamentação biomecânica** — ciclo de marcha, papel do tornozelo, justificativa da articulação single-axis vs SACH.
4. **Justificativa de engenharia** — escolha de material, orientação de impressão, geometria, com trade-offs explícitos.
5. **Validação** — teste de ADM medido, teste de carga (mesmo qualitativo), fotos/vídeo. Ver `testes/`.
6. **Baixo custo demonstrado** — planilha de custo real vs. alternativa comercial.
7. **Apresentação formal** — domínio do tema, defesa dos trade-offs sob arguição.

---

## Candidatos open-source para remixar

| Candidato | Articulação | Prós | Contras |
|---|---|---|---|
| **Make3D "Prosthetic Foot Prototype"** (Printables 293133) | Pino + mola, dedos flexíveis, conector de pylon | Match mais direto; STL grátis; feito em Fusion 360 (editável) | **Não testado**; usa Filaflex40 + mola |
| **Appropedia "3D printed prosthetic foot"** | Snap-fit + amortecedor ball-joint | Open source de verdade; ~4% do custo comercial; simples | Estágio "infância"; pouca validação |
| **Colorado School of Mines Capstone** | Flex-ankle (dobradiça flexível), passivo | Pensado p/ ABS / PETG-nylon; manual de instruções | Pediátrico; precisa reescalar |

**Recomendação:** começar pela **Make3D (Printables)** como base estrutural single-axis e simplificar a mola para batentes TPU (mais imprimível, menos dependência de peça comprada). Baixar o STL/CAD para `cad/` e `refs/`.

Referências acadêmicas para fundamentar o relatório (salvar PDFs em `refs/`):
- Baseline não-articulado: **SACH** (solid-ankle cushion-heel) — comparar contra ele.
- FEA de pé protético: tensão máx. 15 MPa @ 150% BW; recurso de projeto = **split forefoot/heel**.
- Toe joint com rigidez não-linear (Nature Sci. Reports) — se for modelar antepé flexível.
- Composites: PLA/fibra de carbono supera PLA puro em desempenho/peso.

Links em `refs/FONTES.md`.

---

## Riscos (ordem de severidade)

1. **Acesso à impressora 3D** — gargalo absoluto. Um pé inteiro são muitas horas/peça + chance de falha. *Se depende do lab da FUMEC, agendar AGORA.* ⛔ bloqueante.
2. **Falha estrutural por orientação/material** — camada Z fraca. Mitigação: PETG, orientação correta, infill 40%+, parede grossa.
3. **Colisão com o estágio (início 15/06)** — janela de impressão encolhe. Travar CAD até 14/06.
4. **Articulação (pino/folga/batente)** — ponto de movimento = ponto de desgaste/folga. Prototipar a junta isolada antes da peça inteira.

---

## Estrutura de pastas

- `cad/` — arquivos editáveis (Fusion/FreeCAD/STEP)
- `stl/` — malhas prontas para fatiar
- `slicing/` — perfis e .gcode/.3mf, parâmetros de impressão
- `refs/` — design-base baixado, PDFs de referência, `FONTES.md`
- `fotos/` — registro de fabricação/montagem/testes (para o relatório)
- `testes/` — dados de ADM e carga, planilha de custo
- `RELATORIO.md` — relatório técnico (em construção)
- `PLANO.md` — cronograma de 16 dias e caminho crítico
