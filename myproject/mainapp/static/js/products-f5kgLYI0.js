import"./main-CnO608fQ.js";const d=[{id:1,img:"/static/img/products/Image 20-5.png",title:"Механический протез",desc:"Enhanced mobility with ergonomic support. Ideal for walking and running.",disabled:!1},{id:2,img:"/static/img/products/Image 20-5.png",title:"Косметический протез",desc:"Advanced robotics for precise movements. Seamless integration with neural inputs.",disabled:!1},{id:3,img:"/static/img/products/Image 20-2.png",title:"Бионический протез",desc:"Multi-functional grip for versatile tasks. Compact and lightweight design.",disabled:!1},{id:4,img:"/static/img/products/Image 20-4.png",title:"Running Prosthesis",desc:"Perfect for athletes and active users.",disabled:!0}];let c="";d.forEach(e=>{c+=`<div class="products__item${e.disabled?" disabled":""}">
                        <div class="products__img">
                            <img src="${e.img}" alt="${e.title}" />
                            <p class="soon">Скоро...</p>
                        </div>
                        {% for prod in products %}
                        <h3>{{ prod.name_ru }}</h3>
                        {% endfor %}
                        <p>${e.desc.length>50?e.desc.slice(0,51)+"...":e.desc}</p>
                        <button class="products__btn second__button" id=${e.id}>Learn More</button>
                    </div>`});document.getElementById("productList").innerHTML=c;Array.from(document.querySelectorAll(".products__btn")).forEach(e=>{e.addEventListener("click",a=>{const t=d.filter(i=>i.id==a.target.id)[0],s=document.getElementById("detail"),l=document.getElementById("detailContent");s.classList.add("active"),l.innerHTML=`<div class="products__left">
                                <img src="${t.img}" alt="${t.title}">
                            </div>
                            <div class="products__right">
                                <div class="products__detail-header">
                                    <h3>${t.title}</h3>
                                </div>
                                <div class="products__detail-text">
                                    <p>${t.desc}</p>
                                </div>
                            </div>
                            <div class="products__cancel" id="cancel">
                                <img src="/static/icon/cancel.svg" alt="cancel">
                            </div>
                            `,document.getElementById("cancel").addEventListener("click",()=>{s.classList.remove("active")}),s.addEventListener("click",i=>{i.target.className==="products__detail-container"&&s.classList.remove("active")})})});
