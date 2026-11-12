const submitBtn = document.getElementById("submitBtn");
// const visitBtn = document.getElementById("visitbtn");
// const shortCode = visitBtn.dataset.shortcode;

submitBtn.addEventListener("onclick", function () {
  console.log('function called!')
  createURL();
});

// visitBtn.addEventListener("onclick", function () {
//   updateClicks(shortCode);
// });

async function createURL() {
  console.log('create function called!')
  const res = await fetch("/v1/urls/create/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ long_url: input.value }),
  });

  const errorBox = document.getElementById("duplicatemsg");
  const data = await res.json();
  if (!res.ok) {
    errorBox.textContent = data.error; // e.g. the duplicate message
    return;
  }
  resultBox.textContent = data.short_code;
}

function updateClicks(shortcode) {
  const csrftoken = document.queryselector("[name=csrfmiddlewaretoken]").value;
  const url = "v1/urls/<str:shortcode>/stats/";

  fetch(url, {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({}),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "success") {
        console.log("Updated successfully: ", data.count);
      } else {
        console.error("update failed");
      }
    })
    .catch((error) => console.error("Error:", error));
}
