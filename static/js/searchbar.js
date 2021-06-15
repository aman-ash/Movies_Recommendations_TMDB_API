const searchBox = document.getElementById('searchBox'),
  googleIcon = document.getElementById('googleIcon');

googleIcon.onclick = function () {
  searchBox.classList.toggle('active');
};
