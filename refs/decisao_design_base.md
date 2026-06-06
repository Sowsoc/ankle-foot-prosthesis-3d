# Matriz de decisão — design-base para remix

> Missão 1 — entregável 3. Avalia os 3 candidatos open-source; pontua cada critério;
> recomenda qual remixar e o que aproveitar / o que mudar.
> **O veredito final é do João.** Este arquivo entrega a fundamentação; ele bate o martelo.

---

## Candidatos avaliados

| ID | Projeto | Link |
|----|---------|------|
| A | Make3D — Prosthetic Foot Prototype | [Printables #293133](https://www.printables.com/model/293133-prosthetic-foot-prototype) |
| B | Appropedia — 3D printed prosthetic foot | [Appropedia](https://www.appropedia.org/3D_printed_prosthetic_foot) |
| C | Colorado School of Mines — Capstone 3D Printed Foot | [Mines Capstone](https://www.mines.edu/capstoneseniordesign/project/3d-printed-prosthetic-foot/) |

---

## Critérios e pesos

| # | Critério | Peso | Rationale |
|---|----------|------|-----------|
| 1 | Imprimibilidade FDM doméstico (sem suporte excessivo, sem material exótico) | 25% | Gargalo real: impressora FDM do lab; material PETG + TPU |
| 2 | Robustez estrutural / documentação de carga | 20% | Precisamos argumentar que a base foi pensada para carga real |
| 3 | Facilidade de remix / edição CAD (formato, licença de derivação) | 25% | Temos ~8 dias de janela de CAD; partir de base editável já no Fusion/FreeCAD/STEP |
| 4 | Aderência ao mecanismo single-axis (dorsi/plantarflexão com eixo) | 20% | Decisão travada no README; base que já tem isso economiza o maior trabalho de CAD |
| 5 | Licença (permite uso acadêmico, derivação, publicação) | 10% | Portfólio público no GitHub — licença restritiva é bloqueante |

Pontuação: 1 (mínimo) a 5 (máximo) por critério. Score ponderado = Σ(peso × nota).

---

## Pontuação detalhada

### A — Make3D / Printables 293133

| Critério | Nota | Justificativa |
|----------|------|---------------|
| Imprimibilidade FDM | 4 | STL pronto para fatiar; usa Filaflex40 (flexível, exige bowden direto) + mola comprada — a mola é a única peça não-FDM; substitutível por TPU |
| Robustez estrutural | 3 | Feito em Fusion 360, tem geometria de keel com pino. Sem teste de carga documentado ("não testado" per README). Estrutura visible nas fotos parece sólida. |
| Remix / edição CAD | 5 | Modelado em Fusion 360 → STEP/F3D exportável; geometria paramétrica editável; maior comunidade de remix |
| Single-axis | 5 | **Match direto**: pino + mola/Filaflex; conector de pylon padrão já incluído. Troca Filaflex → TPU é o único ajuste de concepção |
| Licença | 4 | Printables usa CC BY-NC-SA por padrão salvo indicação contrária; uso acadêmico e portfólio não-comercial = OK |
| **Score ponderado** | **4,2** | |

### B — Appropedia

| Critério | Nota | Justificativa |
|----------|------|---------------|
| Imprimibilidade FDM | 3 | Open-source "real" mas documentação de impressão escassa; geometria snap-fit + ball-joint pode ser problemática em FDM sem ajuste de tolerância |
| Robustez estrutural | 2 | Explicitamente descrito como em "estágio infância" com pouca validação. Custo baixo é o forte, não a engenharia demonstrada |
| Remix / edição CAD | 3 | Arquivos disponíveis mas em formato menos maduro; comunidade menor; menos referências de remix |
| Single-axis | 2 | Mecanismo ball-joint / snap-fit ≠ single-axis; exigiria reformulação do mecanismo de articulação — trabalho de CAD elevado |
| Licença | 5 | Licença aberta (CC BY-SA ou equivalente); sem restrição comercial |
| **Score ponderado** | **2,85** | |

### C — Colorado School of Mines Capstone

| Critério | Nota | Justificativa |
|----------|------|---------------|
| Imprimibilidade FDM | 3 | Pensado para ABS / PETG-nylon em impressora de engenharia; manual de instruções existente; suportes necessários moderados |
| Robustez estrutural | 4 | Projeto capstone de engenharia com cálculo de carga; documentação mais rigorosa; pensado para PETG/nylon |
| Remix / edição CAD | 3 | Arquivos CAD disponíveis via repositório capstone; formato depende do time (SolidWorks/STEP provável); comunidade menor que Printables |
| Single-axis | 3 | Flex-ankle por dobradiça flexível, não eixo rígido. É articulado, mas o mecanismo é diferente — adaptar para single-axis com pino M8 exige redesign da região do tornozelo |
| Licença | 3 | Capstone acadêmico — geralmente CC ou domínio público para uso acadêmico; mas verificar antes de publicar remix |
| **Score ponderado** | **3,2** | |

---

## Resumo comparativo

| | A — Make3D | B — Appropedia | C — Mines |
|---|---|---|---|
| Score ponderado | **4,2** | 2,85 | 3,2 |
| Maior força | Match single-axis + CAD editável | Licença aberta | Rigor de engenharia |
| Maior fraco | Sem teste de carga documentado | Mecanismo errado + validação mínima | Pediátrico; dobradiça ≠ eixo rígido |

---

## Recomendação fundamentada (veredito a confirmar pelo João)

**Remixar o Make3D (Printables 293133).**

Razão principal: é o único dos três que já tem o mecanismo single-axis com pino — a decisão mais difícil de CAD — implementado. A edição necessária é cirúrgica: trocar o Filaflex/mola por batentes TPU impressos e redimensionar a seção do keel conforme `testes/dimensionamento.py`. O CAD editável em Fusion 360 e a comunidade Printables reduzem o risco de bloquear o cronograma no CAD.

**O que aproveitar do Make3D:**
- Geometria geral do keel (forma do antepé e calcanhar)
- Mecanismo de articulação (furo + flange para pino M8)
- Conector de pylon (pirâmide 30 mm) — já compatível com adaptadores padrão

**O que alterar:**
- Substituir Filaflex/mola → **batentes TPU em dois pinos ou rampas** (dorsal e plantar) impressos no próprio corpo ou como peça separada
- Verificar e ajustar espessura de parede do keel conforme t_min calculado (~4,6 mm para PETG, FS 2,5) — após medir B, H, L reais no STL
- Reescalar para pé 26–27 cm se necessário (pé adulto BR 40–41)
- Adicionar bucha no furo do eixo (espaçador metálico ou de nylon impresso em PETG/PA)

**Alternativa de fallback:** se o STL/CAD do Make3D não for acessível ou imprimível no lab, usar Mines como base de keel (rigor estrutural) e reimplementar o eixo rígido M8 no lugar da dobradiça flexível.

---

> *Data: 06/06/2026 — gerado pela MINERVA como suporte de decisão para Missão 1.*
> *Não é decisão autônoma: o João confirma (ou reverte) o veredito e registra no README.*
