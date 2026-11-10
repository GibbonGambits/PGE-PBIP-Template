#!/bin/bash
# usage: ship.sh "message"
cd /home/user/PGE-PBIP-Template || exit 1
git add guide && git commit -q -m "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_017HhPHV8BymqAtg8QnPKWP6" || exit 1
for d in 0 2 4 8 16; do sleep $d; git push -q origin docs/masterclass-guide 2>&1 && { echo pushed; exit 0; }; done
echo PUSH_FAILED
