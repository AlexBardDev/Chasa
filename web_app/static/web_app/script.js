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
