let pkReview = 0
let indexFilter = 0

async function getBookmarks(filter) {
    return fetch(`/mybooks/get_bookmark_json/?category_filter=${filter}`).then((res) => res.json())
}
async function refreshBookmarks() {
    document.getElementById("table_content").innerHTML = "";
    const products = await getBookmarks(indexFilter);
    let htmlString = "";
    products.result.forEach((bookmark, index) => {
        const reviewContent = bookmark.review ? `<p>${bookmark.review}</p>` : '';
        htmlString += `
            <tr>
                <th scope="row">${index + 1}</th>
                <td>
                    <div class="image-container">
                        <img src="${bookmark.book.image_url}"/>
                    </div>
                </td>
                <td>${bookmark.book.title}</td>
                <td>${bookmark.book.author}</td>
                <td>${bookmark.book.category}</td>
                <td>
                    <div class="review-container">
                        ${reviewContent}
                            <button type="submit" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" onclick="updatePkReview(${bookmark.pk}, '${bookmark.review}')">
                                ${bookmark.review ? 'Edit' : 'Review'}
                            </button>
                    </div>
                </td>
                <td>
                    <button class="btn btn-danger" onclick="removeBookmark(${bookmark.pk})">Remove</button>
                </td>
            </tr>
        `;
    });
    document.getElementById("table_content").innerHTML = htmlString;
}
refreshBookmarks()

function removeBookmark(id) {
    fetch("{%url 'mybooks:remove_bookmark' %}", {
        method: "DELETE",
        body: JSON.stringify({ id: id })
    }).then(refreshBookmarks)
}

function addReview() {
    fetch(`/mybooks/add_review_ajax/${pkReview}/`, {
        method: "POST",
        body: new FormData(document.querySelector('#formReview'))
    }).then(refreshBookmarks)

    document.getElementById("formReview").reset()
    return false
}
document.getElementById("button_add").onclick = addReview

function updatePkReview(newPk, reviewContent) {
    pkReview = newPk;
    const reviewTextarea = document.getElementById("review");
    if (reviewContent) {
        reviewTextarea.value = reviewContent;
    } else {
        reviewTextarea.value = ""; 
    }
}

function updateFilter(newIndex) {
    indexFilter = newIndex
    refreshBookmarks()
}
