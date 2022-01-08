'use-strict';

const animatedBox = document.querySelector('.animatedBox');
const animate = function () {
  animatedBox.classList.toggle('run');
};

animatedBox.addEventListener('click', function (e) {
  e.preventDefault();
  animate();
});
