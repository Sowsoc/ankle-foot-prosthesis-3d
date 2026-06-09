# Matriz de decisão - design-base para remix

> Decisão do grupo (06/06/2026): dois candidatos principais + plano B.

---

## Candidatos

| ID | Projeto | Link | Papel |
|----|---------|------|-------|
| A | Make3D - Prosthetic Foot Prototype | [Printables #293133](https://www.printables.com/model/293133-prosthetic-foot-prototype) | ✅ Principal |
| D | Prosthetic Foot-Ankle for 3D Printing | [Printables #1032352](https://www.printables.com/model/1032352-prosthetic_foot-ankle-for-3d-printing) | ✅ Principal |
| B | Appropedia - 3D printed prosthetic foot | [Appropedia](https://www.appropedia.org/3D_printed_prosthetic_foot) | ⚠ Plano B (página instável) |

---

## Critérios e pesos

| # | Critério | Peso |
|---|----------|------|
| 1 | Imprimibilidade FDM (sem material exótico, sem suporte excessivo) | 25% |
| 2 | Robustez estrutural / documentação de carga | 20% |
| 3 | Facilidade de remix / edição CAD (formato editável, licença) | 25% |
| 4 | Aderência ao mecanismo single-axis (dorsi/plantarflexão com eixo) | 20% |
| 5 | Licença (uso acadêmico, derivação, publicação) | 10% |

Pontuação: 1 (mínimo) a 5 (máximo). Score = Σ(peso × nota).

---

## Pontuação detalhada

### A - Make3D / Printables #293133

| Critério | Nota | Justificativa |
|----------|------|---------------|
| Imprimibilidade FDM | 4 | STL pronto; Filaflex40 substituível por TPU; mola substituível por batente impresso |
| Robustez estrutural | 3 | Geometria de keel com pino em Fusion 360; sem teste de carga documentado |
| Remix / edição CAD | 5 | Fusion 360, STEP/F3D exportável, maior comunidade de remix |
| Single-axis | 5 | Match direto: pino + articulação; conector de pylon padrão já incluído |
| Licença | 4 | CC BY-NC-SA Printables; uso acadêmico OK |
| **Score ponderado** | **4,2** | |

**O que aproveitar:** geometria do keel, mecanismo de articulação (furo + flange para M8), conector de pylon.
**O que alterar:** Filaflex/mola → batentes TPU impressos; ajustar espessura de parede conforme dimensionamento.py; reescalar para pé 26-27 cm se necessário.

### D - Printables #1032352

| Critério | Nota | Justificativa |
|----------|------|---------------|
| Imprimibilidade FDM | 4 | PETG + TPU 65A nativos; sem material exótico; partes de reposição rápidas |
| Robustez estrutural | 3 | Testado pelo autor; resistente a água/poeira; sem documentação de carga formal |
| Remix / edição CAD | 3 | Disponível no Printables; formato CAD editável a confirmar antes de baixar |
| Single-axis | 4 | Articulação de tornozelo funcional + flexão em calcanhar e dedos; próximo do single-axis |
| Licença | 4 | CC BY-NC-SA Printables; uso acadêmico OK |
| **Score ponderado** | **3,65** | |

**O que aproveitar:** material nativo PETG+TPU já alinhado; articulação de tornozelo funcional; simplicidade de fabricação.
**O que alterar:** confirmar/ajustar mecanismo para single-axis puro com eixo M8; verificar formato CAD editável.

### B - Appropedia (plano B)

| Critério | Nota | Justificativa |
|----------|------|---------------|
| Imprimibilidade FDM | 3 | Snap-fit + ball-joint pode ser problemático em FDM sem ajuste de tolerância |
| Robustez estrutural | 2 | "Estágio infância" per documentação; pouca validação |
| Remix / edição CAD | 3 | Arquivos disponíveis mas formato menos maduro |
| Single-axis | 2 | Ball-joint ≠ single-axis; exige reformulação do mecanismo |
| Licença | 5 | CC BY-SA; sem restrição comercial |
| **Score ponderado** | **2,85** | |

Usar só se A e D forem inviáveis. Exige redesign do mecanismo de articulação.

---

## Resumo comparativo

| | A - Make3D #293133 | D - #1032352 | B - Appropedia |
|---|---|---|---|
| Score ponderado | **4,2** | 3,65 | 2,85 |
| Papel | Principal | Principal | Plano B |
| Maior força | Single-axis + CAD editável | PETG+TPU nativo | Licença aberta |
| Maior fraco | Sem teste de carga | Formato CAD incerto | Página instável + mecanismo diferente |

---

## Próximos passos

1. Baixar STL + STEP/F3D de A e D para `cad/`
2. Abrir ambos no FreeCAD/Fusion e comparar geometria do tornozelo
3. Escolher qual serve de base principal para o remix (ou combinar elementos dos dois)
4. Medir B, H, L do keel no design escolhido e rodar `testes/dimensionamento.py` com valores reais

---

> *Decisão registrada em 06/06/2026.*

---

## ✅ VEREDITO (08/06/2026)

**Vencedor: A — Make3D / Printables #293133.** Decidido por votação do grupo.
Razão: maior score (4,2), articulação single-axis direta e conector de pylon já
integrado — menor trabalho de CAD no prazo apertado.

**Status pós-download:**
- STLs baixados e versionados em `cad/A_make3d_293133/` (InnerFoot, FootRubber, TopJoint, Insert, RubberCube) + PDF em `refs/A_make3d_293133/`.
- Keel estrutural = `InnerFoot.stl`. Seção crítica medida (B=43, H=37, L=55 mm) → `dimensionamento.py` re-rodado: **PETG t_parede ≈ 4,3 mm** com FS 2,5.
- ⚠ **Ressalvas a tratar no CAD:** (1) pacote de A **não traz STEP/F3D** — só STL; remix exige edição de malha (Blender) ou baixar o F3D no Printables. (2) **Escala:** pé do modelo ~21 cm < alvo 26–27 cm → escalar ~1,26× (favorável à estrutura).
