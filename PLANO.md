# Plano - 16 dias até 22/06

> Caminho crítico: **escolher base -> CAD -> envio para impressão externa**.
> Impressão terceirizada: STLs precisam sair até **13/06** (prazo de entrega 1-3 dias).
> Travar o design antes do estágio começar (15/06) - mas o envio é antes disso.

| Data | Entrega | Dep. | Risco |
|---|---|---|---|
| **06/06** | Decisão do design-base (ler matriz + bater martelo) + registrar no README | - | ⛔ trava tudo |
| **07/06** | Download STL + STEP/F3D do design escolhido para `cad/` e `refs/` | 06 | baixo |
| **09/06** | Medir B, H, L do keel no STL; rodar `dimensionamento.py` com valores reais; confirmar material | 07 | médio |
| **13/06** | **CAD completo - TRAVAR e exportar STLs** por peça nomeados + doc de especificações de impressão | 09 | ⛔ crítico - envio no mesmo dia |
| **13/06** | **Enviar para impressão externa** com especificações (material, infill, orientação, qtd) | 13 | alto - logística |
| **15/06** | ⚠ Início do estágio (08-14h) | - | colisão de agenda |
| **16–17/06** | Retirada das peças impressas (estimativa - confirmar com quem imprimir) | 13 | médio |
| **18/06** | **Buffer**: reimpressão de emergência se necessário (ter opção de impressora local reserva) | 16 | alto |
| **19/06** | Montagem da articulação (eixo M8 + bucha + batentes TPU) | 16 | médio |
| **20/06** | Validação funcional: ADM + carga + fotos/vídeo | 19 | médio |
| **21/06** | Relatório técnico fechado + slides + ensaio | 20 | alto (acúmulo) |
| **22/06** | **APRESENTAÇÃO** | 21 | - |

### Especificações a entregar para quem imprimir

Arquivo `slicing/ESPECIFICACOES_IMPRESSAO.md` a criar junto com os STLs:

| Peça | Material | Infill | Paredes | Orientação | Qtd |
|---|---|---|---|---|---|
| keel (estrutura principal) | PETG | ≥ 40% | ≥ 3 | deitado (carga no plano XY) | 1 |
| carcaça do tornozelo | PETG | ≥ 40% | ≥ 3 | a definir no CAD | 1 |
| batente dorsal | TPU 95A | 30-40% | 3 | a definir | 1 |
| batente plantar | TPU 95A | 30-40% | 3 | a definir | 1 |
| conector de pylon | PETG | ≥ 50% | ≥ 4 | a definir | 1 |

> Peças e quantidades a confirmar após CAD finalizado.

### Regras do plano
- **CAD trava em 13/06, não 14/06** - envio externo não espera.
- **Ter opção de impressora local reserva** para emergência pós-retirada (peça com defeito).
- Relatório alimentar em paralelo ao CAD - não deixar tudo pra 21/06.
- Colisões de agenda: estágio 15/06 (08-14h) + prova Informática Médica / Eng. Clínica 25/06.
