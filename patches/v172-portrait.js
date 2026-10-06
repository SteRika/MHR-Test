(()=>{
  'use strict';
  const sync=()=>{
    const h=Math.max(520,Math.round(window.visualViewport?.height||window.innerHeight||document.documentElement.clientHeight||800));
    document.documentElement.style.setProperty('--battle-vh',`${h}px`);
    const set=document.getElementById('setBaseButton');
    if(set) set.textContent='SET 1 / DRAW 1';
  };
  sync();
  addEventListener('resize',sync,{passive:true});
  if(window.visualViewport) window.visualViewport.addEventListener('resize',sync,{passive:true});
  document.addEventListener('DOMContentLoaded',sync,{once:true});
})();