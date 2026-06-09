# Levantamento da articulação + escala — design-base A (Make3D / Printables #293133)

> **Missão 1.5** — medição que alimenta o CAD do João (o CAD em si é dele).
> Tudo aqui foi **medido nos STLs nativos**, não chutado. Script reprodutível:
> [`medir_articulacao.py`](medir_articulacao.py) (trimesh + numpy). Figura:
> [`medidas_articulacao.png`](medidas_articulacao.png).
> Régua da sabatina: cada cota tem origem (qual STL, como foi medida).

## Como foi medido (defensável)

- As 5 peças (`InnerFoot`, `TopJoint`, `RubberCube`, `Insert`, `FootRubber`) estão num
  **mesmo referencial de montagem**, porém **explodidas em Z** (cada peça erguida no eixo
  vertical para visualização / mesa de impressão). Prova: o furo do pino e o bore do pino
  têm o **mesmo X** (ΔX = 0,18 mm) — eixo de pivô compartilhado; só o Z difere.
- **Eixos do STL:** `X` = ântero-posterior (calcanhar X<0, dedos X>0) · `Y` = médio-lateral
  = **eixo do pino** (dorsi/plantarflexão gira em torno de Y) · `Z` = vertical.
- **Furos/bores:** secção planar (`mesh.section`) perpendicular ao eixo do furo + ajuste de
  círculo por mínimos quadrados. Qualidade `res = σ_raio / raio_médio`; `res < 0,05` = círculo
  real. Diâmetros varridos em dezenas de secções e medianados.

---

## 1. Geometria da articulação single-axis

| Cota | Valor medido | Origem / como | `res` |
|---|---|---|---|
| **Furo do pino — InnerFoot (keel)** | **Ø 4,77 mm** | `InnerFoot.stl`, secção ⟂Y, mediana de 48 secções | 0,006 |
| Centro do furo (global) | X = −6,20 · Z = 63,50 mm | idem | — |
| Comprimento do furo (largura do knuckle) | 19,0 mm (Y 118,5→137,5) | extensão em Y onde o furo existe | — |
| Largura do bloco do tornozelo (InnerFoot) | 46,0 mm (em Y) | bbox da peça | — |
| **Bore do pino — TopJoint (junta superior)** | **Ø 10,06 mm** | `TopJoint.stl`, secção ⟂Y, mediana | 0,006 |
| Centro do bore (global) | X = −6,38 · Z = 90,50 mm | idem | — |
| Comprimento do bore | ~16 mm (Y 120→136) | extensão em Y do anel Ø10 | — |
| Parede mínima bore→exterior (TopJoint) | ≈ 5,0 mm | distância radial mín. ao contorno externo | — |
| **Coaxialidade do pivô** | **ΔX = 0,18 mm** | bore vs furo (mesmo eixo Y) | — |
| Offset de explosão (não é folga real) | ΔZ = 27,0 mm | peças erguidas em Z; montagem é coaxial | — |

### Veredito do pino — é ~M8? **NÃO.** Precisa normalizar.

O design nativo tem **dois diâmetros diferentes no mesmo eixo**: furo **Ø4,8** (≈ passagem
de **M5**) no InnerFoot e bore **Ø10,0** no TopJoint. Nenhum é M8. Para padronizar em **M8**
(coerente com o `testes/dimensionamento.py`, que dimensionou o eixo como M8 8.8):

1. **Abrir** o furo do InnerFoot de Ø4,8 → **Ø8,4** (folga de M8) e re-furar concêntrico.
2. **Aproveitar o bore Ø10 nativo do TopJoint** como assento de **bucha de nylon 10×8**
   (OD 10 / ID 8) — ela casa **exatamente** com o Ø10 medido. A bucha vira o mancal do M8
   e elimina folga plástico-contra-aço (bearing é o elo fraco da junta — ver
   [`../../testes/dimensionamento.py`](../../testes/dimensionamento.py)).
3. Parede de 5 mm ao redor do bore é suficiente para o assento da bucha sem fragilizar.

### Folga para bucha / anilha de nylon (faces da junta)

Bore (Ø10, 16 mm de comprimento) é mais largo que o furo (Ø4,8, knuckle de 19 mm): há
**degrau radial de ~2,6 mm/lado** e **~3 mm de folga axial** entre os comprimentos. Isso dá
espaço nativo para **anilhas/bucha de nylon (≈1–1,5 mm/lado)** entre as faces — reduz atrito
e desgaste do plástico na rotação. *(Cotas axiais a confirmar no CAD montado — as peças vêm
explodidas; ver caveat no fim.)*

---

## 2. Batente (RubberCube) e conector de pylon (Insert)

**RubberCube** — batente posterior (limita a plantarflexão; é a peça macia que define a ADM):
- Envelope **22,85 × 19,04 × 28,00 mm**, volume 9 610 mm³, preenchimento 0,79 da caixa
  (= **cunha sólida**, sem furos internos). *(`RubberCube.stl`, bbox + secções.)*
- **Trocar por TPU 95A com este mesmo envelope.** A dureza 95A é o que define a rigidez do
  batente e, com ela, a amplitude de movimento — é parâmetro de projeto, não cosmético.

**Insert** — conector proximal (interface com o pylon):
- Prisma externo **26,36 × 14,19 × 46,50 mm** (retangular, alto). *(`Insert.stl`, bbox.)*
- Cavidade interna ≈ **Ø11–12 mm**, mas **não é um bore cilíndrico contínuo** — são
  **dois recessos/soquetes** (em Z ≈ 62 mm e ≈ 94 mm), provavelmente para tubo + parafuso.
- **Não é a pirâmide ISO 30 mm** padrão de prótese: footprint 26×14 mm é retangular e menor
  que a base 30×30 de 4 furos. É **interface custom**. → decisão do João: manter o soquete
  simples (mais imprimível, suficiente para demonstração) ou adaptar a uma pirâmide 30 mm
  comercial (mais "real", porém depende de peça comprada).

---

## 3. Análise de escala ×1,26 (pé ~21 cm → 26–27 cm)

Pé nativo (`FootRubber.stl`, extensão em X) = **209,9 mm**. Alvo BR 40–41 = **265 mm** ⇒
**fator S = 1,262** (bate com o ×1,26 da missão).

**Regra geométrica** (escala uniforme da malha): comprimento ∝ S · seção ∝ S² · volume
(massa/filamento) ∝ S³. **Estrutural:** σ_flexão ∝ (P·L)/(B·H²) ∝ S/S³ = **1/S²** ⇒ escalar
**reduz** a tensão por **0,63×** — escala **ajuda** a estrutura (já antecipado no
`dimensionamento.py`; o caso nativo SCALE=1 é o pior caso de tensão).

| Peça / cota | Nativo | × S (1,262) | Observação |
|---|---:|---:|---|
| Comprimento do pé [mm] | 209,9 | 265,0 | alvo 26–27 cm ✔ |
| Furo pino InnerFoot Ø [mm] | 4,8 | **6,0** | ⚠ ainda ≠ M8 |
| Bore pino TopJoint Ø [mm] | 10,1 | **12,7** | ⚠ deixa de casar c/ bucha 10×8 |
| Recesso pylon Insert ≈Ø [mm] | 11,5 | 14,6 | interface cresce junto |
| Batente RubberCube vol [mm³] | 9 610 | 19 336 | filamento TPU **×2,01** |
| Keel InnerFoot vol [mm³] | 99 161 | 199 524 | filamento **×2,01** |
| Sola FootRubber vol [mm³] | 308 492 | 620 722 | filamento **×2,01** |

⚠ **Escalar a malha escala os furos.** O pino Ø4,8→Ø6,0 e o bore Ø10,1→Ø12,7 — **nenhum vira
M8**, e o bore escalado perde o casamento com a bucha de nylon 10×8 padrão. Ou seja: a
ferragem **tem de ser normalizada de qualquer modo**; escalar só piora o casamento com peça
de prateleira. E o filamento **~dobra** (×2,0).

### Recomendação (João bate o martelo)

**Escalar o casco e congelar a ferragem em M8** (em vez de escalar a malha inteira como bloco):

- **Escalar** uniformemente o **casco estrutural** (sola, keel, comprimento do pé) ×1,262 para
  chegar a 26–27 cm e ganhar o alívio estrutural de 0,63×.
- **NÃO escalar a interface da junta:** manter o assento do pino em **Ø10 nativo** (= bucha
  nylon 10×8) e abrir o furo do InnerFoot para **Ø8,4 (M8)**. Assim a **ferragem fica de
  prateleira** (parafuso M8 8.8 + bucha 10×8 + anilhas nylon), independente da escala.
- Motivo decisivo: o **Ø10 nativo já é a medida de uma bucha comercial** — escalar joga essa
  vantagem fora. Custo de manter a junta sem escala: revisar o encaixe local junta⇄casco no
  CAD para os dois casarem (edição local, não global).

*Alternativa (escalar tudo ×1,26):* mais simples no slicer e melhora a estrutura, mas obriga
bucha/eixo de medida não-padrão (Ø12,7 / re-furo Ø8,4 em furo Ø6,0). Defensável só se a
disponibilidade de ferragem custom não for problema.

---

## 4. Caça ao CAD editável (#293133)

- Página: <https://www.printables.com/model/293133-prosthetic-foot-prototype> — autor
  **Make3D Company Ltd**. A descrição diz que **“the design was made in Autodesk Fusion 360”**,
  mas **o `.f3d`/STEP nativo não está publicado para download** — os arquivos disponíveis são
  malha (o ZIP baixado trouxe só STL; a página lista arquivos no formato imprimível).
- **Conclusão:** não há CAD paramétrico oficial. O **remix será por edição de malha**.
  Caminho mínimo:
  1. **Blender** (grátis): importar STL → *Edit Mode* para o casco; **escalar ×1,262**
     (S/M/X·1.262) o conjunto do casco.
  2. Para o furo M8: *Boolean* com um cilindro Ø8,4 no eixo Y (centro X≈−6,2, Z do pivô) —
     re-furo concêntrico; e Boolean Ø10 mantido no TopJoint para a bucha.
  3. Batente: substituir o sólido do `RubberCube` por bloco TPU 95A do mesmo envelope.
  4. (Opcional) **Fusion 360 / FreeCAD**: *Mesh→BRep* só se for re-parametrizar de fato;
     para escalar + furar, o Blender resolve com menos atrito.
- Registrado também em [`../../refs/FONTES.md`](../../refs/FONTES.md).

---

## Caveats (refinar depois)

- Peças vêm **explodidas em Z** — folgas **axiais** da montagem (anilhas, encosto de faces)
  são estimadas pelos comprimentos; **confirmar no CAD montado** e na junta física.
- Cavidade do `Insert` é irregular (soquetes), não cilindro — Ø11–12 mm é aproximação do
  recesso, não um bore usinado.
- Dimensões viram definitivas **após** o casco escalado e o re-furo M8 no CAD do João; então
  re-rodar `medir_articulacao.py` na malha editada para validar as cotas finais.

> Reproduzir: `cd cad/A_make3d_293133 && python3 medir_articulacao.py`
> (requer `trimesh numpy scipy networkx shapely matplotlib`).
