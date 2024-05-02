// const profile_photo = document.querySelector('.profile_photo_img')
// const profile_photo_input = document.querySelector('.profile_photo_input')
// const button_pass = document.querySelector(".password input");
// const input_text = document.querySelectorAll('.edit-profile-form input ,.edit-profile-form textarea');


// profile_photo_input.addEventListener('change', () => {
//     profile_photo.src = URL.createObjectURL(profile_photo_input.files[0])
// })

// input_text.forEach((field) => {
//     field.addEventListener('focusout', () => {
//         if (field.value !== '') {
//             field.parentElement.classList.add('has-data');

//         } else {
//             field.parentElement.classList.remove('has-data');

//         }

//     })
// })


// function show_hide() {

//     show = false
//     this.addEventListener('click', () => {
//         if (show == false) {
//             button_pass.setAttribute('type', 'text');
//             this.textContent = "visibility_off"
//             show = true
//         } else {
//             button_pass.setAttribute('type', 'password');
//             this.textContent = "visibility"
//             show = false
//         }



//     })
// }

document.querySelector('.share-icon').addEventListener('click', () => {

    document.querySelector('.share_form').classList.toggle('hide')
})