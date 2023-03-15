var contactDropdown = document.getElementById("contact-dropdown");
var dropdownMenu = contactDropdown.nextElementSibling;

contactDropdown.addEventListener("mouseenter", function() {
  dropdownMenu.classList.add("show");
});

contactDropdown.addEventListener("mouseleave", function() {
  dropdownMenu.classList.remove("show");
});
const slides = document.querySelectorAll('.slide');
let currentSlide = 0;
const slideInterval = setInterval(nextSlide, 10000);

function nextSlide() {
  slides[currentSlide].classList.remove('active');
  currentSlide = (currentSlide + 1) % slides.length;
  slides[currentSlide].classList.add('active');
}
var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'))
var dropdownList = dropdownElementList.map(function (dropdownToggleEl) {
    return new bootstrap.Dropdown(dropdownToggleEl)
  })


