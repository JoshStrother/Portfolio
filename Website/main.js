const shareButtons = document.querySelectorAll('.tile-share-button')

async function copyText(e){
//prevent from going to site, copy to clipboard
    e.preventDefault()
    const link = this.getAttribute('link')
    console.log(link)

    try{
        await navigator.clipboard.writeText(link)
        alert("Copied the text: " + link)
    }catch(err){
        console.error(err)
    }
}

shareButtons.forEach( shareButton => 
    shareButton.addEventListener('click', copyText))
