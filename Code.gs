const POST_URL = "https://49dc-128-210-107-129.ngrok-free.app"; //replace with ngrok

function onSubmit(e) {
    const response = e.response.getItemResponses();
    let items = [];

    // Loop through the form responses and prepare the data
    for (const responseAnswer of response) {
        const question = responseAnswer.getItem().getTitle();
        const answer = responseAnswer.getResponse();
        let parts = [];

        try {
            // Split the response into smaller parts if it exceeds the size limit
            parts = answer.match(/[\s\S]{1,1024}/g) || [];
        } catch (err) {
            parts = [answer];
        }

        if (!answer) {
            continue;
        }

        // Handle responses, including splitting them into multiple parts if needed
        for (const [index, part] of Object.entries(parts)) {
            if (index == 0) {
                items.push({
                    "name": question,
                    "value": part,
                    "inline": false
                });
            } else {
                items.push({
                    "name": question + " (cont.)",
                    "value": part,
                    "inline": false
                });
            }
        }
    }

    // Options for the HTTP POST request with the bypass header or User-Agent
    const options = {
        "method": "post",
        "headers": {
            "Content-Type": "application/json",
            // Option 1: Set bypass header to skip tunnel reminder page
            "bypass-tunnel-reminder": "true",  
            // Option 2: Alternatively, set a custom User-Agent to avoid browser detection
            // "User-Agent": "WebhookClient/1.0",  // Uncomment this line if using User-Agent instead
        },
        "payload": JSON.stringify({
            "content": "\u200c", // Unicode to prevent empty string errors
            "embeds": [{
                "title": "Some nice title here",
                "color": 33023, // Optional, decimal color code
                "fields": items,
                "footer": {
                    "text": "Some footer here"
                },
                "timestamp": new Date().toISOString() // Set the timestamp
            }]
        })
    };

    // Send the HTTP POST request to the POST_URL
    UrlFetchApp.fetch(POST_URL, options);
}
