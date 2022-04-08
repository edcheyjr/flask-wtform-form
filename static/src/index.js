// js to alternate between the two parts of the form

const part1 = document.getElementById('part-1')
const part2 = document.getElementById('part-2')
const next = document.getElementById('next')
const previous = document.getElementById('previous')

next.addEventListener('click', () => {
  if (part2.style.display === 'none') {
    part1.style.display = 'none'
    part2.style.display = 'block'
  } else {
    part2.style.display = 'none'
    part1.style.display = 'block'
  }
})

previous.addEventListener('click', () => {
  if (part1.style.display === 'none') {
    part2.style.display = 'none'
    part1.style.display = 'block'
  } else {
    part1.style.display = 'none'
    part2.style.display = 'block'
  }
})
