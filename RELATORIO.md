# Relatório técnico — Prótese funcional de pé-tornozelo articulada (3D, baixo custo)

> Disciplina: Dispositivos de Reabilitação — FUMEC · Autor: João Vítor Silva Oliveira · Entrega: 22/06/2026
> Esqueleto. Cada seção lista o que precisa conter. `[ ]` = a preencher. As decisões de
> engenharia, o CAD e a validação são trabalho seu — este arquivo é o mapa, não o conteúdo.

## Resumo (abstract)
- [ ] 1 parágrafo: o que é, decisão single-axis, material, custo, principal resultado de validação.

## 1. Introdução
- [ ] Problema: custo/acesso de próteses de pé-tornozelo (citar faixa US$ 5k–50k).
- [ ] Objetivo do trabalho e escopo (protótipo demonstrativo, não clínico).
- [ ] Distinção prótese × órtese (você já domina isso do estudo de órteses) — deixar claro que é prótese.

## 2. Fundamentação biomecânica

### 2.1 Ciclo da marcha e papel do tornozelo

O ciclo da marcha divide-se em fase de apoio (stance, ~60% do ciclo) e fase de balanço (swing, ~40%). O tornozelo cumpre três funções biomecânicas críticas durante o apoio [PMC4994968]:

1. **Heel-strike / loading response (0–12% do ciclo):** ao toque do calcanhar, a GRF impõe carga de impacto. O tornozelo entra em plantarflexão rápida (~5–10°) enquanto os dorsiflexores (tibial anterior) desaceleram o pé. Este é o pico de carga estrutural sobre a prótese.

2. **Midstance (10–30%):** o corpo avança sobre o pé fixo; o tornozelo funciona como pivot. GRF vertical ≈ 1,0–1,2 × PC.

3. **Push-off / toe-off (40–60%):** plantarflexão ativa (~20°) pelo tríceps sural impulsiona o corpo para frente. Em prótese passiva, batentes elásticos (TPU) absorvem parte da energia de retorno.

### 2.2 Amplitude de movimento fisiológica na marcha

| Movimento | Valor fisiológico | Alvo do protótipo |
|---|---|---|
| Dorsiflexão | 10–15° [1] | 10–15° — batente anterior TPU |
| Plantarflexão | 15–20° [1] | 15–20° — batente posterior TPU |
| ADM total sagital na marcha | ~25–35° [1] | 25–35° |

[1] Síntese de: OrthoFixar — Ankle Range of Motion; Meloq Devices — Normal Ankle ROM; Biomechanics of the ankle — PMC4994968.

### 2.3 Por que articular: SACH vs. single-axis

A prótese SACH (solid-ankle cushion-heel) é o baseline não-articulado mais difundido — baixo custo, zero manutenção, mas sem mobilidade real de tornozelo:

| Critério | SACH | Single-axis (este projeto) |
|---|---|---|
| ADM | 0° (rígida) | 10–15° dorsi / 15–20° plantar |
| Absorção de choque | calcanhar em espuma | batente TPU dorsal absorve heel-strike |
| Adaptação a terreno | limitada | parcial — ADM absorve variação de inclinação |
| Custo / complexidade | mínimos | baixo — eixo M8 + batentes TPU |

A articulação single-axis é a escolha mínima viável que confere mobilidade real sem a complexidade de sistemas multi-eixo ou ESAR (energy-storing-and-return em carbono), inviáveis no prazo e custo deste projeto.

### 2.4 Cargas na seção crítica (heel-strike)

GRF vertical de pico na marcha normal: **1,0–1,5 × PC** [Nilsson & Thorstensson, Acta Physiol Scand 1989, PMID 2782094]. Para o usuário de projeto (70 kg):

- **Carga de projeto: P = 1,5 × 70 × 9,81 ≈ 1030 N** (extremo conservador da marcha plana)
- Referência de sanidade: FEA de pé protético acha tensão máx. ~15 MPa no heel-strike a 150% PC [ResearchGate 318989655] — mesma ordem do dimensionamento preliminar (ver seção 5).
- Escopo: marcha em superfície plana. Corrida (pico 2,0–2,9 × PC) está fora do escopo deste protótipo acadêmico.

## 3. Requisitos de projeto

**Usuário de projeto:** adulto genérico, ~70 kg, pé 26–27 cm (BR 40–41), marcha em superfície plana.

| Requisito | Valor alvo | Justificativa |
|---|---|---|
| Carga estática de projeto | ≥ 1030 N (= 1,5 × BW) | GRF de pico na marcha normal é 1,0–1,5 × BW [Nilsson & Thorstensson, PMID 2782094]; extremo superior = conservador |
| Fator de segurança | 2–3 (FS = 2,5 adotado) | Faixa padrão para dispositivos com carga dinâmica e fabricação FDM (variabilidade de processo elevada) |
| ADM dorsiflexão | 10–15° | Mínimo para marcha eficiente sem compensação proximal [PMC4994968]; definida por batente TPU anterior |
| ADM plantarflexão | 15–20° | Necessário para push-off e descida [PMC4994968]; definida por batente TPU posterior |
| Conexão proximal | Adaptador pylon pirâmide 30 mm ou simplificado | Padrão ISO 22523; depende do design-base escolhido |
| Custo de material | < R$ 200 | PETG (~250 g × R$ 120/kg ≈ R$ 30) + TPU + M8 + bucha; comparar com SACH comercial (US$ 5k–50k) |
| Massa | minimizar (alvo informativo) | Trade-off com rigidez; aceito no escopo acadêmico |
| Material estrutural | PETG (keel) + TPU ~95A (batentes) + M8 aço 8.8 (eixo) | Justificativa completa em seção 5 e `testes/dimensionamento.py` |
| Orientação de impressão | Keel deitado (carga no plano XY) | Anisotropia Z do FDM reduz resistência 30–50% [OSTI 1808415]; orientar para máxima resistência no plano — ver seção 5 |

## 4. Concepção e projeto (design)

### 4.1 Estratégia: remix de design open-source

Dado o prazo de 16 dias e a régua de "produto funcional defensável", optou-se por **remixar um design open-source comprovado** em vez de modelar do zero. Partir de uma base existente e justificar cada alteração de engenharia é mais defensável — e mais honesto sobre o esforço real — do que reivindicar um projeto original mal validado.

O design-base foi selecionado por matriz de decisão ponderada (ver `refs/decisao_design_base.md`), com critérios de imprimibilidade FDM, robustez, facilidade de edição, aderência ao mecanismo single-axis e licença. Venceu o **Make3D "Prosthetic Foot Prototype"** (Printables #293133, licença CC BY-NC-SA), com score 4,2/5, por oferecer articulação single-axis direta, conector de pylon integrado e a maior comunidade de remix.

**Limitação assumida:** o autor publicou apenas malhas STL — não há arquivo CAD paramétrico (Fusion 360/STEP) oficial. A adaptação foi feita, portanto, por **edição de malha** (script reproduzível em `cad/A_make3d_293133/processar_pecas.py`, biblioteca `trimesh`), e não por modelagem paramétrica. Isso restringe o tipo de alteração possível (escala e operações booleanas, não re-parametrização de features), mas é suficiente para as três mudanças que o projeto exige.

### 4.2 Componentes do design-base e papéis

| Peça (STL nativo) | Papel | Material no remix |
|---|---|---|
| `InnerFoot` | Keel — quilha estrutural; carrega a flexão do heel-strike | PETG |
| `TopJoint` | Junta superior do tornozelo; aloja o eixo de pivô | PETG |
| `FootRubber` | Sola / antepé flexível | TPU 95A |
| `RubberCube` | Batente elástico (define a ADM e amortece) | TPU 95A |
| `Insert` | Conector proximal ao pylon | PETG |

> **Escopo:** este trabalho desenvolve o **módulo pé-tornozelo** de uma prótese **transtibial** modular. O encaixe (cartucho moldado ao coto, paciente-específico) e o pylon (tubo padronizado) são componentes *upstream* fora do escopo — representados apenas em diagrama. O `Insert` é a interface física com o pylon.

### 4.3 Alterações de engenharia (o que mudou e por quê)

Três modificações sobre o design-base, todas defensáveis:

**1. Escala ×1,262 do casco (pé ~21 cm → 26-27 cm).**
O modelo nativo tem pé de 209,9 mm (≈ BR 33), abaixo do usuário de projeto (adulto, pé 26-27 cm, BR 40-41). Aplicou-se escala uniforme de 1,262 às peças do casco (keel, sola, conector, batente). O `TopJoint` foi **mantido em escala nativa** (ver alteração 2). A escala, além de atender ao requisito dimensional, **reduz a tensão estrutural**: como σ_flexão ∝ (P·L)/(B·H²), escalar todas as dimensões por *s* faz σ variar com 1/*s²* — escalar para o alvo melhora a margem em ~37 % (ver seção 5 e `testes/dimensionamento.py`).

**2. Normalização do eixo da articulação para M8.**
O design nativo usa dois diâmetros distintos no mesmo eixo de pivô: furo Ø4,8 mm (≈ passagem de M5) no keel e bore Ø10,0 mm no `TopJoint`. Nenhum corresponde ao eixo M8 8.8 dimensionado na seção 5. A solução:
- **Keel:** furo aberto de Ø4,8 → **Ø8,4 mm** (folga de M8), via operação booleana concêntrica ao eixo nativo.
- **TopJoint mantido nativo:** o bore Ø10,0 mm casa **exatamente** com uma **bucha de nylon comercial 10×8** (OD 10 / ID 8). Manter o `TopJoint` sem escala preserva esse encaixe de prateleira — escalá-lo levaria o bore a Ø12,7 mm e exigiria ferragem fora de padrão. A bucha funciona como mancal do parafuso M8, eliminando o contato direto aço-plástico (o esmagamento do furo no plástico, *bearing*, é o elo estrutural mais fraco da junta — seção 5).

**3. Substituição dos elementos elásticos por TPU 95A impresso.**
O design original previa Filaflex/mola para os elementos compressíveis. No remix, o batente (`RubberCube`, envelope 22,85 × 19,04 × 28 mm) é reproduzido em **TPU 95A**, dispensando peça comprada. A dureza Shore 95A não é cosmética: é o parâmetro que define a rigidez do batente e, com ela, a amplitude de movimento — batente anterior limita a dorsiflexão (10-15°), posterior limita a plantarflexão (15-20°).

### 4.4 Mecanismo single-axis resultante

A articulação final é um **eixo único** (parafuso M8 classe 8.8) atravessando o keel (furo Ø8,4) e a junta superior, apoiado em bucha de nylon 10×8 no bore do `TopJoint`. O movimento de dorsi/plantarflexão ocorre em torno desse eixo no plano sagital; os batentes de TPU 95A definem os limites angulares e absorvem energia. É a escolha mínima viável que confere mobilidade real de tornozelo sem a complexidade de sistemas multi-eixo ou ESAR (energy-storing-and-return em carbono), inviáveis no prazo e custo (comparação SACH × single-axis na seção 2.3).

**Ferragem de montagem:** 1× parafuso M8 × 60 mm cl. 8.8 (eixo), 2× bucha nylon 10×8 (mancal), 1× porca M8 autotravante + arruelas de nylon (reduzem atrito entre faces).

### 4.5 Arquivos gerados

STLs finais nomeados por peça em `stl/` (`keel_petg`, `tornozelo_superior_petg`, `sola_tpu`, `conector_pylon_petg`, `batente_tpu`), parâmetros de fabricação em `slicing/ESPECIFICACOES_IMPRESSAO.md`, e preview em `stl/preview_pecas.png`. *(Renders/fotos finais do CAD a inserir aqui.)*

## 5. Materiais e fabricação

### 5.1 Material por componente

| Componente | Material | Justificativa |
|---|---|---|
| Keel / corpo estrutural | **PETG** (infill ≥ 50%, ≥ 4 perímetros) | Tenaz e dúctil: absorve impacto sem fratura frágil; melhor adesão entre camadas que PLA puro e PLA-CF sob carga cíclica; UTS impresso ~40–45 MPa no plano XY [MDPI Polymers 11(7):1220; PMC12694470] |
| Batentes dorsi/plantar | **TPU ~95A** | Define a ADM e absorve energia do heel-strike; imprimível por FDM; 95A = compromisso entre amortecimento e estabilidade |
| Eixo da articulação | **Parafuso M8 classe 8.8** | Aço, UTS 800 MPa, A_s = 36,6 mm², τ_adm = 480 MPa; o eixo é superdimensionado (FS real ≈ 34×) — o elo crítico é o **furo no plástico** (bearing), não o parafuso |
| Bucha do furo | Nylon ou bronze (recomendado) | Distribui tensão de bearing no furo; reduz desgaste em movimento cíclico |

**Por que PETG e não PLA-CF?**
PLA reforçado com fibra de carbono picada parece mais rígido (E ≈ 3 GPa vs 1 GPa do PETG), mas: (1) UTS impresso pode ser *menor* que PLA puro (~17–28 MPa vs ~40–45 MPa do PETG) pela fusão inter-filamento pior com fibra [Oxford Acad. MAM 29 S1:1447]; (2) a fibra agrava a anisotropia Z — Z pode cair 80–90% vs XY [OSTI 1808415]. PETG bem orientado com k_z = 0,50 entrega σ_adm ≈ 9 MPa; PLA-CF com k_z = 0,40 entrega 6,1 MPa, exigindo parede quase 2,5× mais grossa. PETG ganha em tenacidade, previsibilidade e imprimibilidade.

### 5.2 Parâmetros de impressão (recomendados)

| Parâmetro | Valor | Razão |
|---|---|---|
| **Orientação do keel** | **Deitado** (eixo longo horizontal) | Flexão solicita o plano XY — o mais resistente; imprimir vertical coloca carga no eixo Z (adesão entre camadas), 30–50% mais fraco [OSTI 1808415] |
| Perímetros | **≥ 4–6** (linha 0,4 mm → 1,6–2,4 mm) | Flexão é carregada pelas paredes externas, não pelo infill; mais perímetros = maior I da seção |
| Infill | **≥ 50%, padrão giroide** | Giroide é isotrópico, imprime sem suporte interno, resiste a cisalhamento; 100% só agrega massa sem ganho proporcional em flexão |
| Layer height | 0,2 mm | Melhor fusão interlaminar; balanço com tempo de impressão |
| Temperatura bico PETG | 230–240 °C | Limite superior da faixa melhora adesão Z [MDPI Polymers 11(7):1220] |
| Temperatura mesa | 70–80 °C | Previne warping em peças longas de PETG |
| Suportes | Mínimos; interface com gap 0,2 mm | Keel deitado minimiza necessidade; usar só na região do furo do eixo |

### 5.3 Dimensionamento estrutural preliminar

> Script reproduzível: `testes/dimensionamento.py` — gráficos em `testes/dimensionamento_flexao.png` e `testes/dimensionamento_materiais.png`.
> Geometria **medida** no STL do design-base A (Make3D #293133), keel = `InnerFoot.stl`.

**Parâmetros de entrada (medidos no STL de A):**
- Carga de projeto: P = 1030 N (1,5 × 70 kg × 9,81 m/s²)
- Seção crítica medida (região do tornozelo, ~55 mm do calcanhar): B = 43 mm, H = 37 mm
- Momento fletor na seção crítica: M = P × L = 1030 × 55 ≈ 56 700 N·mm (L = 55 mm medido)
- Modelo: viga em flexão, seção retangular oca (casca); infill desprezado (conservador — a favor da segurança)
- **Escala:** keel nativo do modelo (pé ~21 cm) é menor que o alvo 26–27 cm. Os cálculos usam a escala **nativa (pior caso)**; escalar ao alvo (×~1,26) só aumenta a margem (σ ∝ 1/escala², pois o módulo de seção cresce ∝ escala³ enquanto o braço cresce ∝ escala).

**Resultados (FS = 2,5):**

| Material | UTS_xy [MPa] | k_z [-] | σ_adm [MPa] | t_min casca [mm] |
|---|---|---|---|---|
| PETG | 45 | 0,50 | 9,0 | 4,3 |
| PLA-CF | 38 | 0,40 | 6,1 | 10,1 |

Sanity-check: tensão na seção sólida equivalente = 5,8 MPa — mesma ordem do FEA de literatura (~15 MPa @150% PC [ResearchGate 318989655]), com folga.

**Articulação — eixo M8 8.8 (junta dupla, 2 planos de cisalhamento):**
- τ atuante = 14,1 MPa → FS real do pino ≈ **34×** — superdimensionado, não é o elo fraco
- σ_bearing admissível no furo (PETG): 20,8 MPa → espessura mínima de material ao redor do furo ≈ **6,2 mm**
- **Elo crítico: esmagamento (bearing) do furo no plástico** → mitigar com bucha metálica e material generoso ao redor do eixo

**Recomendação consolidada:** PETG para keel (t_min 4,6 mm, tenacidade, anisotropia Z aceitável com orientação correta), TPU ~95A para batentes, M8 8.8 para eixo com bucha metálica obrigatória no furo.

### 5.4 Tempo e consumo de filamento

> A preencher com dados do slicer após CAD travado (etapa 15/06 — ver `PLANO.md`).

## 6. Validação / testes
- [ ] Teste de ADM: medir dorsi/plantarflexão real vs alvo (transferidor/foto).
- [ ] Teste de carga: aplicar carga conhecida, observar deformação/falha (qualitativo já vale).
- [ ] Registro fotográfico/vídeo (de `fotos/`).

## 7. Custo
- [ ] Planilha: filamento (g × R$/kg) + parafuso/bucha + TPU = total. Comparar com comercial.

## 8. Resultados e discussão
- [ ] O que funcionou, o que falhou, o que reimprimiria. Limitações (FDM, sem ciclagem de fadiga, etc.).

## 9. Conclusão
- [ ] Atingiu os requisitos? Trade-offs centrais. Próximos passos.

## Referências
- [ ] Ver `refs/FONTES.md` + livro-texto da disciplina. Formatar ABNT.
