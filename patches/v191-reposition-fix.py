from pathlib import Path

root=Path("android-project")

app=root/"app/src/main/assets/app.js"
s=app.read_text()
old="""document.querySelectorAll('[data-field-card]').forEach(b=>{const [w,s]=b.dataset.fieldCard.split(':');armHoldPreview(b,()=>game[w].board[s],w);b.onclick=e=>{if(suppressArenaClick){suppressArenaClick=false;e.stopPropagation();return;}if(w==='p'&&game.phase==='action'&&!game.locked){game.selectedField=game.selectedField===s?null:s;game.selectedHand=null;renderGame();}else showCardDetail(game[w].board[s],w);e.stopPropagation();};});"""
new="""document.querySelectorAll('[data-field-card]').forEach(b=>{const [w,s]=b.dataset.fieldCard.split(':');armHoldPreview(b,()=>game[w].board[s],w);b.onclick=e=>{if(suppressArenaClick){suppressArenaClick=false;e.stopPropagation();return;}if(w==='p'&&game.phase==='reposition'&&!game.locked){reposition(s);e.stopPropagation();return;}if(w==='p'&&game.phase==='action'&&!game.locked){game.selectedField=game.selectedField===s?null:s;game.selectedHand=null;renderGame();e.stopPropagation();return;}showCardDetail(game[w].board[s],w);e.stopPropagation();};});"""
if old not in s:
    raise SystemExit("v1.9 field-card handler not found")
s=s.replace(old,new,1)
s=s.replace("Hero Rush Live v1.9 · SP01 Catalog Alpha","Hero Rush Live v1.9.1 · Reposition Tap Fix")
app.write_text(s)

idx=root/"app/src/main/assets/index.html"
s=idx.read_text()
s=s.replace("Hero Rush Live v1.9","Hero Rush Live v1.9.1")
s=s.replace("LIVE ALPHA · v1.9","LIVE ALPHA · v1.9.1")
s=s.replace("LIVE · v1.9","LIVE · v1.9.1")
s=s.replace("v1.9 adds the complete 80-card SP01 Era of Spiders Character catalog","v1.9.1 keeps the complete 80-card SP01 Era of Spiders Character catalog and fixes reposition tap behavior")
idx.write_text(s)

grad=root/"app/build.gradle"
s=grad.read_text().replace("versionCode 23","versionCode 24").replace("versionName '1.9-sp01-catalog-alpha'","versionName '1.9.1-reposition-fix'")
grad.write_text(s)

man=root/"app/src/main/AndroidManifest.xml"
s=man.read_text().replace('android:label="Hero Rush Live v1.9"','android:label="Hero Rush Live v1.9.1"')
man.write_text(s)

test=root/"tools/reposition-interaction-validation.js"
test.write_text(r"""const fs = require('fs');
const s = fs.readFileSync('app/src/main/assets/app.js','utf8');
const bindStart = s.indexOf('function bindGameElements()');
if (bindStart < 0) throw new Error('bindGameElements missing');
const bind = s.slice(bindStart, s.indexOf('function animateSlot', bindStart));
const repos = "if(w==='p'&&game.phase==='reposition'&&!game.locked){reposition(s);e.stopPropagation();return;}";
const action = "if(w==='p'&&game.phase==='action'&&!game.locked)";
const preview = 'showCardDetail(game[w].board[s],w)';
const iRepos = bind.indexOf(repos);
const iAction = bind.indexOf(action);
const iPreview = bind.indexOf(preview);
if (iRepos < 0) throw new Error('Reposition tap branch missing');
if (!(iRepos < iAction && iAction < iPreview)) throw new Error('Reposition tap must be handled before action/preview fallback');
if (!bind.includes('armHoldPreview(b,()=>game[w].board[s],w)')) throw new Error('Hold preview binding missing');
if (!bind.includes('if(suppressArenaClick){suppressArenaClick=false;e.stopPropagation();return;}')) throw new Error('Long-press click suppression missing');
console.log('Reposition interaction validation passed: tap swaps/selects, hold previews.');
""")
