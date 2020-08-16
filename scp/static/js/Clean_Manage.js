$(function(){
	// 編集ボタン押下
	$("#sort").on("click", function(){
		$(".list").sortable("enable");
		$(".sort-before").removeClass("active");
		$(".sort-after").addClass("active");
	});

	// 完了ボタン押下
	$("#sort-finish").on("click", function(){
		$(".list").sortable("disable");
		$(".sort-before").addClass("active");
		$(".sort-after").removeClass("active");

	});

	// キャンセルボタン押下
	$("#sort-cancel").on("click", function(){
		$("#list1").html(cache1).sortable("refresh");
		$("#list2").html(cache2).sortable("refresh");
		$("#list3").html(cache3).sortable("refresh");
		$("#list4").html(cache4).sortable("refresh");
		$("#list5").html(cache5).sortable("refresh");
		$(".list").sortable("disable");
		$(".sort-before").addClass("active");
		$(".sort-after").removeClass("active");

	});



	// sortable
	$(".list").sortable({disabled: "true", connectWith: ".list"});
	var cache1 = $("#list1").html();
	var cache2 = $("#list2").html();
	var cache3 = $("#list3").html();
	var cache4 = $("#list4").html();
	var cache5 = $("#list5").html();


});