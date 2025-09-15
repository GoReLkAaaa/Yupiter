(function () {
  const l = document.createElement("link").relList;
  if (l && l.supports && l.supports("modulepreload")) return;
  for (const e of document.querySelectorAll('link[rel="modulepreload"]')) a(e);
  new MutationObserver((e) => {
    for (const t of e)
      if (t.type === "childList")
        for (const c of t.addedNodes)
          c.tagName === "LINK" && c.rel === "modulepreload" && a(c);
  }).observe(document, { childList: !0, subtree: !0 });
  function i(e) {
    const t = {};
    return (
      e.integrity && (t.integrity = e.integrity),
      e.referrerPolicy && (t.referrerPolicy = e.referrerPolicy),
      e.crossOrigin === "use-credentials"
        ? (t.credentials = "include")
        : e.crossOrigin === "anonymous"
        ? (t.credentials = "omit")
        : (t.credentials = "same-origin"),
      t
    );
  }
  function a(e) {
    if (e.ep) return;
    e.ep = !0;
    const t = i(e);
    fetch(e.href, t);
  }
})();
Array.from(document.getElementsByClassName("faq__item")).forEach((s) => {
  s.addEventListener("click", () => {
    console.log(s), s.classList.toggle("faq__active");
  });
});
document.getElementById("header");
document.getElementById("footer");
let r = !1;
const o = document.getElementById("burger");
o.addEventListener("click", (s) => {
  const l = document.getElementById("phoneMenu");
  (r = !r),
    (o.style.position = r ? "fixed" : "relative"),
    (o.style.right = r ? "15px" : "0"),
    o.classList.toggle("white"),
    l.classList.toggle("hide");
});
Array.from(document.querySelectorAll(".header__select")).forEach((s) => {
  s.addEventListener("click", () => {
    document.querySelectorAll(".select__list").forEach((i) => {
      i.classList.toggle("active"), s.classList.toggle("active");
    }),
      Array.from(document.querySelectorAll(".select__item")).forEach((i) => {
        i.addEventListener("click", (a) => {
          console.log(a.target.textContent.trim()),
            console.log(i),
            Array.from(document.querySelectorAll(".select__head")).forEach(
              (e) => {
                e.textContent = a.target.textContent.trim();
              }
            );
        });
      });
  });
});
Array.from(document.getElementById('menuList').children).forEach(element => {
    console.log(element);
    element.addEventListener('click', () => {
        const l = document.getElementById("phoneMenu");
        const o = document.getElementById("burger");
        l.classList.add('hide')
        o.classList.toggle('white')
    })
});