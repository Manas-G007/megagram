const showChat=document.querySelector('.chatHere');
const message=document.querySelector('.message');
const send=document.querySelector('.send');
const timerr=document.querySelector('#timerr');

var cTime=new Date();
// send.addEventListener('click',()=>{
//     showChat.innerHTML+=`
//         <div class="r">
//             <div class="Right">
//                 <p class="eleM">${message.value}</p>
//                 <p class="time">${cTime.getHours()}:${cTime.getMinutes()}</p>
//             </div>
//         </div>`;
//         timerr.value=`${cTime.getHours()}:${cTime.getMinutes()}`;
//         message.value='';
//         document.querySelector('#boT').click();
// })
document.querySelector('#boT').click();

const chatter=document.querySelectorAll('.chatUser');
const topImg=document.querySelector('.topImg');
const topChat=document.querySelector('.userName');
const recieverName=document.querySelector('#recieverName');
const statuso=document.querySelector('.status');
chatter.forEach(e=>{
    e.addEventListener('click',()=>{
        topChat.innerHTML=e.innerHTML;
        topImg.src=e.getAttribute('my');
        recieverName.value=e.innerHTML;
        statuso.textContent='online';
    })
})