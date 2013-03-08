$(document).ready(function() {
						   
		
		$('.searchInput input[type=text]').focus(function() { //onclick remove Search phrase if is default
							if ($(this).val() == 'Search') {
								$(this).val('');
							}
							$('.errorSearch').hide();
		}).focusout(function () {
							if ($(this).val() == '') {
								$(this).val('Search');
							}		
		});
		
		$('.searchButton').mouseover(function() { //search buttom mouseover effect
							$(this).addClass('searchButtonHover');
		}).mouseout(function () {
							$(this).removeClass('searchButtonHover');		
		});
				
		$('.search form').submit(function() { // search form validation
			var errs = 0;
			
			if ( $('.searchInput input[type=text]').val() == 'Search' || $('.searchInput input[type=text]').val().length < 3 ) {
				errs = 1;
			}
			
			if (errs == 1 ) {
          		$('.errorSearch').show();
				return false;
     	 	}

		});
		
	
});