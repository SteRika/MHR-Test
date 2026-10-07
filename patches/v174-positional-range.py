from pathlib import Path

p=Path("android-project/app/src/main/assets/app.js")
s=p.read_text()

old="""const targetDepth = Object.freeze({front:1,wingL:2,wingR:2,back:3});
function targetInRange(w,attackerSlot,targetSlot){const attacker=game?.[w]?.board?.[attackerSlot];if(!attacker)return false;const depth=targetDepth[targetSlot];if(!depth)return false;return effectiveRange(w,attacker,attackerSlot)>=depth;}"""
new="""const targetDepth = Object.freeze({front:1,wingL:2,wingR:2,back:3});
const attackerPenalty = Object.freeze({front:0,wingL:1,wingR:1,back:2});
function requiredRange(attackerSlot,targetSlot){const depth=targetDepth[targetSlot],penalty=attackerPenalty[attackerSlot];if(!depth||penalty==null)return Infinity;return depth+penalty;}
function targetInRange(w,attackerSlot,targetSlot){const attacker=game?.[w]?.board?.[attackerSlot];if(!attacker)return false;return effectiveRange(w,attacker,attackerSlot)>=requiredRange(attackerSlot,targetSlot);}"""
if old not in s:
    raise SystemExit("v1.7.3 range helper block not found")
s=s.replace(old,new,1)

needle="Choose a highlighted legal target based on Range: R-1 = FRONT; R-2 = FRONT + WINGS; R-3+ = all Battle zones. Or decline this attack."
replacement="Choose a highlighted legal target. Range counts from the attacker's current row: FRONT adds 0 steps, WING adds 1, BACK adds 2."
if needle in s:
    s=s.replace(needle,replacement,1)

s=s.replace("Hero Rush Live v1.7.3 · Correct Range Rules","Hero Rush Live v1.7.4 · Positional Range")
p.write_text(s)
