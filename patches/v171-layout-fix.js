(()=>{
  'use strict';
  const syncBattleViewport=()=>{
    const h=Math.max(280,Math.round(window.visualViewport?.height||window.innerHeight||document.documentElement.clientHeight||360));
    document.documentElement.style.setProperty('--battle-vh',`${h}px`);
  };
  syncBattleViewport();
  window.addEventListener('resize',syncBattleViewport,{passive:true});
  window.addEventListener('orientationchange',()=>setTimeout(syncBattleViewport,80),{passive:true});
  if(window.visualViewport) window.visualViewport.addEventListener('resize',syncBattleViewport,{passive:true});
})();