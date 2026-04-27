"""
Welcome to Brightvale — page builder
====================================

Generates `Welcome_to_Brightvale.html` (one folder up from this script) by
assembling the data below with the JPEGs in `./images/` as embedded base64.

HOW TO USE
----------
1. Edit any of the data structures below — ANCESTRIES, COMMUNITIES,
   STANDINGS, OLD_HOUSES, RECENT_HOUSES, GUILDS, CLASSES, UMBRA_STAGES.
   Each is a list of tuples; the comments and order should make the shape
   obvious.

2. To swap an image: drop a new JPG into ./images/ named e.g. `slayers.jpg`,
   `caretakers.jpg`, etc. (matching the keys in IMG_KEYS below). The script
   reads whatever JPG is at that path. To resize/compress before drop-in:
       magick "source.png" -resize 1100x1100^> -strip -quality 72 slayers.jpg
   (any image converter works; aim for ~100–250 KB per image)

3. To rebuild, from this folder run:
       python build.py
   The HTML lands at ../Welcome_to_Brightvale.html, replacing the old one.

4. The hero, page-break, and Umbra-section background images are wired to
   `hero.jpg`, `staircase.jpg`, and `effigies.jpg` respectively — see CSS.

5. Quotes are inline strings further down (search for `<blockquote>`).
"""
import base64, pathlib, re

HERE = pathlib.Path(__file__).parent
IMG_DIR = HERE / "images"
WEBSITE_DIR = HERE.parent          # WestmarchesWebsite/ — where the .md files live
OUT = HERE.parent.parent / "index.html"

def b64(name):
    with open(IMG_DIR / f"{name}.jpg", "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

# ---------------------------------------------------------------------------
# Minimal Markdown → HTML converter (for modal content)
# ---------------------------------------------------------------------------
def _inline(t):
    """Handle inline markdown: wikilinks, bold, italic."""
    t = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', t)    # [[target|label]]
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)                 # [[target]]
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)            # [text](url) → text
    t = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*([^*\n]+)\*', r'<em>\1</em>', t)
    t = re.sub(r'_([^_\n]+)_', r'<em>\1</em>', t)
    return t

def md_to_html(text):
    """Convert markdown text to HTML for modal display."""
    lines = text.split('\n')
    out = []
    in_ul = in_ol = in_table = table_header_done = False

    for line in lines:
        stripped = line.strip()

        # Table row (starts with |)
        if stripped.startswith('|'):
            # Separator row (|:---|:---|) — skip
            if re.match(r'^[\s|:\-]+$', stripped) and '-' in stripped:
                continue
            cells = [_inline(c.strip()) for c in stripped.strip('|').split('|')]
            if not in_table:
                out.append('<table class="modal-table"><thead><tr>')
                out.append(''.join(f'<th>{c}</th>' for c in cells))
                out.append('</tr></thead><tbody>')
                in_table = True
                table_header_done = True
            else:
                out.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
            continue
        else:
            if in_table:
                out.append('</tbody></table>')
                in_table = table_header_done = False

        # Empty line — close open lists
        if stripped == '':
            if in_ul:
                out.append('</ul>')
                in_ul = False
            if in_ol:
                out.append('</ol>')
                in_ol = False
            continue

        # Close lists when a non-list line arrives
        if in_ul and not re.match(r'^[-*] ', line):
            out.append('</ul>')
            in_ul = False
        if in_ol and not re.match(r'^\d+\. ', line):
            out.append('</ol>')
            in_ol = False

        # Block elements
        if line.startswith('#### '):
            out.append(f'<h5>{_inline(line[5:])}</h5>')
        elif line.startswith('### '):
            out.append(f'<h4>{_inline(line[4:])}</h4>')
        elif line.startswith('## '):
            out.append(f'<h3>{_inline(line[3:])}</h3>')
        elif line.startswith('# '):
            pass  # Main title already in modal header — skip
        elif stripped == '---':
            out.append('<hr class="modal-hr">')
        elif re.match(r'^[-*] ', line):
            if not in_ul:
                out.append('<ul>')
                in_ul = True
            out.append(f'<li>{_inline(line[2:])}</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_ol:
                out.append('<ol>')
                in_ol = True
            out.append(f'<li>{_inline(re.sub(r"^\d+\. ", "", line))}</li>')
        else:
            out.append(f'<p>{_inline(line)}</p>')

    if in_ul:
        out.append('</ul>')
    if in_ol:
        out.append('</ol>')
    if in_table:
        out.append('</tbody></table>')
    return '\n'.join(out)

IMG_KEYS = ["map","hero","medsen","staircase","village","caretakers","dragon",
    "effigies", "emberguard","slayers","aetherweavers","explorers","venturers_trail",
    "hvergi","ruin","hearthlands","emberfort","other_villages",
    "monster_1","monster_2","monster_3","monster_4","monster_5",
    "monster_6","monster_7","monster_8","monster_9","monster_10"]
IMG = {k: f"data:image/jpeg;base64,{b64(k)}" for k in IMG_KEYS}

ANCESTRIES = [
    ("humankind", "Humankind", "Heirs of the Armisian Empire",
     "Short-lived, ambitious, obsessed with lineage. The most numerous people in the Vale, carriers of the Empire's architecture, law, and habit of organizing everything into Houses.",
     "Their magic, before the Elves taught them otherwise, was pure conviction — fire because you needed fire enough that reality provided it. The Dawnfather's Beacon is the supreme example. Modern human mages use the Arcanum, a borrowed and adapted Elven framework.",
     "Kaleb · Florian · Lucien · Petyr · Matthias · Reinhardt · Narcissa · Liana · Lilianne · Wyll · Azi · Nayar · Thalia · Shadia · Neera"),
    ("elves", "Elves", "Children of the Severed Threshold",
     "Long-lived, precise, and still mourning the Faewilds. Four centuries on, the wound is unresolved. Three philosophical paths fracture them: the Seekers, who would restore the connection; the Scholars, who would solve the Apostasy first; and the Urban Elves, who have made peace with neither.",
     "Their tradition is Formulaic — a spell as the inevitable conclusion of correct reasoning. The hazard is the Arcane Lock: a perfectly consistent framework that one's own mind has ruled out the next step from. Aeldenbarrow, half-concealed by glamours, remains their cultural heart.",
     "Cillian · Ciara · Eira · Maeve · Aodhán · Faolan · Fíadh · Elowen · Enriel · Cirdan · Hwynfer · Taliesin"),
    ("dwarvenkind", "Dwarvenkind", "Rune-Keepers from the Great Sea",
     "They arrived on the Armisian coastline less than a century before the Apostasy — recent enough that the first generation had made the crossing themselves. They knew where home was. The march north severed them from every coast. Brightvale is landlocked, and the Dwarves have not forgotten that.",
     "Hvergi's three ruling clans: Clan Brumdain reads the deep rock and drives the search for a passage northeast; Clan Hjalrim forges the finest blades in Brightvale — crystal-shard steel that glows in the Umbra and burns what it touches; Clan Sigr manages the crystal trade that feeds the Academy's Lumen-craft. The prophecy of Heimsfar — the Homeward Voyage — holds them all: one day they will reach open water, build ships, and return.",
     "Storvald · Hjalrim · Merlos · Brumdain · Dain · Thormor · Tyr · Gyrid · Brigitte · Dyanna · Freyr · Eivor · Sigr"),
    ("halflings", "Halflings", "Guardians of Hearth and Field",
     "Agrarian, communal, tending the Hearthlands and the stories that keep them fertile. They blend practical farming with ritual storytelling they believe keeps the lingering Fae woven into the soil. The harvests do not entirely make sense without it.",
     "Like Elves, they retain a Fae-adjacent connection to the natural world. They are not political the way Humans and Dwarves are political. They tend joy as maintenance, not luxury — work that requires active hands, especially in dark times.",
     "Rosie · Bramble · Tobias · Merric · Calla · Fen · Aldric · Petal · Oswin · Brix"),
    ("orcenfolk", "Orcenfolk", "The Nomadic Senshi",
     "Martial artists and horse-stewards, carriers of the Verse of the Blade. The Vale's surviving horse bloodlines pass through their hands. Through House Kaze, they own the Vale's fastest communication network. Outside Medsen, their clans hold significant autonomy.",
     "The Verse of the Blade — the dominant philosophy among Slayers — is theirs. Combat as craft, craft as identity. A warrior who fights without soul is no better than the things in the Wastes.",
     "Musha · Ryuujin · Orochi · Kasai · Kenshi · Haru · Rin · Hana · Hama · Goro · Goryo · Sakae · Nari · Jin · Nantai"),
    ("infernis", "Infernis", "The Shard-Kin",
     "Children of desperate Apostasy-era pacts, marked in blood and skin. The Infernis did not exist before the cataclysm. They are its inheritance — the consequence of bargains struck in the worst hours of the collapse.",
     "Red-skinned Infernis descend from diabolical pacts: order, contracts, hierarchy. Gray and blue-skinned Infernis descend from demonic pacts: raw power, primal resonance, the chaos of those final hours. House Lugner carries the latter most prominently — and considers it a feature.",
     "Standard human names are common; Caretaker-devoted Infernis often adopt Latinate names: Dante · Maximus · Beatrice · Gabriel · Vergil · Lucia · Augustus · Cassius · Sylvia · Orpheus"),
]

COMMUNITIES = [
    ("Highborne", "Noble House circles in Medsen — ballrooms, inheritance politics, the weight of a family name."),
    ("Loreborne", "Aurore's Peak among Academy scholars, or a family of archivists and chroniclers."),
    ("Orderborne", "Within the structure of the Emberguard, the Caretakers, or another institutional framework."),
    ("Ridgeborne", "Mountain edges — Hvergi, the mining camps, or remote plateau settlements."),
    ("Seaborne", "Cultural memory of the Dwarven Great Sea or the lost Armisian coastlines — water in a world that has none. For a Dwarven character, this is Heimsfar: the prophecy of return to a shore their ancestors left within living memory of the Apostasy."),
    ("Slyborne", "A Slyborne character may have grown up in a group that operates outside of the law, including all manner of criminals, grifters and con artists."),
    ("Underborne", "Medsen's lower districts, its tunnels, its underside — places people don't talk about."),
    ("Wanderborne", "Moved between settlements — Orcish relay riders, traveling merchants, displaced families that never quite settled."),
    ("Wildborne", "Outside the walls: Aeldenbarrow's druidic enclaves, the Hearthlands' outer edges, where the Beacon's light barely reaches."),
]

STANDINGS = [
    ("None", "No Noble Affiliation",
     "Most Venturers. Common-born, guild-raised, or simply from families that never had titles to lose. You owe nothing to anyone except the guild that trained you. The most dangerous position — no patron, no safety net — and in some ways, the most free."),
    ("Minor", "Minor or Unknown Nobility",
     "A small estate, a rural title, a name that once meant something three generations ago. You are noble in the legal sense but not in any way that opens doors in Medsen. Your claim is real but quiet, and you may be the only person who cares about it."),
    ("Recent", "A Recent House",
     "Your family was elevated <em>after</em> the Apostasy — for services rendered, debts called in, or strategic marriages. Houses Ashwood, Drevorn, Kaze, Ravenna, and Thalum are respected, but the Old Houses never let them forget the difference."),
    ("Old", "An Old House",
     "Your lineage predates the end of the world. Houses Aerincorvus, Aurelian, Iyengar, Kaewdyn, Lugner, and Von Zoltraak carry the weight of Armisian legacy. You were born into expectation, obligation, and a name people recognize. Whether that's a gift or a cage depends on you."),
]

OLD_HOUSES = [
    ("Aerincorvus", "Between two worlds, we are the door.",
     "Crow on silver ivy. Half-Elven lineage, deep ties to druidic communities and Fae researchers. Their Concordance archive documents Fae-contact anomalies. Most of the Vale calls it folklore. Aerincorvus calls that a data point.",
     "Elven heritage · druidic connections · Faewilds research"),
    ("Aurelian", "We remember the sky.",
     "Golden eagle above a half-submerged sun. Former agricultural nobility. Manage the Vale's seed vaults and experimental greenhouses, cultivating crops to thrive under Beacon-light. Reliable conservative votes. Genuinely optimistic — occasionally easy to exploit.",
     "Religious conviction · agrarian background · grief for the lost world"),
    ("Iyengar", "In every tongue, one word: endure.",
     "Crossed blade and quill over an open fist. Half-orc lineage — descended from an ancient marriage with an Orcish Prince. Brightvale's neutral arbitrators. Their Paladins draw power from personal ideals, not divine light — which the Caretakers find quietly offensive.",
     "Diplomatic · legal · Orcish heritage · Paladins of conviction"),
    ("Kaewdyn", "The blood remembers what the mind forgets.",
     "Silver lion holding a pale dragon's scale. Carries draconic resonance from a union with extinct House Rjioha. Their Ashen-Heirs sense the Umbra's resonance directly — a gift with a heavy psychological toll. Mandatory Emberguard service before any leadership claim.",
     "Draconic heritage · martial · innate Umbra-sense"),
    ("Lugner", "Truth is buried. We dig.",
     "A lidded eye over a burning candle. Magisters and deep-weave scholars. Their ancestral matriarch's pact with a Void-Binder produced the Azure Stain — many Lugners are Infernis with gray-blue skin and dark horns. Funds the Old Magic faction at the Academy.",
     "Infernis · scholarly · pre-Apostasy magical history"),
    ("Von Zoltraak", "The old lamp lit the road to the cliff. We build a new one.",
     "Flame in an open hand. Unsentimental about Armisian lineage. Old Magic failed; the Apostasy proves it. Funds Progressive Aetherweaving. Their strategist Drago was sacrificed to the Beacon by Queen Wendreda after the Brightblood War — a portrait hangs in the Crucible, facing the door.",
     "Progressive mages · engineers · practical survival over reverence"),
]

RECENT_HOUSES = [
    ("Ashwood", "The grove outlasts the storm.",
     "A great oak with extending roots. Elevated from foresters who defended the wilderness after the Apostasy. Supplies the Lumen-infused wood the Academy depends on. Three Council cycles spent fighting for a permanent Forested Reserve. The trees, at least, are patient.",
     "Rangers · druids · roots in the common people · conservation"),
    ("Drevorn", "What is held cannot be taken.",
     "Closed fist gripping scales. Out-logisticed the old elite during the Apostasy. Half the Vale's aristocracy owes them money. Patriarch Corvin Drevorn intends to secure a permanent Council seat in his lifetime, and has twenty years of favors to spend.",
     "Merchants · information brokers · Medsen's political underworld"),
    ("Kaze", "(none recorded)",
     "Predominantly Orcenfolk. Rose to nobility through an absolute monopoly on speed — the horse messenger relay. Emberfort to Medsen in under four hours. They know exactly what indispensability is worth.",
     "Orcish characters · messengers · spies · transportation"),
    ("Ravenna", "Every road leads somewhere. We know where.",
     "Crow in flight over a forked road. Couriers and intelligence both. No one lies in a Ravenna post; their clerks recognize inconsistencies. Quiet ambition: become a state-funded, Council-protected intelligence body.",
     "Rogues · information traders · scouts · shadowy connections"),
    ("Thalum", "The mountain holds. So shall we.",
     "Pickaxe and mason's level crossed. Built Brightvale before the Apostasy — literally. Engineering corps designed the plateau's walls. Permanently frustrated by politicians who defer maintenance until structures fail.",
     "Engineers · soldiers · working-class Medsen · little patience for theater"),
]

GUILDS = [
    ("caretakers", "The Caretakers", "Order of the Eternal Hearth",
     "Maintain the Beacon. Without them, the holy fire dims. Without the holy fire, everything else is academic. They perform the Last Rites that prevent Revenants. They distill light into Lumen-Casks. They run the Vale's most extensive charity network. They ask only that you not question what they do behind closed doors.",
     "High Caretaker Kaelen · The Dawnfather Temple, Medsen"),
    ("emberguard", "The Emberguard", "Shield of the Vale",
     "The Vale's military and police. Border defense, civil order, first response when something comes down from the mountains. Their tactical doctrine is the Chain of Flame — overlapping defensive auras that create a temporary pocket of Beacon-adjacent protection in the field. The Ashen Oath leaves a silvery Embermark on the forearm.",
     "Lord Commander Varis Lugner · Emberfort"),
    ("slayers", "The Slayers", "Elite of the Wastes",
     "Specialists called when soldiers are not enough. They hunt Rotlords, Arch-Revenants, Warp-Nests, and things that don't yet have names. The Ingress of Ash leaves them no longer entirely human. Admission requires Venturing into the Wastes and returning with a new piece of knowledge about the Umbra-touched. Hearsay is not sufficient.",
     "First Slayer Makjar One-Eyed · The Pit, Emberfort"),
    ("explorers", "The Explorers' Guild", "Trailblazers of the End-Times",
     "Administrative backbone of every expedition into the Wastes. They set the task boards, maintain the checkpoints, record the maps, and push the Council to be more aggressive about reclaiming what was lost. The highest mortality rate of any institution in Brightvale, and the warmest hall in the coldest profession.",
     "Grand Explorer Mira Ravenna · The Guild-Hall, Emberfort"),
    ("aetherweavers", "The Aetherweaver Academy", "What Was Made Can Be Understood",
     "Carved into the cliffs of Aurore's Peak. Teaches structured arcane magic. Site of the Vale's most significant ideological war — House Lugner backing the Old Magic faction, House Von Zoltraak backing Progressive Aetherweaving. Many scholars have simply relocated to the Crucible to avoid the politics.",
     "The Arch-Aetherweavers · Aurore's Peak"),
]

CLASSES = [
    ("Bard", ["explorers","slayers","caretakers","aetherweavers","emberguard"],
     "Power flows through expression, persuasion, and the manipulation of narrative. Every guild needs people who can inspire, coordinate, and communicate under pressure."),
    ("Druid", ["explorers","aetherweavers"],
     "A tertiary division of the Academy on paper; in practice, most working Druids end up in the Explorers' Guild, where their affinity for terrain and living systems is invaluable in the Wastes."),
    ("Guardian", ["explorers","slayers","caretakers","emberguard"],
     "The backbone of any guild that puts bodies in harm's way. The immovable anchor around which a hunting party pivots."),
    ("Ranger", ["explorers","slayers"],
     "Scouts, pathfinders, and wilderness specialists who map the Wastes and maintain the checkpoint network. Some end up as Slayers — the finest ones do."),
    ("Rogue", ["explorers","slayers","emberguard"],
     "Infiltration, trap-handling, ruin-delving. No home in the Academy or among the Caretakers — institutions that value transparency, neither of which is a Rogue's strong suit."),
    ("Seraph", ["slayers","caretakers","emberguard"],
     "Power from conviction and radiant faith. Spiritual home with the Caretakers; practical use as divine wrath against Umbra-touched horrors with the Slayers."),
    ("Sorcerer", ["caretakers","aetherweavers"],
     "Power innate rather than learned, shaped by bloodline or exposure. The Academy both trains and studies them; the Caretakers employ them where raw luminous energy is needed."),
    ("Warrior", ["explorers","slayers","caretakers","emberguard"],
     "The generalists of violence. Every guild except the Academy counts Warriors in its ranks. The skillset is universally in demand."),
    ("Wizard", ["caretakers","aetherweavers"],
     "Power from study, formulae, and deep arcane principles. The Academy trains them. The Caretakers employ them for ward maintenance and the rituals around the Beacon."),
]

UMBRA_STAGES = [
    ("The Blight", "Sickness of the marrow. Skin shedding. Translucency spreading beneath the surface. Withdrawal to clean air and Beacon light can still halt progression."),
    ("The Warp", "Extra sensory organs bud. Bone-spurs break through skin. Violet ichor replaces blood. Reversal is possible, but difficult — significant Caretaker intervention."),
    ("Unnatural Melding", "In the deepest Umbra, distinct living things fuse into a single, agonized mass of flesh and shadow. No recorded reversal exists."),
]

PLACES = [
    ("medsen",        "Medsen",
     "The seat of the Beacon and the Noble Houses. Its spires rise at the plateau's northern end — ballrooms, inheritance politics, and a light that has not gone out in four hundred years."),
    ("aetherweavers", "Aurore & the Aetherweaver Academy",
     "Carved into the cliffs of Aurore's Peak. The Vale's school of structured arcane magic, and the site of its deepest ideological war — Old Magic against Progressive Aetherweaving."),
    ("hvergi",        "Hvergi",
     "Dwarven stronghold in the eastern peaks. Three ruling clans govern it: Brumdain reads the deep rock, Hjalrim forges the finest blades in Brightvale — crystal-shard steel that glows in the Umbra and burns what it touches — and Sigr manages the crystal trade that feeds the Academy's Lumen-craft. All three carry Heimsfar: the prophecy that one day they will reach open water and sail home."),
    ("ruin",          "Aeldenbarrows",
     "The Elven cultural heart, half-concealed by glamours. Neither entirely in this world nor the Faewilds it once bordered. The Concordance archive is here — so are most of the unanswered questions about the Apostasy."),
    ("emberfort",     "Emberfort",
     "The Vale's southern gate and military stronghold. Every expedition into the Wastes begins and ends here. Home to the Emberguard, the Slayers, and the Explorers' Guild — the last wall between the Enduring and the dark."),
    ("hearthlands",   "The Hearthlands",
     "Halfling farmland in the southwest of the plateau, tended with practical agriculture and ritual storytelling. The harvests do not entirely make sense without the stories. The Vale eats because of the Hearthlands."),
    ("other_villages","Other Villages",
     "Relay posts, mining camps, druidic enclaves, and small communities scattered across the plateau — settlements that chose not to live in Medsen's shadow, and make do on their own terms."),
]

RESOURCES = [
    # (modal-id,  card title,                  card blurb,                                             md filename)
    ("umbra",     "The Umbra",                 "What lives in the dark, and what the dark does to living things.",     "the-umbra.md"),
    ("history",   "A History of the Enduring", "The world's past and its key terms.",                                  "history-and-legendarium.md"),
    ("order",     "The Order of Brightvale",   "Who runs the Vale, and how.",                                          "order-of-brightvale.md"),
    ("guilds",    "The Guilds",                "The five institutions you'll work with.",                               "guilds.md"),
    ("houses",    "The Noble Houses",          "The aristocracy you'll navigate.",                                     "noble-houses.md"),
    ("ancestries","Ancestries &amp; Cultures", "Who the Enduring are.",                                                "ancestries.md"),
    ("rumours",   "Rumours &amp; Whispers",    "What you've heard before the first expedition.",                       "rumours.md"),
]

ICONS = {
    "humankind": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="7" r="3.5"/><path d="M5 21c1-4.5 4-7 7-7s6 2.5 7 7"/></svg>',
    "elves":     '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="9" r="3"/><path d="M8 9l-3-3M16 9l3-3M6 22c1.5-4 4-6 6-6s4.5 2 6 6"/></svg>',
    "dwarvenkind":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="8" r="3"/><path d="M9 11c-1 2-1.5 4-1.5 6h9c0-2-.5-4-1.5-6M10 14l-2 6M14 14l2 6"/></svg>',
    "halflings": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="9" r="3"/><path d="M7 21c1-3.5 3-5.5 5-5.5s4 2 5 5.5M9 21l-1 1M15 21l1 1"/></svg>',
    "orcenfolk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="9" r="3"/><path d="M8 6L6 4M16 6l2-2M6 21c1-4 3-6 6-6s5 2 6 6"/></svg>',
    "infernis":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="10" r="3"/><path d="M9 8C8 5 6 4 5 4c0 3 1 5 3 6M15 8c1-3 3-4 4-4 0 3-1 5-3 6M6 21c1-4 3-6 6-6s5 2 6 6"/></svg>',
    "ember":     '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3c1.5 3 5 5 5 9a5 5 0 01-10 0c0-2 1-3 2-4 0 1 1 2 2 2 0-2-1-4 1-7z"/></svg>',
    "umbra":     '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3c-2 4-6 6-6 11a6 6 0 0012 0c0-5-4-7-6-11z" opacity=".4"/><path d="M12 3c-2 4-6 6-6 11a6 6 0 0012 0c0-5-4-7-6-11z"/></svg>',
    "caretakers":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3v18M3 12h18M7 7l10 10M17 7L7 17"/></svg>',
    "emberguard":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6l8-3z"/><path d="M12 8v8M9 12h6"/></svg>',
    "slayers":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 19l9-9M14 5l5 5M11 8l5 5M5 19h3v-3"/></svg>',
    "explorers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M12 3v18M3 12h18M8 8l8 8M16 8l-8 8" opacity=".5"/></svg>',
    "aetherweavers":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/></svg>',
    "scroll":    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 4h11a3 3 0 013 3v10a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3z"/><path d="M8 9h7M8 13h7M8 17h4"/></svg>',
    "compass":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M15 9l-2 6-4 1 2-6z" fill="currentColor" opacity=".5"/></svg>',
}

# Helpers
def ancestry_card(key, name, subtitle, summary, magic, names):
    return f'''<article class="card ancestry" data-key="{key}">
  <div class="card-head">
    <span class="ico ico-{key}">{ICONS[key]}</span>
    <div><h3>{name}</h3><p class="sub">{subtitle}</p></div>
  </div>
  <p class="lead">{summary}</p>
  <details>
    <summary>Magic & Tradition</summary>
    <p>{magic}</p>
    <p class="names"><span>Names &mdash;</span> {names}</p>
  </details>
</article>'''

def community_chip(name, desc):
    return f'<div class="chip"><span class="chip-name">{name}</span><span class="chip-desc">{desc}</span></div>'

def standing_card(key, name, desc):
    return f'<article class="card standing standing-{key.lower()}"><h3>{name}</h3><p>{desc}</p></article>'

def house_card(name, motto, body, hooks):
    motto_html = f'<p class="motto">&ldquo;{motto}&rdquo;</p>' if motto != "(none recorded)" else '<p class="motto motto-none">No motto recorded</p>'
    return f'''<article class="card house">
  <h4>House {name}</h4>
  {motto_html}
  <p>{body}</p>
  <p class="hook"><span>Good for:</span> {hooks}</p>
</article>'''

def guild_card(key, name, subtitle, body, leader, image_key=None):
    img_block = f'<div class="guild-img" style="background-image:url({IMG[image_key]})"></div>' if image_key else ''
    return f'''<article class="card guild" data-key="{key}">
  {img_block}
  <div class="guild-body">
    <div class="card-head">
      <span class="ico ico-{key}">{ICONS[key]}</span>
      <div><h3>{name}</h3><p class="sub">{subtitle}</p></div>
    </div>
    <p>{body}</p>
    <p class="leader"><span>Leadership &mdash;</span> {leader}</p>
  </div>
</article>'''

def place_card(img_key, name, desc):
    return f'''<article class="card place-card">
  <div class="place-img" style="background-image:url({IMG[img_key]})"></div>
  <div class="place-body">
    <h4>{name}</h4>
    <p>{desc}</p>
  </div>
</article>'''

def class_row(name, guilds, body):
    cells = ""
    for g in ["explorers","slayers","caretakers","aetherweavers","emberguard"]:
        active = "on" if g in guilds else "off"
        glyph = "&#10022;" if active == "on" else "&middot;"
        cells += f'<td class="cell cell-{active}" data-guild="{g}"><span aria-hidden="true">{glyph}</span></td>'
    return f'<tr data-class="{name.lower()}"><th><strong>{name}</strong><span class="class-blurb">{body}</span></th>{cells}</tr>'

places_html = "\n".join(place_card(*p) for p in PLACES)
resource_content = {
    rid: md_to_html((WEBSITE_DIR / fname).read_text(encoding="utf-8"))
    for rid, _title, _blurb, fname in RESOURCES
}
ancestries_html = "\n".join(ancestry_card(*a) for a in ANCESTRIES)
communities_html = "\n".join(community_chip(*c) for c in COMMUNITIES)
standings_html = "\n".join(standing_card(*s) for s in STANDINGS)
old_houses_html = "\n".join(house_card(*h) for h in OLD_HOUSES)
recent_houses_html = "\n".join(house_card(*h) for h in RECENT_HOUSES)
guild_imgs = {"caretakers":"caretakers","emberguard":"emberguard","slayers":"slayers","explorers":"explorers","aetherweavers":"aetherweavers"}
guilds_html = "\n".join(guild_card(*g, image_key=guild_imgs.get(g[0])) for g in GUILDS)
class_rows = "\n".join(class_row(*c) for c in CLASSES)
umbra_stages_html = "\n".join(f'<li><h4>{n}</h4><p>{d}</p></li>' for n,d in UMBRA_STAGES)

CSS = r"""
  :root {
    --bg: #0e0c0a; --bg-2: #15110d; --bg-3: #1d1813;
    --paper: #e8dcc4; --paper-2: #c9bfa8; --paper-dim: #8c8270;
    --ember: #e8a14a; --ember-dim: #b07232;
    --umbra: #6b58a6; --umbra-dim: #3d2a5e;
    --crimson: #8b3a3a;
    --hairline: rgba(232, 220, 196, 0.12);
    --hairline-strong: rgba(232, 161, 74, 0.35);
    --shadow: 0 1rem 3rem rgba(0,0,0,.55);
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; background: var(--bg); color: var(--paper); }
  body {
    font-family: 'EB Garamond', Garamond, 'Times New Roman', serif;
    font-size: 21px; line-height: 1.65; font-weight: 400;
    background-image:
      radial-gradient(1200px 800px at 20% 10%, rgba(232,161,74,.05), transparent 70%),
      radial-gradient(1000px 700px at 80% 80%, rgba(107,88,166,.05), transparent 70%),
      linear-gradient(180deg, #0e0c0a 0%, #120e0a 100%);
    min-height: 100vh;
  }
  ::selection { background: var(--ember); color: var(--bg); }
  h1, h2, h3, h4 {
    font-family: 'Cinzel', 'Trajan Pro', Georgia, serif;
    font-weight: 600; letter-spacing: .04em; color: var(--paper);
    margin: 0 0 .5em;
  }
  h2 { font-size: 2.2rem; line-height: 1.2; letter-spacing: .12em; text-transform: uppercase; }
  h3 { font-size: 1.4rem; }
  h4 { font-size: 1.1rem; letter-spacing: .08em; }
  p { margin: 0 0 1em; }
  em { color: var(--paper-2); }
  a { color: var(--ember); text-decoration: none; border-bottom: 1px dotted var(--ember-dim); }
  a:hover { color: #ffce85; }
  .wrap { max-width: 1180px; margin: 0 auto; padding: 0 2.2rem; }
  section { padding: 6rem 0; position: relative; }
  section + section { border-top: 1px solid var(--hairline); }
  .hero {
    min-height: 96vh; padding: 0;
    display: flex; align-items: center; justify-content: center; text-align: center;
    background:
      linear-gradient(180deg, rgba(14,12,10,.45) 0%, rgba(14,12,10,.7) 60%, rgba(14,12,10,1) 100%),
      url(__HERO__) center / cover no-repeat;
    position: relative;
  }
  .hero-inner { max-width: 800px; padding: 2rem; }
  .hero h1 {
    font-family: 'Cinzel', serif; font-size: clamp(2.4rem, 6vw, 4.6rem);
    font-weight: 600; letter-spacing: .14em; text-transform: uppercase;
    margin: 0 0 .4em; color: var(--paper); text-shadow: 0 4px 30px rgba(0,0,0,.8);
  }
  .hero h1 .ember { color: var(--ember); }
  .hero .kicker {
    font-family: 'Cinzel', serif; font-size: .9rem; letter-spacing: .5em;
    text-transform: uppercase; color: var(--ember); margin-bottom: 2rem;
  }
  .hero .lede { font-style: italic; font-size: 1.25rem; color: var(--paper-2); max-width: 36em; margin: 0 auto 2.5rem; }
  .hero .scroll-cue {
    position: absolute; bottom: 2rem; left: 50%; transform: translateX(-50%);
    font-size: .75rem; letter-spacing: .4em; text-transform: uppercase;
    color: var(--paper-dim); animation: bob 2.4s ease-in-out infinite;
  }
  @keyframes bob { 0%,100% {transform: translateX(-50%) translateY(0);} 50% {transform: translateX(-50%) translateY(8px);} }
  .divider {
    display: flex; align-items: center; justify-content: center; gap: 1rem;
    color: var(--ember-dim); margin: 0 0 3rem;
  }
  .divider::before, .divider::after {
    content: ''; flex: 1; height: 1px;
    background: linear-gradient(90deg, transparent, var(--hairline-strong), transparent);
  }
  .divider svg { width: 28px; height: 28px; }
  .step-num {
    font-family: 'Cinzel', serif; font-size: .8rem; letter-spacing: .5em;
    text-transform: uppercase; color: var(--ember); margin-bottom: .8rem;
  }
  .section-head { text-align: center; margin-bottom: 3rem; }
  .section-head .lede { font-style: italic; color: var(--paper-2); font-size: 1.1rem; max-width: 38em; margin: 0 auto; }
  .grid { display: grid; gap: 1.5rem; }
  .grid-2 { grid-template-columns: repeat(auto-fit, minmax(min(380px, 100%), 1fr)); }
  .grid-3 { grid-template-columns: repeat(auto-fit, minmax(min(280px, 100%), 1fr)); }
  .grid-4 { grid-template-columns: repeat(auto-fit, minmax(min(220px, 100%), 1fr)); }
  .card {
    background: linear-gradient(180deg, var(--bg-2) 0%, var(--bg-3) 100%);
    border: 1px solid var(--hairline); border-radius: 4px;
    padding: 1.6rem 1.7rem; position: relative;
    transition: border-color .25s ease, transform .25s ease;
  }
  .card:hover { border-color: var(--hairline-strong); transform: translateY(-2px); }
  .card h3 { margin: 0 0 .15em; }
  .card .sub {
    font-style: italic; color: var(--ember); margin: 0 0 .9em;
    font-size: 1rem; font-family: 'Cinzel', serif; letter-spacing: .05em; text-transform: none;
  }
  .card .lead { color: var(--paper-2); }
  .card-head { display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 1rem; }
  .ico { flex: 0 0 auto; width: 44px; height: 44px;
    display: inline-flex; align-items: center; justify-content: center;
    border: 1px solid var(--hairline-strong); border-radius: 50%;
    color: var(--ember); background: rgba(232, 161, 74, .06);
  }
  .ico svg { width: 24px; height: 24px; }
  .ancestry details { margin-top: 1rem; }
  .ancestry summary {
    cursor: pointer; color: var(--ember); font-family: 'Cinzel', serif;
    letter-spacing: .1em; font-size: .85rem; text-transform: uppercase;
    list-style: none; padding: .5rem 0; border-top: 1px solid var(--hairline);
    transition: color .2s ease;
  }
  .ancestry summary::-webkit-details-marker { display: none; }
  .ancestry summary::after { content: " +"; }
  .ancestry details[open] summary::after { content: " \2014 "; }
  .ancestry summary:hover { color: #ffce85; }
  .ancestry .names { color: var(--paper-dim); font-size: .95rem; font-style: italic; }
  .ancestry .names span { color: var(--ember); font-style: normal; font-family: 'Cinzel', serif; letter-spacing: .1em; font-size: .82rem; text-transform: uppercase; }
  .communities {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(min(290px, 100%), 1fr));
    gap: .8rem; margin-top: 1.5rem;
  }
  .chip {
    padding: 1rem 1.2rem; border: 1px solid var(--hairline); border-radius: 3px;
    background: rgba(255,255,255,.015); transition: border-color .2s ease;
  }
  .chip:hover { border-color: var(--hairline-strong); }
  .chip-name {
    display: block; font-family: 'Cinzel', serif;
    color: var(--ember); letter-spacing: .12em; font-size: .92rem;
    text-transform: uppercase; margin-bottom: .3em;
  }
  .chip-desc { color: var(--paper-2); font-size: .98rem; line-height: 1.5; }
  .standings { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%), 1fr)); gap: 1.2rem; }
  .standing { position: relative; padding-top: 2.5rem; }
  .standing::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: var(--ember-dim); }
  .standing-recent::before { background: #2a72b3; }
  .standing-old::before { background: var(--ember); }
  .standing-minor::before { background: #5e94c7; }
  .standing-none::before { background: var(--paper-dim); }
  .house h4 { color: var(--ember); font-size: 1.05rem; }
  .house .motto { font-style: italic; color: var(--paper-2); margin: 0 0 1em; }
  .house .motto-none { color: var(--paper-dim); font-size: .88rem; }
  .house .hook {
    font-size: .88rem; color: var(--paper-dim); border-top: 1px solid var(--hairline);
    padding-top: .8rem; margin-top: 1rem; margin-bottom: 0;
  }
  .house .hook span {
    color: var(--ember); font-family: 'Cinzel', serif;
    letter-spacing: .1em; text-transform: uppercase; font-size: .74rem;
  }
  .guild { overflow: hidden; padding: 0; }
  .guild .guild-img {
    height: 220px; background-size: cover; background-position: center;
    border-bottom: 1px solid var(--hairline-strong);
    filter: saturate(.9) contrast(1.05);
  }
  .guild .guild-body { padding: 1.6rem 1.7rem; }
  .guild .leader {
    margin: 1rem 0 0; font-size: .88rem; color: var(--paper-dim);
    border-top: 1px solid var(--hairline); padding-top: .8rem;
  }
  .guild .leader span {
    color: var(--ember); font-family: 'Cinzel', serif;
    letter-spacing: .1em; text-transform: uppercase; font-size: .74rem;
  }
  .matrix-controls {
    display: flex; flex-wrap: wrap; gap: .5rem; justify-content: center; margin: 0 0 2rem;
  }
  .matrix-controls button {
    background: transparent; border: 1px solid var(--hairline-strong);
    color: var(--paper-2); padding: .55rem 1rem; cursor: pointer;
    font-family: 'Cinzel', serif; font-size: .8rem; letter-spacing: .15em;
    text-transform: uppercase; border-radius: 2px; transition: all .2s ease;
  }
  .matrix-controls button:hover { border-color: var(--ember); color: var(--paper); }
  .matrix-controls button.active { background: var(--ember); color: var(--bg); border-color: var(--ember); }
  .matrix-wrap { overflow-x: auto; }
  table.matrix { width: 100%; border-collapse: collapse; margin: 0 auto; min-width: 760px; }
  table.matrix th, table.matrix td {
    padding: 1rem .8rem; vertical-align: middle; border-bottom: 1px solid var(--hairline);
  }
  table.matrix thead th {
    text-align: center; font-family: 'Cinzel', serif; color: var(--ember);
    font-size: .8rem; letter-spacing: .15em; text-transform: uppercase;
    border-bottom: 1px solid var(--hairline-strong); padding-bottom: 1rem;
  }
  table.matrix thead th:first-child { text-align: left; }
  table.matrix tbody th {
    text-align: left; font-weight: 600; max-width: 320px;
    font-family: 'Cinzel', serif; color: var(--paper); font-size: 1rem;
    letter-spacing: .05em;
  }
  table.matrix .class-blurb {
    display: block; font-family: 'EB Garamond', serif; font-weight: 400;
    color: var(--paper-dim); font-size: .9rem; margin-top: .4em;
    letter-spacing: 0; line-height: 1.45; font-style: italic;
  }
  table.matrix .cell { text-align: center; font-size: 1.2rem; }
  table.matrix .cell-on { color: var(--ember); }
  table.matrix .cell-off { color: var(--paper-dim); opacity: .35; }
  table.matrix tbody tr { transition: opacity .25s ease, background .25s ease; }
  table.matrix tbody tr.dim { opacity: .25; }
  table.matrix tbody tr.match { background: rgba(232, 161, 74, .04); }
  table.matrix .cell.highlight { background: rgba(232, 161, 74, .12); color: var(--ember); }
  .umbra-section {
    background:
      linear-gradient(180deg, rgba(14,12,10,.85) 0%, rgba(14,12,10,.96) 100%),
      url(__EFFIGIES__) center / cover no-repeat;
    background-attachment: fixed;
  }
  .umbra-section h2 { color: #c9bfd9; }
  .umbra-section .step-num { color: var(--umbra); }
  .umbra-stages { list-style: none; padding: 0; counter-reset: stage; }
  .umbra-stages li {
    counter-increment: stage; padding: 1.5rem 1.8rem 1.5rem 4.5rem;
    border-left: 2px solid var(--umbra-dim); position: relative;
    margin-bottom: 1rem; background: rgba(0,0,0,.25);
  }
  .umbra-stages li::before {
    content: counter(stage, upper-roman);
    position: absolute; left: 1.2rem; top: 1.4rem;
    font-family: 'Cinzel', serif; color: var(--umbra);
    font-size: 1.4rem; font-weight: 600; letter-spacing: .05em;
  }
  .umbra-stages h4 { color: var(--paper); margin: 0 0 .3em; }
  .creature-row {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: .8rem; margin-top: 2rem;
  }
  .creature {
    aspect-ratio: 3/4; background-size: cover; background-position: center;
    border: 1px solid var(--hairline); overflow: hidden;
    filter: saturate(.92) contrast(1.05);
    transition: transform .25s ease, border-color .25s ease, filter .25s ease;
  }
  .creature:hover { transform: scale(1.02); border-color: var(--umbra); filter: saturate(1.05); }
  .map-section { text-align: center; }
  .place-gallery {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%), 1fr));
    gap: 1.2rem; margin-top: 3.5rem;
  }
  .place-card { overflow: hidden; padding: 0; }
  .place-card .place-img {
    height: 180px; background-size: cover; background-position: center;
    border-bottom: 1px solid var(--hairline-strong);
    filter: saturate(.9) contrast(1.05);
    transition: filter .3s ease;
  }
  .place-card:hover .place-img { filter: saturate(1.05) contrast(1.08); }
  .place-card .place-body { padding: 1.1rem 1.3rem 1.3rem; }
  .place-card h4 { color: var(--ember); font-size: 1rem; margin-bottom: .4em; }
  .place-card p { color: var(--paper-2); font-size: .93rem; margin: 0; line-height: 1.55; }
  .map-section img {
    width: 100%; max-width: 1100px; height: auto;
    border: 1px solid var(--hairline-strong); box-shadow: var(--shadow);
    filter: sepia(.15) saturate(.95);
  }
  .map-caption { color: var(--paper-dim); font-style: italic; margin-top: 1.5rem; font-size: 1rem; }
  .quote-break {
    background-image: linear-gradient(180deg, rgba(14,12,10,.85), rgba(14,12,10,.85)),
      url(__STAIRCASE__);
    background-size: cover; background-position: center; background-attachment: fixed;
    padding: 8rem 0; text-align: center;
  }
  .quote-break blockquote {
    font-family: 'Cinzel', serif; font-style: normal;
    font-size: clamp(1.4rem, 3vw, 2.2rem); line-height: 1.4;
    max-width: 30em; margin: 0 auto; color: var(--paper); letter-spacing: .04em;
  }
  .quote-break cite {
    display: block; margin-top: 1.5rem; font-style: italic;
    color: var(--ember); font-size: .92rem; font-family: 'EB Garamond', serif;
    letter-spacing: .15em; text-transform: uppercase;
  }
  .reflect { list-style: none; padding: 0; max-width: 720px; margin: 0 auto; }
  .reflect li {
    padding: 1.4rem 0; border-bottom: 1px solid var(--hairline); font-size: 1.15rem;
  }
  .reflect li:last-child { border-bottom: 0; }
  .reflect strong {
    display: block; color: var(--ember); font-family: 'Cinzel', serif;
    font-size: .88rem; letter-spacing: .15em; text-transform: uppercase;
    margin-bottom: .3em; font-weight: 600;
  }
  .resources { background: linear-gradient(180deg, var(--bg-2), var(--bg)); }
  .resource-list {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(min(260px, 100%), 1fr));
    gap: 1rem; max-width: 880px; margin: 2rem auto 0;
  }
  .resource-list .card { padding: 1.2rem 1.4rem; }
  .resource-list h4 { color: var(--ember); margin-bottom: .3em; font-size: .95rem; }
  .resource-list p { font-size: .94rem; color: var(--paper-2); margin: 0; }
  footer.foot {
    text-align: center; padding: 4rem 1rem 5rem;
    color: var(--paper-dim); font-size: .85rem;
    border-top: 1px solid var(--hairline);
  }
  footer.foot strong { color: var(--ember); font-family: 'Cinzel', serif; letter-spacing: .15em; }
  .progress {
    position: fixed; right: 1.5rem; top: 50%; transform: translateY(-50%);
    z-index: 50; display: flex; flex-direction: column; gap: .8rem;
  }
  .progress a {
    width: 12px; height: 12px; border-radius: 50%;
    border: 1px solid var(--hairline-strong); background: transparent;
    transition: all .2s ease; position: relative;
  }
  .progress a:hover, .progress a.active { background: var(--ember); border-color: var(--ember); }
  .progress a span {
    position: absolute; right: 22px; top: 50%; transform: translateY(-50%);
    font-family: 'Cinzel', serif; font-size: .72rem; letter-spacing: .15em;
    text-transform: uppercase; color: var(--paper); white-space: nowrap;
    background: var(--bg-2); border: 1px solid var(--hairline-strong);
    padding: .3rem .7rem; opacity: 0; pointer-events: none; transition: opacity .2s ease;
  }
  .progress a:hover span, .progress a.active span { opacity: 1; }
  @media (max-width: 800px) { .progress { display: none; } }
  @media (max-width: 700px) {
    body { font-size: 19px; }
    section { padding: 4rem 0; }
    .wrap { padding: 0 1.2rem; }
    h2 { font-size: 1.6rem; }
  }
  /* Touch devices: kill background-attachment:fixed (causes repaint on every scroll frame)
     !important is required to override the inline styles on step2, step3, quote-breaks. */
  @media (hover: none) {
    * { background-attachment: scroll !important; }
    .modal-overlay, .lightbox-overlay { backdrop-filter: none; }
  }
  .reveal { opacity: 0; transform: translateY(20px); transition: opacity .8s ease, transform .8s ease; }
  .reveal.in { opacity: 1; transform: translateY(0); }
  /* Lightbox */
  .lightbox-overlay {
    position: fixed; inset: 0; z-index: 400;
    background: rgba(0,0,0,.93);
    display: flex; align-items: center; justify-content: center;
    opacity: 0; pointer-events: none;
    transition: opacity .25s ease;
    cursor: zoom-out;
  }
  .lightbox-overlay.open { opacity: 1; pointer-events: all; }
  .lightbox-img {
    max-width: 92vw; max-height: 90vh;
    object-fit: contain;
    border: 1px solid rgba(232,161,74,.25);
    box-shadow: 0 2rem 8rem rgba(0,0,0,.9);
    transform: scale(.96); transition: transform .3s ease;
    cursor: default;
  }
  .lightbox-overlay.open .lightbox-img { transform: scale(1); }
  .lightbox-close {
    position: fixed; top: 1.4rem; right: 1.5rem;
    background: transparent; border: 1px solid rgba(232,220,196,.25);
    color: rgba(232,220,196,.6); font-size: 1rem; cursor: pointer;
    width: 2.3rem; height: 2.3rem;
    display: flex; align-items: center; justify-content: center;
    border-radius: 2px; transition: all .2s ease; z-index: 401;
  }
  .lightbox-close:hover { color: var(--paper); border-color: var(--ember); }
  /* zoom-in cursor on all zoomable image containers */
  .place-img, .creature, .guild-img { cursor: zoom-in; }
  .map-section img { cursor: zoom-in; }
  /* Resource cards — clickable */
  .resource-list .card[data-modal] { cursor: pointer; }
  .resource-list .card[data-modal]:focus { outline: 2px solid var(--ember); outline-offset: 3px; }
  .read-more {
    display: inline-block; margin-top: .7em;
    font-family: 'Cinzel', serif; color: var(--ember);
    font-size: .78rem; letter-spacing: .18em; text-transform: uppercase;
    transition: color .2s ease;
  }
  .card[data-modal]:hover .read-more { color: #ffce85; }
  /* Modal overlay */
  .modal-overlay {
    position: fixed; inset: 0; z-index: 300;
    background: rgba(0,0,0,.8); backdrop-filter: blur(4px);
    display: flex; align-items: center; justify-content: center;
    opacity: 0; pointer-events: none;
    transition: opacity .3s ease;
  }
  .modal-overlay.open { opacity: 1; pointer-events: all; }
  .modal-panel {
    background: var(--bg-2); border: 1px solid var(--hairline-strong);
    max-width: 800px; width: 92%; max-height: 86vh;
    overflow-y: auto; padding: 2.8rem 3.2rem;
    border-radius: 4px; box-shadow: 0 2rem 6rem rgba(0,0,0,.75);
    position: relative;
    transform: translateY(28px); transition: transform .35s ease;
  }
  .modal-overlay.open .modal-panel { transform: translateY(0); }
  .modal-close {
    position: sticky; top: 0; float: right;
    margin: -.5rem -1.2rem 1rem 2rem;
    background: transparent; border: 1px solid var(--hairline-strong);
    color: var(--paper-dim); font-size: .95rem; cursor: pointer;
    width: 2.1rem; height: 2.1rem;
    display: flex; align-items: center; justify-content: center;
    border-radius: 2px; transition: all .2s ease; z-index: 10;
  }
  .modal-close:hover { color: var(--paper); border-color: var(--ember); }
  /* Modal content typography */
  .modal-content h2 { display: none; }   /* title shown in header already */
  .modal-content h3 { font-size: 1.2rem; color: var(--ember); margin: 2em 0 .6em; letter-spacing: .08em; }
  .modal-content h4 { font-size: 1.05rem; color: var(--paper); margin: 1.6em 0 .4em; }
  .modal-content h5 { font-size: .95rem; color: var(--ember-dim); font-family: 'Cinzel',serif; letter-spacing: .1em; text-transform: uppercase; margin: 1.2em 0 .3em; }
  .modal-content p { color: var(--paper-2); margin: 0 0 .85em; font-size: 1rem; }
  .modal-content strong { color: var(--paper); }
  .modal-content em { color: var(--paper-dim); font-style: italic; }
  .modal-content ul, .modal-content ol { padding-left: 1.4em; margin: 0 0 1em; }
  .modal-content li { color: var(--paper-2); margin-bottom: .4em; font-size: 1rem; }
  .modal-content hr.modal-hr { border: none; border-top: 1px solid var(--hairline); margin: 1.8rem 0; }
  .modal-content table.modal-table { width: 100%; border-collapse: collapse; margin: .8em 0 1.5em; font-size: .95rem; }
  .modal-content table.modal-table th { text-align: left; color: var(--ember); font-family: 'Cinzel',serif; font-size: .78rem; letter-spacing: .12em; text-transform: uppercase; padding: .55rem .8rem; border-bottom: 1px solid var(--hairline-strong); }
  .modal-content table.modal-table td { color: var(--paper-2); padding: .55rem .8rem; border-bottom: 1px solid var(--hairline); vertical-align: top; }
  .modal-header { margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid var(--hairline-strong); }
  .modal-header h2 { font-size: 1.6rem; color: var(--paper); margin: 0; }
  @media (max-width: 700px) {
    .modal-panel { padding: 1.8rem 1.4rem; max-height: 90vh; }
  }
"""
CSS = CSS.replace("__HERO__", IMG["hero"]).replace("__EFFIGIES__", IMG["effigies"]).replace("__STAIRCASE__", IMG["staircase"])


JS = r"""
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));

  const matrix = document.querySelector('table.matrix');
  document.querySelectorAll('.matrix-controls button').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.matrix-controls button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      matrix.querySelectorAll('tbody tr').forEach(row => {
        row.classList.remove('dim','match');
        row.querySelectorAll('.cell').forEach(c => c.classList.remove('highlight'));
        matrix.querySelectorAll('thead th').forEach(th => th.classList.remove('highlight'));
        if (filter === 'all') return;
        const cell = row.querySelector('.cell[data-guild="' + filter + '"]');
        const isOn = cell && cell.classList.contains('cell-on');
        if (isOn) { row.classList.add('match'); cell.classList.add('highlight'); }
        else { row.classList.add('dim'); }
        const colHead = matrix.querySelector('thead th[data-guild="' + filter + '"]');
        if (colHead) colHead.classList.add('highlight');
      });
    });
  });

  const sections = ['welcome','world','umbra','begin','step1','step2','step3','step4','step5','resources'];
  const navLinks = {};
  sections.forEach(id => { navLinks[id] = document.querySelector('.progress a[href="#' + id + '"]'); });
  const navIo = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      const id = e.target.id;
      if (e.isIntersecting && navLinks[id]) {
        Object.values(navLinks).forEach(a => a && a.classList.remove('active'));
        navLinks[id].classList.add('active');
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  sections.forEach(id => { const s = document.getElementById(id); if (s) navIo.observe(s); });

  document.querySelectorAll('.progress a, a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth' }); }
    });
  });

  // Lightbox
  const lb      = document.getElementById('lightbox');
  const lbImg   = lb.querySelector('.lightbox-img');
  const lbClose = lb.querySelector('.lightbox-close');
  function bgSrc(el) {
    return el.style.backgroundImage.replace(/^url\(["']?/, '').replace(/["']?\)$/, '');
  }
  function openLightbox(src) {
    lbImg.src = src;
    lb.classList.add('open');
    document.body.style.overflow = 'hidden';
    lbClose.focus();
  }
  function closeLightbox() {
    lb.classList.remove('open');
    document.body.style.overflow = '';
    lbImg.src = '';
  }
  document.querySelectorAll('.place-img, .creature, .guild-img').forEach(el => {
    el.addEventListener('click', e => { e.stopPropagation(); openLightbox(bgSrc(el)); });
  });
  document.querySelectorAll('.map-section img').forEach(el => {
    el.addEventListener('click', () => openLightbox(el.src));
  });
  lb.addEventListener('click', e => { if (e.target === lb) closeLightbox(); });
  lbClose.addEventListener('click', closeLightbox);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && lb.classList.contains('open')) closeLightbox();
  });

  // Resource modals
  function openModal(id) {
    const overlay = document.getElementById('modal-' + id);
    if (!overlay) return;
    overlay.classList.add('open');
    overlay.querySelector('.modal-close').focus();
    document.body.style.overflow = 'hidden';
  }
  function closeModal(overlay) {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }
  document.querySelectorAll('[data-modal]').forEach(card => {
    card.addEventListener('click', () => openModal(card.dataset.modal));
    card.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(card.dataset.modal); }
    });
  });
  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', e => { if (e.target === overlay) closeModal(overlay); });
  });
  document.querySelectorAll('.modal-close').forEach(btn => {
    btn.addEventListener('click', () => closeModal(btn.closest('.modal-overlay')));
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      document.querySelectorAll('.modal-overlay.open').forEach(closeModal);
    }
  });
"""

# Build HTML
parts = []
parts.append('<!doctype html><html lang="en"><head>')
parts.append('<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">')
parts.append('<title>Welcome to Brightvale &mdash; A Venturer\'s Primer</title>')
parts.append('<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">')
parts.append('<style>' + CSS + '</style></head><body>')

parts.append('''<nav class="progress" aria-label="Section navigation">
  <a href="#welcome"><span>Welcome</span></a>
  <a href="#world"><span>The Vale</span></a>
  <a href="#umbra"><span>The Umbra</span></a>
  <a href="#begin"><span>Begin</span></a>
  <a href="#step1"><span>Heritage</span></a>
  <a href="#step2"><span>Standing</span></a>
  <a href="#step3"><span>Guild</span></a>
  <a href="#step4"><span>Class</span></a>
  <a href="#step5"><span>Together</span></a>
  <a href="#resources"><span>Resources</span></a>
</nav>''')

parts.append('''<header class="hero">
  <div class="hero-inner">
    <p class="kicker">A Venturer's Primer</p>
    <h1>Welcome to <span class="ember">Brightvale</span></h1>
    <p class="lede">The gods departed without warning or explanation. The sky closed. A crimson veil choked the light and let in the dark &mdash; a darkness that thinks, that hungers, that remembers. Four hundred years ago, the world ended. In a single valley, a single flame still burns.</p>
    <p style="font-family:'Cinzel',serif; letter-spacing:.4em; color:var(--paper-dim); font-size:.8rem; text-transform:uppercase;">A West Marches Campaign &mdash; Daggerheart</p>
  </div>
  <div class="scroll-cue">Scroll to begin</div>
</header>''')

parts.append('''<section id="welcome" class="reveal"><div class="wrap">
  <div class="section-head">
    <p class="step-num">Prologue</p>
    <h2>The World</h2>
    <p class="lede">What you need to know before you put a name on a sheet.</p>
  </div>
  <div class="divider">''' + ICONS["ember"] + '''</div>
  <div class="grid grid-2">
    <div>
      <p>Beyond the gates of <strong>Emberfort</strong>, the land is claimed by the <strong>Umbra</strong> &mdash; an ancient, sentient darkness that corrodes everything it touches. Cities have fallen. Civilizations have collapsed. The great <strong>Armisian Empire</strong>, which once spanned continents and commanded dragons, exists now only in ruins beneath the shadow.</p>
      <p>Brightvale is a plateau carved into the Teardrop Mountains, protected from the worst of the Umbra by two things: its altitude and its <strong>Beacon</strong> &mdash; a pillar of holy fire at the heart of Medsen, ignited four centuries ago by a man called the Dawnfather, who gave his soul to make it burn. Without it, the valley dies. With it, the Enduring survive.</p>
      <p><em>Survive. Not thrive. Survive.</em></p>
    </div>
    <div>
      <p>You are a <strong>Venturer</strong> &mdash; one of the brave, reckless, or simply desperate souls who descend from the plateau into the Wastes below. Not soldiers. Not scholars. Venturers are a class unto themselves: specialists in surviving conditions that kill everyone else.</p>
      <p>Every Venturer belongs to one of the five <strong>Guilds</strong> that organise life beyond the walls. Guilds care little about your ancestry and blood. Your guild shapes your training and who signs your contracts &mdash; but in the field, the Wastes don't care what badge you carry.</p>
      <p>Brightvale is not a world of hope, exactly &mdash; but it is a world of <em>endurance</em>. The people who live here have chosen, every day, to keep going. That choice has weight. So do its costs.</p>
    </div>
  </div>
</div></section>''')

parts.append(f'''<section id="world" class="map-section reveal"><div class="wrap">
  <div class="section-head">
    <p class="step-num">Geography</p>
    <h2>The Vale</h2>
    <p class="lede">A teardrop of life in a sea of shadow.</p>
  </div>
  <img src="{IMG["map"]}" alt="Map of Brightvale" loading="lazy">
  <p class="map-caption">Medsen rises at the north end of the plateau. The Hearthlands feed the Vale from the southwest. Aurore's Peak teaches at the centre, close to the Aeldenbarrows. Emberfort guards the only safe descent. Beyond the ring of mountains: the Wastes.</p>
  <div class="place-gallery">{places_html}</div>
</div></section>''')

parts.append(f'''<section id="umbra" class="umbra-section reveal"><div class="wrap">
  <div class="section-head">
    <p class="step-num">The Threat</p>
    <h2>The Umbra</h2>
    <p class="lede">It is not mere darkness. It is a hive-minded shroud that thinks, that hungers, that remembers.</p>
  </div>
  <div class="divider">{ICONS["umbra"]}</div>
  <div class="grid grid-2">
    <div>
      <p>The Umbra manifests as a clinging liquid darkness that settles into lowlands, ravines, and the spaces beneath things. Only altitude and the Beacon's light push it back. Outside the plateau, it is everywhere. In the Wastes, the air itself is its territory.</p>
      <p>It hungers for magic. The greater the arcane potency, the faster it comes. The most powerful wizards were consumed first. Dragons, beings of inherent magical nature, suffered the same fate.</p>
      <p>It emits a constant low vibration &mdash; a <strong>Malignant Echo</strong> &mdash; felt more than heard. Extended exposure degrades focus, then memory, then thought.</p>
    </div>
  </div>
  <div style="margin-top: 4rem;">
    <h3 style="text-align:center; color:var(--paper); margin-bottom: 1.5rem;">What Walks There</h3>
    <div class="creature-row">
      <div class="creature" style="background-image:url({IMG["dragon"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_1"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_2"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_3"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_4"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_5"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_6"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_7"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_8"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_9"]})"></div>
      <div class="creature" style="background-image:url({IMG["monster_10"]})"></div>
    </div>
    <p style="text-align:center; margin-top:1.5rem; color: var(--paper-dim); font-style: italic; max-width: 38em; margin-left:auto; margin-right:auto;">The full subversion of a mind to the Umbra is called <strong style="color:var(--paper-2)">Hollowing</strong>. The shell reanimates with cold, instinctive cunning. A Hollowed soldier still fights like a soldier. A Hollowed mage still casts.</p>
    <p style="text-align:center; margin-top:1.2rem;"><a href="https://pt.pinterest.com/cfonsecahenriqu/emberdawn/nox-touched-monsters/" target="_blank" rel="noopener" style="font-family:\'Cinzel\',serif; font-size:.8rem; letter-spacing:.2em; text-transform:uppercase;">See more &rarr;</a></p>
  </div>
</div></section>''')

parts.append('''<section class="quote-break reveal"><div class="wrap"><blockquote>
  &ldquo;There is a stair in the Rift that descends for nine days. The maps end because the cartographers end. I am not finished walking it.&rdquo;
  <cite>Grand Explorer Mira Ravenna</cite>
</blockquote></div></section>''')

parts.append('''<section id="begin"><div class="wrap"><div class="section-head reveal">
  <p class="step-num">Character Creation</p>
  <h2>Building a Venturer</h2>
  <p class="lede">Five steps. Take them in order &mdash; or don't. <em>Before you choose what your character can do, decide who they are.</em></p>
</div></div></section>''')

parts.append(f'''<section id="step1" class="reveal"><div class="wrap">
  <div class="section-head">
    <p class="step-num">Step 1 of 5</p>
    <h2>Heritage</h2>
    <p class="lede">Your <strong>Heritage</strong> is two things at once: your <strong>Ancestry</strong> &mdash; the people you were born from &mdash; and your <strong>Community</strong>, the place that shaped you.</p>
  </div>
  <div class="divider">{ICONS["scroll"]}</div>
  <h3 style="text-align:center; color: var(--ember); font-family:'Cinzel',serif; letter-spacing:.2em; font-size:.95rem; text-transform:uppercase; margin-bottom: 2rem;">Six Ancestries</h3>
  <div class="grid grid-2">{ancestries_html}</div>
  <div class="divider" style="margin: 4rem 0 2rem;">{ICONS["compass"]}</div>
  <h3 style="text-align:center; color: var(--ember); font-family:'Cinzel',serif; letter-spacing:.2em; font-size:.95rem; text-transform:uppercase; margin-bottom: 1rem;">Nine Communities</h3>
  <p style="text-align:center; color: var(--paper-2); font-style: italic; max-width: 40em; margin: 0 auto 1rem;">Where in Brightvale were you raised? In Daggerheart terms, this is your Community card.</p>
  <div class="communities">{communities_html}</div>
</div></section>''')

parts.append(f'''<section id="step2" class="reveal" style="background-image: linear-gradient(180deg, rgba(14,12,10,.92), rgba(14,12,10,.98)), url({IMG["medsen"]}); background-size: cover; background-position: center; background-attachment: fixed;">
<div class="wrap">
  <div class="section-head">
    <p class="step-num">Step 2 of 5</p>
    <h2>Nobility &amp; Standing</h2>
    <p class="lede">Not every Venturer comes from the gutter. Not every Venturer comes from a Great House. Pick one.</p>
  </div>
  <div class="standings">{standings_html}</div>
  <div style="margin-top: 4rem;">
    <details>
      <summary style="cursor:pointer; text-align:center; color:var(--ember); font-family:'Cinzel',serif; letter-spacing:.2em; font-size:.88rem; text-transform:uppercase; padding:1rem; border:1px solid var(--hairline-strong); display:block;">+ The Six Old Houses</summary>
      <div class="grid grid-3" style="margin-top: 1.5rem;">{old_houses_html}</div>
    </details>
    <details style="margin-top: 1rem;">
      <summary style="cursor:pointer; text-align:center; color:var(--ember); font-family:'Cinzel',serif; letter-spacing:.2em; font-size:.88rem; text-transform:uppercase; padding:1rem; border:1px solid var(--hairline-strong); display:block;">+ The Five Recent Houses</summary>
      <div class="grid grid-3" style="margin-top: 1.5rem;">{recent_houses_html}</div>
    </details>
  </div>
</div></section>''')

parts.append(f'''<section id="step3" class="reveal" style="background-image: linear-gradient(180deg, rgba(14,12,10,.93), rgba(14,12,10,.97)), url({IMG["venturers_trail"]}); background-size: cover; background-position: center; background-attachment: fixed;">
<div class="wrap">
  <div class="section-head">
    <p class="step-num">Step 3 of 5</p>
    <h2>Your Guild</h2>
    <p class="lede">Every Venturer belongs to one of five Guilds. Your guild is your training, your mandate, and who signs your contracts.</p>
  </div>
  <div class="divider">{ICONS["ember"]}</div>
  <div class="grid grid-2">{guilds_html}</div>
</div></section>''')

parts.append(f'''<section id="step4" class="reveal"><div class="wrap">
  <div class="section-head">
    <p class="step-num">Step 4 of 5</p>
    <h2>Your Class</h2>
    <p class="lede">In Daggerheart, your Class is an <em>abstraction of skillset</em> &mdash; a way of categorising what you're good at, not prescribing who you are. <strong>A Bard does not have to be a singer.</strong> A Wizard is not necessarily a robed academic. A Warrior is not necessarily a brute.</p>
  </div>
  <div class="matrix-controls" role="group" aria-label="Filter by guild">
    <button data-filter="all" class="active">All Guilds</button>
    <button data-filter="explorers">Explorers</button>
    <button data-filter="slayers">Slayers</button>
    <button data-filter="caretakers">Caretakers</button>
    <button data-filter="aetherweavers">Aetherweavers</button>
    <button data-filter="emberguard">Emberguard</button>
  </div>
  <div class="matrix-wrap">
    <table class="matrix">
      <thead><tr>
        <th>Class</th>
        <th data-guild="explorers">Explorers</th>
        <th data-guild="slayers">Slayers</th>
        <th data-guild="caretakers">Caretakers</th>
        <th data-guild="aetherweavers">Aetherweavers</th>
        <th data-guild="emberguard">Emberguard</th>
      </tr></thead>
      <tbody>{class_rows}</tbody>
    </table>
  </div>
  <p style="text-align:center; color: var(--paper-dim); font-style:italic; margin-top: 1.5rem; font-size: .95rem;">Filter the table by guild to see which classes have an established home there.</p>
</div></section>''')

parts.append(f'''<section class="quote-break reveal" style="background-image: linear-gradient(180deg, rgba(14,12,10,.85), rgba(14,12,10,.85)), url({IMG["village"]}); background-attachment: fixed;">
<div class="wrap"><blockquote>
  &ldquo;The Scholars talk of the Umbra as a darkness to be feared. We know it as a beast to be bled.&rdquo;
  <cite>First Slayer Makjar One-Eyed</cite>
</blockquote></div></section>''')

parts.append(f'''<section id="step5" class="reveal"><div class="wrap">
  <div class="section-head">
    <p class="step-num">Step 5 of 5</p>
    <h2>Putting It Together</h2>
    <p class="lede">You have your Heritage, your standing, your guild, and your class. The bones are set. The rest is yours.</p>
  </div>
  <div class="divider">{ICONS["compass"]}</div>
  <ul class="reflect">
    <li><strong>Why did you become a Venturer?</strong> Duty? Desperation? Curiosity? Debt? Glory? A death wish that hasn't been granted yet?</li>
    <li><strong>What does your guild mean to you?</strong> A family? A paycheck? A cause? An obligation you're trying to escape?</li>
    <li><strong>What do you carry from your heritage?</strong> A name? A grudge? A tradition? A gap where a memory used to be?</li>
    <li><strong>What are you afraid of in the Wastes?</strong> Everyone is afraid of something. The ones who say otherwise haven't been out long enough.</li>
    <li><strong>What is Brightvale to you?</strong> A prison? A haven? Home?</li>
  </ul>
  <p style="text-align:center; margin-top: 3rem; color: var(--paper-2); font-style: italic; max-width: 36em; margin-left: auto; margin-right: auto;">The Wastes will test every answer you give here. Pack accordingly.</p>
</div></section>''')

resource_cards = "\n".join(
    f'<article class="card" data-modal="{rid}" role="button" tabindex="0" aria-haspopup="dialog">'
    f'<h4>{title}</h4><p>{blurb}</p>'
    f'<span class="read-more">Read &rarr;</span></article>'
    for rid, title, blurb, _ in RESOURCES
)
parts.append(f'''<section id="resources" class="resources reveal"><div class="wrap">
  <div class="section-head">
    <p class="step-num">Before First Session</p>
    <h2>Read Next</h2>
    <p class="lede">When you're ready to go deeper.</p>
  </div>
  <div class="resource-list">{resource_cards}</div>
</div></section>''')

parts.append('''<footer class="foot">
  <p><strong>Brightvale</strong> &middot; A Daggerheart West Marches Campaign</p>
  <p style="margin-top: .5em;">May the Beacon hold.</p>
</footer>''')

# Lightbox
parts.append(
    '<div id="lightbox" class="lightbox-overlay">'
    '<button class="lightbox-close" aria-label="Close">&#x2715;</button>'
    '<img class="lightbox-img" src="" alt="">'
    '</div>'
)

# Modal overlays — one per resource
for rid, title, _blurb, _ in RESOURCES:
    parts.append(
        f'<div class="modal-overlay" id="modal-{rid}" role="dialog" aria-modal="true" aria-labelledby="modal-title-{rid}">'
        f'<div class="modal-panel">'
        f'<button class="modal-close" aria-label="Close">&#x2715;</button>'
        f'<div class="modal-header"><h2 id="modal-title-{rid}">{title}</h2></div>'
        f'<div class="modal-content">{resource_content[rid]}</div>'
        f'</div></div>'
    )

parts.append('<script>' + JS + '</script></body></html>')

HTML = "\n".join(parts)

pathlib.Path(OUT).parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"Wrote {OUT}")
print(f"Size: {OUT.stat().st_size:,} bytes")
