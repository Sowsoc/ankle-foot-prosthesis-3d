# Protocolo de validação — prótese pé-tornozelo

> Método definido **antes** dos testes (dia ~20/06) para não improvisar com a peça na mão.
> Objetivo: gerar os dados das seções 6 (validação) e 8 (discussão) do relatório, com
> registro fotográfico/vídeo para a apresentação. Validação **qualitativa/demonstrativa** —
> não é certificação de uso clínico.

---

## Teste 1 — Amplitude de movimento (ADM)

**Pergunta:** a articulação atinge a ADM-alvo? (dorsiflexão 10-15°, plantarflexão 15-20°)

**Material:** transferidor (ou app de medição de ângulo no celular — "Medir"/"Bubble Level"/"Clinometer"), marcador, câmera com tripé ou apoio fixo.

**Procedimento:**
1. Montar a junta (M8 + bucha + batentes TPU) e fixar o pylon/keel numa morsa ou apoio rígido, com a sola livre para girar.
2. Marcar com caneta uma linha de referência no keel (segmento da perna) e outra na sola (segmento do pé) — são os dois braços do ângulo.
3. **Posição neutra:** sola a 90° com o keel (pé plano). Fotografar de lado (plano sagital), câmera perpendicular ao eixo do pino. Anotar ângulo de referência.
4. **Dorsiflexão:** empurrar a ponta do pé para cima até o batente anterior travar. Fotografar. Medir o ângulo entre as duas marcas.
5. **Plantarflexão:** empurrar a ponta do pé para baixo até o batente posterior travar. Fotografar. Medir.
6. Repetir 3× cada movimento e medianar.

**Registro (`testes/adm.csv`):**
```
movimento,alvo_min,alvo_max,medido_1,medido_2,medido_3,mediana
dorsiflexao,10,15,,,,
plantarflexao,15,20,,,,
```

**Critério:** ✅ se a mediana cai dentro (ou próximo) da faixa-alvo. Se ficar fora, registrar e discutir na seção 8 (provável causa: dureza/geometria do batente TPU).

> ⚠ Fotografar **rigorosamente de lado**, com a câmera no nível do eixo do pino — ângulo de câmera enviesado falseia a leitura. App de ângulo no próprio plano da foto ajuda.

---

## Teste 2 — Carga estática

**Pergunta:** a peça suporta a carga de demonstração sem falhar?

> Carga de projeto = 1030 N (≈ 105 kgf, = 1,5×BW de 70 kg). Para um **teste seguro e
> demonstrativo**, NÃO é obrigatório chegar a 105 kgf — começar baixo e subir por degraus,
> observando. O objetivo é mostrar comportamento e ausência de falha catastrófica, não
> levar à ruptura.

**Material:** balança de banheiro (para conhecer a carga aplicada), peso conhecido OU prensa manual/morsa, apoio rígido, paquímetro ou régua, câmera.

**Opção A — carga por peso corporal (simples, demonstrativo):**
1. Apoiar a prótese montada na vertical, sola no chão, conector preso a um apoio rígido.
2. Aplicar carga gradual — pessoa apoiando peso parcial sobre a estrutura via o conector, com balança intermediária medindo quanto está sendo aplicado.
3. Subir em degraus: 20 → 40 → 60 → 80 kgf, fotografando cada degrau.
4. Observar e registrar: deformação visível? a junta cede? algum estalo/trinca?

**Opção B — carga por prensa/morsa (mais controlado):**
1. Posicionar a peça entre as garras com a carga alinhada ao eixo de aplicação real (vertical sobre o tornozelo).
2. Aplicar carga progressiva medindo com célula de carga ou estimando pelo aperto.
3. Mesma observação por degraus.

**Registro (`testes/carga.csv`):**
```
degrau_kgf,deformacao_observada,trinca,nota
20,,,
40,,,
60,,,
80,,,
```
+ medir, se possível, a **deflexão** (deslocamento da ponta do pé sob carga) com régua/paquímetro em cada degrau → permite comparar com o cálculo de flexão da seção 5.

**Critério:** ✅ se suporta a carga demonstrada sem falha estrutural nem deformação permanente. Registrar a carga máxima atingida com segurança (mesmo que abaixo de 105 kgf).

> ⚠ **Segurança:** carga sob estrutura impressa pode falhar de forma súbita e projetar fragmentos. Usar óculos de proteção, não posicionar o rosto sobre a peça, subir devagar. Parar ao primeiro sinal de trinca.

---

## Teste 3 — Funcional da junta (montagem)

**Checklist rápido na montagem (dia 19/06):**
- [ ] O parafuso M8 passa limpo pelo furo Ø8,4 do keel?
- [ ] A bucha nylon 10×8 assenta no bore Ø10 do tornozelo sem folga excessiva?
- [ ] A junta gira livre na ADM, sem travar nem ter folga lateral?
- [ ] Os batentes TPU limitam o movimento nos dois sentidos?
- [ ] Encaixe sola ↔ keel ↔ conector firme?

Se a folga do furo estiver errada (FDM real ≠ nominal): registrar o desvio e ajustar
(reimprimir keel com furo corrigido, ou bucha de espessura diferente).

---

## Entregáveis da validação (alimentam o relatório)

| Saída | Arquivo | Vai para |
|---|---|---|
| Dados de ADM | `testes/adm.csv` | Seção 6 |
| Dados de carga + deflexão | `testes/carga.csv` | Seção 6 + comparar c/ seção 5 |
| Fotos de cada teste | `fotos/` | Seção 6 + slides |
| Vídeo do ciclo de movimento | `fotos/` | Apresentação |
| Planilha de custo real | `testes/custo.csv` | Seção 7 |

> Com ADM e carga medidos, a **MINERVA Missão 2** analisa os dados e fecha as seções 6, 8 e 9.
