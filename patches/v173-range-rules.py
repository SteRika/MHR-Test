from pathlib import Path

p = Path("android-project/app/src/main/assets/app.js")
s = p.read_text()

old = "const ranks = {front:1,wingL:2,wingR:2,back:3};"
new = """const targetDepth = Object.freeze({front:1,wingL:2,wingR:2,back:3});
function targetInRange(w,attackerSlot,targetSlot){const attacker=game?.[w]?.board?.[attackerSlot];if(!attacker)return false;const depth=targetDepth[targetSlot];if(!depth)return false;return effectiveRange(w,attacker,attackerSlot)>=depth;}"""
if old not in s:
    raise SystemExit("range rank declaration not found")
s = s.replace(old, new, 1)

old = "function legalTarget(w,slot,target){const c=game[w].board[slot];if(!c)return false;if(ranks[target]>effectiveRange(w,c,slot))return false;if(c.flags.secondCharacterOnly&&c.attacksLeft===1&&!game[other(w)].board[target])return false;if(c.attachments?.some(a=>a.code==='BP01-098')){const t=game[other(w)].board[target];if(!t||effectiveLevel(other(w),t)!==6)return false;}return true;}"
new = "function legalTarget(w,slot,target){const c=game[w].board[slot];if(!c)return false;if(!targetInRange(w,slot,target))return false;if(c.flags.secondCharacterOnly&&c.attacksLeft===1&&!game[other(w)].board[target])return false;if(c.attachments?.some(a=>a.code==='BP01-098')){const t=game[other(w)].board[target];if(!t||effectiveLevel(other(w),t)!==6)return false;}return true;}"
if old not in s:
    raise SystemExit("legalTarget block not found")
s = s.replace(old, new, 1)

old1 = "if(ranks[q.ds]>effectiveRange(aw,a,q.as)){log('The attack is no longer in Range.');return true;}"
new1 = "if(!targetInRange(aw,q.as,q.ds)){log('The attack is no longer in Range.');return true;}"
if old1 not in s:
    raise SystemExit("counter range recheck #1 not found")
s = s.replace(old1, new1, 1)

old2 = "if(ranks[q.ds]>effectiveRange(aw,a,q.as))return true;"
new2 = "if(!targetInRange(aw,q.as,q.ds))return true;"
if old2 not in s:
    raise SystemExit("counter range recheck #2 not found")
s = s.replace(old2, new2, 1)

needle = "<p>Choose a highlighted legal target, or decline this attack.</p>"
replacement = "<p>Choose a highlighted legal target based on Range: R-1 = FRONT; R-2 = FRONT + WINGS; R-3+ = all Battle zones. Or decline this attack.</p>"
if needle in s:
    s = s.replace(needle, replacement, 1)

s = s.replace("Hero Rush Live v1.7.2 · Portrait Arena", "Hero Rush Live v1.7.3 · Correct Range Rules")
p.write_text(s)
