$(document).ready(function(){
	$(window).scroll(function () {
		if ($(this).scrollTop() > 300)
			$('#backToTop').fadeIn(750);
		else
			$('#backToTop').fadeOut(750);
	});
	$('#backToTop').click(function () {
		$('body,html').animate({scrollTop: 0}, 1000);
	});
});