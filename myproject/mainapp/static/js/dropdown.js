document.addEventListener("DOMContentLoaded", function () {
const dropdown = document.getElementById("languageDropdown");
const toggle = document.getElementById("dropdownToggle");

toggle.addEventListener("click", function () {
  dropdown.classList.toggle("open");
});

document.addEventListener("click", function (e) {
  if (!dropdown.contains(e.target)) {
    dropdown.classList.remove("open");
  }
});
});