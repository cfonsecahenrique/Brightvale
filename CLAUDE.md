# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **Obsidian vault** — a worldbuilding and lore repository for **Brightvale** (also called *Emberdawn*), a dark fantasy post-apocalyptic tabletop RPG setting. There is no build system, test suite, or compilation step. All content is Markdown, designed to be explored and edited in [Obsidian](https://obsidian.md).

**Game system:** Daggerheart SRD (d12 pool-based fantasy RPG).

## Working With This Repo

- Open the root directory as an Obsidian vault to get wikilink navigation, graph view (`Ctrl+G`), and plugin support.
- All internal links use Obsidian wikilink syntax: `[[Note Name]]`. When creating or renaming files, update these links — Obsidian can do this automatically (`alwaysUpdateLinks: true` is set in `.obsidian/app.json`).
- Start reading at `Worldbuilding/Overview.md` for a world summary, or `README.md` for a quick orientation.

## Content Architecture

The vault is split into four top-level sections:

- **`Worldbuilding/`** — All GM-facing lore and reference material:
  - `Bestiary/` — Enemies: Revenants, Rotlords, Shatter-Wing Angels, Umbra-Touched Fiends, Fae, Dragons.
  - `Characters/Ancestries/` — Humankind, Elves/Faefolk, Dwarvenkind, Orcenfolk, Halflings, Infernis.
  - `Characters/NPCs/` — Named non-player characters.
  - `Factions_and_Organizations/` — The Council of Seven, Noble Houses (14 total: Old, Recent, Extinct), and five Guilds.
  - `History_and_Lore/` — Timeline, The Apostasy, The Umbra, Economy, Religions, wars, and myths.
  - `Items/` — Notable items and artifacts.
  - `Locations/` — Cities (Medsen, Emberfort, Aeldenbarrow), villages, and geography of the Vale.
  - `Mysteries_and_Themes/` — Major and minor mysteries for GM use.
  - `Quests_and_Campaigns/` — Campaign primer and expedition frameworks.
  - `Rules_and_Mechanics/` — Daggerheart SRD reference and the Umbra Augmentation/Humanity system.
  - `Overview.md` — World summary entry point.
- **`Players/`** — Player-facing material: player characters, handouts, etc.
  - `Player_Characters/` — Active PC sheets and notes.
- **`Short_Stories/`** — Short fiction set in the world.
- **`Endlessness/`** — Data for the Endlessness app: player stories, characters, and related content.

## Core World Concepts

- **The Apostasy**: A cataclysm that spawned the Umbra (a sentient, parasitic shadow miasma), ending the Armisian Empire. The main mystery of the setting.
- **The Beacon**: A divine artifact protecting Brightvale from the Umbra, powered by sacrificed souls. It is slowly dimming — the central tension.
- **The Umbra**: Corrupts living things into Revenants and mutants. Prolonged exposure mutates survivors (see `Worldbuilding/Rules_and_Mechanics/Umbra_Augmentation_and_Humanity.md`).
- **The Wastes**: Everything beyond Brightvale's walls. Venturers (player characters) are sent on expeditions here.
- **The Council of Seven**: Practical rulers of the Vale. The King (currently Alfwyn) is a symbolic figurehead. The Guilds and Noble Houses compete for Council influence.

## Linking Heuristics

When adding wikilinks to notes, follow these rules to keep the graph readable and clustered rather than a flat spaghetti of cross-links.

### Hub notes (gravity wells)
These are the graph's structural centers. Every thematically related note should link to at least one of them:
- `[[The Apostasy]]` — root cause of everything; link from any note touching the cataclysm, the Umbra, lost history, or the Armisian Empire.
- `[[The Beacon]]` — central tension; link from Caretakers, Religions, King Alfwyn, mysteries involving the dimming.
- `[[Umbra]]` — link from all Bestiary entries, Mysteries, and any note about corruption or the Wastes.
- `[[The Council of Seven]]` — link from all Noble Houses, Guilds, major NPCs, and political notes.
- `[[Medsen]]` — link from NPCs, Noble Houses (most are seated here), and political/religious institutions.

### Rules per note type
- **Noble Houses** — must link to `[[The Council of Seven]]` and their seat city. Key Relationships should be wikilinks, not just bold text.
- **NPCs** — link to their faction/guild + their home city + 1–2 relevant lore articles.
- **Bestiary entries** — link to `[[Umbra]]` and/or `[[Apostasy]]` as their origin; link to any guild that hunts or studies them.
- **Locations** — link to factions present there + any relevant NPCs based there.
- **Mysteries** — link to their root cause hub (`[[Apostasy]]` or `[[The Beacon]]`); link to the guild most likely to investigate.
- **Short fiction** — add a `**Related:**` footer with links to factions, creatures, and concepts that appear.

### General principles
- **Specific → General, not the reverse.** `House Lugner` links to `The Council of Seven`; the Council note doesn't need to enumerate all 14 houses back.
- **Cap at ~3–4 direct links per note.** Hub + 1–2 thematically close peers. More links turns every node into a hairball center.
- **Convert Key Relationships to wikilinks.** Bold text like `**Aetherweaver Academy:**` in a house file should be `**[[Aetherweaver Academy]]:**` so the edge appears in the graph.
- **Use the exact filename.** The Council file is `The Council of Seven.md` — use `[[The Council of Seven]]`, not `[[Council of Seven]]`.
- **Stubs need at least 2 hub links** before they're useful graph nodes.

### Graph color groups (graph.json)
- Ancestries: cyan `#00FFE1`
- NPCs: amber `#E0B152`
- Noble Houses/Old: blue `#0062FF`
- Noble Houses/Recent: light blue `#2BB3EE`
- Noble Houses/Extinct: gray `#696969`
- Guilds: yellow `#FFEA00`
- Locations/Brightvale: green `#59FF00`
- History_and_Lore: orange `#CC6600`
- Mysteries_and_Themes: violet `#5252E0`
- Bestiary: dark red `#570505`
- Rules_and_Mechanics: teal `#009999`

## Obsidian Plugins in Use

- **daggerforge** — Daggerheart system tooling and stat block support.
- **dataview** — Query and aggregate note metadata with code blocks.
- **infranodus-graph-view** — Advanced graph visualization.
- **obsidian-5e-statblocks** — D&D-style stat block rendering for Bestiary entries.
- **obsidian-excalidraw-plugin** — Embedded diagrams and visual notes.
- **statblock-sidekick** — Additional stat block support for Daggerheart.
