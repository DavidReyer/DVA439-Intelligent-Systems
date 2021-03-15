var orig_tree = null;
var tree = null;
var prev_item = null
var prev_val = null

// clears out form and resets the tree
function restartTree(){
    $('#formdiv').html("");
    tree = orig_tree;
    prev_item = null
    prev_val = null
    askTree();
}

// preocess input
function askTree() {
    // grey out previous qustions
    $('#formdiv').children().css("opacity", "0.5");
    // apply previous selection (if there is one)
    if (prev_item !== null){
        prev_val = $("#" + prev_item).val()
        tree = tree[prev_val]
    }
    // on a leaf of the tree there is a string
    if (typeof tree === "string"){
        console.log("success");
        var answer = `<h1> YOU SOULD DO: ${tree} </h1>
                      <button onClick = "restartTree()" > restart </button>`
        $('#formdiv').html(answer);
    }
    // if there is no leaf create a select the different classes of the branch
    else{for (var item in tree) {
        var question = `<p>${item}?</p>
                        <select name="${item}" id="${item}">`
        for (var option in tree[item]){
            question += `<option value="${option}">${option}</option>`
        }
        question += `</select>
                    <button onclick="askTree()">Confirm</button>`
        // save handled item
        prev_item = item
        // move tree forward
        tree = tree[item];
        // put new question into html
        $('#formdiv').append(question);}
    }
}