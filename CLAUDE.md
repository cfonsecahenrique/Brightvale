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

## Obsidian Plugins in Use

- **daggerforge** — Daggerheart system tooling and stat block support.
- **dataview** — Query and aggregate note metadata with code blocks.
- **infranodus-graph-view** — Advanced graph visualization.
- **obsidian-5e-statblocks** — D&D-style stat block rendering for Bestiary entries.
- **obsidian-excalidraw-plugin** — Embedded diagrams and visual notes.
- **statblock-sidekick** — Additional stat block support for Daggerheart.
