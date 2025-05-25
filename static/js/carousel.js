document.addEventListener('DOMContentLoaded', function () {
  let slides = document.querySelectorAll('.carousel-item')
  let buttons = document.querySelectorAll('.btn-circle')
  let currentIndex = 0
  let slideInterval

  function showSlide(index) {
    slides.forEach((slide, i) => {
      slide.style.display = i === index ? 'block' : 'none'
    })
  }

  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length
    showSlide(currentIndex)
  }

  function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length
    showSlide(currentIndex)
  }

  function resetAutoSlide() {
    clearInterval(slideInterval)
    slideInterval = setInterval(nextSlide, 3000)
  }

  buttons.forEach((button) => {
    button.addEventListener('click', function (event) {
      event.preventDefault()
      if (this.innerHTML.includes('❯')) {
        nextSlide()
      } else {
        prevSlide()
      }
      resetAutoSlide()
    })
  })

  slideInterval = setInterval(nextSlide, 5000)
  showSlide(currentIndex)
})
