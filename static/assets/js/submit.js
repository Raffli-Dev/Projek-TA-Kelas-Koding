document.addEventListener("DOMContentLoaded", function () {
  const komentarInput = document.getElementById("komentar");

  komentarInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      document.forms[0].submit();
    }
  });
});
