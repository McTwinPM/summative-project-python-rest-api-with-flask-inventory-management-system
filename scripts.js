fetch("https://world.openfoodfacts.net/api/v2/product/3274080005003.json", {
  method: "GET",
  headers: { Authorization: "Basic " + btoa("off:off") },
})
  .then((response) => response.json())
  .then((json) => console.log(json));

document.querySelector("form").addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.querySelector("#title").value;

  fetch("https://world.openfoodfacts.net/api/v2/product/3274080005003.json", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  })
  .then(response => response.json())
  .then(renderEvent);
});

function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = event.title;
  document.querySelector("#event-list").appendChild(li);
}