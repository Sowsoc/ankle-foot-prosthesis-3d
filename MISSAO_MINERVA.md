# Missões para a MINERVA — Prótese pé-tornozelo

> A MINERVA abre limpa (sem memória). Cada missão é autossuficiente: ela lê os arquivos
> do projeto antes de agir. Régua do modo: tudo defensável numa sabatina. João é dono das
> decisões difíceis; a MINERVA fundamenta, calcula, escreve e versiona.

---

## MISSÃO 1 — Fundação técnica (rodar AGORA, em paralelo ao CAD do João)

**Contexto obrigatório (leia antes de tudo):**
- `~/biomed-lab/protese-tornozelo/README.md` (decisões, requisitos, régua, candidatos, riscos)
- `~/biomed-lab/protese-tornozelo/RELATORIO.md` (esqueleto a preencher)
- `~/biomed-lab/protese-tornozelo/PLANO.md` (cronograma)
- `~/biomed-lab/protese-tornozelo/refs/FONTES.md` (links dos designs e papers)

**Decisões já travadas (não reabrir):** remix open-source, articulação single-axis, alvo
adulto padrão (~70 kg, pé 26–27 cm), carga de projeto 1,5×BW ≈ 1030 N, fator de segurança 2–3.

**Entregáveis (ponta a ponta, e commitar+push ao final):**

1. **Requisitos de engenharia finalizados** — fechar a tabela de requisitos com valores
   justificados (cada número com 1 linha de razão). Atualiza a seção 3 do `RELATORIO.md`.

2. **Fundamentação biomecânica** — ciclo da marcha e papel do tornozelo, ADM fisiológica
   (dorsi ~10°, plantar ~20°), cargas de pico no heel-strike. Com fontes citadas (use as de
   `refs/FONTES.md` + busque o que faltar). Vira a seção 2 do `RELATORIO.md`.

3. **Matriz de decisão dos 3 design-base** (Make3D/Printables, Appropedia, Colorado Mines) —
   critérios: imprimibilidade FDM, robustez estrutural, facilidade de remix/edição, aderência
   ao single-axis, licença. Pontue, recomende **qual remixar** e liste o que aproveitar e o que
   mudar. **NÃO decida sozinha o veredito final** — entregue a recomendação fundamentada para
   o João bater o martelo. Salva em `refs/decisao_design_base.md`.

4. **Dimensionamento estrutural preliminar** — script Python reproduzível em
   `testes/dimensionamento.py` que:
   - calcula a tensão na seção crítica do keel sob 1030 N com FS 2–3;
   - aplica derating de resistência do FDM no eixo Z (adesão entre camadas ~50% da resistência
     no plano) — esse ponto é central, deixe explícito;
   - compara **PETG vs PLA-CF** e recomenda o material;
   - recomenda espessura de parede, nº de paredes e infill mínimos justificados;
   - dimensiona o eixo M8 da articulação ao cisalhamento;
   - gera gráfico(s) (ex: tensão vs espessura de parede).
   Resultados + justificativa preenchem a seção 5 do `RELATORIO.md`.

**Restrições:**
- Não inventar dados. Cite fonte de cada número de material/biomecânica.
- O dimensionamento é **preliminar/paramétrico** — marque claramente o que precisa ser
  refinado com as dimensões reais do STL depois que o design-base for escolhido e baixado.
- Explique cada decisão-chave em 1–2 linhas (régua da sabatina).
- Ao final: `git add` + `commit` + `push` no repo `biomed-lab`.

**Prompt de disparo (colar na MINERVA):**
> Leia `~/biomed-lab/protese-tornozelo/MISSAO_MINERVA.md` e execute a Missão 1 inteira,
> ponta a ponta, commitando ao final.

---

## MISSÃO 1.5 — Levantamento da articulação + escala (rodar AGORA, antes do CAD)

**Contexto:** design-base TRAVADO = **A, Make3D / Printables #293133**. STLs já no repo em
`cad/A_make3d_293133/` (InnerFoot = keel; TopJoint = junta superior; RubberCube = batente;
Insert; FootRubber = sola). Dimensionamento já re-rodado com geometria medida (B=43, H=37,
L=55 → PETG t≈4,3 mm). Esta missão NÃO é o CAD (isso é do João) — é a medição que alimenta o CAD.

**Entregáveis (medir na malha, não chutar; commitar+push ao final):**

1. **Geometria da articulação single-axis** — medir nos STLs e documentar em
   `cad/A_make3d_293133/MEDIDAS_ARTICULACAO.md`:
   - localização e diâmetro do furo/eixo nativo na junta (TopJoint × InnerFoot) — confirmar se já é ~M8 ou precisa rebaixar/abrir;
   - dimensões do bolso/encaixe do batente (RubberCube) — base p/ trocar por TPU 95A;
   - interface do conector de pylon (Insert) — diâmetro/altura, comparar com pirâmide 30 mm padrão;
   - distância entre faces da junta (folga p/ bucha nylon no furo).
   Usar parse direto da malha binária (numpy) ou trimesh; **não inventar cota**.

2. **Análise de escala ×1,26 (pé ~21 → 26–27 cm)** — tabela peça-por-peça do que muda
   ao escalar: comprimento do pé, seção do keel, diâmetro do furo (⚠ escalar a malha
   escala o furo p/ ~10 mm → decidir se mantém M8 e re-fura, ou usa M10), bolso do batente,
   massa/filamento estimados. Recomendar: escalar a malha inteira OU escalar só o casco e
   manter ferragem M8. Salvar em `cad/A_make3d_293133/MEDIDAS_ARTICULACAO.md` (mesma nota).

3. **Caça ao CAD editável** — verificar se o F3D/STEP de #293133 existe no Printables
   (o ZIP baixado só trouxe STL). Se sim, anotar link/instrução em `refs/FONTES.md`; se não,
   registrar que o remix será por edição de malha (Blender) e qual o caminho mínimo.

**Restrições:** cada cota com origem (qual STL, como medida). Marcar o que for estimativa.
Régua da sabatina: defensável. Ao final: `git add` + `commit` + `push` no `biomed-lab`.

**Prompt de disparo (colar na MINERVA):**
> Leia `~/biomed-lab/protese-tornozelo/MISSAO_MINERVA.md` e execute a Missão 1.5 inteira,
> ponta a ponta, commitando ao final.

---

## MISSÃO 2 — Análise dos dados de validação (depois dos testes físicos)
*(a detalhar quando houver dados de ADM e carga)*

## MISSÃO 3 — Relatório técnico completo (fase final)
*(a detalhar quando o produto estiver validado)*
