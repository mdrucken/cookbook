function onSearch() {
    let box = document.getElementById("searchBox");
    if(box.style.display == "none")
        box.style.display = "inline";
    else
        box.style.display = "none";
    box.value = "";
    filterList();
}
function filterList() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchBox");
    filter = input.value.toUpperCase();
    recipes = document.getElementsByClassName("recipe");

    for (i = 0; i < recipes.length; i++) {
        let inner = recipes[i].innerText;
        let text = inner.toUpperCase();
        if (text.indexOf(filter) > -1) 
            recipes[i].style.display = "";
        else
            recipes[i].style.display = "none";
    }
}