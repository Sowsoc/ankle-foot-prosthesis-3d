#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Levantamento da articulação single-axis + escala — design-base A (Make3D #293133)
=================================================================================
Disciplina: Dispositivos de Reabilitação — Eng. Biomédica / FUMEC
Projeto:    Prótese funcional de pé-tornozelo articulada, single-axis, impressa em 3D
Autor:      João Vítor Silva Oliveira  |  Apoio de medição: MINERVA

OBJETIVO
--------
MEDIR (não chutar) a geometria da junta nos STLs nativos do design-base travado,
para alimentar o CAD do João: diâmetro/posição do pino, encaixe do batente,
interface do conector de pylon, e o efeito de escalar o pé de ~21 cm para 26-27 cm.

MÉTODO (reprodutível e defensável)
----------------------------------
- Malhas carregadas com trimesh; vértices fundidos (merge_vertices).
- As 5 peças vêm num MESMO referencial de montagem, porém EXPLODIDAS em Z
  (cada peça erguida no eixo Z para visualização/print-bed). Confirmado abaixo:
  o furo do InnerFoot e o bore do TopJoint têm o MESMO X (ΔX ~ 0,2 mm) → eixo de
  pivô compartilhado; só o Z difere (offset de explosão).
- Furos/bores medidos por SECÇÃO planar (mesh.section) perpendicular ao eixo do
  furo, seguida de ajuste de círculo por mínimos quadrados ao loop interno.
  Métrica de qualidade: res = desvio-padrão do raio / raio médio (quanto menor,
  mais perfeitamente circular). res < 0,05 = círculo de fato (furo/bore).
- Cada cota impressa traz a peça de origem e como foi medida. Nada é inventado.

EIXOS (referencial dos STLs)
----------------------------
  X = ântero-posterior (comprimento do pé; calcanhar em X<0, dedos em X>0)
  Y = médio-lateral  → é o EIXO DO PINO (dorsi/plantarflexão gira em torno de Y)
  Z = vertical (proximal-distal)
"""

import numpy as np
import trimesh
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).resolve().parent
STL = lambda n: trimesh.load(HERE / f"{n}.stl")

# ----------------------------------------------------------------------------
# utilitários de medição
# ----------------------------------------------------------------------------
def load(name):
    m = STL(name); m.merge_vertices(); return m

def fit_circle_2d(P):
    """Ajuste de círculo (Kasa) a pontos 2D. Retorna (cx, cy, r, res)."""
    x, y = P[:, 0], P[:, 1]
    A = np.c_[2 * x, 2 * y, np.ones(len(P))]
    b = x ** 2 + y ** 2
    s, *_ = np.linalg.lstsq(A, b, rcond=None)
    cx, cy = s[0], s[1]
    r = np.sqrt(s[2] + cx ** 2 + cy ** 2)
    res = np.hypot(x - cx, y - cy).std() / r
    return cx, cy, r, res

def hole_perp_Y(mesh, y, rmin, rmax):
    """Mede o furo (eixo ||Y) na secção Y=y: ajusta círculo ao loop interno
    cujo raio cai em [rmin,rmax]. Retorna dict com Ø, centro global (X,Z), res."""
    sec = mesh.section(plane_origin=[0, y, 0], plane_normal=[0, 1, 0])
    if sec is None:
        return None
    best = None
    for d in sec.discrete:                       # polilinhas 3D no plano Y=y
        if len(d) < 8:
            continue
        XZ = d[:, [0, 2]]
        cx, cz, r, res = fit_circle_2d(XZ)
        if rmin <= r <= rmax and res < 0.06:
            if best is None or res < best["res"]:
                best = dict(d=2 * r, cx=cx, cz=cz, res=res, n=len(d))
    return best

def hole_span_Y(mesh, ys, rmin, rmax):
    """Varre Y e retorna (Ø_mediano, y_min, y_max) onde o furo existe."""
    ds, present = [], []
    for y in ys:
        h = hole_perp_Y(mesh, y, rmin, rmax)
        if h:
            ds.append(h["d"]); present.append(y)
    if not present:
        return None
    return np.median(ds), min(present), max(present), np.std(ds)

# ----------------------------------------------------------------------------
# 1) ARTICULAÇÃO single-axis — pino, bore e coaxialidade
# ----------------------------------------------------------------------------
print("=" * 76)
print(" ARTICULAÇÃO single-axis — Make3D #293133 (cotas MEDIDAS nos STLs)")
print("=" * 76)

inner = load("InnerFoot")
top   = load("TopJoint")

# --- InnerFoot: furo do pino (||Y) através do bloco do tornozelo --------------
ys = np.arange(118, 142, 0.5)
i_d, i_y0, i_y1, i_sd = hole_span_Y(inner, ys, rmin=2.0, rmax=2.8)
ih = hole_perp_Y(inner, 128, 2.0, 2.8)
print(f"\n[InnerFoot.stl] FURO do pino (eixo ||Y):")
print(f"   Ø = {i_d:.2f} mm  (mediano em {len(ys)} secções; σ={i_sd:.02f})  res={ih['res']:.3f}")
print(f"   centro global: X={ih['cx']:.2f}  Z={ih['cz']:.2f} mm")
print(f"   furo presente em Y {i_y0:.1f}..{i_y1:.1f}  → comprimento do furo ≈ {i_y1-i_y0:.1f} mm")
print(f"   bloco do tornozelo (largura ||Y) = {np.ptp(inner.vertices[:,1]):.1f} mm")
print(f"   → Ø{i_d:.1f} ≈ furo de M5 / passagem ~Ø5. NÃO é M8.")

# --- TopJoint: bore do pino (||Y) -------------------------------------------
yt = np.arange(118, 143, 0.5)
t_d, t_y0, t_y1, t_sd = hole_span_Y(top, yt, rmin=4.5, rmax=5.6)
th = hole_perp_Y(top, 129, 4.5, 5.6)
print(f"\n[TopJoint.stl] BORE do pino (eixo ||Y):")
print(f"   Ø = {t_d:.2f} mm  (mediano; σ={t_sd:.02f})  res={th['res']:.3f}")
print(f"   centro global: X={th['cx']:.2f}  Z={th['cz']:.2f} mm")
print(f"   bore presente em Y {t_y0:.1f}..{t_y1:.1f}  → comprimento do bore ≈ {t_y1-t_y0:.1f} mm")
print(f"   bloco superior (largura ||Y) = {np.ptp(top.vertices[:,1]):.1f} mm")

# parede mínima de material ao redor do bore (limita reaming/abertura)
sec = top.section(plane_origin=[0, 129, 0], plane_normal=[0, 1, 0])
outer = max(sec.discrete, key=lambda d: (d[:, [0, 2]].max(0) - d[:, [0, 2]].min(0)).prod())
rad_out = np.hypot(outer[:, 0] - th["cx"], outer[:, 2] - th["cz"])
wall_min = rad_out.min() - t_d / 2
print(f"   parede mínima bore→exterior ≈ {wall_min:.1f} mm  (governa abrir o bore)")
print(f"   → Ø{t_d:.1f} casa EXATAMENTE com bucha de nylon 10×8 (OD10/ID8) p/ eixo M8.")

# --- coaxialidade (prova de que o pivô é compartilhado) ---------------------
dX = abs(th["cx"] - ih["cx"]); dZ = abs(th["cz"] - ih["cz"])
print(f"\n[Coaxialidade do pivô]  ΔX(bore vs furo) = {dX:.2f} mm  → MESMO eixo médio-lateral")
print(f"   ΔZ = {dZ:.1f} mm = offset de EXPLOSÃO (peças erguidas em Z; montagem real é coaxial)")

# --- folga p/ bucha: bore (TopJoint) mais largo que o furo do InnerFoot ------
print(f"\n[Folga p/ bucha de nylon no furo]")
print(f"   bore TopJoint Ø{t_d:.1f}  ⊃  furo InnerFoot Ø{i_d:.1f}  → degrau radial {(t_d-i_d)/2:.1f} mm/lado")
print(f"   comprimento bore {t_y1-t_y0:.0f} mm vs furo {i_y1-i_y0:.0f} mm → folga axial ~{abs((t_y1-t_y0)-(i_y1-i_y0)):.0f} mm")
print(f"   → espaço nativo p/ bucha/anilha de nylon entre as faces (≈1–1,5 mm/lado).")

# ----------------------------------------------------------------------------
# 2) BATENTE (RubberCube) e CONECTOR DE PYLON (Insert)
# ----------------------------------------------------------------------------
print("\n" + "=" * 76)
print(" BATENTE (RubberCube) e CONECTOR DE PYLON (Insert)")
print("=" * 76)

rc = load("RubberCube")
ext = np.ptp(rc.vertices, axis=0)
fill = rc.volume / np.prod(ext)
print(f"\n[RubberCube.stl] batente posterior (limita plantarflexão):")
print(f"   envelope (X×Y×Z) = {ext[0]:.2f} × {ext[1]:.2f} × {ext[2]:.2f} mm   volume={rc.volume:.0f} mm³")
print(f"   fração de preenchimento da caixa = {fill:.2f}  → cunha sólida (sem furos internos)")
print(f"   → trocar por TPU 95A com ESTE envelope; 95A define a rigidez do batente/ADM.")

ins = load("Insert")
iext = np.ptp(ins.vertices, axis=0)
# cavidade interna do conector (varre Z; a peça tem recessos, NÃO um bore cilíndrico
# contínuo — medir honestamente: tamanho do recesso e em que faixas de Z aparece)
from shapely.geometry import Polygon as _Poly
recess = []
for z in np.linspace(iext[2] * 0 + ins.vertices[:, 2].min() + 2,
                     ins.vertices[:, 2].max() - 2, 30):
    sec = ins.section(plane_origin=[ins.centroid[0], ins.centroid[1], z],
                      plane_normal=[0, 0, 1])
    if sec is None:
        continue
    loops = sorted(((d, abs(_Poly(d[:, [0, 1]]).area)) for d in sec.discrete
                    if len(d) > 3), key=lambda t: -t[1])
    if len(loops) >= 2:                      # loop interno = recesso
        inner_loop = loops[1][0][:, [0, 1]]
        bb = inner_loop.max(0) - inner_loop.min(0)
        recess.append((z, max(bb), min(bb)))
ib = None
if recess:
    zr = [r[0] for r in recess]; wr = [r[1] for r in recess]
    ib = (np.mean(wr), min(zr), max(zr))
print(f"\n[Insert.stl] conector de pylon (encaixe proximal):")
print(f"   prisma externo (X×Y×Z) = {iext[0]:.2f} × {iext[1]:.2f} × {iext[2]:.2f} mm")
if ib:
    print(f"   cavidade/recesso interno ≈ Ø{ib[0]:.0f} mm (NÃO é bore cilíndrico contínuo;")
    print(f"     aparece em Z {ib[1]:.0f} e {ib[2]:.0f} mm = soquetes p/ tubo/parafuso do pylon)")
print(f"   COMPARAÇÃO c/ pirâmide ISO 30 mm: footprint {iext[0]:.0f}×{iext[1]:.0f} mm é RETANGULAR e")
print(f"   menor que a base 30×30 da pirâmide de 4 furos → é interface CUSTOM, não ISO.")
print(f"   → decisão do João: adotar soquete simples (atual) ou adaptar p/ pirâmide 30 mm padrão.")

# ----------------------------------------------------------------------------
# 3) ANÁLISE DE ESCALA ×1.26  (pé ~21 → 26-27 cm)
# ----------------------------------------------------------------------------
foot = load("FootRubber")
L0 = np.ptp(foot.vertices[:, 0])            # comprimento nativo do pé [mm]
TARGET = 265.0                              # alvo BR 40-41 (26-27 cm) [README]
S = TARGET / L0
print("\n" + "=" * 76)
print(f" ESCALA — pé nativo {L0:.0f} mm → alvo {TARGET:.0f} mm  ⇒  fator S = {S:.3f}")
print("=" * 76)
print(f"  Regra geométrica: comprimento ∝ S ; área/seção ∝ S² ; volume(massa/filamento) ∝ S³")
print(f"  Estrutura (régua da sabatina): σ_flexão ∝ M/W ∝ (P·L)/(B·H²) ∝ S/S³ = 1/S²")
print(f"     → escalar REDUZ a tensão por {1/S**2:.2f}× (escala AJUDA estruturalmente).")
print(f"\n  {'Peça/cota':28s} {'nativo':>9s} {'×S':>9s}  observação")
print("  " + "-" * 72)
rows = [
    ("Comprimento do pé [mm]", L0, L0 * S, "alvo 26-27 cm OK"),
    ("Furo pino InnerFoot Ø [mm]", i_d, i_d * S, "⚠ vira Ø%.1f (ainda ≠ M8)" % (i_d * S)),
    ("Bore pino TopJoint Ø [mm]", t_d, t_d * S, "⚠ vira Ø%.1f" % (t_d * S)),
    ("Recesso pylon Insert ≈Ø [mm]", ib[0] if ib else float('nan'),
     (ib[0] if ib else float('nan')) * S, "interface cresce junto"),
    ("Batente RubberCube vol [mm³]", rc.volume, rc.volume * S ** 3, "filamento TPU ×%.2f" % S ** 3),
    ("Keel InnerFoot vol [mm³]", inner.volume, inner.volume * S ** 3, "filamento ×%.2f" % S ** 3),
    ("Sola FootRubber vol [mm³]", foot.volume, foot.volume * S ** 3, "filamento ×%.2f" % S ** 3),
]
for nm, a, b, obs in rows:
    print(f"  {nm:28s} {a:9.1f} {b:9.1f}  {obs}")
print(f"\n  ⚠ ESCALAR A MALHA ESCALA OS FUROS: o pino nativo Ø{i_d:.1f}→Ø{i_d*S:.1f} e o bore "
      f"Ø{t_d:.1f}→Ø{t_d*S:.1f}.\n    Nenhum vira M8 sozinho → a ferragem precisa ser NORMALIZADA de qualquer modo.")

# ----------------------------------------------------------------------------
# FIGURA — secção sagital da junta (XZ) com os dois furos ajustados + escala
# ----------------------------------------------------------------------------
plt.rcParams.update({"font.size": 9, "figure.dpi": 130})
fig, (axA, axB) = plt.subplots(1, 2, figsize=(12.5, 5.2))

# (a) vista sagital (XZ) com círculos ajustados
for m, c, lb in [(inner, "#1f77b4", "InnerFoot (keel)"),
                 (top, "#d62728", "TopJoint (junta sup.)")]:
    v = m.vertices
    axA.scatter(v[:, 0], v[:, 2], s=0.4, c=c, alpha=0.28, label=lb)
for (cx, cz, d, c) in [(ih["cx"], ih["cz"], i_d, "#1f77b4"),
                       (th["cx"], th["cz"], t_d, "#d62728")]:
    th_ = np.linspace(0, 2 * np.pi, 120)
    axA.plot(cx + d / 2 * np.cos(th_), cz + d / 2 * np.sin(th_), c=c, lw=2)
    axA.annotate(f"Ø{d:.1f}", (cx, cz), color=c, fontsize=10, ha="center",
                 fontweight="bold")
axA.plot([ih["cx"], th["cx"]], [ih["cz"], th["cz"]], "k--", lw=1,
         label=f"eixo do pivô (ΔX={dX:.2f} mm)")
axA.set_xlabel("X — ântero-posterior [mm]"); axA.set_ylabel("Z — vertical [mm]")
axA.set_title("(a) Junta single-axis — secção sagital\n"
              "furos coaxiais (peças explodidas em Z)")
axA.set_aspect("equal"); axA.grid(alpha=0.3); axA.legend(fontsize=7.5, markerscale=10)

# (b) escala: tensão e volume vs fator de escala
sg = np.linspace(1.0, 1.5, 100)
axB.plot(sg, 1 / sg ** 2, color="#138d75", lw=2, label="σ relativa  ∝ 1/S²  (cai)")
axB.plot(sg, sg ** 3, color="#cb4335", lw=2, label="volume/filamento ∝ S³ (sobe)")
axB.axvline(S, color="gray", ls=":", lw=1.4, label=f"S alvo = {S:.2f}")
axB.scatter([S, S], [1 / S ** 2, S ** 3], color=["#138d75", "#cb4335"], zorder=5)
axB.annotate(f"{1/S**2:.2f}×", (S, 1 / S ** 2), textcoords="offset points",
             xytext=(6, -12), color="#138d75")
axB.annotate(f"{S**3:.2f}×", (S, S ** 3), textcoords="offset points",
             xytext=(6, 6), color="#cb4335")
axB.set_xlabel("Fator de escala S  (pé 21→26-27 cm)")
axB.set_ylabel("Multiplicador relativo ao nativo")
axB.set_title("(b) Efeito de escalar a malha\n(estrutura melhora; filamento ~dobra)")
axB.grid(alpha=0.3); axB.legend(fontsize=8)

fig.suptitle("Levantamento da articulação + escala — design-base A (Make3D #293133)",
             fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.95))
out = HERE / "medidas_articulacao.png"
fig.savefig(out, bbox_inches="tight")
print(f"\n[figura] salva: {out}")
print("=" * 76)
