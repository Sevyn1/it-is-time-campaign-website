'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-nav');
function closeMenu() { navigation.classList.remove('open'); menuButton.setAttribute('aria-expanded','false'); }
menuButton.addEventListener('click', () => {
 const open=menuButton.getAttribute('aria-expanded')!=='true';
 navigation.classList.toggle('open',open);menuButton.setAttribute('aria-expanded',String(open));
});
navigation.addEventListener('click',event=>{if(event.target.closest('a'))closeMenu();});
document.addEventListener('keydown',event=>{if(event.key==='Escape' && menuButton.getAttribute('aria-expanded')==='true'){closeMenu();menuButton.focus();}});
const desktop=window.matchMedia('(min-width:701px)');
desktop.addEventListener('change',event=>{if(event.matches)closeMenu();});
const search=document.querySelector('#topic-search');
if(search){
 const cards=[...document.querySelectorAll('[data-topic]')];
 const normalize=value=>value.normalize('NFKD').replace(/\p{M}/gu,'').toLowerCase().trim();
 const update=()=>{
  const query=normalize(search.value);let count=0;
  for(const card of cards){const matches=normalize(card.dataset.search).includes(query);card.hidden=!matches;if(matches)count++;}
  document.querySelector('#search-status').textContent=`${count} ${count===1?'topic':'topics'}${query?' found':''}`;
  document.querySelector('#no-topics').hidden=count!==0;
 };
 search.addEventListener('input',update);
 document.querySelector('#clear-search').addEventListener('click',()=>{search.value='';update();search.focus();});
}
for(const button of document.querySelectorAll('[data-close-dialog]'))button.addEventListener('click',()=>button.closest('dialog').close());
for(const dialog of document.querySelectorAll('dialog')){
 dialog.addEventListener('click',event=>{
  const rect=dialog.getBoundingClientRect();
  if(event.target===dialog && (event.clientX<rect.left || event.clientX>rect.right || event.clientY<rect.top || event.clientY>rect.bottom))dialog.close();
 });
}
const film=document.querySelector('#film-dialog');
if(film){
 const player=film.querySelector('video');
 for(const button of document.querySelectorAll('[data-open-film]'))button.addEventListener('click',()=>{
  if(!player.getAttribute('src')){player.src=player.dataset.videoSrc;player.load();}
  film.showModal();
 });
 film.addEventListener('close',()=>player.pause());
}
const photoDialog=document.querySelector('#photo-dialog');
if(photoDialog){
 const photos=[...document.querySelectorAll('[data-photo]')];let current=0;
 const display=index=>{
  current=(index+photos.length)%photos.length;
  const image=photoDialog.querySelector('#expanded-photo');image.src=photos[current].dataset.photo;
  image.alt=photos[current].querySelector('img').alt;
  photoDialog.querySelector('#photo-count').textContent=`${current+1} of ${photos.length}`;
 };
 for(const [index,button] of photos.entries())button.addEventListener('click',()=>{display(index);photoDialog.showModal();});
 document.querySelector('#previous-photo').addEventListener('click',()=>display(current-1));
 document.querySelector('#next-photo').addEventListener('click',()=>display(current+1));
 photoDialog.addEventListener('keydown',event=>{
  if(event.key==='ArrowLeft'){event.preventDefault();display(current-1);}
  if(event.key==='ArrowRight'){event.preventDefault();display(current+1);}
 });
 const hash=window.location.hash;
 if(/^#photo-\d+$/.test(hash)){const target=document.getElementById(hash.slice(1));if(target?.matches('[data-photo]'))target.click();}
}
