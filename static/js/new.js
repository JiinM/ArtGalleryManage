document.addEventListener("DOMContentLoaded", () => {
    const artistSelect = document.getElementById("artist_select");
    const otherArtistFields = document.getElementById("other_artist_fields");

    function toggleOtherArtistFields() {
        if (artistSelect.value === "other") {
            otherArtistFields.classList.remove("hidden");
        } else {
            otherArtistFields.classList.add("hidden");
        }
    }

    artistSelect.addEventListener("change", toggleOtherArtistFields);
    toggleOtherArtistFields(); // run on page load
});
