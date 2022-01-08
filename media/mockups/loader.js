var gifs = document.querySelectorAll("img[src$='-start.gif']")
console.log("found gifs", gifs.length);
Array.from(gifs).forEach(function(el) {
  var start = el.src;
  var gif = start.replace(/-start/, "");
  el.addEventListener("click", function() {
    if (el.src === start) {
      el.src = gif;
      el.classList.remove("paused");
      overlay.classList.remove("paused");
    } else {
      el.src = start;
      el.classList.add("paused");
      overlay.classList.add("paused");
    }
    console.log("to", el.src, start, gif);
  });
  var outer = document.createElement("figure");
  el.parentNode.appendChild(outer);
  el.style.cursor = "pointer";
  el.classList.add("paused");
  outer.appendChild(el);
  var caption = document.createElement("figcaption");
  caption.textContent = "Click to animate: " + el.getAttribute("alt");
  outer.appendChild(caption);
  console.log("did el", el.outerHTML);
});
