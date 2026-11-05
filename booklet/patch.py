import re,sys
t=open('template.html').read()
def rep(old,new,count=1):
    global t
    assert t.count(old)>=1, old[:60]
    t=t.replace(old,new) if count==0 else t.replace(old,new,count)
rep('<meta name="claude:viewport-fit-sides" content="cover">','<meta name="claude:viewport-fit-sides" content="cover">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n<meta name="apple-mobile-web-app-title" content="Wealth">')
rep('</style>',open('ios.css').read()+'</style>')
rep('  <div class="where" id="where"></div>\n','  <div class="where" id="where"></div>\n  <div class="ptitle" id="ptitle">Guide</div>\n  <button class="btn" id="aaBtn" aria-label="Text size" aria-haspopup="true">Aa</button>\n')
rep('<div class="backdrop" id="backdrop"></div>\n','<div class="backdrop" id="backdrop"></div>\n<div class="ltitle" id="ltitle">Contents</div>\n')
rep('<div class="resume" id="resume"',open('ios.html').read()+'<div class="resume" id="resume"')
# JS
rep("  var md=document.getElementById('guideMd').textContent;","  function phone(){return window.matchMedia('(max-width:760px)').matches;}\n  function hidePop(){var p=document.querySelector('.pop'); if(p) p.hidden=true; document.body.classList.remove('pop-open');}\n  var md=document.getElementById('guideMd').textContent;")
rep("pop.hidden=false; var r=el.getBoundingClientRect(), pw=pop.offsetWidth, ph=pop.offsetHeight;","pop.hidden=false; document.body.classList.add('pop-open'); if(phone()){pop.style.left='';pop.style.top='';return;} var r=el.getBoundingClientRect(), pw=pop.offsetWidth, ph=pop.offsetHeight;")
rep("if(!pop.hidden&&!pop.contains(e.target)&&!e.target.closest('.term')) pop.hidden=true; });","if(!pop.hidden&&!pop.contains(e.target)&&!e.target.closest('.term')) hidePop(); if(!e.target.closest('.sizes')&&!e.target.closest('#aaBtn')) document.body.classList.remove('sizes-open'); });")
rep("if(e.target.tagName==='A') pop.hidden=true; });","if(e.target.tagName==='A') hidePop(); });")
rep("if(e.key==='Escape') pop.hidden=true; });","if(e.key==='Escape') hidePop(); });")
rep("window.addEventListener('scroll',function(){ pop.hidden=true; },{passive:true});","window.addEventListener('scroll',function(){ if(!phone()) hidePop(); },{passive:true});")
rep("if(h.tagName==='H1'&&h!==first){ html+='<div class=\"part\">'","if(h.tagName==='H1'&&h!==first){ html+='<div class=\"part'+(h.closest('#glossary')?' glpart':'')+'\">'")
rep("bd.addEventListener('click',function(){setNav(false);});","bd.addEventListener('click',function(){setNav(false); hidePop();});")
rep("function hdr(){return 52+14;}","function hdr(){return (phone()?44:52)+14;}")
rep("  function spy(){\n    var y=window.scrollY+hdr()+8, best=null;","  function spy(){\n    if(phone()&&tab!=='guide'){ chrome(); return; }\n    var y=window.scrollY+hdr()+8, best=null;")
rep("if(r.top<tr.top+40||r.bottom>tr.bottom-40) a.scrollIntoView({block:'center'});}","if(!phone()&&(r.top<tr.top+40||r.bottom>tr.bottom-40)) a.scrollIntoView({block:'center'});}")
rep("prog.style.width=(max>0?Math.min(100,100*window.scrollY/max):0)+'%';\n  }","prog.style.width=(max>0?Math.min(100,100*window.scrollY/max):0)+'%';\n    chrome();\n  }")
rep("function(){resume.hidden=true; h.scrollIntoView({block:'start'}); });","function(){resume.hidden=true; setTab(h.closest('#glossary')?'glossary':'guide',true); h.scrollIntoView({block:'start'}); });")
ios_js = r"""
  // --- iPhone app chrome: tab bar, nav titles, text-size menu, A–Z index
  var tabbar=document.getElementById('tabbar'), ltitle=document.getElementById('ltitle'), ptitle=document.getElementById('ptitle'), head=document.querySelector('.head');
  var TT={guide:'Guide',contents:'Contents',glossary:'Glossary'}, tpos={guide:0,contents:0,glossary:0}, tab='guide';
  document.body.dataset.tab='guide';
  function jump(y){window.scrollTo(0,y);}
  function setTab(t,keep){ if(!TT[t]) return;
    if(t===tab){ if(!keep) jump(0); return; }
    tpos[tab]=window.scrollY; tab=t; document.body.dataset.tab=t; ltitle.textContent=TT[t];
    tabbar.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.dataset.tab===t);});
    document.body.classList.remove('sizes-open'); hidePop(); if(!keep) jump(tpos[t]); chrome(); }
  function chrome(){ if(!phone()) return; var y=window.scrollY;
    if(tab==='guide'){ ptitle.textContent=(cur&&y>160)?cur.textContent.replace(/^\d+\.\s*/,'').replace(/\s*\(.*?\)\s*$/,''):'Guide'; head.classList.add('titled'); document.body.classList.remove('flat'); }
    else { ptitle.textContent=TT[tab]; var past=y>34; head.classList.toggle('titled',past); document.body.classList.toggle('flat',!past); } }
  tabbar.addEventListener('click',function(e){var b=e.target.closest('button'); if(b) setTab(b.dataset.tab,false);});
  document.addEventListener('click',function(e){ var a=e.target.closest('a[href^="#"]'); if(!a||!phone()) return;
    var id=decodeURIComponent(a.getAttribute('href').slice(1)), el=document.getElementById(id); if(!el) return;
    var want=el.closest('#glossary')?'glossary':'guide';
    if(want==='glossary'&&el.hidden){ glq.value=''; glFilter(); }
    if(want!==tab) setTab(want,true); });
  document.getElementById('aaBtn').addEventListener('click',function(e){ e.stopPropagation(); document.body.classList.toggle('sizes-open'); });
  var az=document.getElementById('azbar'), azh='';
  sec.querySelectorAll('h2.gl-letter').forEach(function(h){ azh+='<a href="#'+h.id+'" data-id="'+h.id+'">'+h.textContent+'</a>'; });
  az.innerHTML=azh;
  function azAt(x,y){ var el=document.elementFromPoint(x,y); var a=el&&el.closest&&el.closest('.azbar a'); if(!a) return; var t=document.getElementById(a.dataset.id); if(t&&!t.hidden) t.scrollIntoView({block:'start'}); }
  az.addEventListener('touchstart',function(e){ az.classList.add('hot'); var p=e.touches[0]; azAt(p.clientX,p.clientY); e.preventDefault(); },{passive:false});
  az.addEventListener('touchmove',function(e){ var p=e.touches[0]; azAt(p.clientX,p.clientY); e.preventDefault(); },{passive:false});
  az.addEventListener('touchend',function(){ az.classList.remove('hot'); });
  if(phone()){ var h0=location.hash.slice(1), el0=h0&&document.getElementById(decodeURIComponent(h0)); if(el0){ if(el0.closest('#glossary')) setTab('glossary',true); setTimeout(function(){el0.scrollIntoView({block:'start'});},0); } }
  spy();
})();
</script>"""
rep("  spy();\n})();\n</script>", ios_js)
open('template.html','w').write(t)
print('patched', len(t))
