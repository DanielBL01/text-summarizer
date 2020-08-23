$(document).ready(function(){
    $('input[type="radio"]').click(function(){
        var inputValue = $(this).attr("value");
        var targetBox = $("." + inputValue);
        var showContent = $("." + inputValue);
        $(".summary_content").not(targetBox).hide();
        $(targetBox).show();
    });
});