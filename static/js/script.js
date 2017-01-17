(function($){
    $(function(){

        $('.button-collapse').sideNav();
        $('.parallax').parallax();
        $('.collapsible').collapsible({
            accordion: false, // A setting that changes the collapsible behavior to expandable instead of the default accordion style
            onOpen: function(el) { alert('Open'); }, // Callback for Collapsible open
            onClose: function(el) { alert('Closed'); } // Callback for Collapsible close
            }
        )
    });
})(jQuery);
