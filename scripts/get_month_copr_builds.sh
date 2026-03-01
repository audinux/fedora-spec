#/bin/bash

#SINCE=$(date -d "30 days ago" +%s)

#curl -s "https://copr.fedorainfracloud.org/api_3/build/list?ownername=ycollet&projectname=audinux&since=$SINCE" \
#| jq -r '.items[] 
#| "\(.source_package.name) \(.source_package.version) - \(.submitted_on | strftime("%Y-%m-%d"))"'


CUTOFF=$(date -d "30 days ago" +%s)
PAGE=1

while : ; do
  DATA=$(curl -s "https://copr.fedorainfracloud.org/api_3/build/list?ownername=ycollet&projectname=audinux&page=$PAGE")
  
  COUNT=$(echo "$DATA" | jq '.items | length')
  [ "$COUNT" -eq 0 ] && break

  echo "$DATA" | jq -r --argjson cutoff "$CUTOFF" '
    .items[]
    | select(.submitted_on >= $cutoff)
    | "  * \(.source_package.name) \(.source_package.version)"
  '
#    | "  * \(.source_package.name) \(.source_package.version) - \(.submitted_on | strftime("%Y-%m-%d"))"

  # Stop si les builds deviennent plus vieux que 30 jours
  OLDEST=$(echo "$DATA" | jq '.items[-1].submitted_on')
  [ "$OLDEST" -lt "$CUTOFF" ] && break

  PAGE=$((PAGE+1))
done
