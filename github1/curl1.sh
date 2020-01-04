#
# Title:curl1.sh
# Description:
# Development Environment: OS X 10.13.6
# Author: G.S. Cole (guycole at gmail dot com)
#
# https://developer.github.com/v3/issues/#list-issues-for-a-repository
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
ACCEPT_MEDIA="Accept: application/vnd.github.full+json"
ACCEPT_TOKEN="Authorization: token 7653a4efa41e865ef96cae2c11e3d6a7eb16ffbf"
GITHUB_TOKEN="57cacbc3b30cb20df433e5a57b7de9192e2147ee"
#
URL="https://api.github.com/repos/shastrax/jaded_traveler/issues"
#
# URL="https://api.github.com/repos/shastrax/jaded_traveler/issues?state=open"
#
# playpen works
# URL="https://api.github.com/repos/guycole/playpen/issues"
#
curl -v -H $ACCEPT_MEDIA -u shastrax@gmail.com $URL
#