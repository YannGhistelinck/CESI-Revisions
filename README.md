# Révisions Grand Oral CESI — MAALSI

Vault Obsidian de révisions pour le Grand Oral du CESI (certification niveau 7, bac+5).

## Contenu

- **185 fiches de notions** couvrant les 10 thématiques du Grand Oral + 7 fiches transversales (management/gestion de projet)
- **10 fiches thèmes** avec les sujets associés, questions types du jury, et liens transversaux
- **~1 200 flashcards** intégrées (plugin Spaced Repetition)
- **10 résumés audio** (~10 min chacun) générés par NotebookLM

## Installation

1. Installer [Obsidian](https://obsidian.md/)
2. Cloner ce repo : `git clone git@github.com:YannGhistelinck/CESI-Revisions.git`
3. Ouvrir le dossier cloné comme vault dans Obsidian (Ouvrir un vault > Ouvrir un dossier existant)
4. Activer le plugin **Spaced Repetition** : Paramètres > Plugins tiers > Activer "Spaced Repetition" (il est déjà installé dans le repo)
5. Copier les templates de suivi pour ta progression personnelle :
   - Copier `Tableaux de suivi/Templates/Suivi par thème.md` → `Tableaux de suivi/Suivi par thème.md`
   - Copier `Tableaux de suivi/Templates/Suivi par notion.md` → `Tableaux de suivi/Suivi par notion.md`

## Comment réviser

- **Par thème** : Ouvrir une fiche thème (ex: `Thèmes/Cybersécurité.md`) → voir les notions, écouter l'audio, parcourir les questions jury
- **Par notion** : Naviguer dans `Notions/` ou suivre les liens `[[]]` depuis les fiches thèmes
- **Flashcards** : Cliquer sur l'icône "paquet" dans la barre latérale pour lancer une session de révision
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

1. SI et environnement (16 notions)
2. Cybersécurité (24 notions)
3. Cloud et Virtualisation (18 notions)
4. Big DATA (21 notions)
5. Développement (25 notions)
6. Mobilité (8 notions)
7. Management et stratégie (14 notions)
8. Blockchain (16 notions)
9. IA (18 notions)
10. Optimisation du SI (18 notions)
11. Transversal — Management/Gestion de projet (7 notions)
