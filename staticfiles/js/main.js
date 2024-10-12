async function request(url, method, body) {
    const response = await fetch(url, {
        method: method,
        headers: {
            "Content-Type": "application/json"
        },
        body: body
    });

    return response;
}

function getCategories(e) {
    let category_btn = document.createElement("input", {
        type: "radio",
        name: "categories",
        class: "btn-check"
    });

    const categories = request("/api/categories/", method="get");
    for (category in categories.body) {
        console.log(category)
    }
}