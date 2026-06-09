#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dimensionamento estrutural PRELIMINAR — prótese de pé-tornozelo articulada (FDM)
================================================================================
Disciplina: Dispositivos de Reabilitação — Eng. Biomédica / FUMEC
Projeto:    Prótese funcional de pé-tornozelo articulada, single-axis, impressa em 3D
Autor:      João Vítor Silva Oliveira  |  Apoio de cálculo: MINERVA

OBJETIVO
--------
Calcular, de forma reproduzível e paramétrica, se a seção crítica do "keel"
(quilha estrutural) e o eixo da articulação aguentam a carga de projeto com
fator de segurança 2–3, e usar isso para escolher material e parâmetros de
impressão (paredes / infill / orientação).

⚠️  ESTE DIMENSIONAMENTO É PRELIMINAR E PARAMÉTRICO.
    A geometria da seção crítica (largura B, altura H, braço de momento L) é um
    PLACEHOLDER plausível para adulto ~70 kg / pé 26–27 cm. Os três parâmetros
    marcados "REFINAR COM STL" devem ser remedidos no design-base depois de
    baixado e escolhido. O modelo de viga em flexão é uma simplificação de 1ª
    ordem; serve para achar ORDEM DE GRANDEZA e comparar materiais, NÃO substitui
    FEA. Nenhum protótipo deste trabalho deve receber carga corporal real.

MODELO
------
Seção crítica do keel  ≈  caixa retangular OCA (casca impressa: perímetros),
                          dimensões externas B × H, parede de espessura t.
                          O infill do miolo é DESPREZADO no cálculo de flexão
                          (fica perto da linha neutra → contribui pouco a I, e
                          desprezá-lo é conservador / a favor da segurança).
Carga de projeto P aplicada com braço L  →  momento fletor M = P·L na seção.
Tensão de flexão  σ = M·(H/2) / I , com I da seção oca.
Resistência de projeto  σ_adm = UTS_xy · k_z / FS
    UTS_xy = resistência à tração no plano de impressão (XY)
    k_z    = derating de anisotropia (a adesão entre camadas no eixo Z é mais
             fraca que o material no plano; orientar a peça para carregar no XY)
    FS     = fator de segurança (2–3)

FONTES DOS NÚMEROS (não inventar dados — cada valor tem origem rastreável)
--------------------------------------------------------------------------
[1] GRF de pico na marcha 1,0–1,5× peso corporal (corrida 2,0–2,9×):
    Nilsson & Thorstensson, "Ground reaction forces at different speeds of
    human walking and running", Acta Physiol Scand 1989. PMID 2782094.
[2] PETG impresso (FDM): UTS ~15–51 MPa conforme parâmetros; filamento bruto
    60–66 MPa, E ~2 GPa; impressão densa otimizada 43–51 MPa, E ~1 GPa.
    MDPI Polymers 11(7):1220 (2019); estudo RSM PMC12694470.
[3] PLA-CF (fibra picada / chopped, imprimível em FDM comum): UTS ~28–40 MPa
    (pode ser MENOR que PLA puro por fusão inter-filamento pior), E ~3 GPa,
    frágil. ColorFabb 20%CF: 40 MPa / E 3 GPa (MDPI Polymers 18(6):771);
    PLA+CF 17,8–28,7 MPa (Oxford Acad. Microsc. Microanal. 29 S1:1447).
[4] Anisotropia Z do FDM: Z tipicamente 30–50% mais fraco que XY; reforço de
    fibra AGRAVA a anisotropia (80–90%+). Z-pinning study, OSTI 1808415;
    Perez et al., 3D Printing & Additive Manuf. 2021 (SagePub).
[5] Parafuso M8 classe 8.8: UTS f_ub = 800 MPa, área de tensão A_s = 36,6 mm²,
    resistência ao cisalhamento ≈ 0,6·f_ub = 480 MPa.
    eurocodeapplied.com (EN1993-1-8 Tab. 3.4); engineersedge grade 8.8.
[6] Sanity-check de ordem de grandeza: FEA de pé protético achou tensão máx.
    ~15 MPa no heel-strike a 150% BW (ResearchGate 318989655).
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")  # backend sem display (gera PNG direto)
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path(__file__).resolve().parent  # salva os gráficos ao lado do script

# =============================================================================
# 1) PARÂMETROS DE PROJETO
# =============================================================================
# --- Carga de projeto ------------------------------------------------------
BW_KG      = 70.0     # massa do usuário de projeto [kg]            (README)
G          = 9.81     # gravidade [m/s²]
GRF_FACTOR = 1.5      # pico de GRF na marcha, extremo alto [×BW]   [1]
P          = BW_KG * G * GRF_FACTOR          # carga de projeto [N]  ≈ 1030 N

# --- Fator de segurança ----------------------------------------------------
FS_BASE  = 2.5        # base (faixa de projeto 2–3)
FS_RANGE = (2.0, 3.0)

# --- Geometria da seção crítica do keel  [MEDIDO no STL — design-base A] -----
# Design-base TRAVADO: A = Make3D "Prosthetic Foot Prototype" (Printables #293133).
# Keel estrutural = InnerFoot.stl (cad/A_make3d_293133/). Medições (parse direto
# da malha binária; varredura de seção a cada 10 mm ao longo do comprimento):
#   bounding box nativa do keel:  L_total = 111.6 ,  Y = 46.0 ,  Z = 40.2  mm
#   altura Z ~ 40 mm quase constante ao longo do pé; largura Y afina do
#   meio-pé (~45) para o antepé (~15). Seção crítica de FLEXÃO sob heel-strike
#   ~ região do tornozelo (X ~ 50 mm do calcanhar): B(Y) ~ 43 , H(Z) ~ 37 mm.
# ESCALA: o pé do modelo (FootRubber = 210 mm) é menor que o alvo 26-27 cm.
#   Escalar p/ alvo exige SCALE ~ 1.26 — e ESCALAR SÓ AJUDA (σ ∝ 1/SCALE²,
#   pois L cresce ∝ s mas o módulo de seção ∝ s³). Logo SCALE=1.0 (nativo) é o
#   caso CONSERVADOR/pior: se PETG passa aqui, passa também escalado ao alvo.
SCALE = 1.0   # 1.0 = escala nativa do STL (pé ~21 cm, pior caso de tensão)
B = 43.0 * SCALE   # largura da seção crítica [mm]  (medido no InnerFoot.stl)
H = 37.0 * SCALE   # altura da seção crítica  [mm]  (medido no InnerFoot.stl)
L = 55.0 * SCALE   # braço heel-strike → tornozelo [mm] (medido: ~50-55 mm)

# --- Materiais candidatos (valores de IMPRESSÃO FDM, plano XY) --------------
# uts_xy [MPa], E [MPa], k_z [-], comp [MPa] (compressão, p/ bearing do furo)
MATERIALS = {
    "PETG":   dict(uts_xy=45.0, E=1000.0, k_z=0.50, comp=52.0,  # [2],[4]
                   nota="tenaz/dúctil; melhor adesão Z e fadiga/impacto"),
    "PLA-CF": dict(uts_xy=38.0, E=3000.0, k_z=0.40, comp=49.0,  # [3],[4]
                   nota="rígido porém frágil; anisotropia Z agravada por fibra"),
}

# --- Eixo da articulação (parafuso M8 classe 8.8) --------------------------
BOLT_UTS   = 800.0    # f_ub [MPa]                                  [5]
BOLT_AS    = 36.6     # área de tensão M8 [mm²]                     [5]
BOLT_SHEAR = 0.6 * BOLT_UTS   # resistência ao cisalhamento [MPa]   [5]
N_SHEAR    = 2        # planos de cisalhamento (junta tipo garfo/clevis = dupla)
D_PIN      = 8.0      # diâmetro do furo da junta [mm] (M8)

# =============================================================================
# 2) FUNÇÕES DE CÁLCULO
# =============================================================================
def I_hollow(B, H, t):
    """Momento de inércia de seção retangular OCA (casca de parede t) [mm^4]."""
    inner_b = np.maximum(B - 2.0 * t, 0.0)
    inner_h = np.maximum(H - 2.0 * t, 0.0)
    return (B * H**3 - inner_b * inner_h**3) / 12.0

def sigma_bending(M, H, I):
    """Tensão de flexão na fibra extrema [MPa] (M em N·mm, H mm, I mm^4)."""
    return M * (H / 2.0) / I

def sigma_adm(mat, FS):
    """Tensão admissível de projeto do material [MPa]."""
    return mat["uts_xy"] * mat["k_z"] / FS

def t_min_for(sig_adm, H, B, M, t_grid):
    """Espessura de parede mínima p/ σ(t) <= σ_adm (interpola curva monotônica)."""
    I = I_hollow(B, H, t_grid)
    sig = sigma_bending(M, H, I)            # decrescente em t
    # inverte para interpolar t como função de σ (σ decrescente → reverter)
    if sig_adm < sig.min():
        return np.nan  # nem a casca cheia atende: seção insuficiente
    return float(np.interp(sig_adm, sig[::-1], t_grid[::-1]))

# =============================================================================
# 3) EXECUÇÃO — RESULTADOS NUMÉRICOS
# =============================================================================
M = P * L  # momento fletor na seção crítica [N·mm]

print("=" * 74)
print(" DIMENSIONAMENTO ESTRUTURAL PRELIMINAR — prótese pé-tornozelo (FDM)")
print("=" * 74)
print(f"  Carga de projeto P      = {P:7.1f} N   "
      f"(= {GRF_FACTOR:.1f}×BW de {BW_KG:.0f} kg) [fonte 1]")
print(f"  Momento fletor   M = P·L = {M:7.0f} N·mm  (L = {L:.0f} mm)  [MEDIDO, SCALE={SCALE}]")
print(f"  Seção crítica (medida no InnerFoot.stl): B = {B:.0f} mm , H = {H:.0f} mm")
print(f"  Fator de segurança base FS = {FS_BASE:.1f}  (faixa {FS_RANGE[0]:.0f}–{FS_RANGE[1]:.0f})")

# Sanity-check: tensão na seção SÓLIDA equivalente vs FEA de referência [6]
I_solid = I_hollow(B, H, t=min(B, H) / 2.0)  # t = H/2 -> seção cheia
sig_solid = sigma_bending(M, H, I_solid)
print(f"\n  Sanity-check: σ na seção sólida equivalente = {sig_solid:5.1f} MPa")
print(f"    (FEA de literatura achou ~15 MPa @150%BW [6] — mesma ordem de grandeza)")

print("\n" + "-" * 74)
print(" RESISTÊNCIA DE PROJETO POR MATERIAL  (σ_adm = UTS_xy · k_z / FS)")
print("-" * 74)
print(f"  {'Material':8s} {'UTS_xy':>7s} {'k_z':>5s} {'FS':>4s} "
      f"{'σ_adm':>7s} {'t_min*':>8s}")
print(f"  {'':8s} {'[MPa]':>7s} {'[-]':>5s} {'[-]':>4s} {'[MPa]':>7s} {'[mm]':>8s}")
t_grid = np.linspace(0.1, min(B, H) / 2.0 - 0.01, 600)
results = {}
for name, mat in MATERIALS.items():
    sa = sigma_adm(mat, FS_BASE)
    tmin = t_min_for(sa, H, B, M, t_grid)
    results[name] = dict(sigma_adm=sa, t_min=tmin)
    tmin_str = f"{tmin:6.2f}" if not np.isnan(tmin) else "  n/a "
    print(f"  {name:8s} {mat['uts_xy']:7.1f} {mat['k_z']:5.2f} {FS_BASE:4.1f} "
          f"{sa:7.2f} {tmin_str:>8s}")
print("  * t_min = espessura de parede mín. da CASCA pura (infill=0, conservador)")

# Eixo / junta -------------------------------------------------------------
tau_pin     = P / (N_SHEAR * BOLT_AS)            # cisalhamento atuante [MPa]
tau_adm_pin = BOLT_SHEAR / FS_BASE              # admissível [MPa]
fs_pin_real = BOLT_SHEAR / tau_pin              # FS real do pino
# bearing (esmagamento) do furo no PLÁSTICO — o elo realmente fraco da junta
mat_keel = MATERIALS["PETG"]
sig_bear_adm = mat_keel["comp"] / FS_BASE
t_bear_min   = P / (D_PIN * sig_bear_adm)        # espessura de material no furo

print("\n" + "-" * 74)
print(" ARTICULAÇÃO — eixo M8 (aço 8.8) e furo no plástico")
print("-" * 74)
print(f"  Cisalhamento no pino: τ = P/(n·A_s) = {tau_pin:6.2f} MPa "
      f"(n={N_SHEAR} planos)")
print(f"  Admissível do pino:   τ_adm = {tau_adm_pin:6.1f} MPa  → "
      f"FS REAL do pino ≈ {fs_pin_real:4.1f}")
print(f"    → o pino de aço é MUITO superdimensionado; NÃO é o elo fraco.")
print(f"  Esmagamento (bearing) do furo no PETG: σ_bear = P/(d·t)")
print(f"    σ_bear_adm = {sig_bear_adm:4.1f} MPa  → "
      f"espessura mín. de material no furo t ≈ {t_bear_min:4.1f} mm")
print(f"    → ELO CRÍTICO da junta = furo no plástico. Reforçar: bucha metálica"
      f" e/ou\n      material generoso ao redor do eixo.")

print("\n" + "-" * 74)
print(" RECOMENDAÇÃO (preliminar — refinar com STL)")
print("-" * 74)
print("  • Material estrutural: PETG (ver matriz em refs/decisao_design_base.md).")
print("  • Orientação: imprimir o keel DEITADO — carga solicita o plano XY,")
print("    não a adesão entre camadas (Z). É o que torna k_z=0.5 aceitável.")
print("  • Paredes: ≥4–6 perímetros (linha 0,4 mm → 1,6–2,4 mm) + infill ≥50%")
print("    (giroide). A flexão é carregada pelas paredes externas; o infill serve")
print("    a cisalhamento, impacto e estabilidade local — 100% só agrega massa.")
print("  • Junta: bucha metálica no furo do eixo (bearing é o ponto crítico).")
print("=" * 74)

# =============================================================================
# 4) GRÁFICOS
# =============================================================================
plt.rcParams.update({"font.size": 9, "figure.dpi": 130})
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.4))

# --- (a) σ atuante vs espessura de parede + admissíveis -------------------
I_curve = I_hollow(B, H, t_grid)
sig_curve = sigma_bending(M, H, I_curve)
ax1.plot(t_grid, sig_curve, color="#1f3a93", lw=2,
         label=f"σ atuante (B={B:.0f}, H={H:.0f} mm)")
colors = {"PETG": "#138d75", "PLA-CF": "#cb4335"}
for name in MATERIALS:
    sa = results[name]["sigma_adm"]
    tmin = results[name]["t_min"]
    ax1.axhline(sa, color=colors[name], ls="--", lw=1.4,
                label=f"σ_adm {name} = {sa:.1f} MPa")
    if not np.isnan(tmin):
        ax1.plot(tmin, sa, "o", color=colors[name], ms=7)
        ax1.annotate(f"t_min={tmin:.1f} mm", (tmin, sa),
                     textcoords="offset points", xytext=(6, 8),
                     color=colors[name], fontsize=8)
ax1.set_xlabel("Espessura de parede t [mm]  (casca, infill desprezado)")
ax1.set_ylabel("Tensão de flexão σ [MPa]")
ax1.set_title("(a) Tensão vs espessura de parede")
ax1.set_ylim(0, min(40, sig_curve.max()))
ax1.grid(alpha=0.3)
ax1.legend(fontsize=7.5, loc="upper right")

# --- (b) sensibilidade: t_min vs altura H da seção -------------------------
H_grid = np.linspace(25, 70, 200)
for name in MATERIALS:
    sa = results[name]["sigma_adm"]
    tmins = []
    for h in H_grid:
        tg = np.linspace(0.1, min(B, h) / 2.0 - 0.01, 400)
        tmins.append(t_min_for(sa, h, B, M, tg))
    ax2.plot(H_grid, tmins, color=colors[name], lw=2, label=name)
ax2.axvline(H, color="gray", ls=":", lw=1.2, label=f"H medido = {H:.0f} mm")
ax2.set_xlabel("Altura H da seção crítica [mm]  (REFINAR COM STL)")
ax2.set_ylabel("Espessura de parede mínima t_min [mm]")
ax2.set_title("(b) t_min vs altura da seção  (σ ∝ 1/H²)")
ax2.grid(alpha=0.3)
ax2.legend(fontsize=8)
ax2.set_ylim(bottom=0)

fig.suptitle("Dimensionamento preliminar — keel da prótese de pé-tornozelo (FDM)",
             fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.96))
out_png = OUT / "dimensionamento_flexao.png"
fig.savefig(out_png, bbox_inches="tight")
print(f"\n[gráfico] salvo: {out_png}")

# --- figura 2: comparação de resistência de projeto por material -----------
fig2, ax = plt.subplots(figsize=(6.2, 4.0))
names = list(MATERIALS.keys())
uts = [MATERIALS[n]["uts_xy"] for n in names]
adm = [results[n]["sigma_adm"] for n in names]
x = np.arange(len(names))
w = 0.38
ax.bar(x - w/2, uts, w, label="UTS no plano XY", color="#85929e")
ax.bar(x + w/2, adm, w, label=f"σ_adm projeto (k_z, FS={FS_BASE})",
       color=[colors[n] for n in names])
for xi, (u, a) in enumerate(zip(uts, adm)):
    ax.text(xi - w/2, u + 0.6, f"{u:.0f}", ha="center", fontsize=8)
    ax.text(xi + w/2, a + 0.6, f"{a:.1f}", ha="center", fontsize=8)
ax.set_xticks(x); ax.set_xticklabels(names)
ax.set_ylabel("Tensão [MPa]")
ax.set_title("Resistência de filamento vs resistência de PROJETO\n"
             "(o que sobra após anisotropia Z + FS)")
ax.legend(fontsize=8)
ax.grid(alpha=0.3, axis="y")
fig2.tight_layout()
out_png2 = OUT / "dimensionamento_materiais.png"
fig2.savefig(out_png2, bbox_inches="tight")
print(f"[gráfico] salvo: {out_png2}")
