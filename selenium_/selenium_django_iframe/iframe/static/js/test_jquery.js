// alert('jquery_js');


$(document).ready(function(){


$("#two").click(function() {
   $('#one').toggle("slow", function() {
    // Animation complete.
   });

});

});

