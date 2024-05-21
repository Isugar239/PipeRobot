let phrases = [
  { image: 'https://i.postimg.cc/dtGMjnmB/1715011590973.jpg' },
  { image: 'https://i.postimg.cc/KYvdFbXq/1715011627060.jpg' },
  { image: 'https://i.postimg.cc/cHv2gcLf/1715011656691.jpg' },
];

function getRandomElement(arr) {
  let randIndex = Math.floor(Math.random() * arr.length);
  return arr[randIndex];
}

let button = document.querySelector('.button');
let phrase = document.querySelector('.phrase');
let advice = document.querySelector('.advice');
let image = document.querySelector('.image');

button.addEventListener('click', function () {
  let randomElement = getRandomElement(phrases);
  image.src = randomElement.image;
});
