function checkForm(){
    if(document.form1.input01.value == "" || document.form1.input02.value == ""){
        alert("必須項目を入力して下さい。");
	return false;
    }else{
	return true;
    }
}