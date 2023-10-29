const currentUserId = document.querySelector(".invisible").innerHTML;

async function getRequests() {
    return fetch(`/library/get-request/`).then((res) => res.json())
}

async function getUsername(user_id) {
    const response = await fetch(`/get_username/${user_id}`);
    return response.json();
}

async function refreshRequests() {
    document.getElementById("all_requests").innerHTML = ""
    const products = await getRequests()
    let counter = 0;

    let htmlString = ``
    
    for (const item of products.reverse()) {
        const user_id = item.fields.user;
        const user = await getUsername(user_id);

        let textCol = "green-text";
        let addedText = "";

        if (Number(currentUserId) === user_id) {
            textCol = "orange-text";
            addedText = "(you)";
        }

        htmlString += `\n
        <div class="col" id="card_${item.pk}">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${item.fields.book_title}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">Book by ${item.fields.book_author}</h6>
                    <p class="card-text">${item.fields.reason}</p>

                    <p class="card-text ${textCol}">@${user.username} ${addedText}</p>
                    <p class="card-text date-post" style="font-size: 1vh;">
                    Request posted on ${item.fields.date_added}
                    </p>
                    <br/>\n`;

        if (Number(currentUserId) === user_id) {
            htmlString += `\n
            <form class="date-post del-req" action="/library/delete-request/${item.pk}/" method="post" id="delete_form_${item.pk}" onsubmit="return false;">
                ${csrfToken}
                <button type="button" onclick="delRequest(${item.pk})" class="btn btn-sm btn btn-outline-danger">Delete</button>
            </form>\n`;
        }

        htmlString += `\n
                </div>
            </div>
        </div>\n`;

        counter++;
        if (counter >= 3) break;
    }
    
    document.getElementById("all_requests").innerHTML = htmlString
}

refreshRequests()

function delRequest(id) {
    fetch(`/library/delete-request/${id}/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
        },
    }).then(refreshRequests)

    return false
}

function addRequest() {
    fetch(`/library/create-request-ajax/`, {
        method: "POST",
        body: new FormData(document.querySelector('#requestForm')),
        headers: {
            "X-CSRFToken": csrfToken,
        },
    }).then(refreshRequests)

    document.getElementById("requestForm").reset()
    return false
}

document.getElementById("button_add").onclick = addRequest