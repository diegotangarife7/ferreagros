const mayorCheckbox = document.getElementById("greader");
  const menorCheckbox = document.getElementById("minor");

  mayorCheckbox.addEventListener("click", () => {
    if (mayorCheckbox.checked) {
      menorCheckbox.checked = false;
    }
  });

  menorCheckbox.addEventListener("click", () => {
    if (menorCheckbox.checked) {
      mayorCheckbox.checked = false;
    }
  });