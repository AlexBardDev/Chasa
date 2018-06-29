/* Hovering on the menu */
$("#navbarDropdown2").on("mouseover", function () {
	$(".dropdown-menu").show();
});

$("#navbarDropdown2").on("mouseleave", function () {
	$(".dropdown-menu").hide();
});

$(".dropdown-menu").on("mouseover", function () {
	$(this).show();
});

$(".dropdown-menu").on("mouseleave", function () {
	$(this).hide();
});

/* Enable tooltips */
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

/* Close or open accordion */
$("a[href='#AccordionOne']").on("click", function () {
	$("a[href='#AccordionOne'] span").toggleClass("fas fa-caret-down").toggleClass("fas fa-caret-up")
});

$("a[href='#AccordionTwo']").on("click", function () {
	$("a[href='#AccordionTwo'] span").toggleClass("fas fa-caret-down").toggleClass("fas fa-caret-up")
});
