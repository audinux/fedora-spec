#!/bin/bash

VERSION=44
CHROOT_PREFIX="fedora-${VERSION}-"

CUTOFF=$(date -d "30 days ago" +%s)
GIT_CUTOFF=$(date -d "30 days ago" '+%Y-%m-%d')

PAGE=1
BUILDS='[]'

echo "### News for $(date '+%B %Y')"

# ----------------------------------------------------------------------
# Récupération des builds COPR du mois pour Fedora $VERSION
# ----------------------------------------------------------------------

while : ; do
    DATA=$(curl -s \
        "https://copr.fedorainfracloud.org/api_3/build/list?ownername=ycollet&projectname=audinux&page=$PAGE")

    COUNT=$(echo "$DATA" | jq '.items | length')
    [ "$COUNT" -eq 0 ] && break

    BUILDS=$(jq -c \
        --argjson cutoff "$CUTOFF" \
        --arg chroot_prefix "$CHROOT_PREFIX" \
        --argjson builds "$BUILDS" '
        $builds + [
            .items[]
            | select(.submitted_on >= $cutoff)
            | select(any(.chroots[]; startswith($chroot_prefix)))
            | {
                name: .source_package.name,
                version: .source_package.version,
                submitted_on: .submitted_on
              }
        ]
    ' <<< "$DATA")

    OLDEST=$(echo "$DATA" | jq '.items[-1].submitted_on')

    [ "$OLDEST" -lt "$CUTOFF" ] && break

    PAGE=$((PAGE + 1))
done

# ----------------------------------------------------------------------
# Récupération des nouvelles specs dans Git
# ----------------------------------------------------------------------

REPO_ROOT=$(git rev-parse --show-toplevel)

NEW_PACKAGES=$(
    cd "$REPO_ROOT" || exit 1

    git log \
        --since="$GIT_CUTOFF" \
        --diff-filter=A \
        --name-only \
        --format= \
        -- '*.spec' |
    awk -F/ 'NF >= 2 {print $1}' |
    sort -u
)

# Convertit la liste en tableau JSON
NEW_PACKAGES_JSON=$(printf '%s\n' "$NEW_PACKAGES" | jq -R -s '
    split("\n")
    | map(select(length > 0))
')

# ----------------------------------------------------------------------
# Déduplication : dernier build de chaque package
# ----------------------------------------------------------------------

MONTH_BUILDS=$(echo "$BUILDS" | jq -c '
    sort_by(.name, .submitted_on)
    | group_by(.name)
    | map(last)
')

# ----------------------------------------------------------------------
# New packages
# ----------------------------------------------------------------------

echo "* new packages"

echo "$MONTH_BUILDS" | jq -r \
    --argjson new_packages "$NEW_PACKAGES_JSON" '
    map(
        select(
            .name as $name |
            ($new_packages | index($name)) != null
        )
    )
    | sort_by(.name)
    | .[]
    | "  * \(.name) \(.version)"
'

# ----------------------------------------------------------------------
# Updated packages
# ----------------------------------------------------------------------

echo "* updated packages"

echo "$MONTH_BUILDS" | jq -r \
    --argjson new_packages "$NEW_PACKAGES_JSON" '
    map(
        select(
            .name as $name |
            ($new_packages | index($name)) == null
        )
    )
    | sort_by(.name)
    | .[]
    | "  * \(.name) \(.version)"
'
