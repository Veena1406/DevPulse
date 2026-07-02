const markdownInput = document.getElementById("markdown");
const preview = document.getElementById("preview");

if (markdownInput && preview) {

    function updatePreview() {
        preview.innerHTML = marked.parse(markdownInput.value);
    }

    markdownInput.addEventListener("input", updatePreview);

    updatePreview();
}