// List of image URLs
console.log(catImages)
// Initialize index to 0
let index = 0;

// Function to change image
function changeImage() {
    // Update src attribute with the next image URL
    document.getElementById("catAnimation").src = catImages[index];
    index = (index + 1) % catImages.length;
}

// Call changeImage function every second
setInterval(changeImage, 800);