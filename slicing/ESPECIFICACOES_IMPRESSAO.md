# Especificações de impressão — prótese pé-tornozelo

> Acompanha os STLs em `../stl/`. Design-base A (Make3D #293133), remixado.
> Peças escaladas ×1,262 (pé ~26-27 cm), exceto o tornozelo superior (nativo).

## Tabela por peça

| STL | Material | Qtd | Infill | Paredes | Orientação | Observação |
|---|---|---|---|---|---|---|
| `keel_petg.stl` | PETG | 1 | **50%** | **≥4** | **deitado** (eixo longo na horizontal) | Peça estrutural principal. Furo M8 já modelado. |
| `tornozelo_superior_petg.stl` | PETG | 1 | 50% | ≥4 | a favor da resistência do bore | Bore Ø10 = assento da bucha nylon 10×8. |
| `conector_pylon_petg.stl` | PETG | 1 | 50% | ≥4 | a definir | Interface com o pylon. |
| `sola_tpu.stl` | TPU 95A | 1 | 35% | 3 | base plana na mesa | **265 mm** no eixo maior — exige mesa grande. |
| `batente_tpu.stl` | TPU 95A | **2** | 35% | 3 | qualquer | Batentes dorsi/plantar (definem a ADM). |

## Parâmetros gerais
- **Layer height:** 0,2 mm
- **PETG:** bico 230-240 °C, mesa 70-80 °C
- **TPU 95A:** velocidade reduzida (flexível), retração baixa

## Pontos críticos
1. **Keel deitado** — a carga de flexão solicita o plano XY (forte); imprimir em pé colocaria a carga na adesão entre camadas (eixo Z, 30-50% mais fraco).
2. **Sola = 265 mm** — não cabe em mesa padrão 220 mm. Confirmar impressora ≥ 270 mm OU fatiar em 2 partes.
3. **Bore do tornozelo** intacto em Ø10 — não redimensionar; é o assento da bucha.

## Estimativa de filamento
- PETG: ~215 g
- TPU 95A: ~400 g

## Ferragem de montagem (comprar à parte)
- 1× parafuso M8 × 60 mm (eixo da articulação)
- 2× bucha nylon 10×8 (OD 10 / ID 8) — mancal no bore do tornozelo
- 1× porca M8 (autotravante de preferência) + 2-4× arruela M8
