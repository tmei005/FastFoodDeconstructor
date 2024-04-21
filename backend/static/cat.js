let index = 0;
// Function to change image
function changeImage() {
    // Update src attribute with the next image URL
    document.getElementById("catAnimation").src = catImages[index];
    index = (index + 1) % catImages.length;
}
// Call changeImage function every 800ms
setInterval(changeImage, 800);