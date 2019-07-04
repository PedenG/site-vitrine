$('document').ready(function() {
    var screenHeight = $(window).height();
    var screenWidth = $(window).width();

    $('#burger').click(function() {
		closeOut()
	});

    function closeOut() {
	$('#sidebar').toggleClass('nav-slide');
	$('#container').toggleClass('body-slide');
	$('.nav-item').toggleClass('item-slide');
    }
});