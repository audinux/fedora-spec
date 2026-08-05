#!/usr/bin/env bash
#
# generate-module-screenshots.sh
#
# Génère les screenshots des modules d'une librairie VCV Rack venant d'être
# buildée, en isolant le plugin dans un dossier de travail dédié pour ne pas
# capturer les autres plugins qui pourraient être présents sur la machine de
# build. Conçu pour être appelé depuis %build ou %install d'un .spec RPM.
#
# Usage:
#   ./generate-module-screenshots.sh <slug_plugin> <dist_dir> <rack_bin> <output_dir> [zoom]
#
# Exemple:
#   ./generate-module-screenshots.sh MyPlugin ./dist/MyPlugin /usr/bin/Rack \
#       ./build/screenshots 1
#
set -euo pipefail

SLUG="${1:?slug du plugin manquant}"
DIST_DIR="${2:?chemin vers le dossier dist/<slug> manquant}"
RACK_BIN="${3:?chemin vers executable Rack manquant}"
OUTPUT_DIR="${4:?dossier de sortie manquant}"
ZOOM="${5:-1}"   # facteur, PAS un pourcentage (1 = 100%, 1.5 = 150%, etc.)

# --- Vérifications préalables -----------------------------------------------

if [[ ! -d "$DIST_DIR" ]]; then
    echo "Erreur: dossier dist introuvable: $DIST_DIR" >&2
    exit 1
fi

if [[ ! -x "$RACK_BIN" ]]; then
    echo "Erreur: binaire Rack introuvable ou non exécutable: $RACK_BIN" >&2
    exit 1
fi

if ! command -v xvfb-run >/dev/null 2>&1; then
    echo "Erreur: xvfb-run n'est pas installé (paquet xorg-x11-server-Xvfb / xvfb)" >&2
    exit 1
fi

# --- Détection de l'arch, pour le nom du dossier plugins-<os>-<cpu> ---------

case "$(uname -m)" in
    x86_64) CPU="x64" ;;
    aarch64) CPU="arm64" ;;
    *) echo "Erreur: architecture non gérée: $(uname -m)" >&2; exit 1 ;;
esac
OS="lin"   # ce script vise un build RPM donc Linux

# --- Préparation du workdir isolé -------------------------------------------

WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

PLUGDIR="$WORKDIR/plugins-${OS}-${CPU}/${SLUG}"
mkdir -p "$PLUGDIR"
cp -a "$DIST_DIR"/. "$PLUGDIR"/

echo "Workdir isolé: $WORKDIR"
echo "Plugin copié dans: $PLUGDIR"

# --- Lancement de Rack en mode dev sous Xvfb --------------------------------
#
# -d / --dev fixe les dossiers système ET utilisateur au cwd courant. Comme
# le workdir ne contient que notre plugin (Core reste toujours chargé, car il
# fait partie du binaire Rack lui-même), on filtrera son sous-dossier ensuite.
#
# LIBGL_ALWAYS_SOFTWARE force le rendu logiciel Mesa (llvmpipe), utile sur les
# machines de build sans GPU/driver — même logique que pour JUCE en headless.

pushd "$WORKDIR" >/dev/null

LIBGL_ALWAYS_SOFTWARE=1 xvfb-run -a --server-args="-screen 0 1920x1080x24" \
    "$RACK_BIN" -d --screenshot "$ZOOM"

popd >/dev/null

# --- Vérification et récupération des résultats -----------------------------

SRC_SCREENSHOTS="$WORKDIR/screenshots/${SLUG}"

if [[ ! -d "$SRC_SCREENSHOTS" ]]; then
    echo "Erreur: aucun screenshot généré pour ${SLUG} (dossier attendu: $SRC_SCREENSHOTS)" >&2
    exit 1
fi

COUNT="$(find "$SRC_SCREENSHOTS" -name '*.png' | wc -l)"
if [[ "$COUNT" -eq 0 ]]; then
    echo "Erreur: dossier de screenshots vide pour ${SLUG}" >&2
    exit 1
fi

mkdir -p "$OUTPUT_DIR"
cp -a "$SRC_SCREENSHOTS"/. "$OUTPUT_DIR"/

echo "OK: $COUNT screenshot(s) copié(s) vers $OUTPUT_DIR"
