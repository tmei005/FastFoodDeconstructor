// List of image URLs
        const images = ["{{ url_for('static', filename='Images/cat1.png') }}", "{{ url_for('static', filename='Images/cat2.png') }}", "{{ url_for('static', filename='Images/cat4.png') }}"];

        // Initialize index to 0
        let index = 0;
        // Function to change image
        function changeImage() {
            // Update src attribute with the next image URL
            document.getElementById("catAnimation").src = images[index];
            index = (index + 1) % images.length;
        }
        // Call changeImage function every second
        setInterval(changeImage, 800);