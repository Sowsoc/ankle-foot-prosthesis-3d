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
- [ ] Ciclo da marcha e papel do tornozelo (heel-strike → stance → toe-off).
- [ ] ADM fisiológica: dorsiflexão ~10°, plantarflexão ~20° na marcha.
- [ ] Por que articular: SACH (não-articulado) vs single-axis — absorção de choque, energia, conforto.
- [ ] Cargas: pico de ~1,2–1,5× peso corporal no heel-strike.

## 3. Requisitos de projeto
- [ ] Tabela de requisitos (copiar/refinar do README): carga, FS, ADM, conexão, custo, massa.
- [ ] Usuário de projeto (adulto 70 kg, pé 26–27 cm).

## 4. Concepção e projeto (design)
- [ ] Design-base open-source escolhido + o que foi alterado e **por quê** (defensável na banca).
- [ ] Mecanismo single-axis: eixo, batentes TPU dorsi/plantar, definição da ADM.
- [ ] Desenhos/renders do CAD (exportar de `cad/`).
- [ ] Recurso de projeto: split forefoot/heel (se aplicado).

## 5. Materiais e fabricação
- [ ] Material por componente + justificativa (PETG estrutura, TPU batentes, M8 eixo).
- [ ] Parâmetros de impressão: orientação (argumentar o eixo Z!), infill, paredes, suportes.
- [ ] Tempo e consumo de filamento por peça (do slicer).

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
