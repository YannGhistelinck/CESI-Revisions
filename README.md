# Révisions Grand Oral CESI — MAALSI

Vault Obsidian de révisions pour le Grand Oral du CESI (certification niveau 7, bac+5).

## Contenu

- **185 fiches de notions** couvrant les 10 thématiques du Grand Oral + 7 fiches transversales (management/gestion de projet)
- **10 fiches thèmes** avec les sujets associés, questions types du jury, et liens transversaux
- **~1 200 flashcards** intégrées (plugin Spaced Repetition), organisées en decks `#flashcards/<Thème>/<Notion>`
- **10 résumés audio** (~10 min chacun) générés par NotebookLM

## Installation

1. Installer [Obsidian](https://obsidian.md/) — **version 1.9 minimum** (les tableaux de notions utilisent le plugin interne *Bases*)
2. Cloner ce repo : `git clone git@github.com:YannGhistelinck/CESI-Revisions.git`
3. Ouvrir le dossier cloné comme vault dans Obsidian (Ouvrir un vault > Ouvrir un dossier existant)
4. Activer les plugins tiers (Paramètres > Plugins tiers) :
   - **Spaced Repetition** — flashcards (déjà installé dans le repo)
   - **Dataview** — requis par le tableau de progression de `Suivi par thème.md`
     (Bases couvre tout le reste ; il ne sait pas encore agréger une propriété de type liste)
5. Copier les templates de suivi pour ta progression personnelle :
   - Copier `Tableaux de suivi/Templates/Suivi par thème.md` → `Tableaux de suivi/Suivi par thème.md`
   - Copier `Tableaux de suivi/Templates/Suivi par notion.md` → `Tableaux de suivi/Suivi par notion.md`

## Comment réviser

- **Par thème** : Ouvrir une fiche thème (ex: `Thèmes/Thème 2 — Cybersécurité.md`) → voir les notions, écouter l'audio, parcourir les questions jury
- **Par notion** : Naviguer dans `Notions/` ou suivre les liens `[[]]` depuis les fiches thèmes
- **Flashcards** : Cliquer sur l'icône "paquet" dans la barre latérale. Les decks sont hiérarchisés
  (`flashcards` → thème → notion) : on peut réviser un thème entier ou une seule notion
- **Audio** : Les résumés sont intégrés dans chaque fiche thème, ou disponibles dans `Audios/`

## Structure

```
Thèmes/              → 10 fiches hub (sujets, notions, questions jury, audio)
Notions/              → 185 fiches de révision (En bref + Approfondir + Flashcards)
Audios/               → 10 résumés audio NotebookLM
Exports NotebookLM/   → Fichiers sources utilisés pour générer les audios
Tableaux de suivi/    → Suivi personnel (gitignored) + Templates
Templates/            → Templates Obsidian pour les fiches
```

## Thématiques couvertes

1. SI et environnement (18 notions)
2. Cybersécurité (39 notions)
3. Cloud et Virtualisation (38 notions)
4. Big DATA (31 notions)
5. Développement (37 notions)
6. Mobilité (20 notions)
7. Management et stratégie (33 notions)
8. Blockchain (17 notions)
9. IA (32 notions)
10. Optimisation du SI (42 notions)
11. Transversal — Management/Gestion de projet (7 notions)

Les fiches thèmes listent toutes les notions qui les concernent : une notion rattachée à plusieurs thèmes (ex. `RGPD`, qui en déclare 5) apparaît dans chacun d'eux. Le total des décomptes ci-dessus (314) dépasse donc le nombre de fiches (185).

Ces listes sont générées automatiquement depuis le champ `thèmes:` du frontmatter de chaque notion : pour rattacher une notion à un thème, il suffit de l'ajouter à cette liste, il n'y a aucun tableau à tenir à jour.
