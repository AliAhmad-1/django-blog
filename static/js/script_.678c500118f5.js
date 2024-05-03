const menu = document.querySelector('.menu');
const user_photo = document.querySelector('.user-photo')


// const profile_photo = document.querySelector('.profile_photo_img')
// const profile_photo_input = document.querySelector('.profile_photo_input')



user_photo.addEventListener('click', () => {
    menu.classList.toggle('hide')
})




document.querySelector('.profile_photo_input').addEventListener('change', () => {
    document.querySelector('.profile_photo_img').src = URL.createObjectURL(document.querySelector('.profile_photo_input').files[0])
})
document.querySelector('.share-icon').addEventListener('click', () => {

    document.querySelector('.share_form').classList.toggle('hide')
})