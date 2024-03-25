function hideSearch() {
    let box = document.getElementById("searchBox");
    box.style.display = "none";
    box = document.getElementById("searchHashtagBox");
    box.style.display = "none";
}

function onSearch() {
    hideSearch()
    let box = document.getElementById("searchBox");
    if(box.style.display == "none")
        box.style.display = "inline";
    else
        box.style.display = "none";
    box.value = "";
    box.focus();
    filterList();
}

function onSearchHashtag() {
    hideSearch()
    let box = document.getElementById("searchHashtagBox");
    if(box.style.display == "none")
        box.style.display = "inline";
    else
        box.style.display = "none";
    box.value = "";
    box.focus();
    filterHashtagList();
}

function filterList() {
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

function filterHashtagList() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchHashtagBox");
    filter = input.value.toUpperCase();
    recipes = document.getElementsByClassName("recipe");

    for (i = 0; i < recipes.length; i++) {
        let visible = false;
        let attributes = recipes[i].attributes;
        let text = attributes.tags.value.toUpperCase()
        if (text.indexOf(filter) > -1) 
        {
            visible = true;
        }
        if(visible)
        {
            recipes[i].style.display = "";
        }
        else
        {
            recipes[i].style.display = "none";
        }
    }
} 
