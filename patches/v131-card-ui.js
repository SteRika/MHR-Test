(()=>{
'use strict';
const db=window.CARD_DB||[], byCode=Object.fromEntries(db.map(c=>[c.code,c]));
const esc=s=>String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
const short=(s,n=118)=>String(s||'').length>n?String(s).slice(0,n-1).trimEnd()+'…':String(s||'');
let lastCollectionCode=null, busy=false;
function frame(c,detail=false){
  const color=(c.color||'Red').toLowerCase(), traits=(c.traits||[]).map(t=>`<span>${esc(t)}</span>`).join('');
  return `<article class="v131-card v131-${color} ${detail?'detail':''}"><header><span class="v131-level"><small>LV</small><b>${c.level??'—'}</b></span><span class="v131-name"><b>${esc(c.title)}</b><em>${esc(c.hero)}</em></span><span class="v131-rarity">${esc(c.rarity||'—')}</span></header><div class="v131-art"><small>${esc(c.color)} CHARACTER</small><strong>${esc(c.hero)}</strong><i>TEXT-ONLY ALPHA · NO CARD ART</i></div><div class="v131-meta"><span>${esc(c.code)}</span><span>BP01</span><span class="${c.impl==='live'?'live':'ref'}">${c.impl==='live'?'PLAYABLE':'REFERENCE'}</span></div><div class="v131-traits">${traits||'<span>—</span>'}</div><section><small>EFFECT · PARAPHRASED</small><p>${esc(detail?c.effect:short(c.effect))}</p></section><footer><span><small>RANGE</small><b>${c.range??'—'}</b></span><span><small>POWER</small><b>${c.power==null?'—':Number(c.power).toLocaleString()}</b></span></footer></article>`;
}
function addFilters(){
  const row=document.querySelector('#collectionScreen .filter-row'); if(!row||row.dataset.v131)return; row.dataset.v131='1'; row.classList.add('v131-filters');
  row.insertAdjacentHTML('beforeend',`<select id="v131Level"><option value="all">All levels</option>${[1,2,3,4,5,6].map(x=>`<option value="${x}">Lv${x}</option>`).join('')}</select><select id="v131Range"><option value="all">All ranges</option>${[1,2,3,4].map(x=>`<option value="${x}">R-${x}</option>`).join('')}</select><select id="v131Rarity"><option value="all">All rarities</option>${['UR','GR','SR','R'].map(x=>`<option>${x}</option>`).join('')}</select><select id="v131Trait"><option value="all">All traits</option>${['Human','Machine','Avengers','Wakanda','Asgard','Variant','Fantastic Four','The Defenders','Mutant','Atlantis','Zenn-La'].map(x=>`<option>${x}</option>`).join('')}</select>`);
  ['v131Level','v131Range','v131Rarity','v131Trait'].forEach(id=>document.getElementById(id).onchange=enhance);
  const search=document.getElementById('collectionSearch');
  if(search&&search.oninput){const base=search.oninput;search.oninput=()=>{const q=search.value;search.value='';base.call(search);search.value=q;queueMicrotask(enhance);};search.placeholder='Search name, hero, code, trait or effect';}
}
function enhance(){
  if(busy)return;busy=true;
  try{
    addFilters();
    const grid=document.getElementById('collectionGrid');if(!grid)return;
    const q=(document.getElementById('collectionSearch')?.value||'').trim().toLowerCase();
    const lv=document.getElementById('v131Level')?.value||'all', rg=document.getElementById('v131Range')?.value||'all', rar=document.getElementById('v131Rarity')?.value||'all', tr=document.getElementById('v131Trait')?.value||'all';
    let shown=0;
    grid.querySelectorAll('[data-collection-detail]').forEach(btn=>{
      const c=byCode[btn.dataset.collectionDetail];if(!c)return;
      if(!btn.dataset.v131){btn.dataset.v131='1';btn.classList.add('v131-card-button');btn.innerHTML=frame(c,false);}
      const hay=(c.code+' '+c.title+' '+c.hero+' '+(c.traits||[]).join(' ')+' '+(c.effect||'')).toLowerCase();
      const ok=(!q||hay.includes(q))&&(lv==='all'||String(c.level)===lv)&&(rg==='all'||String(c.range)===rg)&&(rar==='all'||c.rarity===rar)&&(tr==='all'||(c.traits||[]).includes(tr));
      btn.hidden=!ok;if(ok)shown++;
    });
    const p=document.querySelector('#collectionScreen .screen-head p');if(p)p.innerHTML=`30 playable · <b>120 BP01 detailed</b> · ${shown} shown`;
    const home=document.querySelector('#homeCollection small');if(home)home.textContent='120 BP01 cards detailed';
    const brand=document.querySelector('.brand small');if(brand)brand.textContent='LIVE ALPHA · v1.3.1';
    const dev=[...document.querySelectorAll('.panel-block')].find(x=>x.textContent.includes('DEVELOPMENT STATUS'));if(dev)dev.innerHTML='<strong>DEVELOPMENT STATUS</strong><p>v1.3.1 includes complete BP01 Character metadata for all 120 cards. The 30 Red cards remain playable; Yellow, Blue and Green are detailed reference cards pending engine implementation.</p>';
  } finally {busy=false;}
}
function enhanceModal(){
  if(!lastCollectionCode)return;const body=document.getElementById('cardModalBody'), c=byCode[lastCollectionCode];if(!body||!c||body.dataset.v131===lastCollectionCode)return;body.dataset.v131=lastCollectionCode;body.innerHTML=frame(c,true);
}
document.addEventListener('click',e=>{const b=e.target.closest?.('[data-collection-detail]');if(b){lastCollectionCode=b.dataset.collectionDetail;setTimeout(enhanceModal,0);}if(e.target.closest?.('#cardModal .modal-close,.modal-backdrop')){lastCollectionCode=null;const body=document.getElementById('cardModalBody');if(body)body.dataset.v131='';}},true);
const observer=new MutationObserver(()=>{enhance();enhanceModal();});
window.addEventListener('DOMContentLoaded',()=>{addFilters();enhance();observer.observe(document.body,{childList:true,subtree:true});});
})();