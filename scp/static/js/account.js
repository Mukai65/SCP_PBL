/*
 * appendRow: テーブルに行を追加
 */
function appendRow()
{
    var objTBL = document.getElementById("tbl");
    if (!objTBL)
        return;
    
    var count = objTBL.rows.length;
    
    // 最終行に新しい行を追加
    var row = objTBL.insertRow(count);

    // 列の追加
    var c1 = row.insertCell(0);
    var c2 = row.insertCell(1);
    var c3 = row.insertCell(2);
    var c4 = row.insertCell(3);
// 各列にスタイルを設定
c1.style.cssText = "";
c2.style.cssText = "";
c3.style.cssText = "";
c4.style.cssText = "";

// 各列に表示内容を設定
c1.innerHTML = '<input class="inpval" type="text"   id="txt' + count + '" name="txt' + count + '" value="" size="30" style="border:1px solid #888;">';
c2.innerHTML = '<input class="inpval" type="text"   id="txt' + count + '" name="txt' + count + '" value="" size="30" style="border:1px solid #888;">';
c3.innerHTML = '<input class="inpval" type="text"   id="txt' + count + '" name="txt' + count + '" value="" size="30" style="border:1px solid #888;">';
c4.innerHTML = '<input class="inpval" type="text"   id="txt' + count + '" name="txt' + count + '" value="" size="30" style="border:1px solid #888;">';
// 追加した行の入力フィールドへフォーカスを設定
var objInp = document.getElementById("txt" + count);
if (objInp)
    objInp.focus();
}







/*
 * deleteRow: 削除ボタン該当行を削除
 */
function deleteRow(obj)
{
    // 確認
    if (!confirm("この行を削除しますか？"))
        return;

    if (!obj)
        return;

    var objTR = obj.parentNode.parentNode;
    var objTBL = objTR.parentNode;
    
    if (objTBL)
        objTBL.deleteRow(objTR.sectionRowIndex);
    
    // <span> 行番号ふり直し
    var tagElements = document.getElementsByTagName("span");
    if (!tagElements)
        return false;

    var seq = 1;
    for (var i = 0; i < tagElements.length; i++)
    {
        if (tagElements[i].className.match("seqno"))
            tagElements[i].innerHTML = seq++;
    }

    // id/name ふり直し
    var tagElements = document.getElementsByTagName("input");
    if (!tagElements)
        return false;

    // <input type="text" id="txtN">
    var seq = 1;
    for (var i = 0; i < tagElements.length; i++)
    {
        if (tagElements[i].className.match("inpval"))
        {
            tagElements[i].setAttribute("id", "txt" + seq);
            tagElements[i].setAttribute("name", "txt" + seq);
            ++seq;
        }
    }

    // <input type="button" id="edtBtnN">
    seq = 1;
    for (var i = 0; i < tagElements.length; i++)
    {
        if (tagElements[i].className.match("edtbtn"))
        {
            tagElements[i].setAttribute("id", "edtBtn" + seq);
            ++seq;
        }
    }

    // <input type="button" id="delBtnN">
    seq = 1;
    for (var i = 0; i < tagElements.length; i++)
    {
        if (tagElements[i].className.match("delbtn"))
        {
            tagElements[i].setAttribute("id", "delBtn" + seq);
            ++seq;
        }
    }
}

/*
 * editRow: 編集ボタン該当行の内容を入力・編集またモード切り替え
 */
function editRow(obj)
{
    var objTR = obj.parentNode.parentNode;
    var rowId = objTR.sectionRowIndex;
    var objInp = document.getElementById("txt" + rowId);
    var objBtn = document.getElementById("edtBtn" + rowId);

    if (!objInp || !objBtn)
        return;
    
    // モードの切り替えはボタンの値で判定   
    if (objBtn.value == "編集")
    {
        objInp.style.cssText = "border:1px solid #888;"
        objInp.readOnly = false;
        objInp.focus();
        objBtn.value = "確定";
    }
    else
    {
        objInp.style.cssText = "border:none;"
        objInp.readOnly = true;
        objBtn.value = "編集";
    }
}