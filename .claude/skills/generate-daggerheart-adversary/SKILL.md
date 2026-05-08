# Skill: Generate Daggerheart Adversary Block

## Trigger
Invoke when the user asks to "generate an adversary," "make a stat block," "create a monster," or provides a creature/NPC description for Daggerheart.

## Instructions

### Step 1 — Parse the Prompt
Extract (ask if unclear):
- **Creature concept**: name, appearance, narrative role, flavor.
- **Tier(s)**: Which tiers to generate (1–4). Default: ALL four tiers.
- **Role**: Infer from the concept if not stated (use the role-selection table below).
- **Setting hooks**: If the adversary belongs to Brightvale/Emberdawn, tie it to existing lore. Read `Worldbuilding/Bestiary/` and `Worldbuilding/Rules_and_Mechanics/Umbra-Touched Monsters.md` for context.

### Step 2 — Select the Role

| Does your Adversary…                                      | Role            |
| --------------------------------------------------------- | --------------- |
| Throw people around and make big hits                     | Bruiser         |
| Consist of a large group of individually weak creatures   | Minion or Horde |
| Command others to attack the PCs                          | Leader          |
| Attack from far away and keep pressure on the party       | Ranged          |
| Harry the party as a skirmisher in close quarters         | Skulk           |
| Have a lot of complicated moves that build on each other  | Solo            |
| Have simple abilities and make up the core of your forces | Standard        |
| Cause debuffs and aid allies                              | Support         |

- Supports are weak Leaders; Solos are complicated Bruisers.
- Multiple body parts or segments → consider **Colossal Enemy**.

### Step 3 — Assign Stats

Pick specific values within the ranges that fit the creature's fiction.

#### BRUISER
|        | Diff  | Major | Severe | HP  | Stress | ATK | Dmg Avg | Dice Pools               |
|--------|-------|-------|--------|-----|--------|-----|---------|--------------------------|
| Tier 1 | 12-14 | 7-9   | 13-15  | 5-7 | 3-4    | 0-2 | 8-11    | 1d12+2 / 1d10+4 / 1d8+6 |
| Tier 2 | 14-16 | 12-14 | 23-26  | 5-7 | 4-6    | 2-4 | 12-16   | 2d12+3 / 2d10+2 / 2d8+6 |
| Tier 3 | 16-18 | 19-22 | 35-40  | 6-8 | 4-6    | 3-5 | 18-22   | 3d12+1 / 3d10+4 / 3d8+8 |
| Tier 4 | 18-20 | 30-37 | 63-70  | 7-9 | 4-6    | 5-8 | 30-45   | 4d12+15 / 4d10+10 / 4d8+12 |

#### HORDE
|        | Diff  | Major | Severe | HP  | Stress | ATK  | Dmg Avg | Dice Pools               |
|--------|-------|-------|--------|-----|--------|------|---------|--------------------------|
| Tier 1 | 10-12 | 5-10  | 8-12   | 4-6 | 2-3    | -2-0 | 5-8     | 1d10+2 / 1d8+3 / 1d6+4  |
| Tier 2 | 12-14 | 10-15 | 16-20  | 5-6 | 2-3    | -1-1 | 9-13    | 2d10+2 / 2d8+6 / 2d6+3  |
| Tier 3 | 14-16 | 15-25 | 26-32  | 6-7 | 3-4    | 0-2  | 14-19   | 3d10+2 / 3d8+4 / 3d6+6  |
| Tier 4 | 16-18 | 20-30 | 35-45  | 7-8 | 4-5    | 1-3  | 20-30   | 4d10+4 / 4d8+8 / 4d6+10 |

When splitting damage at half HP, halve the dice pool (e.g. 2d10+2 → 1d10+1).

#### LEADER
|        | Diff  | Major | Severe | HP  | Stress | ATK  | Dmg Avg | Dice Pools                |
|--------|-------|-------|--------|-----|--------|------|---------|---------------------------|
| Tier 1 | 12-14 | 7-9   | 13-15  | 5-7 | 3-4    | 2-4  | 6-9     | 1d12+1 / 1d10+3 / 1d8+5  |
| Tier 2 | 14-16 | 12-14 | 23-26  | 5-7 | 4-5    | 3-5  | 12-15   | 2d12+1 / 2d10+3 / 2d8+6  |
| Tier 3 | 17-19 | 19-22 | 35-40  | 6-8 | 5-6    | 5-7  | 15-18   | 3d10+1 / 3d8+8            |
| Tier 4 | 19-21 | 30-37 | 63-70  | 7-9 | 6-8    | 8-10 | 25-35   | 4d12+6 / 4d10+8 / 4d8+10 |

#### MINION
|        | Diff  | Major | Severe | HP | Stress | ATK  | Minion Passive | Damage |
|--------|-------|-------|--------|----|--------|------|----------------|--------|
| Tier 1 | 10-12 | None  | None   | 1  | 1      | -2-0 | 3-5            | 1-3    |
| Tier 2 | 12-14 | None  | None   | 1  | 1      | -1-1 | 5-7            | 2-4    |
| Tier 3 | 14-16 | None  | None   | 1  | 1-2    | 0-2  | 7-9            | 5-8    |
| Tier 4 | 16-18 | None  | None   | 1  | 1-2    | 1-3  | 9-12           | 10-12  |

#### RANGED
|        | Diff  | Major | Severe | HP  | Stress | ATK | Dmg Avg | Dice Pools                |
|--------|-------|-------|--------|-----|--------|-----|---------|---------------------------|
| Tier 1 | 10-12 | 3-5   | 6-9    | 3-4 | 2-3    | 1-2 | 6-9     | 1d12+1 / 1d10+3 / 1d8+5  |
| Tier 2 | 13-15 | 5-8   | 13-18  | 3-5 | 2-3    | 2-5 | 12-16   | 2d12+1 / 2d10+3 / 2d8+6  |
| Tier 3 | 15-17 | 12-15 | 25-30  | 4-6 | 3-4    | 3-4 | 15-18   | 3d10+1 / 3d8+8            |
| Tier 4 | 17-19 | 18-25 | 30-40  | 4-6 | 4-5    | 4-6 | 25-35   | 4d12+6 / 4d10+8 / 4d8+10 |

#### SKULK
|        | Diff  | Major | Severe | HP  | Stress | ATK | Dmg Avg | Dice Pools                 |
|--------|-------|-------|--------|-----|--------|-----|---------|----------------------------|
| Tier 1 | 10-12 | 5-7   | 8-12   | 3-4 | 2-3    | 1-2 | 5-8     | 1d8+3 / 1d6+2 / 1d4+4     |
| Tier 2 | 12-14 | 7-9   | 16-20  | 3-5 | 3-4    | 2-5 | 9-13    | 2d8+3 / 2d6+3 / 2d4+6     |
| Tier 3 | 14-16 | 15-20 | 27-32  | 4-6 | 4-5    | 3-7 | 14-18   | 3d8+4 / 3d6+5 / 3d4+10    |
| Tier 4 | 16-18 | 20-30 | 35-45  | 4-6 | 4-6    | 4-8 | 20-35   | 4d12+10 / 4d10+4 / 4d6+10 |

#### SOLO
|        | Diff  | Major | Severe | HP    | Stress | ATK  | Dmg Avg | Dice Pools                 |
|--------|-------|-------|--------|-------|--------|------|---------|----------------------------|
| Tier 1 | 12-14 | 7-9   | 13-15  | 8-10  | 3-4    | 3    | 8-11    | 1d20 / 1d12+2 / 1d10+4    |
| Tier 2 | 14-16 | 12-14 | 23-26  | 8-10  | 4-5    | 3-4  | 15-20   | 2d20+3 / 2d10+2 / 2d8+6   |
| Tier 3 | 17-19 | 19-22 | 35-40  | 10-12 | 5-6    | 4-7  | 20-30   | 3d20 / 3d12+6 / 3d10+8    |
| Tier 4 | 19-21 | 30-37 | 63-70  | 10-12 | 6-8    | 7-10 | 30-45   | 4d12+15 / 4d10+10 / 4d8+12 |

Solos with phases should have lower HP and thresholds. Always give Solos **Relentless**.

#### STANDARD
|        | Diff  | Major | Severe | HP  | Stress | ATK | Dmg Avg | Dice Pools               |
|--------|-------|-------|--------|-----|--------|-----|---------|--------------------------|
| Tier 1 | 11-13 | 5-8   | 8-12   | 4-5 | 3-4    | 0-2 | 4-6     | 1d8+1 / 1d6+2 / 1d4+4   |
| Tier 2 | 13-15 | 8-12  | 16-20  | 5-6 | 3-4    | 1-3 | 8-12    | 2d8+2 / 2d6+3 / 2d4+4   |
| Tier 3 | 15-17 | 15-20 | 27-32  | 5-6 | 4-5    | 2-4 | 12-17   | 3d8+2 / 3d6+3 / 2d12+2  |
| Tier 4 | 17-19 | 25-35 | 35-55  | 5-6 | 4-5    | 3-5 | 17-28   | 4d10+2 / 4d8+4 / 4d6+10 |

#### SUPPORT
|        | Diff  | Major | Severe | HP  | Stress | ATK | Dmg Avg | Dice Pools              |
|--------|-------|-------|--------|-----|--------|-----|---------|-------------------------|
| Tier 1 | 12-14 | 5-8   | 9-12   | 3-4 | 4-5    | 0-2 | 3-5     | 1d8 / 1d6+2 / 1d4+4    |
| Tier 2 | 13-15 | 8-12  | 16-20  | 3-5 | 4-6    | 1-3 | 5-12    | 2d8+1 / 2d6+2 / 2d4+3  |
| Tier 3 | 15-17 | 15-20 | 28-35  | 4-6 | 5-6    | 2-4 | 13-16   | 3d8 / 3d6+3 / 2d12+1   |
| Tier 4 | 17-19 | 20-30 | 35-45  | 4-6 | 5-6    | 3-5 | 18-25   | 3d10+3 / 4d8+4 / 4d6+8 |

#### COLOSSAL ENEMY — Framework
|        | Major | Severe | Stress | Segment ATK |
|--------|-------|--------|--------|-------------|
| Tier 1 | 8-13  | 18-22  | 5-6    | 1-3         |
| Tier 2 | 15-20 | 24-32  | 5-6    | 2-4         |
| Tier 3 | 25-35 | 44-54  | 6-7    | 2-4         |
| Tier 4 | 30-40 | 60-70  | 6-8    | 3-5         |

**Average Segment:**
|        | Diff  | HP  | Damage | Dice Pools          |
|--------|-------|-----|--------|---------------------|
| Tier 1 | 13-14 | 3-4 | 6-9    | 1d6+3 / 1d10+1      |
| Tier 2 | 14-15 | 3-4 | 12-16  | 2d8+6 / 2d10+4      |
| Tier 3 | 15-16 | 4-5 | 16-20  | 3d6+10 / 3d8+6      |
| Tier 4 | 16-17 | 4-5 | 25-30  | 4d10+6 / 4d8+12     |

**Strong Segment:**
|        | Diff  | HP  | Damage | Dice Pools          |
|--------|-------|-----|--------|---------------------|
| Tier 1 | 14-16 | 5-6 | 9-12   | 1d8+6 / 1d12+4      |
| Tier 2 | 15-17 | 5-7 | 16-20  | 2d10+8 / 2d12+6     |
| Tier 3 | 16-18 | 6-7 | 20-30  | 3d12+12 / 3d10+6    |
| Tier 4 | 17-19 | 6-8 | 30-45  | 3d20+8 / 4d12+12    |

### Step 4 — Choose Experiences
Select 1–3 thematic Experiences (or invent fitting ones):

| Role     | Suggested Experiences                                 |
|----------|-------------------------------------------------------|
| Bruiser  | Crusher, Charger, Intimidation, Throw                 |
| Leader   | For the Realm!, Backstabber, Commander, Leadership    |
| Ranged   | Hunter, Survival, Tracker, Trapper                    |
| Skulk    | Camouflage, Stealth, Rabblerouser, Intrusion          |
| Solo     | Never Enough!, I See You, Vengeful                    |
| Standard | Often none, or shared with allied forces              |
| Support  | Magical Knowledge, Lore                               |

### Step 5 — Choose Features (2–4 per adversary)
Order: Passives first, then Actions, then Reactions.

**Mark a Stress** on features that:
- Attack more than 1 target
- Increase damage by a die face or number of dice
- Attack all targets in Very Close
- Do something spell-equivalent
- Impart conditions (not Restrained or Vulnerable)
- Give allies the spotlight at reduced damage (≤5)
- Do extra damage and push a target

**Spend a Fear** on features that:
- Increase die size and AoE damage
- Summon something
- Give allies the spotlight without reducing damage
- Start countdowns on characters
- AoE bigger than Very Close
- AoE moves that do direct damage

#### Feature Library by Role

**Bruiser:**
- *Momentum - Reaction:* When the \<Adversary\> makes a successful attack against a PC, you gain a Fear.
- *Ramp Up - Passive:* You must **Spend a Fear** to spotlight the \<Adversary\>. While spotlighted, they can make their standard attack against all targets within range.
- *Slow - Passive:* When spotlighted without a token, place a token (describe what they're preparing). When spotlighted with a token, clear it and they act.
- *Terrifying - Passive:* When the \<Adversary\> makes a successful attack, all PCs within Far range lose a Hope and you gain a Fear.

**Horde:**
- *Horde (\<damage\>) - Passive:* When the \<Adversaries\> have marked half or more HP, standard attack deals \<damage\> physical damage instead.

**Leader:**
- *Terrifying - Passive:* (same as Bruiser)
- *Relentless (X) - Passive:* Can be spotlighted up to X times per GM turn.
- *Activate Allies - Action:* **Spend X Fear** to spotlight 1d4 allies. Attacks deal half damage.
- *Direct Damage - Action:* If target or adversary has a Condition, damage is direct.
- *Call Reinforcements - Action:* Once per scene, **mark a Stress** to summon a \<different adversary\> at \<Range\>.
- *Merciless (1) - Passive:* When spotlighted, spotlight one additional ally without spending Fear.
- *Tactician - Action:* When spotlighted, **mark a Stress** to also spotlight two allies within Close range.

**Minion:**
- *Minion (X) - Passive:* Defeated on any damage. For every X damage dealt, defeat an additional Minion in range.
- *Group Attack - Action:* **Spend a Fear** to spotlight all \<Adversaries\> within Close range of target. They move to Melee, make one shared attack. On success, each deals \<damage\>. Combine damage.

**Ranged:**
- *Opportunity Shot - Reaction:* When another adversary deals damage to a target within Far range, **mark a Stress** to add \<extra damage\>.
- *Opportunist - Passive:* When 2+ adversaries are within Very Close of a creature, all damage is doubled.
- *Hit Multiple Targets - Reaction:* **Spend a Fear** to attack # targets within Far range at \<reduced damage\>.

**Skulk:**
- *Ambush - Action:* While _Hidden_, attack target within \<Range\>. On success, deal \<increased damage\>.
- *Cloaked - Action:* Become _Hidden_ until after next attack. Attacks while _Hidden_ have advantage.

**Solo:**
- *Relentless (X) - Passive:* Can be spotlighted up to X times per GM turn.
- *Countdown to Something Bad - Reaction:* Countdown (Loop 1d6). When \<condition\>, activate. When triggered, \<powerful effect\>. Targets that fail suffer \<negative outcome\>.

**Standard:**
- *Too Many to Handle - Passive:* When within Melee of a creature and another ally is within Close, attacks have advantage.
- *Pack Tactics - Passive:* On successful attack with another ally in Melee of target, deal \<extra damage\> and gain a Fear.

**Support:**
- *AOE Condition - Action:* **Spend a Fear** to attack all targets within Very Close. Successes become _Restrained_ and _Vulnerable_. Target can break free with a successful Trait Roll.

**Common (any role):**
- *Armor-Shredding Move - Action:* Standard attack; on success, target must mark an Armor Slot without benefits. If unable, mark an additional HP.
- *Conditional Extra Damage - Passive:* On successful attack \<because of condition\>, deal \<higher damage\> instead.
- *Cause Condition - Action:* Target gains \<Condition\>. Describe what it does and how to clear it.

**Undead:**
- *Ghost - Passive:* Resistance to physical damage. **Mark a Stress** to move Close through solid objects.
- *Horrifying - Passive:* Targets who mark HP must also mark a Stress.
- *Unsettling - Passive:* PCs that roll with Fear when attacking mark a Stress.

**Flying:**
- *Flying - Passive:* While flying, +3 bonus to Difficulty.

**Note:** Momentum + Relentless is Fear-neutral. Reserve this combo for truly difficult adversaries only.

### Step 6 — Write the Soft Move
Each role has a suggested soft move for Success with Fear / Failure with Hope moments:

| Role     | Soft Move                                               |
|----------|---------------------------------------------------------|
| Bruiser  | Prepares next strike; gains +1d4 to next attack roll.   |
| Horde    | Rallies; clears 1 HP or 1 Stress.                      |
| Leader   | Encourages an ally; gives advantage on next attack.     |
| Minion   | Moves to surround the target.                           |
| Ranged   | Focuses; adds +X damage to next hit.                    |
| Skulk    | Retreats/disengages to better position.                 |
| Solo     | Dependent on adversary concept.                         |
| Standard | Braces; Difficulty +1 until next GM Turn.               |
| Support  | Clears a condition on self or an ally.                  |

### Step 7 — Brightvale / Emberdawn Setting Integration
If the adversary belongs to the Brightvale setting:
- **Umbra-Touched type:** Critically succeeds on attacks against a PC on a die roll of 19–20. Describe how the Umbra has warped their form.
- Tie to existing lore: [[Umbra]], [[The Apostasy]], [[Medsen]], factions (Slayers, Aetherweaver Academy, Emberguard, etc.).
- Reference existing bestiary for consistency: Revenants, Rotlords, Shatter-Wing Angels, Umbra-Touched Fiends, Fae, Dragons.

---

## Output Format

For each requested tier:

```
### <ADVERSARY NAME>
*<Flavor text: 1–2 sentences in present tense>*

**Motives & Tactics:** <How the adversary behaves in combat>

**Role:** <Role> | **Tier:** <1-4>
**Difficulty:** <N> | **Thresholds:** <Major>/<Severe> | **HP:** <N> | **Stress:** <N>
**ATK:** +<N> | **<Weapon Name>:** <Range> | <dice pool> <damage type>
**Experiences:** <Experience Name> +<N>, <Experience Name> +<N>

#### Features
- **<Feature Name> - <Passive/Action/Reaction>:** <description>
- **<Feature Name> - <Passive/Action/Reaction>:** <description>
```

For **Minions**, replace Thresholds with "None/None" and add the Minion Passive line.
For **Colossal Enemies**, output the shared framework followed by each segment as a sub-block.

---

## Style Guide (MUST follow)
1. **Present tense** for all sentences.
2. **Capitalize**: Stress, Fear, Hope, Ranges (Close, Melee, Very Close, Far, Very Far), Conditions (_Hidden_, _Vulnerable_, _Restrained_ — also italicized), Traits, Armor Slot(s), Evasion, Experience, Countdown types, Minor/Major/Severe, Adversary Names.
3. **Adversary name shorthand**: pick the most representative word if multi-word.
4. **Do not spell out numbers** (except in Relentless: "two times").
5. **Targets** = chosen by attacker. **Creatures** = everything in range. **PCs** = player characters.
6. **Bold** "mark a Stress" when the adversary marks it. Do NOT bold when a target marks it or loses Hope.
7. **Bold** "Spend a Fear" when spending Fear.
8. **Bold** damage dice in features.
9. Damage types: "physical" or "magic" (not "magical"). "Direct physical/magic damage."
10. Feature order: Passives → Actions → Reactions.
11. Reaction Rolls: use "must make" if success AND failure states; "must succeed on" if only failure state.
12. HP is always "HP" (never "Hit Points"), singular and plural.
13. Ranges: "within Close range", "within Far range."

## Design Tips
- Number of dice rolled ≈ tier number. Die type stays roughly the same across tiers.
- For more consistent damage: go down a die size, add +2 to modifier.
- When bumping 2+ tiers, consider adding another feature.
- Mono-typed encounters don't function well — mix roles.
- Fear expenditure dials up encounter lethality significantly.
- Solos are NOT "Legendary Action" creatures — they should still be accompanied by environments or other adversaries.

---

## After Generating
Save the stat block to `Worldbuilding/Bestiary/Daggerheart_Statblocks/<Adversary Name>.md`.
