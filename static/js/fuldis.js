const setting=document.getElementById('setting');
const set=document.getElementById('settingBtn');
const dropper=document.querySelector('.dropper');
let check1=true;
set.addEventListener("click",()=>{
if(check1){
    dropper.style.display="block";
    check1=false;
}else{
    dropper.style.display="none";
    check1=true;
}
});
setting.addEventListener("click",()=>{
if(check1){
    dropper.style.display="block";
    check1=false;
}else{
    dropper.style.display="none";
    check1=true;
}
});

// full screen feature
const fuldis= document.querySelector('.fuldis');
const ppImg=document.querySelector('.ppImg');
const pImg=document.querySelectorAll('.pImg');
const blur1=document.querySelector('.navbar');
const blur2=document.querySelector('.topinfo');
const blur3=document.querySelector('.postGrid');
const blur4=document.querySelector('.botbar');

pImg.forEach(x=>{x.addEventListener('click',()=>{
    ppImg.src=x.src;
    fuldis.style.display='flex';
    blur1.style.filter='blur(2px)';
    blur2.style.filter='blur(2px)';
    blur3.style.filter='blur(2px)';
    blur4.style.filter='blur(2px)';
})})

fuldis.addEventListener('click',()=>{
    fuldis.style.display='none';  
    blur1.style.filter='blur(0)';
    blur2.style.filter='blur(0)';
    blur3.style.filter='blur(0)';
    blur4.style.filter='blur(0)';
})

