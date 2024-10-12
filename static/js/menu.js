async function request(url, method, body) {
    const response = await fetch(url, {
        method: method,
        headers: {
            "Content-Type": "application/json",
            // "X-Requested-With": "XMLHttpRequest"
        },
        body: body
    });

    return await response.json();
}

let categoryListDiv = document.getElementById("category-list");
let dishListDiv = document.getElementById("dish-list");
let dishDetailsModal = document.getElementById("dishDetails")

const categoryTemplate = document.getElementById("category").content;
const dishTemplate = document.getElementById("dish").content;

async function getDishDetails(event) {
    const dish_details = await request(`api/dishes/${event.target.id}/`);

    dishDetailsModal.querySelector(".modal-title").innerText = dish_details.name;
    dishDetailsModal.querySelector("#price").innerText = `$${dish_details.price}`;
    dishDetailsModal.querySelector(".modal-body").innerText = dish_details.description;
}

async function getDishList(element) {
    dishListDiv.innerHTML = "";
    
    const dish_list = await request(element.dataset.url);
    
    dish_list.forEach((dish) => {
        dishDiv = dishTemplate.cloneNode(true);

        dishDiv.querySelector(".card-header").innerText = dish.name;
        dishDiv.querySelector(".card-title").innerText = `$${dish.price}`;
        dishDiv.querySelector(".card-text").innerText = dish.description;
        
        dishDiv.querySelector(".btn").addEventListener("click", getDishDetails)
        dishDiv.querySelector(".btn").id = dish.id;

        dishListDiv.appendChild(dishDiv.children[0]);
    })
}

async function getCategoryList() {
    const category_list = await request("/api/categories/", method="GET");

    category_list.forEach((category) => {
        let categoryButton = categoryTemplate.cloneNode(true);

        categoryButton.querySelector("label").setAttribute("for", `category${category.id}`);
        categoryButton.querySelector("img").setAttribute("src", category.icon)
        categoryButton.querySelector("#category-name").innerText = category.name;

        categoryButton.querySelector("input").value = category.id;
        categoryButton.querySelector("input").id = `category${category.id}`;
        categoryButton.querySelector("input").dataset["url"] = category.dishes;

        categoryListDiv.appendChild(categoryButton);
    }) 
}

function setup() {
    const allDishesButton = document.querySelector("#all");
    allDishesButton.onclick();

    getCategoryList();
}

document.addEventListener("DOMContentLoaded", setup);