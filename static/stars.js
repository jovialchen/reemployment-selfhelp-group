document.addEventListener("DOMContentLoaded", function() {
  var ratings = document.querySelectorAll('.rating');
  ratings.forEach(function(rating) {
    var stars = parseInt(rating.getAttribute('data-rating'));
    var starsHTML = '';
    for (var i = 0; i < 5; i++) {
      if (i < stars) {
        starsHTML += '★';
      } else {
        starsHTML += '☆';
      }
    }
    rating.innerHTML = starsHTML;
  });
});
