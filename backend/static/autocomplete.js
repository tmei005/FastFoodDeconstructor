const restaurants_list= JSON.parse('{{restaurants_list | tojson | safe}}');
        console.log(restaurants_list)
        const resultsBox = document.querySelector(".result-box");
const inputBox = document.getElementById("input-box");
console.log(typeof restaurants)

inputBox.onkeyup = function(){
    let result = [];
    let input = inputBox.value;
    if(input.length){
        result = restaurants_list.filter((keyword)=>{
            return keyword.toLowerCase().startsWith(input.toLowerCase());
        });
    }
    console.log(result)
    display(result);
}
function display(result) {
    const content = result.map((list)=>{
        return "<li onclick=selectInput(this)>" + list + "</li>";
    });

    resultsBox.innerHTML = "<ul>" + content.join('') + "</ul>"
}
function selectInput(list){
    inputBox.value = list.innerHTML
}