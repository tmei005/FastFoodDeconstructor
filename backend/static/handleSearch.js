const resultsBox = document.querySelector(".result-box");
const inputBox = document.getElementById("input-box");

    inputBox.onkeyup = function(){
        let result = [];
        let input = inputBox.value.trim().toLowerCase();
        if(input.length){
            result = restaurants_list.filter((keyword)=>{
                return keyword.toLowerCase().startsWith(input);
        });
    }
        display(result);
    if(!result.length) {
        resultsBox.innerHTML = '';
    }
}
function display(result) {
        const content = result.map((list)=>{
        return "<li onclick=selectInput(this)>" + list + "</li>";
    });
    resultsBox.innerHTML = "<ul>" + content.join('') + "</ul>"
}
function selectInput(list){
        inputBox.value = list.innerHTML
        resultsBox.innerHTML = ''
    document.getElementById("selectedRestaurant").value = list.innerHTML;
}
        // Function to display categories
// function displayCategories() {
//             const categoriesResult = document.getElementById('categoriesResult');
//             categoriesResult.innerHTML = '<h2>Categories:</h2>';
//             const categoriesList = document.createElement('ul');
//
//             categories.forEach(category => {
//                 const categoryItem = document.createElement('li');
//                 categoryItem.textContent = category;
//                 categoriesList.appendChild(categoryItem);
//             });
//
//             categoriesResult.appendChild(categoriesList);
//         }
//         displayCategories();
//
//                 function displayMenu(categories) {
//             const menuDropdown = document.getElementById('menuDropdown');
//             menuDropdown.innerHTML = ''; // Clear existing options
//
//             categories.forEach(category => {
//                 const option = document.createElement('option');
//                 option.textContent = category;
//                 menuDropdown.appendChild(option);
//             });
//         }