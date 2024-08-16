function closePopup() {
    window.opener.location.reload();
    window.close();
}

function openPopup(url) {
    const width = 600;
    const height = 400;
    const left = (window.innerWidth / 2) - (width / 2);
    const top = (window.innerHeight / 2) - (height / 2);
    const uniqueWindowName = "AddAuthor_" + new Date().getTime();
    const popup = window.open(url, uniqueWindowName, `width=${width},height=${height},scrollbars=yes,resizable=yes,left=${left},top=${top}`);

    if (!popup || popup.closed || typeof popup.closed === 'undefined') {
        alert('Popup blocked! Please allow popups for this website.');
    }
}
