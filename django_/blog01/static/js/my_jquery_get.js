// alert('jquery_js');


$(document).ready(function(){


$("#dobavka").click(function() {

        $.ajax({
           type: "GET",

           url: "?page={{ article.next_page_number }}",

           cache: false,
           success: function(html){

           html = $('#vot_eto').html() //
           $("#results").append(html);

        }

        });


}); // $("#dobavka").click(function() {

   
   $('#prev_2').toggle("slow", function() {
    // Animation complete.
   });

});  // $(document).ready(function(){
