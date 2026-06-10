#!/usr/bin/env python3
"""
Processamento das peças da prótese pé-tornozelo (design-base A, Make3D #293133).
Edição de malha sem CAD paramétrico (não há STEP/F3D oficial).

Operações:
  1. Escala ×1,262 no CASCO (FootRubber, InnerFoot, Insert, RubberCube)
     → pé nativo ~21 cm vira ~26-27 cm (alvo BR 40-41).
  2. TopJoint: MANTIDO nativo (bore Ø10 = assento de bucha nylon 10×8).
  3. InnerFoot: furo do pino aberto de Ø~4,9 (nativo) para Ø8,4 (folga M8).
Saída: STLs nomeados em ../../stl/.
"""
import trimesh, numpy as np
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = SRC.parent.parent / "stl"
OUT.mkdir(exist_ok=True)
S = 1.262                      # fator de escala do casco
HOLE_C = np.array([-6.21, 0.0, 63.50])   # centro do furo (nativo), eixo Y
HOLE_D_M8 = 8.4               # Ø do furo final (folga M8)

def load(name): return trimesh.load(SRC / name)

def save(mesh, name):
    mesh.export(OUT / name)
    d = mesh.bounds[1]-mesh.bounds[0]
    print(f"  → {name:32s} bbox {np.round(d,1).tolist()}  wt={mesh.is_watertight}  {mesh.volume/1000:.1f}cm³")

print("="*70)
print(" PROCESSAMENTO DAS PEÇAS — prótese pé-tornozelo (design A)")
print("="*70)

# --- 1. Peças do casco: escalar ×S -----------------------------------------
print(f"\n[escala ×{S} — casco]")
for src, dst in [("FootRubber.stl","sola_tpu.stl"),
                 ("Insert.stl","conector_pylon_petg.stl"),
                 ("RubberCube.stl","batente_tpu.stl")]:
    m = load(src); m.apply_scale(S); save(m, dst)

# --- 2. TopJoint: nativo (não escalar) -------------------------------------
print("\n[TopJoint — NATIVO, bore Ø10 mantido p/ bucha 10×8]")
save(load("TopJoint.stl"), "tornozelo_superior_petg.stl")

# --- 3. InnerFoot: escalar + abrir furo M8 ---------------------------------
print(f"\n[InnerFoot — escala ×{S} + furo Ø{HOLE_D_M8} (M8)]")
keel = load("InnerFoot.stl"); keel.apply_scale(S)
c = HOLE_C * S                      # centro do furo escalado
# cilindro ao longo de Y, atravessando o knuckle inteiro
cyl = trimesh.creation.cylinder(radius=HOLE_D_M8/2, height=80)
# orientar o cilindro de Z (default) para Y: rotação -90° em X
cyl.apply_transform(trimesh.transformations.rotation_matrix(np.radians(-90), [1,0,0]))
cyl.apply_translation([c[0], 0.0, c[2]])  # Y=0 → atravessa todo o knuckle (Y 148-175)
# posicionar o cilindro no Y do furo
ymid = (keel.bounds[0][1]+keel.bounds[1][1])/2
cyl.apply_translation([0, ymid, 0])
keel_drilled = trimesh.boolean.difference([keel, cyl], engine="manifold")
save(keel_drilled, "keel_petg.stl")

# verificar Ø do furo resultante
v = keel_drilled.vertices
cx, cz = c[0], c[2]
d = np.sqrt((v[:,0]-cx)**2 + (v[:,2]-cz)**2)
ring = d[(d>3.0)&(d<5.5)]
if len(ring): print(f"     furo resultante: Ø ~{2*ring.min():.1f} mm (alvo {HOLE_D_M8})")
print("\nConcluído. STLs em:", OUT)
