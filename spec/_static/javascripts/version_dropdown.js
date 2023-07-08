/**
* Returns a URL corresponding to a versioned resource (if one exists).
*
* @private
* @param {string} url - base URL
* @param {string} path - resource path
* @returns {Promise} promise which resolves a resource URL
*/
async function href(url, path) {
    const defaultURL = url + "/index.html";
    url += "/" + path;
    await fetch(url).then(onResponse).catch(onError);

    /**
    * Success handler.
    *
    * @private
    * @param {Object} response - response object
    */
    function onResponse(response) {
        if (response.ok) {
            return url;
        }
        return defaultURL;
    }

    /**
    * Error handler.
    *
    * @private
    * @param {Error} error - error object
    */
    function onError(error) {
        return defaultURL;
    }
}

/**
* Adds a version dropdown menu with custom URL paths depending on the current page.
*
* @param {string} json_loc - JSON URL
* @param {string} target_loc - target URL
* @param {string} text - text
* @returns {Promise} promise which resolves upon adding a version menu
*/
async function add_version_dropdown(json_loc, target_loc, text) {
    const dropdown = document.createElement("div");
    dropdown.className = "md-flex__cell md-flex__cell--shrink dropdown";

    const button = document.createElement("button");
    button.className = "dropdownbutton";

    const content = document.createElement("div");
    content.className = "dropdown-content md-hero";

    dropdown.appendChild(button);
    dropdown.appendChild(content);

    await $.getJSON(json_loc).done(onDone).fail(onFail).always(onAlways);

    /**
    * Callback invoked upon resolving a JSON resource.
    *
    * @private
    * @param {Object} versions - versions object
    */
    async function onDone(versions) {
        const currentURL = window.location.href;
        let path = currentURL.split(/_site|array_api/)[1];
        if (path) {
            path = path.split("/");
            path = path.slice(2, path.length);
            path = path.join("/");
        } else {
            path = "";
        }
        for (let key in versions) {
            if (versions.hasOwnProperty(key)) {
                let a = document.createElement("a");
                a.innerHTML = key;
                a.title = key;
                a.href = await href(target_loc + versions[key], path);
                content.appendChild(a);
            }
        }
        button.innerHTML = text;
    }

    /**
    * Callback invoked upon failing to resolve a JSON resource.
    *
    * @private
    */
    function onFail() {
        button.innerHTML = "Other Versions Not Found";
    }

    /**
    * Callback which is always invoked upon attempting to resolve a JSON resource.
    *
    * @private
    */
    function onAlways() {
        $(".navheader").append(dropdown);
    }
};
