;(function($) {
  "use strict";

  $(function() {
    var $courses = $(".course-result");

    var displayResults = function(searchTerm) {
      var searchTerm = searchTerm || "";

      // should normalise case, take it out of the equation
      var numOfResults = $courses
        .hide()
        .filter(function(ind, el) {
            return $(el).text().indexOf( searchTerm ) !== -1; 
          })
          .show().length;
        $(".numofresults").text(numOfResults);
    };

    $(".top-search form").on("submit", function() {
      var term = $( this ).find(".search__input").val();
      displayResults( term );
      return false;
    });

});

}(jQuery));