# Votação - Design-base da Prótese

**Projeto:** Prótese funcional pé-tornozelo articulada, single-axis, 3D FDM, baixo custo
**Disciplina:** Dispositivos de Reabilitação - FUMEC - Entrega: 22/06/2026
**Decisão necessária:** qual design remixar como base estrutural

> Votar até: definir com o grupo. Após votação, registrar no README e baixar os arquivos.

---

## Contexto do projeto

| Item | Definição |
|------|-----------|
| Tipo de dispositivo | Prótese transtibial de pé-tornozelo (substitui segmento ausente) |
| Mecanismo | Single-axis: 1 eixo de rotação, dorsi/plantarflexão com batentes elásticos |
| Usuário de projeto | Adulto ~70 kg, pé 26-27 cm (BR 40-41), marcha em superfície plana |
| Carga de projeto | 1.030 N (1,5 × peso corporal - pico do heel-strike) |
| Fator de segurança | 2,5 |
| Material definido | PETG (estrutura) + TPU 95A (batentes) + parafuso M8 aço (eixo) |
| Custo-alvo | < R$ 200 em material |
| Abordagem | Remixar design open-source existente - não partir do zero |
| Impressão | Terceirizada - enviar STLs + especificações até 13/06 |

---

## Opção A - Make3D Prosthetic Foot Prototype
**Link:** https://www.printables.com/model/293133-prosthetic-foot-prototype
**Score técnico:** 4,2 / 5,0

### O que é
Prótese de pé transtibial com articulação de tornozelo, dedos flexíveis e conector de pylon padrão. Desenvolvida pela Make3D em Fusion 360, disponível em STL e STEP/F3D exportável. Projeto com maior comunidade de remix no Printables.

### Articulação
Single-axis com pino metálico + mola (ou Filaflex40). A mola/Filaflex será substituída por batentes de TPU impressos - única adaptação de concepção necessária.

### Materiais (original / nosso remix)

| Peça | Original | Remix proposto |
|------|----------|----------------|
| Keel / estrutura | PLA ou PETG | PETG (infill ≥ 40%, paredes ≥ 3) |
| Dedos / antepé flexível | Filaflex 40A | TPU 95A |
| Batentes dorsi/plantar | Mola metálica comprada | TPU 95A impresso |
| Eixo da articulação | Parafuso | Parafuso M8 aço 8.8 + bucha nylon |
| Conector de pylon | Integrado ao design | Manter (pirâmide 30 mm padrão) |

### Custo estimado (remix)

| Item | Qtd | Custo estimado |
|------|-----|----------------|
| PETG 1kg (Polymaker, Bambu etc.) | ~200-250g | R$ 25-35 |
| TPU 95A 1kg | ~50-80g | R$ 10-15 |
| Parafuso M8 × 60mm aço 8.8 | 1 | R$ 3-5 |
| Porca M8 + arruelas | 2-4 | R$ 2-4 |
| Bucha nylon M8 | 1 | R$ 3-5 |
| **Total estimado** | | **R$ 43-64** |

*Comparativo: prótese comercial equivalente = US$ 5.000-50.000 (R$ 25.000-250.000)*

### Prós
- Maior score técnico (4,2/5)
- Match direto com single-axis - menor trabalho de CAD
- CAD editável em Fusion 360 (STEP/F3D exportável)
- Conector de pylon padrão já integrado
- Maior comunidade de remix e referências

### Contras
- Sem teste de carga documentado pelo autor
- Filaflex40 original exige troca por TPU (simples, mas é alteração)
- Verificar escala para pé 26-27 cm

---

## Opção D - Prosthetic Foot-Ankle for 3D Printing
**Link:** https://www.printables.com/model/1032352-prosthetic_foot-ankle-for-3d-printing
**Score técnico:** 3,65 / 5,0

### O que é
Prótese de pé-tornozelo projetada para ser acessível, simples de produzir e resistente a água/poeira. Material nativo já é PETG + TPU - alinhamento direto com as decisões do projeto. Testada pelo autor.

### Articulação
Articulação de tornozelo com movimento similar ao humano + flexão em calcanhar e dedos. Mecanismo próximo do single-axis; confirmar se usa eixo rígido ou dobradiça flexível após baixar o CAD.

### Materiais (original / nosso remix)

| Peça | Original | Remix proposto |
|------|----------|----------------|
| Keel / estrutura | PETG | PETG (manter - já alinhado) |
| Tendões / flexão | TPU 65A | TPU 95A (ajuste de dureza) |
| Batentes dorsi/plantar | TPU (integrado) | TPU 95A impresso (manter conceito) |
| Eixo da articulação | A confirmar | Parafuso M8 aço 8.8 + bucha nylon |
| Conector de pylon | A confirmar | Adaptar ao projeto |

### Custo estimado (remix)

| Item | Qtd | Custo estimado |
|------|-----|----------------|
| PETG 1kg | ~200-250g | R$ 25-35 |
| TPU 95A 1kg | ~80-100g | R$ 15-20 |
| Parafuso M8 + porca + arruelas | - | R$ 5-9 |
| Bucha nylon M8 | 1 | R$ 3-5 |
| **Total estimado** | | **R$ 48-69** |

*Comparativo: prótese comercial equivalente = US$ 5.000-50.000 (R$ 25.000-250.000)*

### Prós
- PETG + TPU nativos - zero troca de material
- Testada pelo autor em condições reais
- Resistente a água e poeira (durabilidade)
- Simples de produzir e repor peças

### Contras
- Score menor (3,65/5) principalmente por incerteza no formato CAD
- Formato editável (STEP/F3D) a confirmar antes de baixar
- Mecanismo de articulação a detalhar - pode exigir mais adaptação

---

## Opção B - Appropedia (plano B)
**Link:** https://www.appropedia.org/3D_printed_prosthetic_foot
**Score técnico:** 2,85 / 5,0
**Status: página instável - usar só se A e D forem inviáveis**

### O que é
Design open-source OSAT (appropriate technology) de código aberto completo. Articulação snap-fit com amortecedor ball-joint. Custo muito baixo (~4% do comercial). Projeto em estágio inicial conforme documentação.

### Articulação
Snap-fit + ball-joint (amortecedor). Mecanismo diferente do single-axis definido - exigiria redesign completo da região do tornozelo para adaptar ao eixo M8.

### Materiais

| Peça | Material |
|------|----------|
| Pé + perna | PLA ou PETG |
| Articulação | Snap-fit impresso |
| Amortecedor | Ball-joint impresso |

### Custo estimado

| Item | Custo estimado |
|------|----------------|
| PETG ~200g | R$ 25-30 |
| Hardware mínimo | R$ 5-10 |
| **Total estimado** | **R$ 30-40** |

### Prós
- Licença mais aberta (CC BY-SA, sem restrição comercial)
- Menor custo de material
- Filosofia open-source mais pura

### Contras
- Página instável - arquivos podem não estar acessíveis
- Mecanismo ball-joint ≠ single-axis - exige redesign completo
- Documentado pelo próprio autor como "estágio infância"
- Menor validação estrutural
- Score mais baixo nos critérios do projeto

---

## Comparativo final

| Critério | A - Make3D #293133 | D - #1032352 | B - Appropedia |
|----------|-------------------|--------------|----------------|
| Score técnico | **4,2** | 3,65 | 2,85 |
| Custo estimado | R$ 43-64 | R$ 48-69 | R$ 30-40 |
| Material estrutura | PETG | PETG | PETG/PLA |
| Material batentes | TPU (trocar Filaflex) | TPU nativo | Impresso rígido |
| Articulação | Single-axis direto | Próximo - confirmar | Ball-joint (redesign) |
| CAD editável | ✅ Fusion 360 / STEP | ⚠ confirmar | ⚠ formato incerto |
| Testado | Não (pelo autor) | Sim | Não |
| Página acessível | ✅ | ✅ | ⚠ instável |
| Trabalho de remix | Baixo | Médio | Alto |

---

## Como votar

Responder com:
- **Voto:** A / D / B / A+D (combinar elementos dos dois)
- **Razão:** 1-2 linhas

> Recomendação técnica: **A como base principal** (score 4,2, single-axis direto, CAD editável)
> com elementos de D se o CAD for editável (material nativo PETG+TPU sem troca).
