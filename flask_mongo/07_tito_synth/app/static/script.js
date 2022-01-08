'use-strict';

const hamburgerIcon = document.querySelector('.hamburger-icon');
const primaryNav = document.querySelector('.primary-nav');
const animatedBox = document.querySelector('.animatedBox');
const nav = document.querySelector('.nav');
const pnav = document.querySelectorAll('.pnav');
const header = document.querySelector('.header');
const secondaryNavs = document.querySelectorAll('.secondary-nav');

const toggleMenu = function () {
  hamburgerIcon.classList.toggle('clicked');
  primaryNav.classList.toggle('open');
  secondaryNavs.forEach(nav => {
    nav.classList.remove('open');
    pnav.forEach(pnav => pnav.classList.remove('clicked'));
  });

};
hamburgerIcon.onclick = toggleMenu;

const toggleSubMenu = function (e) {
  const navbar = e.target.closest('.pnav');

  if (navbar.classList.contains('html-nav')) {
    secondaryNavs[0].classList.toggle('open');
  }
  if (navbar.classList.contains('css-nav')) {
    secondaryNavs[1].classList.toggle('open');
  }
  if (navbar.classList.contains('js-nav')) {
    secondaryNavs[2].classList.toggle('open');
  }
  if (navbar.classList.contains('react-nav')) {
    secondaryNavs[3].classList.toggle('open');
  }
  if (navbar.classList.contains('nodejs-nav')) {
    secondaryNavs[4].classList.toggle('open');
  }
  if (navbar.classList.contains('mongodb-nav')) {
    secondaryNavs[5].classList.toggle('open');
  }

  navbar.classList.toggle('clicked');
}

document.querySelectorAll('.pnav').forEach(nav => nav.addEventListener('click', toggleSubMenu));


const animate = function () {
  animatedBox.classList.toggle('run');
};

animatedBox.addEventListener('click', function (e) {
  e.preventDefault();
  animate();
});

const navHeight = nav.getBoundingClientRect().height;

const stickyNav = function (entries) {
  const [entry] = entries;
  if (!entry.isIntersecting) nav.classList.add('sticky');
  else nav.classList.remove('sticky');
};

const headerObserver = new IntersectionObserver(stickyNav, {
  root: null,
  threshold: 0,
  rootMargin: `-${navHeight}px`,
});
headerObserver.observe(header);