const formAdditional = document.getElementById("formAdditional")

document.getElementById('formInput').addEventListener('click', (e) => {
    formAdditional.classList.toggle('active')

    Array.from(formAdditional.children[0].children).forEach(element => {
        element.addEventListener('click', (e) => {
            const formValue = document.getElementById('formValue')
            console.log(element.dataset.value); // отсюда берётся значение data-value из тега <p></p>
            formValue.value = element.dataset.value
            formValue.dataset.value = element.dataset.value // Присваивается значение data-value из тега <p></p> тегу input с id 'formValue'
            formAdditional.classList.remove('active')
        })
    })
})

document.addEventListener('click', (e) => {
    if (formAdditional.classList.contains("active") && e.target.id != "formInput" && e.target.id != "formAdditional") {
        formAdditional.classList.remove("active")
    }
})