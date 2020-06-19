window.addEventListener("load", function() {
    const select = document.getElementById('id_type');
    function toggle_fields() {
        const text = document.getElementsByClassName('field-text')[0];
        const image = document.getElementsByClassName('field-image')[0];

        text.style.display = select.value == 'text' ? 'block' : 'none';
        image.style.display = select.value == 'image' ? 'block' : 'none';
    }

    toggle_fields();
    select.addEventListener('change', toggle_fields);
});
