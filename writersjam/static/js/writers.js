async function getStory() {
    return fetch("{% url 'writersjam:get_story_json' %}").then((res) => res.json())
}

async function refreshPage() {
    document.getElementById("story-submission").innerHTML=""
    let htmlstring = ``
    const stories = await getStory()
    stories.forEach((submit) => {
        htmlstring += `\n
        <div class="col">
            <div class="card">
                <div class="card-body">
                    <div id="story-title" style="padding-top: 0px;">
                        <h4 class="card-title">${submit.fields.title}</h4>
                        <hr>
                        <p class="card-text" style="font-weight: bold; padding-top: 0px;">by ${submit.fields.username}</p>
                    </div>
                    <div id="story-body">
                        <p class="card-text">${submit.fields.story}</p>
                    </div>
                    <div class="story-create-date">
                        <br>
                        <p class="card-text">${submit.fields.date}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>\n`
    });

    document.getElementById("story-submission").innerHTML = htmlstring
}

refreshPage();

function addStory() {
    fetch("{% url 'writersjam:submit_story_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#submissionForm'))
    }).then(refreshPage)

    document.getElementById("submissionForm").reset()
    return false
}

document.getElementById("submit_story").onclick = addStory